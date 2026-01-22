# Week 1 – Day 4
# Topic: Dictionaries, Tuples, and File Handling


# Dictionary example
student = {"name": "Dhruv", "age": 22,"course": "Python, AI & ML"}

print("Student Details:")
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# Tuple example
subjects = ("Python", "AI", "Machine Learning")

print("\nSubjects:")
for subject in subjects:
    print(subject)
    

# File handling - write to file
file = open("day-4/data.txt", "w")
file.write("This file was created on Day 4.\n")
file.write("Learning Python file handling.\n")
file.close()


# File handling - read from file
file = open("day-4/data.txt", "r")
content = file.read()
file.close()

print("\nFile Content:")
print(content)



