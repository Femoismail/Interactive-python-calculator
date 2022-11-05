print("---Welcome to the python calculator---")
option = ""
while option != "1" or option == "2" or option == "3" or option == "4" or option != "q" or option != "Q": # To keep us in the options loop if no option is choosen.
    print("""
Calculator options.

Please enter: 1 - For Addition
Please enter: 2 - For Subtraction
Please enter: 3 - For Division
Please enter: 4 - For multiplication
Please type: Q - To exit program
""")

    option = input("Please enter your option :")  # option input field

    if option == "q" or option == "Q": # Exit program.
        print("The program will exit.")
        break

    if option == "1": # if option 1 is choosen Addition should take place
        print("")
        print(f"Choosen option {option} Addition.") 
        print("")
        print("Please choose 2 numbers.")
        print("")
        def number(value1, value2): # addition function
            answer = float(value1) + float(value2)
            print(f"Your answer is = {answer}")
            return

        while (True): # a loop is used to check if the length of the input matches the requirements as well as if there are any errors we have a try and except function to capture those as well.
            try:
                value1 = ""
                if len(value1) < 1:
                    value1 = input("please enter number1 :")
                    value1 = float(value1)
                    break
            except:
                print("This is not a number")

        while (True):
            try:
                value2 = ""
                if len(value2) < 1:
                    value2 = input("please enter number2 :")
                    print("")
                    value2 = float(value2)
                    break
            except:
                print("This is not a number")
                
        number(value1, value2)


    if option == "2": # option 2 is choosen Subtraction should take place
        print("")
        print(f"Choosen option {option} Subtraction.") 
        print("")
        print("Please choose 2 numbers.")
        print("")
        def number(value1, value2):
            answer = float(value1) - float(value2)
            print(f"Your answer is = {answer}")
            return

        while (True): # a loop is used to check if the length of the input matches the requirements as well as if there are any errors we have a try and except function to capture those as well.
            try:
                value1 = ""
                if len(value1) < 1:
                    value1 = input("please enter number1 :")
                    value1 = float(value1)
                    break
            except:
                print("This is not a number")

        while (True):
            try:
                value2 = ""
                if len(value2) < 1:
                    value2 = input("please enter number2 :")
                    print("")
                    value2 = float(value2)
                    break
            except:
                print("This is not a number")
                
        number(value1, value2)  


    if option == "3": # option 3 is choosen Division should take place
        print("")
        print(f"Choosen option {option} Division.") 
        print("")
        print("Please choose 2 numbers.")
        print("")
        def number(value1, value2):
            answer = float(value1) / float(value2)
            print(f"Your answer is = {answer}")
            return
        
        while (True): # a loop is used to check if the length of the input matches the requirements as well as if there are any errors we have a try and except function to capture those as well.
            try:
                value1 = ""
                if len(value1) < 1:
                    value1 = input("please enter number1 :")
                    value1 = float(value1)
                    break
            except:
                print("This is not a number")

        while (True):
            try:
                value2 = ""
                if len(value2) < 1:
                    value2 = input("please enter number2 :")
                    print("")
                    value2 = float(value2)
                    break
            except:
                print("This is not a number")
                
        number(value1, value2)

    
    
    if option == "4": # option 4 is choosen Multiplication should take place
        print("")
        print(f"Choosen option {option} multiplication.")
        print("")
        print("Please choose 2 numbers.")
        print("")
        def number(value1, value2):
            answer = float(value1) * float(value2)
            print(f"Your answer is = {answer}")
            return

        while (True):  # a loop is used to check if the length of the input matches the requirements as well as if there are any errors we have a try and except function to capture those as well.
            try:
                value1 = ""
                if len(value1) < 1:
                    value1 = input("please enter number1 :")
                    value1 = float(value1)
                    break
            except:
                print("This is not a number")

        while (True):
            try:
                value2 = ""
                if len(value2) < 1:
                    value2 = input("please enter number2 :")
                    print("")
                    value2 = float(value2)
                    break
            except:
                print("This is not a number")
                
        number(value1, value2)

    
