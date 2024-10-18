class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_average(self):
        return sum(self.scores) / len(self.scores)

    def is_passing(self, passing_score=40):
        return all(score >= passing_score for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}

    def add_student(self, name, scores):
        new_student = Student(name, scores)
        self.students[name] = new_student

    def calculate_class_average(self):
        total = 0
        for student in self.students.values():
            total += student.calculate_average()
        return total / len(self.students) if self.students else 0

    def display_student_performance(self):
        for student in self.students.values():
            average = student.calculate_average()
            passing = "Passing" if student.is_passing() else "Failing"
            print(f"Student: {student.name}, Average Score: {average:.2f}, Status: {passing}")


def get_student_input():
    while True:
        try:
            name = input("Enter student's name (or type 'done' to finish): ").strip()
            if name.lower() == 'done':
                break

            scores = []
            for subject in ['Math', 'Science', 'English']:
                score = int(input(f"Enter {subject} score for {name}: "))
                scores.append(score)

            yield name, scores

        except ValueError:
            print("Invalid input! Please enter numeric values for the scores.")


def main():
    tracker = PerformanceTracker()

    # Collect input from the teacher
    for name, scores in get_student_input():
        tracker.add_student(name, scores)

    # Display student performances
    print("\nStudent Performance Report:")
    tracker.display_student_performance()

    # Display the overall class average
    class_average = tracker.calculate_class_average()
    print(f"\nClass Average Score: {class_average:.2f}")


# Run the main program
if __name__ == "__main__":
    main()
