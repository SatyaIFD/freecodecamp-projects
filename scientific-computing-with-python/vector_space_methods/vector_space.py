class R2Vector:
    # Initialize a 2D vector with keyword-only arguments x and y
    def __init__(self, *, x, y):
        self.x = x
        self.y = y

    # Calculate the Euclidean norm (length) of the vector
    def norm(self):
        # sum of squares of all attributes, then square root
        return sum(val**2 for val in vars(self).values())**0.5

    # Return a string representation of the vector as a tuple (x, y)
    def __str__(self):
        return str(tuple(getattr(self, i) for i in vars(self)))

    # Return a formal string representation for debugging and instantiation
    def __repr__(self):
        arg_list = [f'{key}={val}' for key, val in vars(self).items()]
        args = ', '.join(arg_list)
        return f'{self.__class__.__name__}({args})'

    # Define vector addition for two vectors of the same class
    def __add__(self, other):
        if type(self) != type(other):
            return NotImplemented
        # Add corresponding components and create new instance
        kwargs = {i: getattr(self, i) + getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    # Define vector subtraction for two vectors of the same class
    def __sub__(self, other):
        if type(self) != type(other):
            return NotImplemented
        # Subtract corresponding components and create new instance
        kwargs = {i: getattr(self, i) - getattr(other, i) for i in vars(self)}
        return self.__class__(**kwargs)

    # Define multiplication: scalar multiplication or dot product
    def __mul__(self, other):
        if type(other) in (int, float):
            # Scalar multiplication: multiply each component by the scalar
            kwargs = {i: getattr(self, i) * other for i in vars(self)}
            return self.__class__(**kwargs)        
        elif type(self) == type(other):
            # Dot product: sum of products of corresponding components
            args = [getattr(self, i) * getattr(other, i) for i in vars(self)]
            return sum(args)            
        return NotImplemented

    # Check equality of two vectors (all components must be equal)
    def __eq__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return all(getattr(self, i) == getattr(other, i) for i in vars(self))
        
    # Check inequality of two vectors (opposite of equality)
    def __ne__(self, other):
        return not self == other

    # Compare vectors by norm: less than
    def __lt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() < other.norm()

    # Compare vectors by norm: greater than
    def __gt__(self, other):
        if type(self) != type(other):
            return NotImplemented
        return self.norm() > other.norm()

    # Less than or equal to (opposite of greater than)
    def __le__(self, other):
        return not self > other

    # Greater than or equal to (opposite of less than)
    def __ge__(self, other):
        return not self < other


class R3Vector(R2Vector):
    # Initialize a 3D vector (inherits x, y from R2Vector and adds z)
    def __init__(self, *, x, y, z):
        super().__init__(x=x, y=y)
        self.z = z
        
    # Compute the cross product of two 3D vectors
    def cross(self, other):
        if type(self) != type(other):
            return NotImplemented
        # Apply the cross product formula component-wise
        kwargs = {
            'x': self.y * other.z - self.z * other.y,
            'y': self.z * other.x - self.x * other.z,
            'z': self.x * other.y - self.y * other.x
        }
        # Return a new R3Vector instance representing the cross product
        return self.__class__(**kwargs)


# Create two 3D vectors v1 and v2
v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)

# Print the vectors using the __str__ method (tuple representation)
print(f'v1 = {v1}')   # Output: v1 = (2, 3, 1)
print(f'v2 = {v2}')   # Output: v2 = (0.5, 1.25, 2)

# Vector addition: component-wise sum
v3 = v1 + v2
print(f'v1 + v2 = {v3}')   # Output: v1 + v2 = (2.5, 4.25, 3)

# Vector subtraction: component-wise difference
v4 = v1 - v2
print(f'v1 - v2 = {v4}')   # Output: v1 - v2 = (1.5, 1.75, -1)

# Dot product: scalar product of two vectors
v5 = v1 * v2
print(f'v1 * v2 = {v5}')   # Output: scalar value

# Cross product: vector perpendicular to v1 and v2
v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')   # Output: vector resulting from cross product
