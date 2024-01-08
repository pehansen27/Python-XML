# Peyton Hansen
# DSCI 551 Fall 2023
# HW2: add_course
# hw2.xml

import sys
from lxml import etree


def add_course(courseNumber, courseTitle, semester):
    # start XML file
    tree = etree.parse("hw2.xml")
    root = tree.getroot()


    # add arguments to course
    course = etree.Element("course")
    etree.SubElement(course, "number").text = courseNumber
    etree.SubElement(course, "title").text = courseTitle
    etree.SubElement(course, "semester").text = semester

    # add course element to xml under courses
    courses = root.find("courses")
    courses.append(course)

    # write to xml
    tree.write("hw2.xml", pretty_print=True)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    courseNumber, courseTitle, semester = sys.argv[1], sys.argv[2], sys.argv[3]
    add_course(courseNumber, courseTitle, semester)
