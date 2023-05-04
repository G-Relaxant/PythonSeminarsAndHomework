"""
Напишите функцию, которая заменяет оценки, переданные в виде списка, но наоборот: все максимальные на минимальные
"""




def grade(lst1):
    new_grades = lst1.copy()
    min_grade = min(new_grades)
    max_grade = max(new_grades)
    if min_grade == max_grade:
        return None
    for idx in range(len(new_grades)):
        if new_grades[idx] == max_grade:
            new_grades[idx] = min_grade
    return new_grades

lst2 = [1, 3, 3, 3, 3, 4, 2, 5, 5, 2]
res_lst = grade(lst2)
print(f'Оценки до манимуляций:    {lst2}')
print(f'Оценки после манипуляций: {res_lst}')
