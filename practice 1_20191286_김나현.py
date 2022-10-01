1
name='Bill Gates'
first_name, family_name=name.split(sep=' ')


2
x=list(range(1,21))
print(x)


3
print(x[::-2])


4
x=[element*0.5 for element in range(1,41)]
y=[int(element) if element%1==0 else element for element in x]
print(y)


5
x=()
for i in range(1,11):
    x=x+(i,)
print(x)


6
x=[0.2618024 , 0.85541582, 0.62747845, 0.8995334 , 0.02430872, 0.32935667, 0.12351787, 0.54484519, 0.89314498, 0.40300014]
print(sorted(x))


7
y=list(range(1,11))
x=[sum(y[:n]) for n in range(1,len(y)+1]


8
val=1
for x in range(1,11):
    val*=x
print(val)
