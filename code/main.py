from datetime import datetime


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        # self.generation = self.getGeneration()
        self.life_path_num = self.get_life_path_number()

    def get_lucky_color(self, life_path_number):
        """Determines the lucky color based on the Life Path Number."""
        lucky_colors = {
            1: "Red", 2: "Orange", 3: "Yellow", 4: "Green", 5: "Blue",
            6: "Indigo", 7: "Violet", 8: "Gray", 9: "Gold",
            11: "Silver", 22: "Platinum", 33: "Diamond"
        }
        return lucky_colors.get(life_path_number)

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


# class LifePathCalculator:
#     @staticmethod
#     def calculate(birthday):
#         pass

class BirthdayComparer:
    @staticmethod
    def compare(person1, person2):
        pass

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

    # print(person.generation)

    print(f"{person.name} life path number is {person.life_path_num}\n{person2.name} life path number is {person2.life_path_num}")
    
    if(person.life_path_num == person2.life_path_num):
        print("life path number is same")
    else:
        print("life path number is not same")


if __name__ == '__main__':
    main()