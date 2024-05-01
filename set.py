num=[1,2,3,4,5,6,7,8,9]

squares=set()

for item in num:
    squares.add(item ** 2)
print(squares)
print(item)

# Using Set Comprehension
square = {item ** 2 for item in num}