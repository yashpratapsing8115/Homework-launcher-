def q1():
    print ('Python program to sum all the items in a list.')
    a=[]
    print ('enter 00 to end inputs')
    while True:
        n=int(input('enter number:'))
        a.append(n)
        if n==00:
            break
    print (sum(a))       
        
def q2():
    print ('Python program to get the largest number from a list.')
    a=[]
    print ('enter 00 to end inputs')
    while True:
        n=int(input('enter number:'))
        a.append(n)
        if n==00:
            break
    print ('largest number is',max(a))       
def q3():
    print ('Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.')
    a=[]
    print ('enter 00 to end inputs')
    while True:
        n=input('enter list item:')
        a.append(n)
        if n=='00':
            break
    c=0
    for s in a:
        if len(s)>=2 and s[0]==s[-1]:
            c +=1
    print ('count of matching string',c)              
def q4():
    print ('Python program to remove duplicates from a list.')
    a=[]
    print ('enter 00 to end inputs')
    while True:
        n=input('enter list item:')
        a.append(n)
        if n=='00':
         break
    unique_numbers = list(set(a))
    print(unique_numbers)      
def q5():
   print('Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).')
   a=[x**2 for x in range(1,31)]
   print(a[:5]+a[-5:])
print ('enter "0" to end ')   
while True:    
 a=input ('enter question no:')   
 if a=="1":
    print (q1())
 elif a=="2":
    print (q2())  
 elif a=="3":
    print (q3()) 
     
 elif a=="4":
    print (q4())  
    
 elif a=="5":
    print (q5())  
 else:
    break    
print ('Thank you for giving your precious time .Hope you will be satisfied')          


