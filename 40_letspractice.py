"""
1. Create a class (2-D vector) and use it to create another class representing a 3-D
vector.

class TwoDVector:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")


a = TwoDVector(1, 2)
a.show()

b = ThreeDVector(1, 2, 3)
b.show()

# OutPut:- The vector is 1i + 2j
#          The vector is 1i + 2j + 3k
#===========================================================================================================================
#===========================================================================================================================
2. Create a class 'Pets' from a class 'Animals' and further create a class 'Dog' from
'Pets'. Add a method 'bark' to class 'Dog'.


class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):
    
    @staticmethod
    def bark():
        print("Bow Bow!")
         
d = Dog
d.bark()

#OutPut:-   Bow Bow!

#===========================================================================================================================
#===========================================================================================================================
3. Create a class 'Employee' and add salary and increment properties to it.

Write a method 'salaryAfterincrement' method with a @property decorator with a setter
which changes the value of increment based on the salary.

class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary +self.salary*(self.increment/100))

    @increment.setter
    def increment(self, salary):
    self.increment = ((salary/self.salary)-1)*100
        

e = Employee()
#print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 280.8
print(e.increment)
# OutPut:- 280.8

#===========================================================================================================================
#===========================================================================================================================
4. Write a class 'Complex' to represent complex numbers, along with overloaded
operators '+' and '*' which adds and multiplies them.

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
         
    def __add__(self, c2):
        return Complex(self.r + c2.r, self.i + c2.i)
    
    def __mul__(self, c2):
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        return f"{self.r} + {self.i}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)

print(c1 + c2)  # Output: 4 + 6i
print(c1 * c2)  # Output: -5 + 10i

#===========================================================================================================================
#===========================================================================================================================
5. Write a class vector representing a vector of n dimensions. Overload the + and *
operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, components):
        self.components = components  # a list of numbers

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add")
        result = [x + y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product")
        result = sum(x * y for x, y in zip(self.components, other.components))
        return result

    def __str__(self):
        return f"Vector({', '.join(str(x) for x in self.components)})"


# 🔍 Example usage
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

print("v1 + v2 =", v1 + v2)     # Vector(5, 7, 9)
print("v1 * v2 =", v1 * v2)     # 1*4 + 2*5 + 3*6 = 32

#===========================================================================================================================
#===========================================================================================================================
6. Write __str__() method to print the vector as follows:
            7i +8j +10k


class Vector:
    def __init__(self, components):
        self.components = components  # e.g., [7, 8, 10]

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add")
        result = [x + y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product")
        result = sum(x * y for x, y in zip(self.components, other.components))
        return result

    def __str__(self):
        # Variables: i, j, k, l, m, n, ... (alphabetical)
        suffixes = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
        terms = [f"{val}{suffixes[i]}" for i, val in enumerate(self.components)]
        return " + ".join(terms)


#  Example usage
v = Vector([7, 8, 10])
print(v)  # Output: 7i + 8j + 10k


#===========================================================================================================================
#===========================================================================================================================
7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class Vector:
    def __init__(self, components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add")
        result = [x + y for x, y in zip(self.components, other.components)]
        return Vector(result)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product")
        return sum(x * y for x, y in zip(self.components, other.components))

    def __len__(self):
        return len(self.components)

    def __str__(self):
        suffixes = ['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r']
        terms = [f"{val}{suffixes[i]}" for i, val in enumerate(self.components)]
        return " + ".join(terms)


# 🔍 Example usage
v = Vector([7, 8, 10])
print(v)             # Output: 7i + 8j + 10k
print(len(v))        # Output: 3 (dimension)

"""
