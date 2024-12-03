#Write a program to understand how the value error exception works?

try:
    a = int(input('Enter the value:'))
    print('The number that has been entered by the use is:', a)
    


except ValueError as ex:
    print("Exception: ",ex)