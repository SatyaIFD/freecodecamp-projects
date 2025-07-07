import math

# Constants
GRAVITATIONAL_ACCELERATION = 9.81  # Earth's gravity in m/s^2
PROJECTILE = "∙"                  # Symbol to represent the projectile in the graph
x_axis_tick = "T"                # Symbol for x-axis tick
y_axis_tick = "⊣"                # Symbol for y-axis tick

# =========================
# Class: Projectile
# =========================
class Projectile:
    __slots__ = ('__speed', '__height', '__angle')  # Optimize memory usage

    def __init__(self, speed, height, angle):
        # Convert angle from degrees to radians (needed for trig functions)
        self.__speed = speed
        self.__height = height
        self.__angle = math.radians(angle)

    def __str__(self):
        # Nicely formatted string showing projectile details
        return f'''
Projectile details:
speed: {self.speed} m/s
height: {self.height} m
angle: {self.angle}°
displacement: {round(self.__calculate_displacement(), 1)} m
'''

    def __calculate_displacement(self):
        # Calculate total horizontal distance using physics formula
        horizontal = self.__speed * math.cos(self.__angle)
        vertical = self.__speed * math.sin(self.__angle)
        extra = math.sqrt(vertical ** 2 + 2 * GRAVITATIONAL_ACCELERATION * self.__height)
        return horizontal * (vertical + extra) / GRAVITATIONAL_ACCELERATION

    def __calculate_y_coordinate(self, x):
        # Compute the y position for a given x using projectile motion equation
        y0 = self.__height
        tan_angle = math.tan(self.__angle)
        cos_angle_sq = math.cos(self.__angle) ** 2
        gravity_term = (GRAVITATIONAL_ACCELERATION * x ** 2) / (2 * self.__speed ** 2 * cos_angle_sq)
        return y0 + x * tan_angle - gravity_term

    def calculate_all_coordinates(self):
        # Get all (x, y) coordinate pairs along the trajectory
        return [(x, self.__calculate_y_coordinate(x))
                for x in range(math.ceil(self.__calculate_displacement()))]

    # ====== Property Getters ======
    @property
    def speed(self):
        return self.__speed

    @property
    def height(self):
        return self.__height

    @property
    def angle(self):
        # Convert internal radians back to degrees for user
        return round(math.degrees(self.__angle))

    # ====== Setters ======
    @speed.setter
    def speed(self, value):
        self.__speed = value

    @height.setter
    def height(self, value):
        self.__height = value

    @angle.setter
    def angle(self, value):
        self.__angle = math.radians(value)

    def __repr__(self):
        # Programmer-friendly string representation
        return f'{self.__class__.__name__}({self.speed}, {self.height}, {self.angle})'


# =========================
# Class: Graph
# =========================
class Graph:
    __slots__ = ('__coordinates',)

    def __init__(self, coordinates):
        # Accepts a list of (x, y) coordinates
        self.__coordinates = coordinates

    def __repr__(self):
        return f"Graph({self.__coordinates})"

    def create_coordinates_table(self):
        # Return a string showing all coordinates in a table format
        table = '\n  x      y\n'
        for x, y in self.__coordinates:
            table += f'{x:>3}{y:>7.2f}\n'
        return table

    def create_trajectory(self):
        # 1. Round all coordinates to nearest integers
        rounded_coords = [(round(x), round(y)) for x, y in self.__coordinates]

        # 2. Determine max x and y to size the matrix
        x_max = max(x for x, _ in rounded_coords)
        y_max = max(y for _, y in rounded_coords)

        # 3. Create an empty matrix filled with spaces
        matrix_list = []
        for _ in range(y_max + 1):
            matrix_list.append([" "] * (x_max + 1))

        # 4. Place projectile symbol (∙) at each coordinate
        for x, y in rounded_coords:
            if 0 <= x <= x_max and 0 <= y <= y_max:
                matrix_list[y_max - y][x] = PROJECTILE  # y-axis is flipped (bottom = 0)

        # 5. Add y-axis ticks to each row
        with_y_axis = [y_axis_tick + "".join(row) for row in matrix_list]

        # 6. Add x-axis ticks as the final row
        x_axis_row = " " + x_axis_tick * (x_max + 1)

        # 7. Return as a formatted multi-line string
        return "\n" + "\n".join(with_y_axis + [x_axis_row]) + "\n"


# =========================
# Function: projectile_helper
# =========================
def projectile_helper(speed, height, angle):
    # 1. Create the projectile
    ball = Projectile(speed, height, angle)

    # 2. Print the projectile's info
    print(ball)

    # 3. Calculate coordinates and pass to graph
    coordinates = ball.calculate_all_coordinates()
    graph = Graph(coordinates)

    # 4. Print coordinates table
    print(graph.create_coordinates_table())

    # 5. Print visual trajectory
    print(graph.create_trajectory())


# ✅ Final call to run it
projectile_helper(10, 3, 45)
