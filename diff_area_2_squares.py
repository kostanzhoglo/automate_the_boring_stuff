# there was a challenge on edabit.com, where a square was inscribed inside a circle, and another square surrounded the same circle.
# you were given the radius of the circle only, and were asked to determine the difference in area of the 2 squares.  

def diff_area(r):
    smallSquare = int(((2*r)**2)/2)
    largeSquare = 4*r**2
    difference_in_area = largeSquare - smallSquare
    return difference_in_area

radius5 = diff_area(5)
radius6 = diff_area(6)
radius7 = diff_area(7)

print(radius5)
print(radius6)
print(radius7)