#Write a program using nested while loop. If the value is divided by two, then it will run an infinite loop of the bye.

a = False

while not a:
    try:
        b = int(input('Enter number please.'))
        
        while b%2==0:
            print('BYE BYE')
            a=True



    except ValueError:
        print('You did everything wrong!!!!!')