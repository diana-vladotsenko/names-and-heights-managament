file_pikk_sis = "pikk.sis.txt"
file_pikk_val = "pikk.val.txt"

filehandle = open(file_pikk_sis, "r" , encoding="UTF8")
row_reading = int(filehandle.readline())
row = filehandle.readline()
print("There is", row_reading, "row/s")

#Converting rows to a list with split() method:
for _ in range(row_reading):
    students_heights = row.split()
print("There is a list of heights:", students_heights)
filehandle.close()

#Finding maximum and minimum of the list:
biggest_height = max(students_heights)
smallest_height = min(students_heights)
print("The biggest height of students is", biggest_height, "cm and smallest one is", smallest_height, "cm")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜẞÉÈÊÇÑØÅŁΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯابتثجحخدذرزسشصضطظعغفقكلمنهويאבגדהוזחטיכלמנסעפצקרשתअआइईabcdefghijklmnopqrstuvwxyzäöüßéèêçñøåłαβγδεζηθικλμνξοπρστυφχψωабвгдеёжзийклмнопрстуфхцчшщъыьэюяابتثجحخدذرزسشصضطظعغفقكلمنهويאבגדהוזחטיכלמנסעפצקרשתअआइई"
alphabet_from_all_languages = list(letters)
found = True
# print(alphabet_from_all_languages)
students_names = list()
for _ in range(row_reading):
    while found:
        students = input("Give a name for student: ").strip()
        if students and students[0] in alphabet_from_all_languages:
            students_names.append(students)
            break
        else:
            print("Please, write a name again:)")
print("All names that you gave for students: ",students_names)

al = [students_names,students_heights]
dictionary = {}
for i in range (row_reading):
    dictionary[al[0][i]] = al[1][i]
print("Student names to heights",dictionary)
result = str(dictionary)

#Let`s write data to another file:
filehandle_w = open(file_pikk_val,"a",encoding="UTF8")
filehandle_w.write("There is a result of student names and heights:")
for k,v in dictionary.items():
    filehandle_w.write("\n" + k +" "+ v)
filehandle_w.close()