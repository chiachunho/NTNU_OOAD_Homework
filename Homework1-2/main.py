from Triangle import Triangle
from Square import Square
from Circle import Circle
from ShapeDatabse import ShapeDatabase

# construct shapes
shape1 = Triangle(0, 1, 6)
shape2 = Square(2, 2, 4, side_length=2)
shape3 = Circle(3, 3, 5, radius=3)
shape4 = Circle(2, 3, 3, radius=4)
shape5 = Square(1, 2, 1, side_length=5)
shape6 = Triangle(3, 1, 2, side_length=6)

# construct database
db = ShapeDatabase()

# append shapes to database
db.append(shape1)
db.append(shape2)
db.append(shape3)
db.append(shape4)
db.append(shape5)
db.append(shape6)

# print amount to console
print(f'Shape amount in database: {len(db)}')
print('')

# iterate the database to get shape and print its info out
print('Print shape in database:')
for shape in db:
    print(shape)

# sort the database
print('\nSort shapes in database by z-value.\n')
db.sort()

print('Print shape in database:')
for shape in db:
    print(shape)

# clear database
print('\nClear database.\n')
db.clear()

print(f'Shape amount in database: {len(db)}')
if len(db) == 0:
    print('Database is empty.')

# print(db.__shape_list) # shape_list is private variable can't direct access
