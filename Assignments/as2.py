#2. Input length and breadth of rectangle. Calculate its area and perimeter. A= l*b, P= (l+b)*2



l = float(input("Length of rectangle: "))
b = float(input("Breadth of rectangle: "))

Area = l*b
perimeter = (l+b)*2

print("Area of rectangle: ", Area)
print("Perimeter of rectangle: ", perimeter)


#using functions:

def area(l,b):
    area = l*b
    print(area)

def per(l,b):
    per = (l+b)*2
    print(per)

area(5,5)
per(5,5)

