import json
import os

class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = {}
        self.scores = {}
        self.average = 0
        self.grade = ""

    def add_subject(self, subject):
        self.subjects[subject] = 0
        self.scores[subject] = 0

    def update_score(self, subject, score):
        if subject in self.subjects:
            self.scores[subject] = score
            self.calculate_average()
            self.calculate_grade()
        else:
            print("Subject not found.")

    def calculate_average(self):
        total_score = sum(self.scores.values())
        self.average = total_score / len(self.scores)

    def calculate_grade(self):
        if self.average >= 90:
            self.grade = "A"
        elif self.average >= 80:
            self.grade = "B"
        elif self.average >= 70:
            self.grade = "C"
        elif self.average >= 60:
            self.grade = "D"
        else:
            self.grade = "F"

    def __str__(self):
        report_card = f"Name: {self.name}\n"
        report_card += "Subjects:\n"
        for subject, score in self.scores.items():
            report_card += f"{subject}: {score}\n"
        report_card += f"Average: {self.average:.2f}\n"
        report_card += f"Grade: {self.grade}\n"
        return report_card

def save_data(students):
    with open("student_data.json", "w") as file:
        json.dump([{"name": student.name, "subjects": student.subjects, "scores": student.scores} for student in students], file)

def load_data():
    if os.path.exists("student_data.json"):
        with open("student_data.json", "r") as file:
            data = json.load(file)
            students = []
            for student_data in data:
                student = Student(student_data["name"])
                for subject in student_data["subjects"]:
                    student.add_subject(subject)
                    student.scores[subject] = student_data["scores"][subject]
                    student.calculate_average()
                    student.calculate_grade()
                students.append(student)
            return students
    else:
        return []

def main():
    students = load_data()
    while True:
        print("\nStudent Report Card App")
        print("1. Add student")
        print("2. Add subject to student")
        print("3. Update student score")
        print("4. View student report card")
        print("5. Save data")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter student name: ")
            student = Student(name)
            students.append(student)
            print("Student added successfully.")
        elif choice == "2":
            name = input("Enter student name: ")
            for student in students:
                if student.name == name:
                    subject = input("Enter subject name: ")
                    student.add_subject(subject)
                    print("Subject added successfully.")
                    break
            else:
                print("Student not found.")
        elif choice == "3":
            name = input("Enter student name: ")
            for student in students:
                if student.name == name:
                    subject = input("Enter subject name: ")
                    score = float(input("Enter score: "))
                    student.update_score(subject, score)
                    print("Score updated successfully.")
                    break
            else:
                print("Student not found.")
        elif choice == "4":
            name = input("Enter student name: ")
            for student in students:
                if student.name == name:
                    print(student)
                    break
            else:
                print("Student not found.")
        elif choice == "5":
            save_data(students)
            print("Data saved successfully.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

