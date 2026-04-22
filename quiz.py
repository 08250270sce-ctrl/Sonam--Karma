#Input student IDs
id1 = input("Enter Student 1 ID: ")
id2 = input("Enter Student 2 ID: ")

# Extract last two digits and convert to integer
last_two_1 = int(id1[-2:])
last_two_2 = int(id2[-2:])

# Generate unique value
unique_value = (last_two_1 + last_two_2) % 10
print (f"Unique value for the quiz: {unique_value}")

#step 2: Generate quiz questions based on unique value

name=input("Enter your name: ")
if unique_value == 0:
    print(f"{name}, your quiz question is: What is the capital of Bhutan?")

elif unique_value == 1:
    print(f"{name}, your quiz question is: What is the largest planet in our solar system?")

elif unique_value == 2:
    print(f"{name}, your quiz question is: Who wrote the play 'Romeo and Juliet'?")

elif unique_value == 3:
    print(f"{name}, your quiz question is: What is the chemical symbol for water?")

print(f"{name}, good luck with your quiz!")
