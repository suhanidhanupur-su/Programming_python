## Operators:
 #=> it can perform any specific operation between two values/Operands.


#4 + 5 => it can perform addition 
#4 * 5 => it can perform multiplication 

#=> 4 and  5 => are values/Operands 
#=> +, *, - =>  are the operators


#Types of Operators:
##1. Arithmetic Operators
#2. Assignment Operators
#3. Comparison Operators
#4. Logical Operators
#5. Bitwise Operators
#6. Membership Operators
#7. Identity Operators

# ------------------------------------------------ 

#1. Arithmetic Operators:
#=> it is used to perform mathematical operations between two values/Operands.

#Operators: +, -, *, /, %, //, **

#+ => Addition
#- => Subtraction
#* => Multiplication
#/ => Division
#% => Modulus
#// => Floor Division
#** => Exponentiation

#3**6 => 3^6 => 3*3*3*3*3*3 => 729

#4**2 => 4*4 = 16


## Division operator ("/") => it gives us Quient value.
#=> it includes the decimal part.

#Ex: 3.5, 4.6, 4.1, 2.5 etc. 

## Floor Division ("//") => it gives us Quient value.
#=> it removes the decimal part .

## Modulus ("%") => it gives us the remainder part .


#2. Membership Operators : in, not in
# in => it returns True if the value is present in the sequence otherwise it returns False

# not in => it returns True if the value is not present in the sequence otherwise it returns False

# list is similar to arrary in other programming languages

# Question : check 10 is present in the list1 or not ?
list1 = [10, 20, 30, 40, 50]
print(" 10 in list1: ", 10 in list1)  # True
print(" 100 in list1: ", 100 in list1)  # False
print(" 100 not in list1: ", 100 not in list1)  # True

#3. Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=

x = 20
y = 5
# x += y  
x = x + y 
print(x)

# the task is we wanna add in x => both  X and Y 
# x = x + y => it takes more time to run 
# x += y  => it takes less time to run 
# print(x + y) 

# in future we will learn about Time complexity, Space complexity

#4. Comparison Operators: ==, !=, >, <, >=, <=

# => in this case we will get the output in boolean format => True, False

#5. Logical Operators: and, or, not

# and => both the conditions should be true
# or => any one condition should be true
# not => negates the condition



#6. Bitwise Operators: &, |, ^, ~, <<, >>

# & =>  Bitwise AND
# | =>  Bitwise OR           
# ^ =>  Bitwise XOR
# ~ =>  Bitwise NOT

#0 => 0000
#1=> 0001
#2 => 0010
#3 => 0011
#4 => 0100
#5 => 0101
#6 => 0110
#7 => 0111
#8 => 1000
#9 => 1001
#10 => 1010
#11 => 1011
#12 => 1100
#13 => 1101
#14 => 1110
#15 => 1111


#Hexadecimal ( 16 digts)

#Digital Electronics 

# Operators: +, -, *, /, %, //, **

# + => Addition
# - => Subtraction
# * => Multiplication
# / => Division
# % => Modulus
# // => Floor Division
# ** => Exponentiation

# 3**6 => 3^6 => 3*3*3*3*3*3 => 729

a = 10
b = 3
print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333333333333335
print(a // b)  # 3
print(a % b)  # 1

print(a ** 3)
# 10 * 10 * 10 = 1000


# Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=

x = 20
y = 5
# x += y  
x = x + y 
print(x)

# the task is we wanna add in x => both  X and Y 
# x = x + y => it takes more time to run 
# x += y  => it takes less time to run 
# print(x + y) 

# in future we will learn about Time complexity, Space complexity

# # 3. Comparison Operators: ==, !=, >, <, >=, <=

p = 10
q = 20
C = 20
print(p == q)  
print(p == C)
print(p != q)
print(p > q)
print("Hii Wilmot plzz confirm this stmt: ",p < q)
print("hello Wilmot plzz confirm this stmt: ",p >= q)

print("Hello SHarky plzz confirm this stmt: ",C <= q)


# 4. Logical Operators: and, or, not

#and operator
u = 10
v = 20
print(u < v and  u > v)
# True and False => False

# or operator 

s = 10
t = 20
print(s < t or s > t)
# True or False => True

#not operator => it negates the condition
m = 10
n = 20
print(not(m < n))
# not(True) => False
print(not(m > n))
# not(False) => True


