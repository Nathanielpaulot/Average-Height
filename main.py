# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
n = 0
heights = 0
for student in student_heights:
  heights += student
  n += 1

average_height = round(heights/n)
print(average_height)

