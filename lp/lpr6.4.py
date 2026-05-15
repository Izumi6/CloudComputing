'''
# FIRST SIMPLE CODE

print("Employee Performance Evaluation Expert System")

attendance = int(input("Enter attendance percentage: "))
task_score = int(input("Enter task completion score out of 100: "))
behavior = input("Enter behavior (good/average/poor): ").lower()

if attendance >= 90 and task_score >= 85 and behavior == "good":
    print("Performance: Excellent")
    print("Recommendation: Promotion or bonus can be given.")

elif attendance >= 75 and task_score >= 70 and (behavior == "good" or behavior == "average"):
    print("Performance: Good")
    print("Recommendation: Continue good work.")

elif attendance >= 60 and task_score >= 50:
    print("Performance: Average")
    print("Recommendation: Training is required.")

else:
    print("Performance: Poor")
    print("Recommendation: Warning and improvement plan required.")
'''


def evaluate_employee(user_input):
    user_input = user_input.lower()

    if "excellent attendance" in user_input and "high task" in user_input:
        return "Performance: Excellent. Recommendation: Employee is eligible for promotion or bonus."

    elif "good attendance" in user_input and "good task" in user_input:
        return "Performance: Good. Recommendation: Employee performance is satisfactory."

    elif "average attendance" in user_input or "average task" in user_input:
        return "Performance: Average. Recommendation: Employee needs training and improvement."

    elif "poor attendance" in user_input or "low task" in user_input:
        return "Performance: Poor. Recommendation: Warning should be given and improvement plan is required."

    elif "bad behavior" in user_input:
        return "Performance Issue: Employee behavior needs improvement."

    elif "teamwork" in user_input and "punctual" in user_input:
        return "Performance: Very Good. Recommendation: Employee shows discipline and teamwork."

    else:
        return "Performance data not recognized. Please provide attendance, task completion, or behavior details."


def employee_performance_expert_system():
    print("Employee Performance Evaluation Expert System")
    print("Type 'exit' to quit")

    while True:
        details = input("\nEnter employee performance details: ")

        if details.lower() == "exit":
            print("Exiting system. Goodbye!")
            break

        result = evaluate_employee(details)
        print("Evaluation Result:", result)


if __name__ == "__main__":
    employee_performance_expert_system()
    