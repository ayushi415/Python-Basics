##  Student Marks & Percentage Calculator

maths = float(input("Enter marks of Maths: "))
science = float(input("Enter marks of Science :"));
computer = int(input("Enter marks of Computer :"));
english = int(input("Enter marks of English :"));
hindi = int(input("Enter marks of Hindi :"));

total_marks = 500
total_obtained_marks = maths + science + computer + english + hindi
percentage = (total_obtained_marks / total_marks) * 100

print(f"Total_Marks is : {total_obtained_marks}");
print(f"Percentage is : {percentage}");
