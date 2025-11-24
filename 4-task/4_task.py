'''
Создать классы студент, аспирант. Студент содержит свойства: номер группы, средний балл. Аспирант отличается от студента наличием научной работы (название работы в виде строки). Реализовать в классах следующие методы:

вывести информацию о человеке (фио, возраст)
вывести размер стипендии. Если средняя оценка равна 5, то стипендия 8000р для аспиранта и 6000р для студента, если меньше 5, то стипендия для аспиранта 6000р, для студента 4000р, в других случаях стипендия 0р
Сравнение размера стипендии с другим студентом/аспирантом (больше или меньше)
'''


class Student:
    high_scholarship: int = 6000
    regular_scholarship: int = 4000

    def __init__(self, full_name: str, age: int, group_number: str, average_score: float):
        if average_score < 0 or average_score > 5:
            raise ValueError("Средний балл должен быть в диапазоне 0–5")

        self.full_name = full_name
        self.age = age
        self.group_number = group_number
        self.average_score = average_score

    def get_info(self) -> str:
        return f'ФИО: {self.full_name}, возраст: {self.age}, группа: {self.group_number}'

    def get_scholarship_amount(self) -> int:
        if self.average_score == 5:
            return self.high_scholarship
        elif self.average_score < 5:
            return self.regular_scholarship
        return 0

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только со студентом или аспирантом")
        return self.get_scholarship_amount() < other.get_scholarship_amount()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только со студентом или аспирантом")
        return self.get_scholarship_amount() > other.get_scholarship_amount()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.get_scholarship_amount() == other.get_scholarship_amount()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только со студентом или аспирантом")
        return self.get_scholarship_amount() <= other.get_scholarship_amount()

    def __ge__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только со студентом или аспирантом")
        return self.get_scholarship_amount() >= other.get_scholarship_amount()


class GraduateStudent(Student):
    high_scholarship: int = 8000
    regular_scholarship: int = 6000

    def __init__(self, full_name: str, age: int, group_number: str, average_score: float, academic_work_name: str):
        super().__init__(full_name, age, group_number, average_score)
        self.academic_work_name = academic_work_name

    def get_info(self) -> str:
        base_info = super().get_info()
        return f'{base_info}, научная работа: "{self.academic_work_name}"'

    def get_scholarship_amount(self) -> int:
        if self.average_score == 5:
            return self.high_scholarship
        elif self.average_score < 5:
            return self.regular_scholarship
        return 0


if __name__ == '__main__':
    maks = Student('Максим Максимович', 20, '5132704/30801', 5.0)
    pavel = Student('Павел Павлович', 24, '5132704/30802', 3.89)
    roman = GraduateStudent('Роман Романович', 25, '5132704/30803', 4.21, 'Моделирование ИИ')
    ilya = GraduateStudent('Илья Ильич', 27, '5132704/30804', 5.0, 'ИИ в энергосистемах')

    print(maks.get_info())
    print(roman.get_info())

    print(f"{maks.full_name}: {maks.get_scholarship_amount()} руб.")
    print(f"{roman.full_name}: {roman.get_scholarship_amount()} руб.")

    print(f"{maks.full_name} vs {roman.full_name} → {maks == roman}")
    print(f"{roman.full_name} vs {ilya.full_name} → {roman > ilya}")
