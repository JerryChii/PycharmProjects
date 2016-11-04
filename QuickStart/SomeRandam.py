import random

print random.choice(range(10))

print random.randint(2, 4)

print random.randrange(2)

lst = [1, '2', '5', 4]
random.shuffle(lst)
print lst

print random.uniform(2, 4)