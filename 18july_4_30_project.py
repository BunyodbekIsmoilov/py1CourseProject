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
        if phone_num.startswith(998) and len(phone_num) == 12:
            self.__phone = phone_num
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
        self.__course = course
        self.__occupation = occupation

    def set_course(self, course):
        raise TypeError("You are not allowed to enter")

    def set_occupation(self, occupation):
        if occupation=="Full Time" or occupation=="Part time":
            self.__occupation = occupation
        else:
            raise Exception("Enter correctly your occupation")

    def set_co_hours(self, co_hours):
        if 2<= co_hours <= 18:
            self.__co_hours = co_hours
        else:
            raise Exception("Your course must be between 2 to 18")

    def set_salary(self, salary):
    #2to18 hours is full time
    #1to9 hours is part time

    def __ocup

    def set_title(self, title):
        title_list=["TA", "LR", "SLR", "APR"]
        if title in title_list:
            self.__title = title
        else:
            raise Exception("You are not allowed to enter")





type = input("Choose the option related to you:")
name = input("Enter your name:")
pass_id = input("Enter your Passport ID:")
email = input("Enter your email:")
bd = input("Enter your birthday date as YYYY/MM/DD:")
gender = input("Enter your gender:")
nationality = input("Enter your nationality:")
phone = input("Enter your phone")

user = User(type, name, bd, pass_id, email, gender, nationality, phone)


def read_from_file(file_path):
    try:
        # Open the file in read mode
        with open(file_path, "r") as file:
            # Read the content of the file
            content = file.read()

        words = content.split()

        return words  # return a list that contains the words

        # Print the content of the file
        print(f"The content of the file {file_path} is:\n{content}")
    except Exception as e:
        # Print any error that occurs during the process
        print(f"An error occurred: {e}")
    finally:
        print("read_from_file function execution completed.")


print(read_from_file("input.txt"))