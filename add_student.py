# Peyton Hansen
# DSCI 551 Fall 2023
# HW2: add_student
# hw2.xml

import sys
from lxml import etree


def studentValid(root, studentID):
    # see if student ID alrdy exists
    return root.xpath(f"//student[id='{studentID}']")


def add_student(studentID, studentName, program):
    # start XML file
    tree = etree.parse("hw2.xml")
    root = tree.getroot()

    if studentValid(root, studentID):
        print("This student ID has already been entered in the system.")
    else:
        # add arguments to student
        student = etree.Element("student")
        etree.SubElement(student, "id").text = studentID
        etree.SubElement(student, "name").text = studentName
        etree.SubElement(student, "program").text = program

        # add student element to xml under students
        students = root.find("students")
        students.append(student)

        # write to xml
        tree.write("hw2.xml", pretty_print=True)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    studentID, studentName, program = sys.argv[1], sys.argv[2], sys.argv[3]
    add_student(studentID, studentName, program)
