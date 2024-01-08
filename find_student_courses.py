# Peyton Hansen
# DSCI 551 Fall 2023
# HW2: find_student_courses
# hw2.xml

import sys
from lxml import etree


def find_student_courses(studentID):
    # start XML file
    tree = etree.parse("hw2.xml")
    root = tree.getroot()

    # find student
    student = root.find(f"students/student[id='{studentID}']")

    if student is None:
        print("Student not found.")
    else:
        # find student name
        studentName = student.find("name").text

        # find student courses
        coursesTaken = []
        for takes in student.iter("takes"):
            courseNumber = takes.find("courseNumber").text
            semester = takes.find("semester").text
            coursesTaken.append({"courseNumber": courseNumber, "semester": semester})

        # return output in XML format
        output = etree.Element("studentCourses")
        etree.SubElement(output, "name").text = studentName
        courses = etree.SubElement(output, "courses")

        for courseInfo in coursesTaken:
            course = etree.SubElement(courses, "course")
            etree.SubElement(course, "courseNumber").text = courseInfo["courseNumber"]
            etree.SubElement(course, "semester").text = courseInfo["semester"]

        print(etree.tostring(output, pretty_print=True).decode("utf-8"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid format of arguments.")
    else:
        studentID = sys.argv[1]
        find_student_courses(studentID)
