PASSING_THRESHOLD = 60

def collect_grade():
    grades = []
    while True:
        user_input = input("Enter a grade (1–100), 'show' or 'exit': ").strip()

        if user_input.lower() == "exit":
            print("Goodbye.")
            break
        elif user_input.lower() == "show":
            print(grades)
        elif user_input.isdigit():
            number = int(user_input)

            if 1 <= number <= 100:
                grades.append(number)
            else:
                print("Error: number must be between 1 and 100.")
        else:
            print("Error: digits only, no letters.")

    return grades

def show_report(grades):
    if not grades:
        print("No grades entered.")
        return

    passed = 0
    for grade in grades:
        if grade >= PASSING_THRESHOLD:
            passed += 1
    average = round(sum(grades) / len(grades), 1)

    
    print(f"count: {len(grades)}")
    print(f"total: {sum(grades)}")
    print(f"highest: {max(grades)}")
    print(f"lowest: {min(grades)}")
    print(f"avg: {average}")
    print(f"passed: {passed}")
    print(f"list: {grades}")

    
def main():
    grades = collect_grade()
    show_report(grades)

if __name__ == "__main__":
    main()