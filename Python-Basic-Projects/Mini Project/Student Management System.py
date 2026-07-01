# Project 1: Student Management System

# Initialize empty dictionary to store records
student_db = {}


# Function to calculate letter grade
def calculate_grade(percentage):
    if percentage >= 90:
        return "A++"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B+"
    elif percentage >= 50:
        return "B"
    else:
        return "F"


# Function to add a new student
def add_student():
    print("\nAdd Student Record ")
    roll_no = int(input("Enter Roll Number: "))

    # Check if roll number already exists
    if roll_no in student_db:
        print("This Roll Number already exists!")
        return

    name = input("Enter Student Name: ")

    # Take marks for 5 subjects using a while loop
    marks = []
    print("\nEnter marks for 5 subjects:-")
    i = 1
    while i <= 5:
        mark = float(input(f"Subject {i} Marks: "))
        if mark < 0 or mark > 100:
            print("Marks must be between 0 and 100! Please re-enter.")
        else:
            marks.append(mark)
            i += 1  

    # Calculate total and percentage
    total_marks = sum(marks)
    percentage = total_marks / 5
    grade = calculate_grade(percentage)

    # Save to dictionary
    student_db[roll_no] = {
        "name": name,
        "marks": marks,
        "percentage": percentage,
        "grade": grade,
    }
    print("\nRecord Added Successfully ")
    print(f"Name: {name} | Roll: {roll_no} | %: {percentage:.2f} | Grade: {grade}")


# Function to view all student profiles
def view_all():
    print("\nAll Student Records ")
    if not student_db:
        print("Database is empty! No records found.")
        return

    for roll_no, profile in student_db.items():
        print(f"Roll No: {roll_no} | Name: {profile['name']} | Percentage: {profile['percentage']:.2f}% | Grade: {profile['grade']}")


# Function to search student profile by roll number
def search_student():
    print("\nSearch Student ")
    roll_no = int(input("Enter Roll Number to search: "))

    if roll_no in student_db:
        student = student_db[roll_no]
        print(f"\nStudent Profile Found:")
        print(f"Roll Number : {roll_no}")
        print(f"Name        : {student['name']}")
        print(f"Percentage  : {student['percentage']:.2f}%")
        print(f"Grade       : {student['grade']}")
    else:
        print("Profile Not Found.")


# Function to modify existing data
def update_student():
    print("\nUpdate Student Record ")
    roll_no = int(input("Enter Roll Number to update: "))

    if roll_no in student_db:
        print(f"Updating profile for: {student_db[roll_no]['name']}")

        new_name = input("Enter new name (Leave blank to keep old): ")
        if new_name.strip():
            student_db[roll_no]["name"] = new_name

        change_marks = (input("Do you want to update marks? (yes/no): ").strip().lower())
        
        if change_marks == "yes" or change_marks == "y":
            new_marks = []
            print("Enter new marks for 5 subjects:")
            i = 1
            while i <= 5:
                m = float(input(f"Subject {i} New Marks: "))
                if m < 0 or m > 100:
                    print("Marks must be between 0 and 100! Please re-enter.")
                else:
                    new_marks.append(m)
                    i += 1

            # Update scores and recalculate grade
            student_db[roll_no]["marks"] = new_marks
            student_db[roll_no]["percentage"] = sum(new_marks) / 5
            student_db[roll_no]["grade"] = calculate_grade(student_db[roll_no]["percentage"])

        print("Student details updated.")
    else:
        print("Student roll number not found.")


# Function to delete a student profile
def delete_student():
    print("\nDelete Student Record ")
    roll_no = int(input("Enter Roll Number to delete: "))

    if roll_no in student_db:
        while True:
            confirm = (input(f"Are you sure you want to delete {student_db[roll_no]['name']}? (yes/no): ").strip().lower())

            if confirm == "yes" or confirm == "y":
                student_db.pop(roll_no)
                print("Record deleted successfully.")
                break
            elif confirm == "no" or confirm == "n":
                print("Deletion cancelled. Student record is safe.")
                break
            else:
                print("Invalid input! Please type exactly 'yes' or 'no'.")
    else:
        print("Roll number does not exist.")


# Main Menu Loop
while True:
    print("\nSTUDENT MANAGEMENT SYSTEM ")
    print("1. Add Student")
    print("2. View All")
    print("3. Search")
    print("4. Update")
    print("5. Delete")
    print("6. Exit")

    choice = input("Enter choice (1-6): ").strip()

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid number from 1 to 6.")