#Global variables can be used by everyone, both inside of functions and outside.

#Creating a variable outside of a function, and using it inside the function.
x="awesome"

def my_func():
    print("ABC is " +x)

my_func()

#Creating a variable inside a function, with the same name as the global variable.

x="awsome"

def my_func():
    x="Fantastic"
    print("DEF is " +x)

my_func()
print("GHI is " + x)

#Normally, when create a variable inside a function, that variable is local, and can only be used inside that function.

#To create a global variable inside a function, I can use the global keyword.

def myfunc():
    global x
    x="Superboss"

myfunc()
print("JKL is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("MNO is " + x)