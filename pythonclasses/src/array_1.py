import numpy 
a=numpy.array([[1,2,3,4],[2,3,5,6],[4,5,3,5],[6,9,10,5]])
print (a[0][0])
print(a.ndim)
for i in a:
    print(i)
    print("\n")

b=numpy.array([[3,5,4,6],[9,6,5,3],[7,5,3,2],[8,5,2,4]])
sum=0
print(b.ndim)
print(numpy.sort(b))
for j in b:
    for i in j:
        sum=sum+i 
print(sum)
print(numpy.where(b==10))
print(b.size)
print(numpy.sort(b))
print(numpy.add(a,b))
print(numpy.multiply(a,b))
        
