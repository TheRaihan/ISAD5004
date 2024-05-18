from datetime import datetime


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def calculate_life_path_number(self):
        # Calculate life path number based on the birthday
        pass

    def identify_lucky_colour(self):
        # Identify lucky color based on the life path number
        pass

    def is_master_number(self,num):
        master_number = [11,22,23]
        return True

    def get_life_path_number(self,num):
        total = 0
        while num > 0:
            digit = num%10
            total = total + digit
            num = num//10
        return total

class LifePathCalculator:
    @staticmethod
    def calculate(birthday):
        # Calculate life path number
        pass

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
    # person1 = Person("Alice", "1990-05-15")
    # person2 = Person("Bob", "1985-10-20")

    name = "Raihan"
    birthdate = get_valid_birthday_input()
    person = Person(name, birthdate)

    life_path_num = int(birthdate)
    while life_path_num > 9:
        life_path_num = person.get_life_path_number(life_path_num)
        if person.is_master_number(life_path_num):
            print(f"{life_path_num} is master number")
            break

    print(life_path_num)

    # person1_life_path_number = LifePathCalculator.calculate(person1.birthday)

    # person1_lucky_colour = person1.identify_lucky_colour()

    # is_person1_master_number = person1.is_master_number()

    # same_life_path_number = BirthdayComparer.compare(person1, person2)

    # print(f"{person1.name}'s life path number: {person1_life_path_number}")


    # print(f"{person1.name}'s lucky colour: {person1_lucky_colour}")

    # print(f"{person1.name} is a master number: {is_person1_master_number}")

    # print(f"Life path numbers of {person1.name} and {person2.name} are the same: {same_life_path_number}")


if __name__ == '__main__':
    main()