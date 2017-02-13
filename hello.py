print("Hello world!")
# print(100 + 100)
# print(100 ** 2)

# accumulator = 0

accumulator = 0
for i in range(0, 1000):
	if i % 3 == 0 or i % 5 == 0:
		accumulator += i

print(accumulator)
