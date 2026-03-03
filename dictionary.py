# ============================
#  First Example of Dictionary
# ============================
print("# ============================")
print("#  First Example of Dictionary")
print("# ============================")
student = {
  "name" :"Danish",
  "age"  :20,
  "city" :"Karachi"}
print(student)

# =============================================
# key() method is srf keys show kreega
# =============================================
print("# =============================================")
print("# key() method is srf keys show kreega")
print("# =============================================")
print(student.keys())
for key in student.keys():
    print(key)

# =============================================
# values() method is srf values show kreega 
# =============================================
print("# =============================================")
print("# values() method is srf values show kreega ")
print("# =============================================")
print(student.values())
for value in student.values():
    print(value)
# =============================================
# items() method is key aur value dono show kreega
# =============================================
print("# =============================================")
print("# items() method is key aur value dono show kreega")
print("# =============================================")
print(student.items())
for key, value in student.items():
    print(f"{key}: {value}")