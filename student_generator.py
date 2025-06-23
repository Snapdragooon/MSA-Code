from Student import Student

def main():
    # open students.csv
    data_file = open("students.csv", "r")

    # create a list to store students
    student_list = []

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
            continue

        if len(student_info) != 6:
            continue
        else:
            student_list.append(student_info)
    
    for student in student_list:
        new_student = Student(student[0], student[1], student[2], student[3], student[4], student[5])
        new_student.print_student_data()

main()