

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

            elif 85 <= grade_input < 88:
                print("PASED: GPA is 2.00")
            
            elif 82 <= grade_input < 85:
                print("PASSED: GPA is 2.25")
            
            elif 79 <= grade_input < 82:
                print("PASSED: GPA is 2.5")
            
            elif 76 <= grade_input < 79:
                print("PASSED: GPA is 2.75")

            elif 75 <= grade_input < 76:
                print("PASSED GPA is 3.00")

            elif grade_input < 75:
                print("FAILED: GPA is 5.00")
        
            else:
                print("FAILED: DROPPED")
                
    except ValueError:
        print("ERROR: Grade must be Digit only")

   
get_student_grade()