#Lucas Lima
#This program identifies if a number from 1-100 is prime or composite and also finds some other properties of that number and its relationship with primes

#The = assignment is used for assigning a value to a variable
name = str(input("Enter your name: "))

#string addition is used for the concatenation of multiple strings
print("Hello" + " " + name + ", this program will check if a number you think of from 1-100 is prime or not.")

def prime_classifier(num):
    #All prime numbers are odd except 2
    #the modulus operator divides a number with another number and outputs the remainder of the quotient
    if num%2 == 0 and not num == 2:
        num_class = "Not prime"
        
    #1 is universally agreed as non-prime
    elif input_num == 1:
        num_class = "Not prime"

    #Most commonly known primes from for small values 1-10
    elif num == 2 or num == 3 or num == 5 or num == 7 or num == 11:
        num_class = "Prime"

    #The following code applies a primality test known as Trial Division
    #The method essentially states that if an integer is divisble by any prime number between 2 and the square root of that integer, then it is not prime
    else:
    #the ** operator is for exponentiation of numbers
        test_num = int(num**(0.5))
    #The following block of conditions finds the set of prime numbers used for this method that fit the range 1-10, or the square root of all integers from 1-100
        if test_num >= 7:
            prime_nums = [2, 3, 5, 7, 11, 13, 17, 19]

        elif test_num < 7 and test_num >= 5:
            prime_nums = [2, 3, 5]

        elif test_num < 5 and test_num >= 3:
            prime_nums = [2, 3]

        elif test_num == 2:
            prime_nums = [2]
    #This creates a list of the numbers that represent the remainder of the number when divided by the identified prime numbers
    #A for loop is used to find the remainder when the number is divided by each element in the list
        remainders = [num%i for i in prime_nums]
    #If the number is found to be divisible by one of the identified prime numbers, then the number itself is composite
        p=0
        while p < 2:  
            for i in remainders:
                if i == 0:
                    num_class = "Not prime"
                else:
                    num_class = "Prime"
            p += 1
    return(num_class)

input_num = int(input(" Please enter an integer between 1 and 100: "))
print(prime_classifier(input_num))

response = str(input("Would you like to know what the smallest prime factor of your number is? Please enter yes or no: "))
if response == "yes":
#The prime factors of a prime number are 1 and itself
    if prime_classifier(input_num) == "Prime":
        prime_factor = 1
        print("The smallest prime factor of your number is: " + str(prime_factor))
    else:
#Trivially, each number from 1-100 that is not prime has a smallest prime factor that is <= 7 
        if input_num%2 == 0:
            prime_factor = 2
        elif input_num%3 == 0:
            prime_factor = 3
        elif input_num%5 == 0:
            prime_factor = 5
        elif input_num%7 == 0:
            prime_factor = 7
#1 has no prime factors
        else:
            prime_factor = "empty set or undefined"
        print("The smallest prime factor of your numer is: " + str(prime_factor))



prop_response = str(input("Would you like to see some other properties of your number? Please enter yes or no: "))

if prop_response == "yes":
#Any number will output another prime factor or composite factor when divided by one of its other prime factors 
#The / operator divides a number with another number
    factor = input_num
#Shortcut operators can be used to simplify the process of assigning a new value to an existing variable by applying an arithmetic operator on it such as / in this case
    factor /= prime_factor
    if input_num == 10:
#Numbers 1-9 only have only one digit and are an exception to the following calculations
        sum_digits = input_num
#100 is conveniently, the only three-digit number in this set
    elif input_num != range(1,99):
        sum_digits = 1
    else:
#The digits of a two-digit number can be found by using floor division and the modulus operators like so
#The + operator is used for adding numbers
        sum_digits = (input_num//10 + input_num%10)

    if input_num < 10:
        diff_digits = input_num
    elif input_num == 100:
        diff_digits = 1
    else:
#The - operator is used for subtracting two numbers       
        diff_digits = input_num//10 - input_num%10

    if input_num < 10:
        prod_digits = input_num
    elif input_num == 100:
        prod_digits = 0
    else:
#The * operator is used for multiplying two numbers
        prod_digits = (input_num//10)*(input_num%10)

    print("The factor left from the quotient of your number and its least prime factor is: " + str(factor))
    print("The sum of the digits of your number is: " + str(sum_digits))
    print("The different of the digits of your number is: " + str(diff_digits))
    print("The product of the digits of your number is: " + str(prod_digits))

#String multiplication is used for repeating strings
print(2*"Bye" +", " +name)
    



    
