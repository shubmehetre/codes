

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
            pass
        except ArithmeticError:
            pass
        except ValueError:
            pass

        else:
                return ans
def exception_handler():
    pass