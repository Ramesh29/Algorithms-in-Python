
def wins_rock_scissors_paper( str1, str2):
    if ( str1.lower() == "scissor" and str2.lower() == "paper" ) or ( str1.lower() == "paper" and str2.lower() == "rock" ) or ( str1.lower() == "rock" and str2.lower() == "scissor" ):
        return True
    return False


# function to return the factorial of a number
def factorial(num):
    if num == 1: 
        return 1
    else:
        return num * factorial( num - 1 )
    

# function to return the nth Fibonacci number in the Fibonacci sequence.
def Fibonacci(num):
    if num == 1 or num == 2:
        return 1
    else:
        return Fibonacci(num-1) + Fibonacci(num-2)
    
    