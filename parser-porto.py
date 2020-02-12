from csv import reader
import time

minimum_values = 50  # Minimum number of points in a line to be considered significant trajectory (line)
maximum_values = 50  # Stream this many number of separate points file
streaming_delay = 1  # Delay in seconds to generate a new values file for each trajectory (line) in output dir

input_file = 'C:/Users/Samad-i5/largeDatasets/Porto/porto.txt'
output_dir = 'C:/Users/Samad-i5/largeDatasets/Porto/stream/'

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
    for rowNumber, rows in enumerate(column):
        # f.write(rows+'\n')

        # Nightly tweak: Append previous ones:
        for i in range(count):
            f.write(columns[i][rowNumber])
            if i < count:
                f.write(';')

        f.write(rows + '\n')

    f.close()

