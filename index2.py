def main():
    # Kërkesa 1: Përdoruesi shkruan numrin total të nxënësve në klasë
    total_students = int(input("Shkruani numrin total të nxënësve në klasë: "))
    
    # Kërkesa 3: Krijohet një dictionary zbrazët për të ruajtur emrat dhe notat e nxënësve
    students = {}

    # Kërkesa 2: Përdoruesi shkruan emrin dhe notën për secilin nxënës
    for _ in range(total_students):
        name = input(f"Shkruani emrin e nxënësit {_ + 1}: ")
        grade = float(input(f"Shkruani notën për {name}: "))
        students[name] = grade
    
    # Kërkesa 4: Llogaritet mesatarja e notave të nxënësve
    average_grade = calculate_average(students)
    
    # Kërkesa 5: Gjendet vlera minimale dhe maksimale e notave
    min_grade, max_grade = find_min_max(students)
    
    # Kërkesa 6: Krijohen dy dictionaries për nxënësit që kanë kaluar dhe ata që nuk kanë kaluar
    passed_students, failed_students = categorize_students(students)
    
    # Kërkesa 8: Shtimi i emrit të nxënësit tek objektet për të cilat kanë kaluar ose nuk kanë kaluar
    add_passed_failed_labels(passed_students, failed_students)
    
    # Kërkesa 9: Printimi i mesatares, notës së lartë dhe të ulët, si dhe vargjet e emrave të nxënësve që kanë kaluar dhe nuk kanë kaluar
    print_results(average_grade, min_grade, max_grade, passed_students, failed_students)

def calculate_average(students):
    total_grade = sum(students.values())
    average_grade = total_grade / len(students)
    return average_grade

def find_min_max(students):
    min_grade = min(students.values())
    max_grade = max(students.values())
    return min_grade, max_grade

def categorize_students(students):
    passed_students = {}
    failed_students = {}
    for name, grade in students.items():
        if grade >= 60:
            passed_students[name] = grade
        else:
            failed_students[name] = grade
    return passed_students, failed_students

def add_passed_failed_labels(passed_students, failed_students):
    for student in passed_students:
        passed_students[student] = {'grade': passed_students[student], 'status': 'Passed'}
    for student in failed_students:
        failed_students[student] = {'grade': failed_students[student], 'status': 'Failed'}

def print_results(average_grade, min_grade, max_grade, passed_students, failed_students):
    print(f"\nMesatarja e notave është: {average_grade}")
    print(f"Nota minimale është: {min_grade}")
    print(f"Nota maksimale është: {max_grade}")
    
    print("\nNxënësit që kanë kaluar:")
    print_students(passed_students)
    
    print("\nNxënësit që nuk kanë kaluar:")
    print_students(failed_students)

def print_students(students):
    for student, info in students.items():
        print(f"{student}: {info['grade']} ({info['status']})")

# Thirrja e funksionit kryesor
if __name__ == "__main__":
    main()

