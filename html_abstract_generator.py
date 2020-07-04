import csv

with open('attendee.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[0] == 'Nightmare Panel':
            s = "<li><p><strong>" + row[1] + " / " + row[2] + " / " + row[
                3] + "</strong><br> <u>Abstract:</u> " + row[
                    4] + "<br>" + "<u>Reference:</u> " + row[5] + "</p></li>"
            print(s)