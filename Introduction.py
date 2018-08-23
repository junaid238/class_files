Introduction 
------------
features 
--------
	- easy syntax
		usage of control chars (EOL , ; , { }) is less 
	- interpreted 
		compiler vs interpreter
		compiler --> entire code 
			code(100){13,19,35} --> compile --> 13,19,35
			code(100) --> compile --> <code> --> run --> full output 
		interpreter --> line by line 
			code(100){13,19,35} --> interpret --> output till 12 {13}
			code(100){19,35} --> interpret --> output till 18 {19}
			code(100){35} --> interpret --> output till 18 {35}
			code(100){} --> interpret --> full output
	- dynamically typed
		run time changes 
		10 --> number --> dynamically typing 
		number 10  --> static typing
	- pure OOPS (ruby) 
		python --> abstraction --> XXX 
		everything is an object 
	- strict intended 
		intendation --> beautify code 
		tabs and spaces --> structured code 
		Indendation error

install python
--------------
	- mac --> already 
	- linux --> ubuntu --> already
	- windows --> python.org --> 3.7 
		- download -- run (path in machine)
		- pip , make system variable 
			- install (path in machine)
			- IDLE  --> default interpreter for python
		cmd --> c:/>python
		 1) Python 3.7 
			---
			---
			---
			>>>
			ready to use --> global install
		2) error 
		cmd --> c:/>where python
		path in machine --> copy 
		cmd --> c:/>python
		>>> 

writing code 
------------
- cmd / terminal --> runtime 
- python files --> editor  --> SlT3
			   --> IDE --> PyCharm (CE)

Running of python files 
-----------------------
ide --> editor + console 
editor --> code + cmd for run
c/file/location>:</>python <filename>.py 


python2 and python3 
global and laid 

c:/> python 
2.7
>>>

c:/> python3
3.7
>>>

Libraries --> keywords and pre defined components 
keywords --> 31 -- 2.7
		 --> 33 -- 3.6

- pre defined words --> particular operative 
- change XX 
- delete XX 
- modify their functionality

>>> import keyword 
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

identifiers 
-----------
- user defined keywords
- changed
- modified
- purpose --> changed
- names of components -->values , classes , objects , errors .....
- rules 
	- lower case ( recommended )
	- upper case ( constant )
	- XX number XX
	- XX symbol XX
	- @ (special case)
	- _ (underscore) , __ ( double underscore ) (special case)

variables 
---------
- mini storage for data 
- dynamically alloted 
- three components 
	- values (data)
	- name (identifier)
	- address (location)

Data types 
----------
all --> int , float , long , double , char , string , boolean 
python --> numbers , strings , lists , tuples , dictionaries 

numbers --> int , float , complex --> 3.X
numbers --> int , float , long , complex --> 2.X

Boolean -->XXX data type XXX --> Status ( True , False )




subhasrigandham@gmail.com
sivaprasadg509@gmail.com
kollisravani0123@gmail.com














