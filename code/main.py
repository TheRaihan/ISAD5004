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

    def is_master_number(self):
        # Check if the life path number is a master number
        pass

    def get_life_path_number(self):
        # Get the life path number
        pass

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
        return datetime.strptime(birthday, "%d-%m-%Y").strftime("%d-%m-%Y")
    except ValueError:
        try:
            return datetime.strptime(birthday, "%d %B %Y").strftime("%d-%m-%Y")
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



# person1 = Person("Alice", "1990-05-15")
# person2 = Person("Bob", "1985-10-20")

# Example usage:
name = input("Enter name: ")
birthdate = get_valid_birthday_input()
person = Person(name, birthdate)

print(birthdate)

# person1_life_path_number = LifePathCalculator.calculate(person1.birthday)


# person1_lucky_colour = person1.identify_lucky_colour()

# is_person1_master_number = person1.is_master_number()

# same_life_path_number = BirthdayComparer.compare(person1, person2)

# print(f"{person1.name}'s life path number: {person1_life_path_number}")


# print(f"{person1.name}'s lucky colour: {person1_lucky_colour}")

# print(f"{person1.name} is a master number: {is_person1_master_number}")

# print(f"Life path numbers of {person1.name} and {person2.name} are the same: {same_life_path_number}")
