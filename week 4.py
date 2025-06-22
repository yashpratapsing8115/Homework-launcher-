print("=>DATA FILE PROGRAM")
while True:
   print("\n1. Create a file of doner.\n2. Display the record in file.\n3. Add record to the file.\n4. Modify existing information of doner.\n5. Display the name and adress of doner when blood group is given. \n6. Exit the program.")
   c= input("Enter choice: ")
   if c =="1":
       u= input("Enter doner name: ")
       m= input("Enter doner date of birth:")
       j= input("Enter doner adress:")
       k= input("Enter doner phone number:")
       i= input("Enter doner blood group:")
       with open("blood.dat", "w") as file:             # w for any thing written by user get wrote in file
         file.write(f"{u},{m},{j},{k},{i}\n")
       print("Your statement saved to blood.dat successfully!")
   elif c=="2" :
         with open("blood.dat", "r") as file:            # r to open file in reading format 
           print(file.read())
   elif c=="3" :
       q= input("Enter doner name: ")
       w= input("Enter doner date of birth:")
       e= input("Enter doner adress:")
       r= input("Enter doner phone number:")
       t= input("Enter doner blood group:")
       with open("blood.dat", "a") as file:              # a to add input in file
        file.write(f"{q},{w},{e},{r},{t}\n")
   elif c=="4" :
       u= input("Enter doner name: ")
       m= input("Enter doner date of birth:")
       j= input("Enter doner adress:")
       k= input("Enter doner phone number:")
       i= input("Enter doner blood group:")
       with open("blood.dat", "w") as file:             # w for any thing written by user get wrote in file
         file.write(f"{u},{m},{j},{k},{i}\n")
   elif c=="5":
       x=input('enter blood group:')
       with open("blood.dat", "r") as file:
           c=file.read()
           if x in c:
               print(f"{u} is doner name and {j} is doner adress")
           elif c in c:    
               print(f"{q} is doner name and {e} is doner adress")
   else:     
       print('Program has been ended')
       break
print ('Thank you for giving your precious time .Hope you will be satisfied')      