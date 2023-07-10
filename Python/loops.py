"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    failed_count = 0
    for score in student_scores:
        if score <= 40:
            failed_count += 1
    return failed_count

    # failed_students =  [score for score in student_scores if score <= 40]
    # return len(failed_students)


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """

    spread = highest - 40
    segment_length = spread // 4
    return [41, 41 + segment_length, 41 + segment_length * 2, 41 + segment_length * 3]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in ascending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """

    students = []
    for (name, score) in zip(student_names, student_scores):
        rank = f"{student_names.index(name) + 1}. {name}: {score}"
        students.append(rank)

    return students


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    student = []

    for info in student_info:
        if info[1] == 100:
            student = info
            break

    return student


# data = [
#     (([82], ['Betty']), ['1. Betty: 82']),
#     (([88, 73], ['Paul', 'Ernest']), ['1. Paul: 88', '2. Ernest: 73']),
#     (
#         ([100, 98, 92, 86, 70, 68, 67, 60], ['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose']),
#         ['1. Rui: 100', '2. Betty: 98', '3. Joci: 92', '4. Yoshi: 86',
#          '5. Kora: 70', '6. Bern: 68', '7. Jan: 67', '8. Rose: 60'])]

scores = [100, 98, 92, 86, 70, 68, 67, 60]
students = ['Rui', 'Betty', 'Joci', 'Yoshi', 'Kora', 'Bern', 'Jan', 'Rose']
for rank in student_ranking(scores, students):
    print(rank)