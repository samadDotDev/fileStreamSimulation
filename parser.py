from csv import reader
import time
import sys

minimum_values = 50  # Minimum number of points in a line to be considered significant trajectory (line)
maximum_values = 50  # Stream this many number of separate points file
streaming_delay = 1  # Delay in seconds to generate a new values file for each trajectory (line) in output dir

input_file = 'input/trajectory.txt' # '/home/csgrads/samad028/largeDatasets/Porto/porto.txt'
output_dir = 'output/'  # /home/csgrads/samad028/largeDatasets/Porto/stream/

streaming_method = 'cumulative'   # {cumulative, individual}

if len(sys.argv) > 1:
    if len(sys.argv) > 1: streaming_delay = sys.arg[1]
    if len(sys.argv) > 2: minimum_values = sys.arg[2]
    if len(sys.argv) > 3: maximum_values = sys.arg[3]
    if len(sys.argv) > 4: input_file = sys.arg[4]
    if len(sys.argv) > 5: output_dir = sys.arg[5]
    if len(sys.argv) > 6: streaming_method = sys.arg[6]


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

print("Total lines(trajectories) considered: " + str(len(database)))

columns = []

for count in range(maximum_values):
    col = []
    for row in database:
        col.append(row[count])
    columns.append(col)

print(f"Total values(points) considered: {len(columns)}")

for count, column in enumerate(columns):

    print("Streaming Value # " + str(count))
    file_name = output_dir + str(count) + '.txt'
    f = open(file_name, 'w+')

    for rowNumber, rows in enumerate(column):

        if streaming_method == 'cumulative':

            # Nightly tweak: Append previous ones:
            for i in range(count):
                f.write(columns[i][rowNumber])
                if i < count:
                    f.write(';')

        else:
            # Streaming individual points for each trajectory separately in files (not appending previously streamed)
            f.write(rows)

        f.write('\n')

    f.close()
    time.sleep(streaming_delay)
