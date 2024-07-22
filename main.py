from datetime import date

class User:
    def __init__(self, type, name, birth_date, pass_id, email, gender, nationality, phone_num):
        self.set_type(type)
        self.set_name(name)
        self.set_birth_date(birth_date)
        self.set_email(email)
        self.set_gender(gender)
        self.set_nationality(nationality)
        self.set_phone_num(phone_num)
        self.set_pass_id(pass_id)

    def set_type(self, type):
        type_list=["Student", "Faculty", "Staff"]
        if type in type_list:
            self.__type = type
        else:
            raise Exception("You are not allowed to enter")

    def set_name(self, name):
        if all(not letter.isdigit() for letter in name) and len(name) >= 2:
            self.__name = name
        else:
            raise ValueError("Enter your name as your passport!")

    def set_birth_date(self, birth_date):
        if (birth_date[:4].isdigit() and birth_date[4] == "/" and birth_date[5:7].isdigit() and birth_date[7] == "/" and birth_date[8:10].isdigit()):
            if (int(birth_date[:4]) <= date.today().year and int(birth_date[5]) <= 1 and int(birth_date[6]) < 10 and int(birth_date[8]) <= 3 and int(
                    birth_date[9]) < 10):
                self.__bd = birth_date
        else:
            raise ValueError("Enter your birthday: YYYY/MM//DD")

    def set_pass_id(self, pass_id):
        if (pass_id[:2].isupper() and pass_id[2:].isdigit() and len(pass_id) == 9):
            self.__pass_id = pass_id
        else:
            raise Exception("Enter your passport ID as your passport")

    def set_email(self, email):
        if (email.endswith(".com") and email.__contains__("@")):
            self.__email = email
        else:
            raise ValueError("It should contains @gmail.com")

    def set_gender(self, gender):
        gender=gender.lower()
        if gender == "male" or gender == "female":
            self.__gender = gender
        else:
            raise ValueError("Something gets wrong!!!")

    def set_nationality(self, nationality):
        if isinstance(nationality, str):
            self.__nationality = nationality
        else:
            raise ValueError("Wrong data type, enter your nationality with letters!!!")

    def set_phone_num(self, phone_num):
        if phone_num.startswith('998') and len(phone_num) == 12:
            self.__phone_num = phone_num
        else:
            raise ValueError("You entered incorrect value")


    def get_type(self):
        return self.__type

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_pass_id(self):
        return self.__pass_id

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_nationality(self):
        return self.__nationality

    def get_phone_num(self):
        return self.__phone_num

class Faculty(User):
    def __init__(self, course, occupation, co_hours, salary, title, type, name, birth_date, pass_id, email, gender,
                 nationality, phone_num):
        super().__init__(type, name, birth_date, pass_id, email, gender, nationality, phone_num)
        self.set_course(course)
        self.set_occupation(occupation)
        self.set_co_hours(co_hours)
        self.set_salary(salary)
        self.set_title(title)

        self.__extra_hours=0
        self.__extra_salary=0

    def set_course(self, course):
        if isinstance(course, str):
            course = course.strip().upper()
            f = open("courses.txt")
            lines = f.readlines()
            f.close()
            for line in lines:
                list_types = line.split()
            if course in list_types:
                self.__course = course
        else:
            raise Exception("You are not allowed to enter")

    def set_occupation(self, occupation):
        occupation = occupation.strip().lower()
        if occupation=="full time" or occupation=="part time":
            self.__occupation = occupation
        else:
            raise Exception("Enter correctly your occupation")

    def set_co_hours(self, co_hours):
        extra_hours = 0
        co_hours=co_hours.strip()
        if co_hours.isnumeric():
            if self.get_occupation() == 'full-time':
                if co_hours > 24:
                    raise ValueError("It's illegal")
                elif 19 <= co_hours <= 24:
                    self.__co_hours = 18
                    self.__extra_hours = co_hours - 18
                elif 2 <= co_hours <= 18:
                    self.__co_hours = co_hours
                    self.__extra_hours = 0
                else:
                    raise ValueError("You are not working at all")
            elif self.get_occupation() == 'part-time':
                if co_hours > 12:
                    raise ValueError("It's illegal")
                elif 10 <= co_hours <= 12:
                    self.__co_hours = 9
                    self.__extra_hours = co_hours - 9
                elif 1 <= co_hours <= 9:
                    self.__co_hours = co_hours
                    self.__extra_hours = 0
                else:
                    raise ValueError("You are not working at all")

    def set_salary(self, salary):
        salary = {"TEACHING ASSISTANTS": 100, "LECTURERS": 150, "SENIOR LECTURERS": 200, "ASSISTANT PROFESSOR": 250,
                 "ASSOCIATE PROFESSOR": 300, "FULL PROFESSOR": 350, "ACADEMICIAN": 400}
        if salary.isdigit():
            if self.get_title() in salary.keys():
                self.__salary = self.get_hours() * salary[self.get_title()]
                self.__extra_salary = self.get_extra_hours() * salary[
                    self.get_title()] * 2  # get_extra_hours() should either be private or should not exist at all
        else:
            raise ValueError("salary must be numeric")

    def set_title(self, title):
        title = title.strip().upper()
        f = open("titles.txt")
        lines = f.readlines()
        f.close()
        for line in lines:
            list_types = line.split(",")
        if title in list_types:
            self.__title = title
        else:
            raise ValueError("Invalid title entered")

    def get_course(self):
        return self.__course

    def get_occupation(self):
        return self.__occupation

    def get_co_hours(self):  # course hours
        return self.__hours

    def get_salary(self):
        return self.__salary

    def get_title(self):
        return self.__title



type = input("Choose the option related to you:")
name = input("Enter your name:")
pass_id = input("Enter your Passport ID:")
email = input("Enter your email:")
bd = input("Enter your birthday date as YYYY/MM/DD:")
gender = input("Enter your gender:")
nationality = input("Enter your nationality:")
phone = input("Enter your phone")

user = User(type, name, bd, pass_id, email, gender, nationality, phone)

#user = User("Student", "ashd", '2000/12/22', 'AD2309876', 'asda@gmail.com', 'male', 'kasjd', '998902123343')

salary = input('enter')
if salary.isnumeric():
    print('correct')
else:
    print('incorrect')