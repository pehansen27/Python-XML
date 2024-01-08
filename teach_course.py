# Peyton Hansen
# DSCI 551 Fall 2023
# HW2: teach_course
# hw2.xml

import sys
from lxml import etree


def teach_course(instructorID, courseNumber, semester):
    # start XML file
    tree = etree.parse("hw2.xml")
    root = tree.getroot()

    # validate that arguments don't already exist
    instructor = root.find(f"instructors/instructor[id='{instructorID}']")
    course = root.find(f"courses/course[number='{courseNumber}']")
    semesterExists = root.xpath(f"//semester[text()='{semester}']")

    if not (instructor and course and semesterExists):
        print("Invalid instructor, course, or semester.")
    else:
        # add teaches subelement under instructor element
        teaches = etree.Element("teaches")
        etree.SubElement(teaches, "courseNumber").text = courseNumber
        etree.SubElement(teaches, "semester").text = semester

        # append
        instructor.append(teaches)

        # write to xml
        tree.write("hw2.xml", pretty_print=True)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Invalid format of arguments.")
    else:
        instructorID, courseNumber, semester = sys.argv[1], sys.argv[2], sys.argv[3]
        teach_course(instructorID, courseNumber, semester)
