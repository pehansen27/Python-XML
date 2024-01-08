# Peyton Hansen
# DSCI 551 Fall 2023
# HW2: add_instructor
# hw2.xml

import sys
from lxml import etree


def instructorValid(root, instructorID):
    # see if student ID alrdy exists
    return root.xpath(f"//instructor[id='{instructorID}']")


def add_instructor(instructorID, instructorName, department):
    # start XML file
    tree = etree.parse("hw2.xml")
    root = tree.getroot()

    if instructorValid(root, instructorID):
        print('This instructor ID has already been entered in the system.')
    else:
        # add arguments to instructor
        instructor = etree.Element("instructor")
        etree.SubElement(instructor, "id").text = instructorID
        etree.SubElement(instructor, "name").text = instructorName
        etree.SubElement(instructor, "department").text = department

        # add instructor element to xml under instructors
        instructors = root.find("instructors")
        instructors.append(instructor)

        # write to xml
        tree.write("hw2.xml", pretty_print=True)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    instructorID, instructorName, department = sys.argv[1], sys.argv[2], sys.argv[3]
    add_instructor(instructorID, instructorName, department)
