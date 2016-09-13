print "do the lengths of the three sides form a triangle?\n"


a = int(input("What is the length of side a  "))

b = int(input("What is the length of side b  "))

c = int(input("what is the length of side c  "))





def is_triangle(a, b, c):
    if (a > b + c) or (b > a + c) or (c > a + b):
        print "No"
    else:
        print "Yes"


is_triangle(a, b, c)

