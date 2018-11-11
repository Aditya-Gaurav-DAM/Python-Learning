==========================
#decorator================
==========================
#In Python, we can define a function inside another function.
#In Python, a function can be passed as parameter to another function (a function can also return another function).
#Python has an interesting feature called decorators to add functionality to an existing code.
#This is also called metaprogramming as a part of the program tries to modify another part of the program at compile time.
#When you run the code, both functions first and second gives same output. Here, the names first and second refer to the same function object.
#Now things start getting weirder.
#Functions can be passed as arguments to another function.
#If you have used functions like map, filter and reduce in Python, then you already know about this.

Such function that take other functions as arguments are also called higher order functions. Here is an example of such a function.
def first(msg):
    print(msg)

first("Hello")
second = first
second("Hello")

#Hello
#Hello
=============================
def add1(a):
  return 1+a

def add2(a):
  return 2+a

def abc(func,a):
  result = func(a)
  print(result)

abc(add1,5)
abc(add2,6)
#6
#8
==============================
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

pretty = make_pretty(ordinary)
pretty()

#I got decorated
#I am ordinary
===================================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        print("abc function")
    return inner
def outer1():
    print("in outer1 function")
obj = outer(outer1)
obj()

#inner function
#in outer1 function
#abc function
======================
def outer(abc):
    def inner():
        print("in inner function")
        abc()
        print("in abc ")
        abc()
        print("again in abc")
    return inner

@outer
def outer1():
    print("in outer1 function")

outer1()

#in inner function
#in outer1 function
#in abc 
#in outer1 function
#again in abc
=====================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer1,outer2)
obj()
#inner function
#in outer2 function
#abcd function
#in outer1 function
#abc function
=======================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
        abc()
        print("abc function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer1,outer2)
obj()

#inner function
#in outer2 function
#abcd function
#in outer1 function
#abc function
#in outer1 function
#abc function
=======================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        print("abc function")
    return inner
@outer
def outer1():
    print("in outer1 function")
outer1()
#nner function
#in outer1 function
#abc function
==========================
def add_num_decorate(abc):
    def add_num1(i,j):
        print("before adding")
        print("sum = ",abc(i,j))
        print("after adding")
    return add_num1
def add_num2(i,j):
    return i+j
obj = add_num_decorate(add_num2)
obj(10,15)
#before adding
#sum =  25
#after adding
========================
def outer(abc):
    def inner(i,j):
        print("before sum :")
        print("sum = ",abc(i,j))
        print("after sum")
    return inner
@outer
def outer1(i,j):
    return i+j
outer1(10,15)
#before sum :
#sum =  25
#after sum
========================
def add_num_decorate(abc):
    def add_num1(i,j):
        print("before adding")
        print("sum = ",abc(i,j))
        print("after adding")
    return add_num1

@add_num_decorate
def add_num2(i,j):
    return i+j
@add_num_decorate
def add_num3(i,j):
    return i+j
add_num2(10,15)
add_num3(10,10)
#before adding
#sum =  25
#after adding
#before adding
#sum =  20
#after adding
============================
def add_num_decorate(abc):
    def add_num1(i,j):
        print("before adding")
        print("sum = ",abc(i,j))
        print("after adding")
    return add_num1

@add_num_decorate
def add_num2(i,j):
    return i+j
add_num2(10,10)
#before adding
#sum =  20
#after adding
============================
def outer(abc,abcd,abcde):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
        abcde()
        print("abcde function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer1,outer2)
obj()
#TypeError: outer() missing 1 required positional argument: 'abcde'
============================
def outer(abcd):
    def inner():
        print("inner function")
        print("after inner",abcd())
    return inner
def outer1():
    print("in outer1 function")
obj = outer(outer1)
obj()
#inner function
#in outer1 function
#after inner None
===========================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        print("abc function 00 ")
        abc()
        print("abc function 01")
    return  inner
@outer
def outer1():
    print("outer1 function")
outer1()
#inner function
#outer1 function
#abc function 00 
#outer1 function
#abc function 01
=======================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        abc()
    return  inner
@outer
def outer1():
    print("outer1 function")
outer1()
#inner function
#outer1 function
#outer1 function
=====================
#file name : learning.py
def outer(abc):
    def inner():
        print("inner function")
        abc()
        abc()
    return  inner

#file name : learning1.py

from learning import outer
@outer
def outer1():
    print("outer1 function")
outer1()

#inner function
#outer1 function
#outer1 function
========================
def outer(abc):
    def inner(*args):
        print("*" * 5)
        abc(*args)
        print("%" * 10)
        abc(*args)
        print("^" * 15)
    return inner
@outer
def inner01(x):
    print("Here we go :")
inner01(10)
#*****
#Here we go :
#%%%%%%%%%%
#Here we go :
#^^^^^^^^^^^^^^^
============================
def star(star):
    def inner(*a,**b):
        print("X" *10)
        star(*a,**b)
        print("X"*15)
        star(*a,**b)
        print("X"*30)
    return inner
@star
def inner01(x,y):
    print("anuj")
inner01("anything","anything")
#XXXXXXXXXX
#anuj
#XXXXXXXXXXXXXXX
#anuj
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
=============================================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer2,outer1)
obj()
#inner function
#in outer1 function
#abcd function
#in outer2 function
#abc function
===============================
def outer(abc):
    def inner():
        print("inner function")
        abc()
        print("abc function")
        abcd()
        print("abcd")
    return inner
def outer1():
    print("in outer1 function")
obj = outer(outer1)
obj()
#inner function
#in outer1 function
#abc function
#NameError: name 'abcd' is not defined
==========================================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abc()
        print("abc function")
        abcd()
        print("abcd")
    return inner
def outer1():
    print("in outer1 function")
obj = outer(outer1)
obj()
#TypeError: outer() missing 1 required positional argument: 'abcd'
==============================================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abc function")
        abcd()
        print("abcd")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer1,outer2)
