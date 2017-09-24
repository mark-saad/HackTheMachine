import csv





with open('C:\\Users\\nstolting\\Downloads\\classA_ship1_meanfilled_MRG2.csv', 'r') as csvfile:
    print(csvfile)
    data_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    failure = False
    current_state = "1"
    for row in data_reader:
        if row[-1] == current_state:
            pass

        elif row[-1] == '-1' and current_state == "1":
            failure = True
            print("Start: {0}".format(row[0]))
            current_state = row[-1]

        elif row[-1] == "1" and current_state == "-1":
            print("End: {0}".format(row[0]))
            current_state = row[-1]


