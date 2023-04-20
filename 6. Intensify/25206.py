subject_grade = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}


def main():
    total_score = 0.0
    total_grade_point = 0.0
    for _ in range(20):
        name, grade, s_grade = input().split()
        grade = float(grade)
        if s_grade != "P":
            total_grade_point += grade
            total_score += grade * subject_grade[s_grade]
    major_score = total_score / total_grade_point
    print(major_score)


if __name__ == "__main__":
    main()
