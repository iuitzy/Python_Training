# For loop
print("For loop:")
for i in range(5):
    print(i)

# While loop
print("\nWhile loop:")
count = 0
while count < 5:
    print(count)
    count += 1

# Nested loop
print("\nNested loop:")
for i in range(3):
    for j in range(3):
        print(f"i: {i}, j: {j}")

# Loop with else
print("\nLoop with else:")
for i in range(5):
    print(i)
else:
    print("Loop completed")

# Break statement
print("\nBreak statement:")
for i in range(5):
    if i == 3:
        break
    print(i)

# Continue statement
print("\nContinue statement:")
for i in range(5):
    if i == 3:
        continue
    print(i)

# Pass statement
print("\nPass statement:")
for i in range(5):
    if i == 3:
        pass
    print(i)