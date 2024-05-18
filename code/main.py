from datetime import datetime

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.generation = self.getGeneration()
        self.life_path_num = self.get_life_path_number()

    def get_lucky_color(self):
        lucky_colors = {
            1: "Red", 2: "Orange", 3: "Yellow", 4: "Green", 5: "Blue",
            6: "Indigo", 7: "Violet", 8: "Gray", 9: "Gold",
            11: "Silver", 22: "Platinum", 33: "Diamond"
        }
        return lucky_colors.get(self.life_path_num)

    def is_master_number(self,num):
        master_number = [11,22,33]
        return num in master_number

    def get_life_path_number(self):
        life_path_num = int(self.birthday)
        while life_path_num > 9:
            life_path_num = self.sum_digits(life_path_num)
            if self.is_master_number(life_path_num):
                print(f"{life_path_num} is master number")
                break
        return life_path_num

    def sum_digits(self,num):
        total = 0
        while num > 0:
            digit = num%10
            total = total + digit
            num = num//10
        return total

    def getGeneration(self):
        year = int(self.birthday[-4:])
        if 1901 <= year <= 1945:
            return "Silent Generation"
        elif 1946 <= year <= 1964:
            return "Baby Boomers"
        elif 1965 <= year <= 1979:
            return "Generation X"
        elif 1980 <= year <= 1994:
            return "Millennials"
        elif 1995 <= year <= 2009:
            return "Generation Z"
        elif 2010 <= year <= 2024:
            return "Generation Alpha"
        else:
            return "Unknown Generation"

class BirthdayComparer:
    @staticmethod
    def compare(person1, person2):
        print(f"{person1.name} life path number is {person1.life_path_num}\n{person2.name} life path number is {person2.life_path_num}")
        if(person1.life_path_num == person2.life_path_num):
            print("life path number is same")
        else:
            print("life path number is not same")

def parse_birthday(birthday):
    try:
        return datetime.strptime(birthday, "%d-%m-%Y").strftime("%d%m%Y")
    except ValueError:
        try:
            return datetime.strptime(birthday, "%d %B %Y").strftime("%d%m%Y")
        except ValueError:
            return False

def get_valid_birthday_input():
    while True:
        birthdate = input("Enter birthday (DD-MM-YYYY or DD Month YYYY): ")
        birthdate = parse_birthday(birthdate)
        if birthdate:
            return birthdate
        else:
            print("Invalid birthday format. Please use either DD-MM-YYYY or DD Month YYYY.")

def main():
    birthdate = get_valid_birthday_input()
    person = Person("Raihan", birthdate)
    person2 = Person("Anakin Skywalker", "16111942")
    print("Lucky Color:", person.get_lucky_color())
    print(person.generation)
    BirthdayComparer.compare(person,person2)

if __name__ == '__main__':
    main()