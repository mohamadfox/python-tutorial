# Low level Verilog
# static type -> Java, Scala, C, C++, C#, Go, ...
#   - restricted
# dynamic type -> Python, Javascript, Ruby, Lua,
#
# functional programming
# object oriented programming

# Compiler java -> byte code -> run [Platform independent]
# Interpreter python -> run [Platform dependent]

# = assignment operator

a = 12
# variable
# name: a
# value: 12
# type: int [find type from value]

# typing
a: int = 12  # increase readability
# Int a = 12; Java
# a Int = 12 Golang
# variable
# name: 1
# value: 12
# type: int

a = "hello"

print("hello world")
print('hello world')

print(a)  # find variable a, print the value of a
print("a")

"""
Traceback (most recent call last):
  File "c:\Users\MFT SERVER\Desktop\python\beginner python 3\01\01_hello_world.py", line 36, in <module>
    print(12/0)
ZeroDivisionError: division by zero
PS C:\Users\MFT SERVER\Desktop\python\beginner python 3>
"""
print(12/0)
