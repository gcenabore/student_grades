

def get_student_grade():

    try:
        grade_input = float(input("Please enter your grade: "))

        if 50 <= grade_input <= 100:

            if grade_input >= 97:
                print("PASSED: GPA is 1.00")
            
            elif 94 <= grade_input <97:
                print("PASSED: GPA is 1.25")
            
            elif 91 <= grade_input < 94:
                print("PASSED: GPA is 1.5")

            elif 88 <= grade_input < 91:
                print("PASSED: GPA is 1.75")

    except ValueError:
        print("ERROR: Grade must be Digit only")

   
get_student_grade()