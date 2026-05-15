#Job Scheduling Problem
# Function to perform Job Scheduling
def job_scheduling(jobs):

    # 🔹 Step 1: Sort jobs based on profit in descending order
    # x[2] means profit, reverse=True means highest profit first
    jobs.sort(key=lambda x: x[2], reverse=True)

    # 🔹 Step 2: Find maximum deadline
    # This decides number of available time slots
    max_deadline = max(job[1] for job in jobs)

    # 🔹 Step 3: Create slots (initialize with -1 means empty)
    slots = [-1] * (max_deadline + 1)

    # 🔹 Step 4: Initialize total profit
    total_profit = 0

    # 🔹 Step 5: Iterate through each job
    for job in jobs:
        job_id, deadline, profit = job   # unpack job details

        # 🔹 Step 6: Try to assign job to a free slot
        # Start from last possible slot (deadline) and move backward
        for j in range(deadline, 0, -1):

            # If slot is empty, assign job
            if slots[j] == -1:
                slots[j] = job_id        # assign job to slot
                total_profit += profit   # add profit
                break                    # move to next job

    # 🔹 Step 7: Return result
    return slots, total_profit


# 🔹 User Input
n = int(input("Enter number of jobs: "))

jobs = []
print("Enter job details (id deadline profit):")

for _ in range(n):
    job_id, deadline, profit = input().split()
    jobs.append((job_id, int(deadline), int(profit)))

# 🔹 Call function
slots, profit = job_scheduling(jobs)

# 🔹 Output result
print("\nScheduled Jobs:")
for i in range(1, len(slots)):
    if slots[i] != -1:
        print(f"Slot {i} -> Job {slots[i]}")

print("Total Profit:", profit)

