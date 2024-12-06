

def get_student_grade():

    try:
        grade_input = float(input("Please enter your grade: "))

        if 50 <= grade_input <= 100:

            if grade_input >= 97:
                result = "PASSED - 1.00"
            
            elif 94 <= grade_input <97:
                result = "PASSED - 1.25"
            
            elif 91 <= grade_input < 94:
                result = "PASSED - 1.5"

            elif 88 <= grade_input < 91:
                result = "PASSED - 1.75"

            elif 85 <= grade_input < 88:
                result = "PASSED - 2.00"
            
            elif 82 <= grade_input < 85:
                result = "PASSED - 2.25"
            
            elif 79 <= grade_input < 82:
                result = "PASSED - 2.5"
            
            elif 76 <= grade_input < 79:
                result = "PASSED - 2.75"

            elif 75 <= grade_input < 76:
                result = "PASSED - 3.00"

            elif grade_input < 75:
                result = "FAILED - 5.00"
        
            else:
                return None
            
            print(f"Your Grade is equivalent to {result}")
    
        else:
            print("INVALID: Enter a grade from 50-100 only.")
            
    except ValueError:
        print("ERROR: Grade must be Digit only")

   
get_student_grade()