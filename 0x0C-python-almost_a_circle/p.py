from models.square import Square

s = Square(5)

print(s.size)
print(s.width)
print(s.height)

s.size = 45

print(s.size)
print(s.width)
print(s.height)

try:
    s.size = "8"
except Exception as err:
    print(err)

s.update(size=78)

print(s.size)
print(s.width)
print(s.height)

s.update(width=4)


print(s.size)
print(s.width)
print(s.height)
