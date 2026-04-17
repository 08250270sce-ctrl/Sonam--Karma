#Input student IDs
id1 = input("Enter Student 1 ID: ")
id2 = input("Enter Student 2 ID: ")

# Extract last two digits and convert to integer
last_two_1 = int(id1[-2:])
last_two_2 = int(id2[-2:])

# Generate unique value
unique_value = (last_two_1 + last_two_2) % 10
print (f"Unique value for the quiz: {unique_value}")

