processes = [
    ["P1", 3, 3],
    ["P2", 2, 5],
    ["P3", 5, 4],
    ["P4", 1, 3],
    ["P5", 6, 2]
]

print("========== SJF ==========\n")

ready = processes[:]
time = 0
sjf_result = []

while ready:

    available = []

    for p in ready:
        if p[1] <= time:
            available.append(p)

    if len(available) == 0:
        time = min(ready, key=lambda x: x[1])[1]
        continue

    job = min(available, key=lambda x: x[2])
    ready.remove(job)

    name, at, bt = job

    ct = time + bt
    tat = ct - at
    wt = tat - bt

    sjf_result.append([name, at, bt, ct, tat, wt])

    time = ct

print(f'{"Pd":<6}{"AT":<6}{"BT":<6}{"CT":<6}{"TAT":<6}{"WT":<6}')
for i in sjf_result:
    print(f'{i[0]:<6}{i[1]:<6}{i[2]:<6}{i[3]:<6}{i[4]:<6}{i[5]:<6}')

sjf_avg_tat = sum(i[4] for i in sjf_result) / len(sjf_result)
sjf_avg_wt = sum(i[5] for i in sjf_result) / len(sjf_result)

print("\nExecution Sequence:")
for i in sjf_result:
    print(i[0], end=" ")

print("\n\nAverage TAT =", sjf_avg_tat)
print("Average WT =", sjf_avg_wt)

print("\n\n========== FCFS ==========\n")

fcfs = sorted(processes, key=lambda x: x[1])

time = 0
fcfs_result = []

for p in fcfs:

    name, at, bt = p

    if time < at:
        time = at

    ct = time + bt
    tat = ct - at
    wt = tat - bt

    fcfs_result.append([name, at, bt, ct, tat, wt])

    time = ct

print(f'{"Pd":<6}{"AT":<6}{"BT":<6}{"CT":<6}{"TAT":<6}{"WT":<6}')
for i in fcfs_result:
    print(f'{i[0]:<6}{i[1]:<6}{i[2]:<6}{i[3]:<6}{i[4]:<6}{i[5]:<6}')

fcfs_avg_tat = sum(i[4] for i in fcfs_result) / len(fcfs_result)
fcfs_avg_wt = sum(i[5] for i in fcfs_result) / len(fcfs_result)

print("\nExecution Sequence:")
for i in fcfs_result:
    print(i[0], end=" ")

print("\n\nAverage TAT =", fcfs_avg_tat)
print("Average WT =", fcfs_avg_wt)

print("\n========== COMPARISON ==========\n")

print(f'{"Algorithm":<12}{"Avg TAT":<12}{"Avg WT":<12}')
print("-"*36)
print(f'{"SJF":<12}{sjf_avg_tat:<12.2f}{sjf_avg_wt:<12.2f}')
print(f'{"FCFS":<12}{fcfs_avg_tat:<12.2f}{fcfs_avg_wt:<12.2f}')

print()

if sjf_avg_tat < fcfs_avg_tat:
    print("SJF has lower Average Turnaround Time.")

if sjf_avg_wt < fcfs_avg_wt:
    print("SJF has lower Average Waiting Time.")

print("\nResult: SJF is Better than FCFS.")
