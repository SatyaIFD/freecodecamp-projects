from abc import ABC, abstractmethod
import re

# Abstract Base Class for equations
class Equation(ABC):
    degree: int  # Expected degree of the equation (e.g., 1 for linear, 2 for quadratic)
    type: str    # A human-readable description of the equation type

    def __init__(self, *args):
        # Validate the number of coefficients
        if (self.degree + 1) != len(args):
            raise TypeError(
                f"'Equation' object takes {self.degree + 1} positional arguments but {len(args)} were given"
            )
        # Validate coefficient types
        if any(not isinstance(arg, (int, float)) for arg in args):
            raise TypeError("Coefficients must be of type 'int' or 'float'")
        # First coefficient (highest degree) must not be 0
        if args[0] == 0:
            raise ValueError("Highest degree coefficient must be different from zero")
        
        # Store coefficients in a dictionary: {degree: coefficient}
        self.coefficients = {(len(args) - n - 1): arg for n, arg in enumerate(args)}

    def __init_subclass__(cls):
        # Ensure subclasses define 'degree' and 'type' class attributes
        if not hasattr(cls, "degree"):
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'degree'")
        if not hasattr(cls, "type"):
            raise AttributeError(f"Cannot create '{cls.__name__}' class: missing required attribute 'type'")

    def __str__(self):
        # Create a string representation of the equation (e.g., x**2 + 2x + 1 = 0)
        terms = []
        for n, coefficient in self.coefficients.items():
            if not coefficient:
                continue
            if n == 0:
                terms.append(f'{coefficient:+}')
            elif n == 1:
                terms.append(f'{coefficient:+}x')
            else:
                terms.append(f"{coefficient:+}x**{n}")
        equation_string = ' '.join(terms) + ' = 0'
        return re.sub(r"(?<!\d)1(?=x)", "", equation_string.strip("+"))

    @abstractmethod
    def solve(self):
        # Abstract method to be implemented by subclasses
        pass

    @abstractmethod
    def analyze(self):
        # Abstract method to analyze properties of the equation
        pass


# Linear equation implementation
class LinearEquation(Equation):
    degree = 1
    type = 'Linear Equation'

    def solve(self):
        # Solving ax + b = 0 => x = -b / a
        a, b = self.coefficients.values()
        x = -b / a
        return [x]

    def analyze(self):
        # Return slope and y-intercept
        slope, intercept = self.coefficients.values()
        return {'slope': slope, 'intercept': intercept}


# Quadratic equation implementation
class QuadraticEquation(Equation):
    degree = 2
    type = 'Quadratic Equation'

    def __init__(self, *args):
        super().__init__(*args)
        a, b, c = self.coefficients.values()
        self.delta = b**2 - 4 * a * c  # Discriminant

    def solve(self):
        # Solve using the quadratic formula
        if self.delta < 0:
            return []  # No real roots
        a, b, _ = self.coefficients.values()
        x1 = (-b + (self.delta) ** 0.5) / (2 * a)
        x2 = (-b - (self.delta) ** 0.5) / (2 * a)
        if self.delta == 0:
            return [x1]  # One real root
        return [x1, x2]  # Two real roots

    def analyze(self):
        a, b, c = self.coefficients.values()
        x = -b / (2 * a)  # x-coordinate of vertex
        y = a * x**2 + b * x + c  # y-coordinate of vertex
        if a > 0:
            concavity = 'upwards'
            min_max = 'min'
        else:
            concavity = 'downwards'
            min_max = 'max'
        return {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}


# Function to solve and display formatted output for any Equation object
def solver(equation):
    if not isinstance(equation, Equation):
        raise TypeError("Argument must be an Equation object")

    # Title block
    output_string = f'\n{equation.type:-^24}'
    output_string += f'\n\n{equation!s:^24}\n\n'
    output_string += f'{"Solutions":-^24}\n\n'

    # Solve the equation
    results = equation.solve()
    match results:
        case []:
            result_list = ['No real roots']
        case [x]:
            result_list = [f'x = {x:+.3f}']
        case [x1, x2]:
            result_list = [f'x1 = {x1:+.3f}', f'x2 = {x2:+.3f}']

    # Format and add each result
    for result in result_list:
        output_string += f'{result:^24}\n'

    # Details section
    output_string += f'\n{"Details":-^24}\n\n'
    details = equation.analyze()

    # Format details depending on the type
    match details:
        case {'slope': slope, 'intercept': intercept}:
            details_list = [
                f'slope = {slope:>15.3f}',
                f'y-intercept = {intercept:>15.3f}'
            ]
        case {'x': x, 'y': y, 'min_max': min_max, 'concavity': concavity}:
            details_list = [
                f'concavity = {concavity:>12}',
                f'{min_max} = {f"({x:.3f}, {y:.3f})":>18}'
            ]

    # Append formatted details to output
    for detail in details_list:
        output_string += detail + '\n'

    return output_string


# Example usage:
quadr_eq = QuadraticEquation(1, 2, 1)
print(solver(quadr_eq))
