class Student():
    # define a constructor
    def __init__(self, first_name, last_name, major, credit_hours, gpa, id_number):
        # define class properties with the parameter values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number.strip()
    
    # create getter and setter methods
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self, new_name):
        self.__first_name = new_name

    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self, new_name):
        self.__last_name = new_name

    def get_major(self):
        return self.__major
    
    def set_major(self, new_major):
        self.__major = new_major

    def get_credit_hours(self):
        return self.__credit_hours
    
    def set_credit_hours(self, new_credit_hours):
        self.__credit_hours = new_credit_hours

    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, new_gpa):
        self.__gpa = new_gpa

    def get_id_number(self):
        return self.__id_number
    
    # create a method to determine the class based on the students credit hours
    def get_class_level(self):
        if int(self.__credit_hours) >= 0 and int(self.__credit_hours) <= 30:
            return "Freshman"
        elif int(self.__credit_hours) >= 31 and int(self.__credit_hours) <= 60:
            return "Sophomore"
        elif int(self.__credit_hours) >= 61 and int(self.__credit_hours) <= 90:
            return "Junior"
        else:
            return "Senior"
        
    # create a method to update student's credit hours
    def update_credit_hours(self, additional_hours):
        self.__credit_hours += additional_hours

    # create a method to print out student data
    def print_student_data(self):
        print(f"{self.__first_name} {self.__last_name}")
        print(f"Class Level: {self.get_class_level()}, Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__id_number}\n")
