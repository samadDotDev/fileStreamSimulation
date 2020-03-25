from csv import reader
import time
import argparse


# Define defaults

default_streaming_delay = 1  # Streaming Delay in seconds to generate a new values file for each trajectory (line) in output dir
default_minimum_values = 50  # Minimum number of points in a line to be considered significant trajectory (line)
default_maximum_values = 50  # Stream this many number of separate points file
default_input_file = 'input/trajectory.txt' # '/home/csgrads/samad028/largeDatasets/Porto/porto.txt'
default_output_dir = 'output/'  # /home/csgrads/samad028/largeDatasets/Porto/stream/
default_cumulative = False


# A Useful approach to parse cmdline args

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--delay", default=default_streaming_delay, help="Streaming Delay in seconds to generate a new values file for each trajectory (line) in output dir")
parser.add_argument("-min", "--min_val", default=default_minimum_values, help="Minimum number of points in a line to be considered significant trajectory (line)")
parser.add_argument("-max", "--max_val", default=default_maximum_values, help="Stream this many number of separate points file")
parser.add_argument("-i", "--input_file", default=default_input_file, help="Path to file of line-separated trajectories of comma-sep points which should be read and parsed for streaming")
parser.add_argument("-o", "--output_dir", default=default_output_dir, help="Output Directory to stream to (will generate a new file every streaming delay)")
parser.add_argument("-c", "--cumulative", default=default_cumulative, action="store_true", help="Stream Cumulatively (Append new points to previous points in new files)")
parser.add_argument("-s", "--startFrom", default=0, help="Start from # of Trajectories upto limit defined by -l")
parser.add_argument("-l", "--limit", default=100000, help="Maximum number of values / trajectories to consider")


# Read arguments from the command line

args = parser.parse_args()

streaming_delay = int(args.delay)
minimum_values = int(args.min_val)
maximum_values = int(args.max_val)
input_file = args.input_file
output_dir = args.output_dir
cumulative = args.cumulative
limitMaxTrajectories = int(args.limit)
startFrom = int(args.startFrom)

print("Reading from: "+input_file)
print("Streaming to: "+output_dir)


lines_read = 0
database = []

with open(input_file) as in_file:
    # create a csv reader object
    csv_reader = reader(in_file, delimiter=';')

    # go over each line
    for line in csv_reader:

        # if line is not empty
        if line and len(line) > minimum_values:
            lines_read += 1
            # print(str(lines_read) + " " + str(line))
            database.append(line[:maximum_values])


if limitMaxTrajectories < len(database):
    print("Lines(trajectories) present: " + str(len(database)) + ", Considered: " + str(limitMaxTrajectories) + " starting from "+str(startFrom))
else:
    print("Total lines(trajectories) considered: " + str(len(database)) + " starting from "+str(startFrom))

columns = []

for count in range(maximum_values):
    col = []
    for row in database:
        col.append(row[count])
    columns.append(col)

print(f"Total values/traj considered: {len(columns)}")

for count, column in enumerate(columns):

    print("\nStreaming Value # " + str(count))
    file_name = output_dir + str(count) + '.txt'
    f = open(file_name, 'w+')

    for rowNumber in range(startFrom, startFrom+min(len(column), limitMaxTrajectories)):

        # If running over the available number of columns, break!
        if rowNumber >= len(column):
            break

        if cumulative:

            # Nightly tweak: Append previous ones:
            for i in range(count+1):
                f.write(columns[i][rowNumber])
                if i < count:
                    f.write(';')

        else:
            # Streaming individual points for each trajectory separately in files (not appending previously streamed)
            f.write(column[rowNumber])

        f.write('\n')

    f.close()
    time.sleep(streaming_delay)
