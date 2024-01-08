# Peyton Hansen
# DSCI 551 Fall 2023
# HW2: find_instructor_courses
# hw2.xml

import sys
from lxml import etree


def find_instructor_courses(instructorID):
    # start XML file
    tree = etree.parse("hw2.xml")
    root = tree.getroot()

    # find instructor
    instructor = root.find(f"instructors/instructor[id='{instructorID}']")

    if instructor is None:
        print("Instructor not found.")
    else:
        # find instructor name
        instructorName = instructor.find("name").text

        # find instructor courses
        coursesTaught = []
        for teaches in instructor.iter("teaches"):
            courseNumber = teaches.find("courseNumber").text
            semester = teaches.find("semester").text
            coursesTaught.append({"courseNumber": courseNumber, "semester": semester})

        # return output in XML format
        output = etree.Element("instructorCourses")
        etree.SubElement(output, "name").text = instructorName
        courses = etree.SubElement(output, "courses")

        for courseInfo in coursesTaught:
            course = etree.SubElement(courses, "course")
            etree.SubElement(course, "courseNumber").text = courseInfo["courseNumber"]
            etree.SubElement(course, "semester").text = courseInfo["semester"]

        print(etree.tostring(output, pretty_print=True).decode("utf-8"))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Invalid format of arguments.")
    else:
        instructorID = sys.argv[1]
        find_instructor_courses(instructorID)

