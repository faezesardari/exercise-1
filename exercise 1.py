import math
op = input("enter op(+ ,- , * , / , sin , cos , tan , cot , ! ,sqrt)")

if op == "+":
  num1 = int(input("enter num1 :")) 
  num2 = int(input("enter num2 :"))
  result = num1 + num2

if op =="-":
 num1 = int(input("enter num1 : "))
 num2 = int(input("enter num2 :"))
 result =num1 - num2

if op == "*":
 num1 = int(input("enter num1 :"))
 num2 = int(input("enter num2 :"))
 result = num1 * num2

if op =="/":
   num1 = int(input("enter num1 :"))
   num2 = int(input("enter num2 :"))  
   if num2 == 0 :
        result = "erorr"
   else :
        result =num1 / num2

if op == "sin":
   num = float(input("enter num :"))
result = math.sin(math.radians(num))

if op =="cos":
    num = float(input("enter num:"))
    result = math.cos(math.radians(num))

if op == "tan":
    num = float(input("enter num"))
    result = math.tan(math.radians(num))

if op == "cot":
  num = float(input("enter num :"))
  if math.sin(math.radians(num)) == 0 : 
     result = "erorr"
  else :
      result = 1/math.tan(math.radians(num))

if op == "!" :
    num = int (input("enter num :"))
    if num < 0 :
      result = "erorr"
    else : 
       result = math.factorial(num)

if op == "squrt":
   num = int(input("enter num :"))
   if  num < 0 :
      result = "error"
   else : 
      reualt = math.squrt(num)

      print(result)


      

