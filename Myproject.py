#Part 1 of the question
Radius = float(input("The radius of the circle is: "))
pi = 3.141592653589793238462643383279502884197
Area = pi*Radius**2
print("The area of the circle is", Area)
The radius of the circle is: 1.1
The area of the circle is 3.8013271108436504


#Part 2 of the question
Filename= input("Enter Filename: ")
extension = Filename.split(".")
print ("Extension of the file is : " + extension[-1])
Enter Filename: abc.py
Extension of the file is : py
