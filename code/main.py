from datetime import datetime

class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.generation = self.get_generation()
        self.life_path_num = self.get_life_path_number()

    def get_lucky_color(self):
        lucky_colors = {
            1: "Red", 2: "Orange", 3: "Yellow", 4: "Green", 5: "Blue",
            6: "Indigo", 7: "Violet", 8: "Gray", 9: "Gold",
            11: "Silver", 22: "Platinum", 33: "Diamond"
        }
        return lucky_colors.get(self.life_path_num)

    def get_life_path_number(self):
        life_path_num = int(self.birthday)
        while life_path_num > 9:
            life_path_num = Helper.sum_digits(life_path_num)
            if Helper.is_master_number(life_path_num):
                break
        return life_path_num

    def get_generation(self):
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

class Helper:
    @staticmethod
    def sum_digits(num):
        total = 0
        while num > 0:
            digit = num%10
            total = total + digit
            num = num//10
        return total

    @staticmethod
    def is_master_number(num):
        master_number = [11,22,33]
        return num in master_number

    @staticmethod
    def lifePathCompare(person1, person2):
        return person1.life_path_num == person2.life_path_num
    

    @staticmethod
    def get_valid_birthday_input():
        while True:
            birthdate = input("Enter birthday (DD-MM-YYYY or DD Month YYYY): ")
            try:
                formatted_date = datetime.strptime(birthdate, "%d-%m-%Y").strftime("%d%m%Y")
                return formatted_date
            except ValueError:
                try:
                    formatted_date = datetime.strptime(birthdate, "%d %B %Y").strftime("%d%m%Y")
                    return formatted_date
                except ValueError:
                    print("Invalid birthday format. Please use either DD-MM-YYYY or DD Month YYYY.\n")

def main():
    birthdate = Helper.get_valid_birthday_input()
    person = Person("Raihan", birthdate)
    person2 = Person("Anakin Skywalker", "16111942")
    print("Lucky Color:", person.get_lucky_color())
    print(person.generation)

    print(f"{person.name} life path number is {person.life_path_num}")
    if person.life_path_num in [11,22,33]:
        print("Which is a Master Number")

    print(f"{person2.name} life path number is {person2.life_path_num}")
    if(Helper.lifePathCompare(person,person2)):
        print("Their life path number is same")
    else:
        print("Their life path number is not same")

if __name__ == '__main__':
    main()
    