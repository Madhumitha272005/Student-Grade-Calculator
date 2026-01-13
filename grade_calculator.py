def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining 🌟"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up 👍"
    elif 70 <= marks <= 79:
        return "C", "Good effort! You can do even better 😊"
    elif 60 <= marks <= 69:
        return "D", "You passed! Work harder next time 💪"
    else:
        return "F", "Don't give up! Practice makes perfect 💡"


# Get student name
student_name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid input! Marks must be between 0 and 100.")
    except ValueError:
        print("❌ Please enter numeric values only.")

# Calculate grade
grade, message = calculate_grade(marks)

# Display result
print(f"\n📊 RESULT FOR {student_name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
