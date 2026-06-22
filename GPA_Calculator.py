#Cumlative GPA Calculator
while True:
    def total_qty_points():
        while True:
            try:
                n_course=int(input("Input Number of Course:"))
                break
            except ValueError:
                print("Invalid Input!!! Please Enter Number of Course!!!")
        total_points=0
        for i in range (1,n_course+1):
                    while True:
                        try:
                            grade=float(input(f"Enter Grade for Each Course {i}:"))
                            if 0<=grade<=4:
                                break
                            print("GPA Must be between 0 and 4!!!")
                        except ValueError:
                            print("Invald Input!!! Please Enter Valid GPA for Each Course!!!")
                    total_points+=grade*3   
        credit_attempt=n_course*3
        final_gpa=total_points/credit_attempt
        print("Total Grade Attempt:",credit_attempt)
        return total_points,credit_attempt,final_gpa
    total_points,credit_attempt,final_gpa=total_qty_points()
    print("Total of Quality Points:",total_points)
    print("Final GPA",final_gpa)
    break