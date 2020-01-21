from csv import reader
import time

minimum_values = 50  # Minimum number of points in a line to be considered significant trajectory (line)
maximum_values = 50  # Stream this many number of separate points file
streaming_delay = 1  # Delay in seconds to generate a new values file for each trajectory (line) in output dir

input_file = 'input/trajectory.txt'
output_dir = 'output/'

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

print("Total Lines / Trajectories Considered: "+str(len(database)))

columns = []

for count in range(maximum_values):
    col = []
    for row in database:
        col.append(row[count])
    columns.append(col)

print(f"Total Values / Points Considered: {len(columns)}")

for count, column in enumerate(columns):
    time.sleep(streaming_delay)
    print("Streaming Value # "+str(count))
    file_name = output_dir + str(count) + '.txt'
    f = open(file_name, 'w+')
    for rows in column:
        f.write(rows+'\n')
    f.close()

