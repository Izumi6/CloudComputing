'''
# FIRST SIMPLE CODE

print("Help Desk Management Expert System")

problem = input("Enter problem type (network/software/hardware/login): ").lower()

if problem == "network":
    print("Solution: Check LAN cable or Wi-Fi connection.")
    print("If problem continues, contact network administrator.")

elif problem == "software":
    print("Solution: Restart the software or reinstall it.")
    print("Update the software if required.")

elif problem == "hardware":
    print("Solution: Check power supply and device connections.")
    print("If not solved, assign ticket to hardware technician.")

elif problem == "login":
    print("Solution: Reset password or check username.")
    print("If account is locked, contact admin.")

else:
    print("Problem not found in knowledge base.")
    print("Create a new support ticket.")
'''


def diagnose_issue(user_input):
    user_input = user_input.lower()

    if "password" in user_input or "login" in user_input:
        return "It seems you have a login issue. Try resetting your password or contact admin."

    elif "internet" in user_input or "network" in user_input:
        return "Check your router and cables. Restart the router or contact ISP."

    elif "slow" in user_input or "performance" in user_input:
        return "Your system may be slow due to high usage. Close unused applications or restart your computer."

    elif "printer" in user_input:
        return "Ensure the printer is connected and has paper. Reinstall printer drivers if needed."

    elif "software" in user_input or "install" in user_input:
        return "Try reinstalling the software or check for updates."

    elif "email" in user_input:
        return "Check your internet connection and email server settings."

    elif "virus" in user_input or "malware" in user_input:
        return "Run a full antivirus scan and remove any detected threats."

    else:
        return "Issue not recognized. Please contact the help desk for further assistance."


def helpdesk_expert_system():
    print("Help Desk Expert System")
    print("Type 'exit' to quit")

    while True:
        problem = input("\nDescribe your issue: ")

        if problem.lower() == "exit":
            print("Exiting system. Goodbye!")
            break

        solution = diagnose_issue(problem)
        print("Suggested Solution:", solution)


if __name__ == "__main__":
    helpdesk_expert_system()