

def get_student_grade():

    try:
        grade_input = float(input("Please enter your grade: "))

        if 50 <= grade_input <= 100:

            if grade_input >= 79:
                print("PASSED: GPA is 1.00")
        

    except ValueError:
        print("ERROR: Grade must be Digit only")

   
get_student_grade()