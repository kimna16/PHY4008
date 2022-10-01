Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f1=lambda x:x
>>> f2=lambda x:1./x
>>> f3=lambda x:x**2
>>> f4=lambda x:x-1
>>> 
>>> def function_sum(f1,f2):
	ouput=lambda x:f1(x)+f2(x)
	return output

>>> f12=function_sum(f1,f2)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    f12=function_sum(f1,f2)
  File "<pyshell#8>", line 3, in function_sum
    return output
NameError: name 'output' is not defined
>>> def function_sum(f1,f2):
	output=lambda x:f1(x)+f2(x)
	return output

>>> f12=function_sum(f1,f2)
>>> f12(1)
2.0
>>> 
>>> def function_summation(*arg):
	output=lambda x:0
	for a in arg:
		output=function_sum(output,a)
	return output

>>> f123=function(f1,f2,f3)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    f123=function(f1,f2,f3)
NameError: name 'function' is not defined
>>> f123=function_summation(f1,f2,f3)
>>> f123(1)
3.0
>>> f1234=function_summation(f1,f2,f3,f4)
>>> f1234(1)
3.0
>>> 
>>> 
>>> import matplotlib.pyplot as pl
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    import matplotlib.pyplot as pl
ModuleNotFoundError: No module named 'matplotlib'
>>> 