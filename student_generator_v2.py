import datetime
from Student import Student

"""
Function: to write an error message to a log file
Input: (str)message
Output: none
"""
def write_to_error_log(message:str) -> None:
    # open the log file in append mode: error_log.txt
    # write error message to the file in the format
    # Date: message -> 6/24/2025: Error in datafile on line 5
    # close file
    the_date = datetime.datetime.now()
    this_day = the_date.day
    this_month = the_date.month
    this_year = the_date.year

    with open("error_log.txt", "a") as error_log:
        error_log.write(f"{this_day}/{this_month}/{this_year}: {message}\n")

"""
Function: to return a list of student objects
Input: none
Output: list of student objects
"""
def load_students() -> list[Student]:
    # open students.csv
    data_file = open("students.csv", "r")

    # create a list to store students
    student_list = []
    line_number = 0

    # use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        # split the data at the comma
        student_info = line_of_data.split(",")

        # check if student data is valid
        try:
            int(student_info[3])
            float(student_info[4])
            int(student_info[5])
        except:
            # write an error message to an error log
            line_number += 1
            write_to_error_log(f"Error in datafile on line {line_number}")
            continue

        if len(student_info) != 6:
            # write an error message to an error log
            line_number += 1
            write_to_error_log(f"Error in datafile on line {line_number}")
            continue
        else:
            student_list.append(student_info)
            line_number += 1
        
        new_student_list = []
    
    # print out student data
    for student in student_list:
        new_student = Student(student[0], student[1], student[2], student[3], student[4], student[5])
        new_student_list.append(new_student)

    return new_student_list

"""
Function: to convert student object to student dictionaries
Input: list of student objects
Output: list of student dictionaries
"""
def student_to_dictionary(list_of_students:list[Student]) -> list[dict]:
    # create a list to store the dictionaries in
    student_dictionary_list = []

    # loop through the student list and write each student's data to a dictionary
    for student in list_of_students:
        # create an empty dictionary
        student_dictionary = {}

        # set the keys and values for the dictionary
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id_number()

        # append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
    
    # return the list of dictionaries
    return student_dictionary_list

"""
Function: to get a list of student dictionaries
Input: none
Output: list of student dictionaries
"""
def get_student_dictionaries():
    # get a list of students
    student_list = load_students()

    # get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries

get_student_dictionaries()