file = open(r"C:\Users\Олег\Desktop\students.txt", encoding='utf-8')
try:
    text = file.readlines()
    text[len(text) - 1] += "\n"
    text.sort()
    count = 0
    count2 = 0
    for i in text:
        count += (int)(i.split(' ')[3])
        count2 += 1
finally:
    file.close()
sorted_students = open("sorted_students.txt", "w+", encoding='utf-8')
try:
    for line in text:
        sorted_students.write(line)
    sorted_students.write("Средний балл = " + str(count/count2))
finally:
    sorted_students.close()
