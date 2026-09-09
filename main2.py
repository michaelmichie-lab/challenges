class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi! My name is {self.name} and I am {self.age} years old.")


class Club:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, student):
        self.members.append(student)
        print(f"{student.name} joined {self.name}!")

    def show_members(self):
        print(f"\n--- {self.name} Members ---")
        if not self.members:
            print("No members yet.")
        else:
            for student in self.members:
                print(f"- {student.name}")


student1 = Student("Alice", 18)
student2 = Student("Brian", 19)
student3 = Student("Faith", 18)
student4 = Student("David", 20)

club = Club("Gaming Club")

club.add_member(student1)
club.add_member(student2)
club.add_member(student3)
club.add_member(student4)

club.show_members()
club.show_members()