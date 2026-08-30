processes = [
    ["P1", 0, 3, 3],
    ["P2", 1, 2, 4],
    ["P3", 2, 4, 6],
    ["P4", 3, 6, 4],
    ["P5", 5, 10, 2]
]

n = 5

time = 0
done = []
ct = [0] * n
sequence = []

while len(done) < n:

    available = []

    for i in range(n):
        if i not in done and processes[i][1] <= time:
            available.append(i)

    if not available:
        time += 1
        continue

    x = min(available, key=lambda i: processes[i][2])

    time += processes[x][3]
    ct[x] = time

    done.append(x)
    sequence.append(processes[x][0])


tat = []
wt = []

for i in range(n):
    tat.append(ct[i] - processes[i][1])
    wt.append(tat[i] - processes[i][3])

avg_tat_non = sum(tat) / n
avg_wt_non = sum(wt) / n


print("\nNON-PREEMPTIVE PRIORITY")

print("Execution Sequence : ", " -> ".join(sequence))

print("\n{:<10}{:<10}{:<10}{:<10}".format(
    "Process", "CT", "TAT", "WT"
))



for i in range(n):
    print("{:<10}{:<10}{:<10}{:<10}".format(
        processes[i][0], ct[i], tat[i], wt[i]
    ))

print("Average TAT : {:.2f} seconds".format(avg_tat_non))
print("Average WT  : {:.2f} seconds".format(avg_wt_non))

remaining = []

for i in range(n):
    remaining.append(processes[i][3])

ct = [0] * n
time = 0
sequence = []

while sum(remaining) > 0:

    available = []

    for i in range(n):
        if processes[i][1] <= time and remaining[i] > 0:
            available.append(i)

    if not available:
        time += 1
        continue


    x = min(available, key=lambda i: processes[i][2])

    # Run for 1 second
    remaining[x] -= 1
    time += 1


    if len(sequence) == 0 or sequence[-1] != processes[x][0]:
        sequence.append(processes[x][0])

    if remaining[x] == 0:
        ct[x] = time


tat = []
wt = []

for i in range(n):
    tat.append(ct[i] - processes[i][1])
    wt.append(tat[i] - processes[i][3])

avg_tat_pre = sum(tat) / n
avg_wt_pre = sum(wt) / n


print("\nPREEMPTIVE PRIORITY")

print("Execution Sequence : ", " -> ".join(sequence))

print("\n{:<10}{:<10}{:<10}{:<10}".format(
    "Process", "CT", "TAT", "WT"
))
for i in range(n):
    print("{:<10}{:<10}{:<10}{:<10}".format(
        processes[i][0], ct[i], tat[i], wt[i]
    ))
print("Average TAT : {:.2f} seconds".format(avg_tat_pre))
print("Average WT  : {:.2f} seconds".format(avg_wt_pre))


print("\nFINAL COMPARISON")

print("\n{:<20}{:<15}{:<15}".format(
    "Method", "Average TAT", "Average WT"
))

print("{:<20}{:<15.2f}{:<15.2f}".format(
    "Non-Preemptive",
    avg_tat_non,
    avg_wt_non
))

print("{:<20}{:<15.2f}{:<15.2f}".format(
    "Preemptive",
    avg_tat_pre,
    avg_wt_pre
))

if avg_tat_non < avg_tat_pre and avg_wt_non < avg_wt_pre:
    print("Result : Non-Preemptive is BETTER")
else:
    print("Result : Preemptive is BETTER")