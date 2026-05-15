'''
# FIRST SIMPLE CODE

print("Information Management Expert System")

doc_type = input("Enter document type (confidential/general/public): ").lower()
access_level = input("Enter user access level (admin/staff/guest): ").lower()

if doc_type == "confidential" and access_level == "admin":
    print("Access Granted: You can view and modify the document.")

elif doc_type == "confidential" and access_level == "staff":
    print("Access Denied: Confidential documents need admin permission.")

elif doc_type == "general" and (access_level == "admin" or access_level == "staff"):
    print("Access Granted: You can view the general document.")

elif doc_type == "public":
    print("Access Granted: Public documents are available to all users.")

else:
    print("Invalid access or document type.")
'''


def diagnose_information(user_input):
    user_input = user_input.lower()

    if "confidential" in user_input and "admin" in user_input:
        return "Access Granted: Admin can view and modify confidential information."

    elif "confidential" in user_input and "staff" in user_input:
        return "Access Denied: Staff cannot access confidential information without permission."

    elif "general" in user_input and ("admin" in user_input or "staff" in user_input):
        return "Access Granted: General information can be accessed by admin or staff."

    elif "public" in user_input:
        return "Access Granted: Public information can be accessed by everyone."

    elif "guest" in user_input:
        return "Limited Access: Guest can only view public information."

    else:
        return "Information access rule not found. Please contact system administrator."


def information_management_expert_system():
    print("Information Management Expert System")
    print("Type 'exit' to quit")

    while True:
        query = input("\nEnter document type and user role: ")

        if query.lower() == "exit":
            print("Exiting system. Goodbye!")
            break

        result = diagnose_information(query)
        print("Decision:", result)


if __name__ == "__main__":
    information_management_expert_system()