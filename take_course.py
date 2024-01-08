# Peyton Hansen
# DSCI 551 Fall 2023
# HW2: take_course
# hw2.xml

import sys
from lxml import etree


def take_course(studentID, courseNumber, semester):
    # start XML file
    tree = etree.parse("hw2.xml")
    root = tree.getroot()

    # validate that arguments don't already exist
    student = root.find(f"students/student[id='{studentID}']")
    course = root.find(f"courses/course[number='{courseNumber}']")
    semesterExists = root.xpath(f"//semester[text()='{semester}']")

    if not (student and course and semesterExists):
        print("Invalid student, course, or semester.")
    else:
        # add takes subelement under student element
        takes = etree.Element("takes")
        etree.SubElement(takes, "courseNumber").text = courseNumber
        etree.SubElement(takes, "semester").text = semester

        # append
        student.append(takes)

        # write to xml
        tree.write("hw2.xml", pretty_print=True)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Invalid format of arguments.")
    else:
        studentID, courseNumber, semester = sys.argv[1], sys.argv[2], sys.argv[3]
        take_course(studentID, courseNumber, semester)

