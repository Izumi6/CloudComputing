'''
# FIRST SIMPLE CODE

print("Airline Scheduling and Cargo Expert System")

weather = input("Enter weather condition (clear/rainy/stormy): ").lower()
cargo_weight = int(input("Enter cargo weight in kg: "))
flight_status = input("Enter flight status (available/full/delayed): ").lower()

if weather == "stormy":
    print("Decision: Flight Delayed")
    print("Reason: Stormy weather is unsafe for flying.")

elif flight_status == "full":
    print("Decision: Cargo Rejected")
    print("Reason: Flight capacity is full.")

elif cargo_weight > 5000:
    print("Decision: Special Cargo Flight Required")
    print("Reason: Cargo weight exceeds normal limit.")

elif weather == "clear" and flight_status == "available" and cargo_weight <= 5000:
    print("Decision: Cargo Scheduled Successfully")
    print("Reason: Weather is clear and flight is available.")

elif weather == "rainy" and flight_status == "available":
    print("Decision: Cargo Scheduled with Caution")
    print("Reason: Rainy weather may cause minor delay.")

else:
    print("Decision: Check with airline manager.")
'''


def airline_schedule_advice(user_input):
    user_input = user_input.lower()

    if "stormy" in user_input:
        return "Decision: Flight Delayed. Reason: Stormy weather is unsafe for flying."

    elif "flight full" in user_input:
        return "Decision: Cargo Rejected. Reason: Flight capacity is full."

    elif "heavy cargo" in user_input:
        return "Decision: Special Cargo Flight Required. Reason: Cargo weight exceeds normal limit."

    elif "clear weather" in user_input and "flight available" in user_input:
        return "Decision: Cargo Scheduled Successfully. Reason: Weather is clear and flight is available."

    elif "rainy" in user_input and "flight available" in user_input:
        return "Decision: Cargo Scheduled with Caution. Reason: Rainy weather may cause minor delay."

    elif "delayed" in user_input:
        return "Decision: Reschedule Cargo. Reason: Flight is delayed."

    else:
        return "Decision: Contact airline manager. Reason: Schedule condition not recognized."


def airline_cargo_expert_system():
    print("Airline Scheduling and Cargo Expert System")
    print("Type 'exit' to quit")

    while True:
        condition = input("\nEnter airline or cargo condition: ")

        if condition.lower() == "exit":
            print("Exiting system. Goodbye!")
            break

        result = airline_schedule_advice(condition)
        print("Schedule Advice:", result)


if __name__ == "__main__":
    airline_cargo_expert_system()