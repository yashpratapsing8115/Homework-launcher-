print("=>INTERACTIVE MENU DRIVEN PROGRAM")
while True:
   print("\n1. Create a text file.\n2. Display the text file.\n3. Append content to the file.\n4. Make Copy of a file.\n5. Display the copied text file. \n6. Count no of 'the' in the file. \n7. Exit the program.")
   c= input("Enter choice: ")
   if c =="1":
       u= input("Enter your string: ")
       with open("Nation.txt", "w") as file:             # w for any thing written by user get wrote in file
         file.write(u)
       print("Your statement saved to Nation.txt successfully!")
   elif c=="2" :
         with open("Nation.txt", "r") as file:            # r to open file in reading format 
           print(file.read())
   elif c=="3" :
      t= input("Enter text to add in file : ")
      with open("Nation.txt", "a") as file:              # a to add input in file
       file.write(t+ "\n")
   elif c=="4" :
      with open("Nation.txt", "r") as s:
           with open("Nation2.txt", "w") as d:
                d.write(s.read())   
   elif c=="5":
       with open("Nation2.txt", "r") as file:            # r to open file in reading format 
           print(file.read())  
   elif c=="6" :
       with open("Nation.txt", "r") as file:
        c = file.read()
        o= c.count('the')+c.count('The')
        print(f"Number of times 'The or the' appears: {o}")   
   else:     
       print('Program has been ended')
       break
print ('Thank you for giving your precious time .Hope you will be satisfied')      