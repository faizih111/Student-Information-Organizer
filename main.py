"---Student Information Organizer---"

student1 = ("ali", "18", "12th Grade")
student2 = ("ahmed", "17", "11th Grade")
subjects = {"English", "Math", "Physics"}

my_dict = {"ali": {student1}, "ahmed": {student2}}
print("Students: ", my_dict)
print("Subjects: ", subjects)

my_tuple = my_dict["ali"]
print("Details for ali: ", my_tuple)
subjects = {"English", "Math", "Physics", "English"}
print("Subjects after adding duplicates: ", subjects)
