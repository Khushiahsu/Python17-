#Write a program to check how the exceptions and finally statement works

try:
    num1,num2=eval(input("Enter 2 numbers separating by comma: "))
    num3 = num1/num2
    print('The result is:',num3)

except ZeroDivisionError:
  print('The error here is your divsion is invalid give a proper division!')

except SyntaxError:
    print('I believe that you are missing a comma if you are reading this.')

except:
   print('The error is IndentationError')

else:
   print("No exception!!!!")


finally:
   print("I will run this code no matter what hahahaahha")