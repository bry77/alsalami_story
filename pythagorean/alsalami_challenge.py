print ("I can guess the type of triangle using it's leg lengths")

a = float(input("Enter a leg length: "))
b = float(input("Enter the sencond leg length: "))
c = float(input("Now enter a hypotenuse: "))

if (a+b < c):
    print ('Triangles only')
    
elif (a**2 + b**2 ==c**2):
    print ("That's a right triangle")
    
elif (a**2 + b**2 <c**2):
    print("That's an obtuse triangle")
    
elif ((a**2 + b**2 >c**2) + (a + b > c)):
    print ("that's an acute triangle")
    
    