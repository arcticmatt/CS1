# Matt Lim

import math

# Problem B.1
class Point:
    '''Instances of this class are three-dimensional
    points in Euclidean space (w/real valued coordinates).'''

    def __init__(self, x, y, z):
        '''Constructor that initializes the x, y, z coordinates'''
        self.x = x
        self.y = y
        self.z = z

    def distanceTo(self, Point):
        '''Does: Calculates the distance from one point to another.
        Arguments:
        -- self: Self.
        -- Point: The point that we are calculating the distance to.
        Returns: The distance from one point to another.'''

        return math.sqrt((Point.x - self.x)**2 + (Point.y - self.y)**2 \
                + (Point.z - self.z)**2)

# Problem B.2
class Triangle:
    '''Instances of this class are triangles.'''

    def __init__(self, point1, point2, point3):
        '''Constructor that initializes three points.'''

        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def area(self):
        '''Does: Calculates the area of a triangle.
        Arguments:
        -- self: Self.
        Returns: The area.'''

        side1 = self.point1.distanceTo(self.point2)
        side2 = self.point2.distanceTo(self.point3)
        side3 = self.point3.distanceTo(self.point1)

        half_sum_sides = (side1 + side2 + side3) / 2
        area = math.sqrt(half_sum_sides * (half_sum_sides - side1) * \
                (half_sum_sides - side2) * (half_sum_sides - side3))
        return area

# Problem B.3
class Averager:
    '''Instances of this class store a list of numbers an perform
    various operations on them.'''

    def __init__(self):
        '''Constructor that initializes an empty list.'''

        self.lst = []

    def getNums(self):
        '''Does: Returns a copy of the stored list.
        Arguments:
        -- self: Self.
        Returns: A copy of the stored list.'''

        return self.lst[:]

    def append(self, num):
        '''Does: Appends a number to the stored list.
        Arguments:
        -- self: Self.
        -- num: The number to be appended.
        Returns: Void.'''

        self.lst.append(num)

    def extend(self, add_lst):
        '''Does: Appends a list to the stored list.
        Arguments:
        -- self: Self.
        -- add_lst: The list to be appended.
        Returns: Void.'''

        self.lst.extend(add_lst)

    def average(self):
        '''Does: Calculates the average of the stored list.
        Arguments:
        -- self: Self.
        Returns: The average of the stored list.'''

        if len(self.lst) == 0:
            return 0
        my_sum = sum(self.lst)
        return float(my_sum) / len(self.lst)

    def limits(self):
        '''Does: Calculates the max and min of the stored list.
        Arguments:
        -- self: Self.
        Returns: A tuple of the (min, max).'''

        if len(self.lst) > 0:
            my_max = max(self.lst)
            my_min = min(self.lst)
            return (my_min, my_max)
        else:
            return (0, 0)



# Problem C.1
# a) Unnecessary code: the else statement is not needed.
# b)
def is_positive(x):
    return x > 0

# Problem C.2
# a) Unnecessary code: A lot of the variables and if/else statements
#    are not needed.
#    Excessively complex code: The extra variables and if/else statements
#    make the code more overly complex.
# b)
def find(x ,lst):
    for i, item in enumerate(lst):
        if item == x:
            return i
    return -1

# Problem C.3
# a) Unnecessarily inefficient code: All the if statements are executed no
#    matter what x is.
# b)
def categorize(x):
    if x < 0:
        category = 'negative'
    elif x == 0:
        category = 'zero'
    elif x > 0 and x < 10:
        category = 'small'
    elif x >= 10:
        category = 'large'
    return category

# Problem C.4
# a) Unnecessary code: A lot of unnecessary if/else statements.
#    Excessively complex code: The if/else statements complicate it.
#    Unnecessarily inefficient code: Running through the if/else statements
#    is inefficient.
# b)
def sum_list(lst):
    my_sum = 0
    for num in self.lst:
        my_sum += num
    return my_sum
