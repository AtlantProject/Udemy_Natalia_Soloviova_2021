"""
Результаты экзамена хранятся в словаре: {'John': 75, 'Ann': 80, 'Ally': 60}.
Используя форматированный вывод, выведите результаты экзамена сначала в одной строке,
а затем построчно для каждого студента. При этом результаты должны быть отсортированы
в порядке убывания полученных баллов.
"""

exam_res = {'John': 75, 'Ann': 80, 'Ally': 60}

print(exam_res)

exam_res_sorted = sorted(exam_res.items(), key=lambda pair: pair[1], reverse=True)
print(f"Sorted list: {exam_res_sorted}.")

exam_res_str = ", ".join(map(lambda item: f"{item[0]} - {item[1]}", exam_res_sorted))
print(f"Exam results: {exam_res_str}")

print("=" * 75)
exam_res_str = "\n".join(map(lambda item: f"{item[0]} -- {item[1]}", exam_res_sorted))
print(f"Exam results:\n{exam_res_str}")
