'''
# FIRST SIMPLE CODE

print("Hospital Medical Expert System")

fever = input("Do you have fever? (yes/no): ").lower()
cough = input("Do you have cough? (yes/no): ").lower()
headache = input("Do you have headache? (yes/no): ").lower()
chest_pain = input("Do you have chest pain? (yes/no): ").lower()

if fever == "yes" and cough == "yes":
    print("Possible Disease: Flu or Viral Infection")
    print("Advice: Drink warm water, take rest, consult doctor if symptoms increase.")

elif fever == "yes" and headache == "yes":
    print("Possible Disease: Dengue or Malaria")
    print("Advice: Visit hospital and do blood test.")

elif chest_pain == "yes":
    print("Possible Emergency: Heart related issue")
    print("Advice: Visit emergency department immediately.")

elif cough == "yes":
    print("Possible Disease: Common Cold")
    print("Advice: Take steam and cough syrup.")

else:
    print("No serious symptoms detected.")
    print("Advice: Maintain good diet and hygiene.")
'''


def diagnose_medical_issue(user_input):
    user_input = user_input.lower()

    if "fever" in user_input and "cough" in user_input:
        return "Possible Disease: Flu or viral infection. Advice: Take rest, drink warm water, and consult doctor if symptoms increase."

    elif "fever" in user_input and "headache" in user_input:
        return "Possible Disease: Dengue or malaria. Advice: Visit hospital and do blood test."

    elif "chest pain" in user_input or "breathing problem" in user_input:
        return "Emergency Case: Possible heart or respiratory problem. Advice: Visit emergency department immediately."

    elif "stomach pain" in user_input or "vomiting" in user_input:
        return "Possible Disease: Food poisoning or stomach infection. Advice: Drink ORS and consult doctor."

    elif "cough" in user_input or "cold" in user_input:
        return "Possible Disease: Common cold. Advice: Take steam and drink warm water."

    elif "injury" in user_input or "bleeding" in user_input:
        return "Emergency Case: Injury detected. Advice: Apply first aid and visit hospital."

    else:
        return "Symptoms not recognized. Please consult a doctor for proper diagnosis."


def hospital_expert_system():
    print("Hospital and Medical Facilities Expert System")
    print("Type 'exit' to quit")

    while True:
        symptoms = input("\nDescribe patient symptoms: ")

        if symptoms.lower() == "exit":
            print("Exiting system. Goodbye!")
            break

        result = diagnose_medical_issue(symptoms)
        print("Suggested Result:", result)


if __name__ == "__main__":
    hospital_expert_system()