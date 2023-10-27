courses = {
    "Лежать кайфовать зп получать": {
        'available': 1,
        'average_mark': 98
    },
    "Полицейский": {
        'available': 20,
        'average_mark': 69
    },
    "Русский рэпер": {
        'available': 80,
        'average_mark': 10
    },
}

options = '''
Опции:
1. Выбрать курс
2. Посмотреть распределение
3. Посмотреть список курсов
'''

chart_student = []


def if_available(course=None):
    if course is None:
        return courses["Лежать кайфовать зп получать"]["available"] + courses["Полицейский"]["available"] + \
            courses["Русский рэпер"]["available"]
    return courses[course]["available"]


def average_sum(assessments):
    return sum(assessments) // len(assessments)


def add_record(course, student):
    chart_student.append((student, course))
    courses[course]["available"] -= 1
    print(f"\nВы были добавлены на курс {course}")


def choose_course():
    student = input("\nВведите своё ФИО: ")
    student += ' гр. ' + input("Введите номер группы (цифра от 1 до 9): ")
    assessments = list(map(int, input("Введите оценки по трём предметам через пробел: ").split()))

    if len(assessments) < 3:
        print("Указано недостаточное количество оценок")
        return

    average_assessments = average_sum(assessments)

    print("\nДоступные для вас курсы:\n")

    a = 1
    access_courses = dict()

    for key in courses.keys():
        available = if_available(key)
        if courses[key]["average_mark"] < average_assessments and available:
            print(f"{a}. Курс {key}, осталось свободных мест: {available}")
            access_courses[a] = key
            a += 1

    choose = int(input("\nВыберите курс по выбору: "))
    add_record(access_courses[choose], student)
    input("\nНажмите Enter, чтобы продолжить")


def print_choices():
    print("\nСписок распределенных студентов:\n")
    for num, respond in enumerate(chart_student):
        print(f"{num + 1}. Студент: {respond[0]}; Курс: {respond[1]}")
    input("\nНажмите Enter, чтобы продолжить")


def print_all_courses():
    a = 1
    print('\n Список всех курсов:\n')
    for name, course in courses.items():
        print(
            f"{a}. Курс: {name}; Ср. балл для зачисления: {course['average_mark']}; Кол-во свободных мест: {course['available']}")
        a += 1
    input("\nНажмите Enter, чтобы продолжить")


command = {

    "1": choose_course,
    "2": print_choices,
    "3": print_all_courses
}


def main():
    while if_available():

        print(options)

        choose = input()
        if choose:
            command[choose]()
        else:
            break

    else:
        print("Места на курсах закончились")


if __name__ == "__main__":
    main()