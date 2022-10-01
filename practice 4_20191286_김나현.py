Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> [20-x for x in range(21) if (x % 5 == 0)]
[20, 15, 10, 5, 0]
>>> 
>>> def separate(str):
	x=str.strip().split()
	first=''
	family=''
	if (len(x)==1):
		family+=x[0]
	else:
		count=0
		for name in x:
			if(count==0):
				first+=x[count]
			elif (count!=len(x)-1):
				first+=' '
				first+=x[count]
			count+=1
		family+=x[len(x)-1]
	print('first_name->'+"'"+first+"'")
	print('family_name->'+"'"+family+"'")
	return first, family

>>> first_name, family_name=separate('John Smith')
first_name->'John'
family_name->'Smith'
>>> first_name
'John'
>>> family_name
'Smith'
>>> first_name, family_name=separate('Smith')
first_name->''
family_name->'Smith'
>>> first_name
''
>>> family_name
'Smith'
>>> first_name, family_name=separate('John Edward Smith')
first_name->'John Edward'
family_name->'Smith'
>>> first_name
'John Edward'
>>> family_name
'Smith'
>>> 
>>> str='ABcDeFG'
>>> len([s for s in str if (s.isupper())])
5
>>> 
>>> def findLocalMinima(func, xmin, xmax, n):
	x_vec=[xmin+(xmax-xmin)/(n-1.)*m for m in range(n)]
	dic={x:func(x) for x in x_vec}
	value=list(dic.values())
	items=list(dic.items())
	count=0
	for y in value:
		if (count==0):
			min=y
			index=count
		elif (min > y):
			min=y
			index=count
		count+=1
	return items[index]

>>> min=findLocalMinima(lambda x:x**2, xmin=-10, xmax=10, n=100)
>>> min
(-0.10101010101010033, 0.010203040506070672)
>>> min=findLocalMinima(lambda x:x**2, xmin=0, xmax=10, n=100)
>>> min
(0.0, 0.0)
>>> 