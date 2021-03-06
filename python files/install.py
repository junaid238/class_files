# python - 3.7 
# local instlaled -->global installation 
#  / / /python>python --> c:/>python
#  >>>					>>>

#  / / /python 

# python2 and python3 --> 1 system ??
# yes
# c:/>python ---> python2
# c:/>python3 ---> python3

# path / environment variable  setup

# my comp --> rt click 
# 		--> adv sys settings
# 		--> environment variables

# language -> libraries 
# --> set of words and commands 
# --> set of words --> keywords 
# --> 33 --> 3.x
# --> 31 --> 2.x
# None , True , False , lower case 
# every keyword --> particular purpose 
# 			  --> XX deleted XX 
# 			  --> XX modified XX

# >>>import keyword 
# >>>keyword.kwlist
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# identifiers 
# -----------
# user defined keywords --> identifiers
# modified , deleted , names of components
# 	-> lower case (preferred)
# 	-> upper case (constant value)
# 	-> XX number XX
# 	-> XX symbol XX
# 	-> _ and __ (special case)

# variables 
# ---------
# -> mini storage unit 
# 	- name (identifier) 
# 	- value (data)
# 	- memory location (address)

# <identifier> = <value>
# data --> forms --> data types 
# all
# 	- int , float , double , long , char , string , boolean
# python 3.x
# 	- int , float , string , list , tuple , dictionary 
# 	- numbers (int , float), string , list , tuple , dictionary

# python 2.x
# 	- int , float ,long , string , list , tuple , dictionary 
# 	- numbers (int , float , long), string , list , tuple , dictionary

# list , tuple , dictionary --> collections
# numbers , strings  --> independent data types
# list , tuple , dictionary( collections ) --> derived data types

a = 10
# name , identifier --> a
# value , data --> 10 
# memory location --> 
# data type --> int 
# type(<identifier>) ---> data type of the value --> <class 'int'>
# id(<identifier>) ---> memory location of data --> 4327881616

# Numbers 
# -------
# - decimal values (base 10) 
# - int , float , complex 
# - int --> integer -> -infinite to +infinite
# - float --> -infinite.infinite to +infinite.infinite
# - complex --> a+ib --> a+bj --> 3+4j --> <class 'complex'>

# maximum integer possible
# >>>import sys
# >>>sys.maxsize --> 3.x
# >>>sys.maxint --> 2.x

# 3.x
# biggestInt = 9223372036854775807 --> integer
# c = 9223372036854775809 --> integer

# 2.x
# biggestInt = 9223372036854775807 --> integer
# c = 9223372036854775809L --> long

# 9223372036854775807 --> 2 power 63 --> 64-bit

# all ==> Data type --> boolean --> True , False 
# python ==> boolean --> XXX data type XXX --> status flag 

# operators
# ---------
# arithmetic 
# comparision
# logical
# bitwise 

# identity --> XX numbers XX   --> strings , collections
# membership --> XX numbers XX --> strings , collections

# arithmetic --> 7 --> output --> value
# ---------------------------------------
# +, - , * , / , // , % , **

# conflict
# --------
# a = 25
# b = 3
# a/b --> 8
# a//b --> 8 

# a = 25.0
# b = 3
# a/b --> 8.3333
# a//b --> 8 

# int , float --> math module 
# complex --> cmath module	

# comparision operators --> True / False
# --------------------------------------
# > , < , >= ,<= , == , != 
# a = 25
# b = 30

# logical operators --> True , False
# -----------------
# and or not 

# a 	b 	a and b 	a or b
# t 	t 		t 			t
# f 	f 		f 			f
# t 	f 		f 			t
# f 	t 		f 			t		

# a>b and b>c 
# t and f --> False

# a>b or b>c 
# t or f --> True

# >>>25 and 30
# t t and t  --> 30
# >>>30 or 40
# t t---> 30
# >>> --> always True
# not --> condradicting any statement
# not(True) --> False
# not(False) --> True

23 - 07 -2018 
-------------
bitwise operators
- numbers --> bits (0 and 1)
- binary bitwise operators

bitwise and - & - 2 operands
bitwise or  - | - 2 operands
bitwise not - ~ - 1 operand
right shift - >> - 2 operands
left shift  - << - 2 operands

& --> tt t  --> 11 1
| --> ff f  --> 00 0 

10   -  0000 1010
20   -  0001 0100
-----------------
10 & 20 0000 0000 -> 0 
10 | 20 0001 1110 -> 30

XXX ~(10) --> 1111 0101 --> 1's complement  XXXX
~(10) --> -11 --> 2's complement
~(x) --> -(x+1)
~(25) --> -26

10 >> 2 --> 0000 1010 --> 0000 0010 --> 2 
10 << 2 --> 0000 1010 --> 0010 1000 --> 40

input vs output
----------------
>>> a = 10
>>> b = 20 
>>> a&b
0
>>> a | b
30
>>> ~a
-11
>>> ~b
-21
>>> a>>2
2
>>> a<<2
40
>>> a>>3
1
>>> a<<4
160

Strings 
-------
all --> char , string
python --> strings

- either single or group of alpha numeric chars
- any keyboard value can be a string

- immutable 
- indexed 
- sliced 
- concatenated 
- <class str>

Syntax
------
<stringName> = '<value>'
<stringName> = "<value>"

indexed
-------
name = "Python"

P  y  t  h  o  n 
0  1  2  3  4  5  --> starts 0 to n --> indices(index) --> forward indexing 
-6 -5 -4 -3 -2 -1 --> starts -n to -1 --> reverse(negative) indexing

- get single char from a string

Syntax
------
<stringName>[<index>]
name[3] --> h
name[-3] --> h
name[5] --> n

sliced
------
name = "Python and Data Sciences"

- get substring from a string

Syntax
------
<stringName>[<start> : <end>] # start to end-1
<stringName>[<start> : ] # start to last char
<stringName>[ : <end> ] # first char to end-1
<stringName>[<start> : <end> : <step>] # start to end-1 with +step  

name[2:8] --> 2 3 4 5 6 7  (+1)
default --> step = 1

<stringName>[<start> : <end> : <step>]
name[2:8:2] --> 2 4 6














