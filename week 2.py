def q1():
    print ('Python program to count the number of characters (character frequency) in a string.')
    m=input("enter a string:")
    a={}
    for i in m:
     a[i]=a.get(i,0)+1
    print (a )
def q2():
    print("a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.")
    a=input("enter a string:")
    print(a[0]+'$'*(len(a)-1))
def q3():
    print ('method in python to display the elements of a list twice if it is a number and display the element terminated with*** if it is not a number.')
    print ()
    items = input("Enter items of the list separated by commas: ")
    a = [item.strip() for item in items.split(",")]
    m=[]
    for item in a:
              if item.isdigit(): 
                  m.append(int(item))
              else:
                  m.append(item)     
    for i in m:
              if isinstance(i,int):
                  print(i,i)     
              else:
                  print (i,"*")
def q4():
    a={'aman':9100000001,
    'naman':9100000002,
    'shivam':9100000003}
    print("Your phonebook is:\n",a)
    b=input('Enter name to delete phone number and get updated phonebook:')
    if b in a:
        del a[b] 
    print (a)
def q5():
 e = []
 n = int(input("Enter the number of employees: "))
    
 for i in range(n):
    emp_no = int(input(f"\nEnter employee number for employee {i+1}: "))
    name = input(f"Enter name for employee {i+1}: ")
    e.append((emp_no, name))
    e.sort()
 print("\nEmployee Information (sorted by employee number):")
 for emp in e:
    print(f"Employee Number: {emp[0]}, Name: {emp[1]}")
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
    