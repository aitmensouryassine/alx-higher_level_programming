from models.square import Square

s = Square(5, 5, 5)

print(s.id)
print(s.size)

s.update(None)

print(s.id)
print(s.size)
