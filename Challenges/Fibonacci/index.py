

while True:
    try:
        places = int(input("How many places do you want to generate to?\n   "))
        break
    except:
        print("Please enter an integer\n")
        
print("\n")

numbers = [1,2]

if places > 2:
    for x in range(places-2):
        numbers.append(numbers[-1]+numbers[-2])

print("------------ normal order ------------\n")
for x in range(places):
    print(numbers[x], end=", ")

print("\n\n------------ flipped order ------------\n")
for x in range(places):
    print(numbers[-x-1], end=", ")