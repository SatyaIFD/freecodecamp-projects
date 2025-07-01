Vector Classes in Python 🚀

This repository contains a simple yet powerful implementation of vector classes in Python. It supports 2D and 3D vectors with common vector operations.

Features ✨

- Create 2D (`R2Vector`) and 3D (`R3Vector`) vectors with easy-to-use classes
- Calculate vector **norm** (length)
- Perform vector addition ➕ and subtraction ➖
- Multiply vectors by scalars and compute **dot product** (scalar product) ✖️
- Compute the **cross product** of 3D vectors 🔄
- Compare vectors using relational operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)

Example Usage 💡

v1 = R3Vector(x=2, y=3, z=1)
v2 = R3Vector(x=0.5, y=1.25, z=2)

print(f'v1 = {v1}')
print(f'v2 = {v2}')

v3 = v1 + v2
print(f'v1 + v2 = {v3}')

v6 = v1.cross(v2)
print(f'v1 x v2 = {v6}')

Output 🚀

v1 = (2, 3, 1)
v2 = (0.5, 1.25, 2)
v1 + v2 = (2.5, 4.25, 3)
v1 x v2 = (4.75, -3.5, 1.0)


