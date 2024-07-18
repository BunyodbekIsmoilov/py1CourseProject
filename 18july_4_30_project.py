class User:
    def __init__(self, type, name, birth_date, pass_id, email, gender, nationality, phone_num):
        self.__type(type)
        self.__name(name)
        self.__birth_date(birth_date)
        self.__email(email)
        self.__gender(gender)
        self.__nationality(nationality)
        self.__phone_num(phone_num)
        self._pass_id(pass_id)

    def set_type(self, type):
        self.__type = type

    def set_name(self, name):
        self.__name = name

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def set_pass_id(self, pass_id):
        self._pass_id = pass_id

    def set_email(self, email):
        self.__email = email

    def set_gender(self, gender):
        self.__gender = gender

    def set_nationality(self, nationality):
        self.__nationality = nationality

    def set_phone_num(self, phone_num):
        self.__phone_num = phone_num

    def get_type(self):
        return self.__type

    def get_name(self):
        return self.__name

    def get_birth_date(self):
        return self.__birth_date

    def get_pass_id(self):
        return self._pass_id

    def get_email(self):
        return self.__email

    def get_gender(self):
        return self.__gender

    def get_nationality(self):
        return self.__nationality

    def get_phone_num(self):
        return self.__phone_num
