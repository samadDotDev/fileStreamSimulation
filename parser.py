from csv import reader
import time
import argparse


# Define defaults

default_streaming_delay = 1  # Streaming Delay in seconds to generate a new values file for each trajectory (line) in output dir
default_minimum_values = 50  # Minimum number of points in a line to be considered significant trajectory (line)
default_maximum_values = 50  # Stream this many number of separate points file
default_input_file = 'input/trajectory.txt'
default_output_dir = 'output/'
default_cumulative = False
default_start_from_rows = '0'
default_rows_limit = '100000'
default_delimiter = ';'
default_stream_columns = False


# A Useful approach to parse cmdline args

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--delay", default=default_streaming_delay, help="Streaming Delay in seconds to generate a new values file for each trajectory (line) in output dir")
parser.add_argument("-min", "--min_val", default=default_minimum_values, help="Minimum number of points in a line to be considered significant trajectory (line)")
parser.add_argument("-max", "--max_val", default=default_maximum_values, help="Stream this many number of separate points file")
parser.add_argument("-i", "--input_file", default=default_input_file, help="Path to file of line-separated trajectories of comma-sep points which should be read and parsed for streaming")
parser.add_argument("-o", "--output_dir", default=default_output_dir, help="Output Directory to stream to (will generate a new file every streaming delay)")
parser.add_argument("-c", "--cumulative", default=default_cumulative, action="store_true", help="Stream Cumulatively (Append new points to previous points in new files)")
parser.add_argument("-s", "--start_from", default=default_start_from_rows, help="Start from Row/Line/Trajectory Number upto limit defined by -l")
parser.add_argument("-l", "--limit", default=default_rows_limit, help="Maximum number of values / trajectories to consider")
parser.add_argument("-de", "--delimiter", default=default_delimiter, help="Delimiter that separates points in each line")
parser.add_argument("-sc", "--stream_columns", default=default_stream_columns, action="store_true", help="Stream Columns (Values/Points) or Rows (Lines/Trajectories)")


# Read arguments from the command line

args = parser.parse_args()

streaming_delay = int(args.delay)
minimum_values = int(args.min_val)
maximum_values = int(args.max_val)
input_file = args.input_file
output_dir = args.output_dir
cumulative = args.cumulative
limit_max_rows = int(args.limit)
start_from = int(args.start_from)
delimiter = args.delimiter
stream_columns = bool(args.stream_columns)

print("Reading from: "+input_file)
print("Streaming to: "+output_dir)


lines_read = 0
database = []

with open(input_file) as in_file:
    # create a csv reader object
    csv_reader = reader(in_file, delimiter=delimiter)

    line_num = 0

    # go over each line
    for line in csv_reader:

        line_num += 1

        if line_num <= start_from:
            continue
        if line_num > limit_max_rows:
            break

        # if line is not empty
        if line and len(line) > minimum_values:
            lines_read += 1
            # print(str(lines_read) + " " + str(line))
            database.append(line[:maximum_values])


if limit_max_rows < len(database):
    print("Lines(trajectories) present: " + str(len(database)) + ", Considered: " + str(limit_max_rows) + " starting from " + str(start_from))
else:
    print("Total lines(trajectories) considered: " + str(len(database)) + " starting from " + str(start_from))


if stream_columns:

    columns = []

    for count in range(maximum_values):
        col = []
        for row in database:
            col.append(row[count])
        columns.append(col)

    print("Total values/line considered: {}".format(len(columns)))

    for count, column in enumerate(columns):

        print("\nStreaming Value # " + str(count))
        file_name = output_dir + str(count) + '.txt'
        f = open(file_name, 'w+')

        for rowNumber in range(start_from, start_from + min(len(column), limit_max_rows)):

            # If running over the available number of columns, break!
            if rowNumber >= len(column):
                break

            if cumulative:

                # Nightly tweak: Append previous ones:
                for i in range(count+1):
                    f.write(columns[i][rowNumber])
                    if i < count:
                        f.write(delimiter)

            else:
                # Streaming individual points for each trajectory separately in files (not appending previously streamed)
                f.write(column[rowNumber])

            f.write('\n')

        f.close()
        time.sleep(streaming_delay)


else:

    # Row Streaming

    for current_row in range(0, len(database)):

        print("\nStreaming Row # " + str(current_row))
        file_name = output_dir + str(current_row) + '.txt'
        f = open(file_name, 'w+')
        if cumulative:
            for row_num in range(0, current_row+1):
                row = database[row_num]
                f.write(str(row))
                f.write('\n')
        else:
            row = database[current_row]
            f.write(str(row))
            f.write('\n')

        f.close()
        time.sleep(streaming_delay)
