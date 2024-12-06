

def get_student_grade():

    try:
        grade_input = float(input("Please enter your grade: "))

        print(grade_input)
        
    except ValueError:
        print("ERROR: Grade must be Digit only")

   
get_student_grade()