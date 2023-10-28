class Student:
    def __init__(sf, id, f_n, v, g):
        sf.id = id
        sf.f_n = f_n
        sf.v = v
        sf.g = g
    def print(sf):
        print(f"| {sf.id:<2} | {sf.f_n:<40} | {sf.v:<8} | {sf.g:<7} |")
    


f = open('students.txt', 'r', encoding="utf-8")

ss = []

for l_n, s_str in enumerate(f, start=1):
    s = s_str.strip().split(";")
    if len(s) >= 4:
        id, n, g, v = s[:4]
        sn = Student(id, n, g, v)
        ss.append(sn)
    else:
        print(f"Skipping invalid data on line {l_n}: {s_str}")

f.close()



print("-----------------------------------------------------------------------")
print("| ID | ФИО                                       | ВАРИАНТ  | ГЕНДЕР  |")
print("-----------------------------------------------------------------------")

for sn in ss:
    sn.print()

print("-----------------------------------------------------------------------")

