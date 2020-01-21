from csv import reader

minimum_values = 10
lines_read = 0

with open('input/trajectory.txt') as in_file:

    # create a csv reader object
    csv_reader = reader(in_file, delimiter=';')

    # go over each line
    for line in csv_reader:

        # if line is not empty
        if line and len(line) > minimum_values:
            lines_read += 1
            print(str(lines_read)+" "+str(line))