obj()
#inner function
#in outer2 function
#abc function
#in outer2 function
#abcd
=============================================
def outer(abc,abcd):
    def inner():
        print("inner function")
        abcd()
        print("abc function")
        abcd()
        print("abcd")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
obj = outer(outer2,outer1)
obj()
#inner function
#in outer1 function
#abc function
#in outer1 function
#abcd
===============================================
def outer(abc):
  def inner(i,j):
    print("sadding starts :")
    print("sum is :",abc(i,j))
    print("after ading")
  return inner
def add_number(i,j):
  return (i+j)
obj = outer(add_number)
obj(10,15)
#sadding starts :
#sum is : 25
#after ading
===============================================
def add_num_decorate(abc):
    def add_num1(i,j):
        print("before operation")
        print("sum = ",abc(i,j))
        print("after operation")
    return add_num1

@add_num_decorate
def add_num2(i,j):
    return i+j
@add_num_decorate
def add_num3(i,j):
    return i*j
add_num2(10,15)
add_num3(10,10)

#before operation
#sum =  25
#after operation
#before operation
#sum =  100
#after operation
======================================
def outer(abc,abcd,abcde):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
        abcde()
        print("abcde function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
def outer3():
    print("in outer2 function")
obj = outer(outer1,outer2,outer3)
obj()

#inner function
#in outer2 function
#abcd function
#in outer1 function
#abc function
#in outer2 function
#abcde function
==========================================
def outer(abc,abcd,abcde):
    def inner():
        print("inner function")
        abcd()
        print("abcd function")
        abc()
        print("abc function")
        abcde()
        print("abcde function")
    return inner
def outer1():
    print("in outer1 function")
def outer2():
    print("in outer2 function")
def outer2():
    print("in outer3 function")
obj = outer(outer1,outer2,outer2)
obj()

#inner function
#in outer3 function
#abcd function
#in outer1 function
#abc function
#in outer3 function
#abcde function
=========================================
def outer(abc):
    def inner(*args):
        print("*" * 5)
        abc(*args)
        print("%" * 10)
        abc(*args)
        print("^" * 15)
    return inner
@outer
def inner01(x):
    print("Here we go :")
inner01("anuj")  #any argument

#*****
#Here we go :
#%%%%%%%%%%
#Here we go :
#^^^^^^^^^^^^^^^

===========================================
