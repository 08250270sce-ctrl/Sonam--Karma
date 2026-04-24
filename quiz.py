

# Taking the student Ids as string
id1 = input("Enter Student 1 ID: ")
id2 = input("Enter Student 2 ID: ")

#Make the last  two IDs as integer
last1 = int(id1[-2:])
last2 = int(id2[-2:])           

# Than you can store it in tuple
id_tuple = (last1, last2)

# Now you can generate the unique value
unique_value = (last1 + last2) % 10

print(f"\nUnique Value Generated: {unique_value}")



students = {}  # dictionary
student_list = []  # list
unique_names = set()  # set to avoid duplicates

print("Enter student names (type 'exit' to stop):")

while True:  # while loop
    name = input("Enter name: ")

    # Exit condition
    if name.lower() == "exit":
        break

    # We can useBoolean to check for empty name
    is_empty = (name == "")

    if is_empty:
        print(" Warning: Empty name not allowed!")
        continue

    # we can use set so that we won't have duplicate names.
    if name in unique_names:  
        print(" Duplicate name found, skipping...")
        continue

    # Store values
    students[name] = None  # None used initially
    student_list.append(name)
    unique_names.add(name)

# Display student names
print("Students List:")
for s in student_list:
    print("", s)


# STEP 3: tThis is the quiz Section


for student in students:  # loop through dictionary
    print(f"Quiz for {student}")
    score = 0  # integer

    # Questions stored in list
    questions = [unique_value + 2, unique_value * 3, unique_value + 5]

    # Loop through questions
    for i in range(3):
        answer = int(input(f"Q{i+1}: {unique_value} {'+' if i == 0 else '*' if i == 1 else '+'} {2 if i == 0 else 3 if i == 1 else 5} = "))
        if answer == questions[i]:
            score += 1

    # Store score
    students[student] = score



print(" Performance Report")

for student, score in students.items():

    print("Student: {}".format(student))  # format method
    print(f"Score: {score}")  # f-string

    # Warning for zero score
    if score == 0:
        print(" Warning: Score is zero!")

    # Performance using if-elif-else
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Average"
    else:
        performance = "Poor"

    print("Performance:", performance)

    # Certificate eligibility using logical condition
    if score >= 2:
        print("Certificate: Eligible")
    else:
        print("Certificate: Not Eligible")

    

    print("Stars Pattern:")
    if score == 0:
        print("")  # blank output
    else:
        for i in range(score):  # loop
            for j in range(1):  # nested loop
                print("*", end="")
        print()  # new line