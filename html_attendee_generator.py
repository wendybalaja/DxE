import csv

with open('attendee.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        if row[0] == 'Attendees':
            s = "<div class= \"col-3 col-4-medium col-8-small accordion\"><a href=\"#\" class=\"image\"><img src=\"images/profile_pics/image_holder\" alt=\"\" /></a><button type=\"button\" class=\"accordion-button\"> " + row[
                1] + " / " + row[2] + " / " + row[
                    3] + "</button><div class=\"accordion-content\"><p><br><strong>Bio: </strong>" + row[
                        5] + "<br> <strong>Research interest: </strong>" + row[
                            6] + "<br> <strong>Website: </strong><a href=\"" + row[
                                7] + "\">" + row[7] + "</a></p></div></div>"
            print(s)