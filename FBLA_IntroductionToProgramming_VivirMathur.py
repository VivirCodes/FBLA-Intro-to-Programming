# Asks the user to choose between weighted and unweighted GPA
print("Which type of GPA would you like to calculate?")
print("1. Unweighted GPA")
print("2. Weighted GPA")

choice = input("Enter 1 or 2: ")

# Checks if the selected GPA type is valid
while choice not in ['1', '2']:
    print("Invalid option. Please enter a valid GPA option.")
    choice = input("Enter 1 or 2: ")


# Defines the function that calculates the UNWEIGHTED GPA
def calculate_gpa_unweighted(grades):
    grade_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

    total_courses = len(grades)
    total_grade_points = sum(grade_points[grade] for grade in grades)

    gpa = total_grade_points / total_courses
    return gpa

# Takes user input for grades
grades_list = []

# Only asking for grade when if enters '1' (Unweighted)
if choice == '1':
    num_courses = int(input("Enter the number of courses: "))
    
    for i in range(num_courses):
        grade = input(f"Enter the grade for Course {i + 1} (A, B, C, D, or F): ").upper()

        # Checks if the grade is valid
        while grade not in ['A', 'B', 'C', 'D', 'F']:
            print("Invalid grade. Please enter a valid grade.")
            grade = input(f"Enter the grade for Course {i + 1} (A, B, C, D, or F): ").upper()

        # Adds grades into a list
        grades_list.append(grade)

# Calculates GPA, rounds it to nearest hundredth, and prints it
    result_unweighted_gpa = calculate_gpa_unweighted(grades_list)
    rounded_gpa = round(result_unweighted_gpa, 2)
    print(f"Your Unweighted GPA is: {rounded_gpa}")


# Defines the function that calculates the WEIGHTED GPA
def calculate_gpa_weighted(grades):
    grade_weights = {'REGULAR': {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0},
        'HONORS': {'A': 4.5, 'B': 3.5, 'C': 2.5, 'D': 1.0, 'F': 0.0},
        'AP': {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 1.0, 'F': 0.0},
        'IB': {'A': 5.0, 'B': 4.0, 'C': 3.0, 'D': 1.0, 'F': 0.0}}

    total_courses = len(grades)
    total_weighted_grade_points = 0

    for grade, class_type in grades:
        total_weighted_grade_points += grade_weights[class_type][grade]

    weighted_gpa = total_weighted_grade_points / total_courses
    return weighted_gpa

# Takes user input for grades
grades_list = []

# Asking for grade and type of class if user enters '2' (Weighted)
if choice == '2':
    num_courses = int(input("Enter the number of courses: "))
    
    for i in range(num_courses):
        grade = input(f"Enter the grade for Course {i + 1} (A, B, C, D, or F): ").upper()

        # Checks if the grade is valid
        while grade not in ['A', 'B', 'C', 'D', 'F']:
            print("Invalid grade. Please enter a valid grade.")
            grade = input(f"Enter the grade for course {i + 1} (A, B, C, D, or F): ").upper()

        # The class types are Regular, Honors, AP, and IB
        class_type = input(f"Enter the type of class for course {i + 1} (Regular, Honors, AP, IB): ")

        # Checks if the class type is valid
        while class_type.upper() not in ['REGULAR', 'HONORS', 'AP', 'IB']:
            print("Invalid class type. Please enter a valid class type.")
            class_type = input(f"Enter the type of class for course {i + 1} (Regular, Honors, AP, IB): ")

        # Adds grades and type of class into a list
        grades_list.append((grade, class_type.upper()))

# Calculates GPA, rounds it to nearest hundredth, and prints it
    result_weighted_gpa = calculate_gpa_weighted(grades_list)
    rounded_gpa = round(result_weighted_gpa, 2)
    print(f"Your Weighted GPA is: {rounded_gpa}")