"""Program 1: Student Marks Analyzer

Accept marks for a variable number of subjects, validate the input, and
 display useful statistics and an overall pass/fail result.
"""

MAX_MARKS = 100
PASS_MARK = 40


def read_positive_integer(prompt: str) -> int:
    """Read an integer greater than zero, retrying invalid input."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Input cannot be blank. Please try again.")
            continue

        try:
            number = int(value)
        except ValueError:
            print("Please enter a whole number.")
            continue

        if number <= 0:
            print("The number must be greater than zero.")
            continue
        return number


def read_mark(subject: str) -> float:
    """Read and validate a mark for one subject."""
    while True:
        value = input(f"Enter marks for {subject} (0-{MAX_MARKS}): ").strip()

        if not value:
            print("Marks cannot be blank. Please try again.")
            continue

        try:
            mark = float(value)
        except ValueError:
            print("Please enter a numeric value.")
            continue

        if mark < 0:
            print("Marks cannot be negative.")
        elif mark > MAX_MARKS:
            print(f"Marks cannot be greater than {MAX_MARKS}.")
        else:
            return mark


def calculate_grade(percentage: float) -> str:
    """Return a grade using the predefined percentage rules."""
    if percentage >= 90:
        return "A"
    if percentage >= 80:
        return "B"
    if percentage >= 70:
        return "C"
    if percentage >= 60:
        return "D"
    return "F"


def display_report(marks: dict[str, float]) -> None:
    """Calculate and display the student's marks report."""
    total = sum(marks.values())
    subject_count = len(marks)
    maximum_total = subject_count * MAX_MARKS
    percentage = (total / maximum_total) * 100
    average = total / subject_count
    failed_subjects = [
        subject for subject, mark in marks.items() if mark < PASS_MARK
    ]
    passed = not failed_subjects

    print("\n" + "=" * 40)
    print("STUDENT MARKS REPORT")
    print("=" * 40)
    for subject, mark in marks.items():
        result = "Pass" if mark >= PASS_MARK else "Fail"
        print(f"{subject}: {mark:g}/{MAX_MARKS} ({result})")
    print("-" * 40)
    print(f"Total marks : {total:g}/{maximum_total}")
    print(f"Percentage  : {percentage:.2f}%")
    print(f"Average     : {average:.2f}")
    print(f"Highest mark: {max(marks.values()):g}")
    print(f"Lowest mark : {min(marks.values()):g}")
    print(f"Overall grade: {calculate_grade(percentage)}")

    if passed:
        print("Overall result: PASS - The student passed every subject.")
    else:
        failed_list = ", ".join(failed_subjects)
        print("Overall result: FAIL")
        print(
            f"The student failed {len(failed_subjects)} subject(s): {failed_list}."
        )
        print(
            f"A minimum of {PASS_MARK} marks is required in every subject, "
            "even when the overall percentage is high."
        )
    print("=" * 40)


def main() -> None:
    """Collect a variable number of subject marks and generate a report."""
    print("Student Marks Analyzer")
    print(
        f"Grade rules: A = 90-100, B = 80-89, C = 70-79, "
        f"D = 60-69, F < 60 | Pass mark per subject: {PASS_MARK}"
    )

    subject_count = read_positive_integer("How many subjects? ")
    marks: dict[str, float] = {}

    for index in range(1, subject_count + 1):
        while True:
            subject = input(f"Enter name for subject {index}: ").strip()
            if not subject:
                print("Subject name cannot be blank. Please try again.")
            elif subject in marks:
                print("That subject has already been entered. Please use another name.")
            else:
                break
        marks[subject] = read_mark(subject)

    display_report(marks)


if __name__ == "__main__":
    main()
