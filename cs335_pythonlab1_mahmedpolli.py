#1. Variables and Data Types:
name = "Mahmed Aiyub Polli"
age = 20
ai_course = True

print(f"My name is {name}, I am {age} years old, and my enrollment status in CS 335 is {ai_course}.")

#2. Lists and Loops:
topics = ["Logic", "Search", "NLP", "ML", "Bayesian Inference", "Deep Learning", "Information Retrieval"]

for i, topic in enumerate(topics, start=1):
    print(f"{i}. We will study: {topic}")

#3. Dictionaries and Conditionals:
student = {"name": "Mahmed", "score": 98}

if student["score"] >= 97:
  grade = "A+"
elif student["score"] >= 90:
  grade = "A"
elif student["score"] >= 80:
  grade = "B"
else:
  grade = "C or below"

print(f"{student['name']} received a grade of {grade}.")

#4. Functions:
def greet_student(name):
  return f"Welcome to Omeed class, {name}!"

# Test
print(greet_student("Mahmed"))

def square_number(num):
  return num * num

# Test
print(square_number(5))
print(square_number(10))
