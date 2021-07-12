def divide_two_nos(num1, num2):
    """division of 2 numbers. Error handling practice"""
    while True:
        # num1 = input("input a number: ")
        # if num1 == 'q':
        #     break

        # num2 = input("input a number: ")
        # if num2 == 'q':
        #     break

        try:
            ans = int(num1) / int(num2)
        except ZeroDivisionError:
            print("Cant divide by zero\n")
        except ArithmeticError:
            print("pls check you input\n")
        except ValueError:
            print("Kindly input numerical values\n")

        else:
                return ans
