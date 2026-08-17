from collections import deque

processes = [
    ["P1", 0, 7],
    ["P2", 1, 4],
    ["P3", 2, 15],
    ["P4", 3, 11],
    ["P5", 4, 20],
    ["P6", 4, 9]
]



def round_robin(processes, tq):

    n = len(processes)

    at = [p[1] for p in processes]
    bt = [p[2] for p in processes]
    rt = bt[:]

    ct = [0] * n
    visited = [False] * n

    q = deque()

    time = 0
    completed = 0
    sequence = []

    while completed < n:

        for i in range(n):
            if at[i] <= time and not visited[i]:
                q.append(i)
                visited[i] = True

        if not q:
            time += 1
            continue

        i = q.popleft()

        sequence.append(processes[i][0])

        run = min(tq, rt[i])

        time += run
        rt[i] -= run

        for j in range(n):
            if at[j] <= time and not visited[j]:
                q.append(j)
                visited[j] = True

        if rt[i] > 0:
            q.append(i)
        else:
            ct[i] = time
            completed += 1

    tat = [ct[i] - at[i] for i in range(n)]
    wt = [tat[i] - bt[i] for i in range(n)]

    print("\nROUND ROBIN")
    print("Execution Sequence:")
    print(" -> ".join(sequence))

    print("\n{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
        "P", "AT", "BT", "CT", "TAT", "WT"))

    for i in range(n):
        print("{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
            processes[i][0],
            at[i],
            bt[i],
            ct[i],
            tat[i],
            wt[i]
        ))

    avg_tat = sum(tat) / n
    avg_wt = sum(wt) / n

    print("\nAverage TAT =", round(avg_tat, 2))
    print("Average WT  =", round(avg_wt, 2))

    return round(avg_tat,2), round(avg_wt,2)


def fcfs(processes):

    p = sorted(processes, key=lambda x: x[1])

    time = 0
    result = []
    sequence = []

    for name, at, bt in p:

        if time < at:
            time = at

        sequence.append(name)

        ct = time + bt
        tat = ct - at
        wt = tat - bt

        result.append([name, at, bt, ct, tat, wt])

        time = ct

    print("\nFCFS")
    print("Execution Sequence:")
    print(" -> ".join(sequence))

    print("\n{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
        "P", "AT", "BT", "CT", "TAT", "WT"))

    for r in result:
        print("{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
            r[0], r[1], r[2], r[3], r[4], r[5]
        ))

    avg_tat = sum(r[4] for r in result) / len(result)
    avg_wt = sum(r[5] for r in result) / len(result)

    print("\nAverage TAT =", round(avg_tat,2))
    print("Average WT  =", round(avg_wt,2))

    return round(avg_tat,2), round(avg_wt,2)


def sjf(processes):

    n = len(processes)

    completed = [False] * n

    time = 0
    done = 0

    result = []
    sequence = []

    while done < n:

        ready = []

        for i, p in enumerate(processes):
            if p[1] <= time and not completed[i]:
                ready.append((p[2], i))

        if not ready:
            time += 1
            continue

        ready.sort()

        bt, idx = ready[0]

        name, at, bt = processes[idx]

        sequence.append(name)

        ct = time + bt
        tat = ct - at
        wt = tat - bt

        result.append([name, at, bt, ct, tat, wt])

        time = ct

        completed[idx] = True
        done += 1

    print("\nSJF")
    print("Execution Sequence:")
    print(" -> ".join(sequence))

    print("\n{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
        "P", "AT", "BT", "CT", "TAT", "WT"))

    for r in result:
        print("{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}".format(
            r[0], r[1], r[2], r[3], r[4], r[5]
        ))

    avg_tat = sum(r[4] for r in result) / len(result)
    avg_wt = sum(r[5] for r in result) / len(result)

    print("\nAverage TAT =", round(avg_tat,2))
    print("Average WT  =", round(avg_wt,2))

    return round(avg_tat,2), round(avg_wt,2)


rr_tat, rr_wt = round_robin(processes, 5)

fcfs_tat, fcfs_wt = fcfs(processes)

sjf_tat, sjf_wt = sjf(processes)

print("\nCOMPARISON")

print("{:<15}{:<15}{:<15}".format("Algorithm","Avg TAT","Avg WT"))
print("{:<15}{:<15}{:<15}".format("Round Robin",rr_tat,rr_wt))
print("{:<15}{:<15}{:<15}".format("FCFS",fcfs_tat,fcfs_wt))
print("{:<15}{:<15}{:<15}".format("SJF",sjf_tat,sjf_wt))

algorithms = [
    ("Round Robin", rr_wt),
    ("FCFS", fcfs_wt),
    ("SJF", sjf_wt)
]

best = min(algorithms, key=lambda x: x[1])

print("\nBest Scheduling Algorithm =", best[0])
print("Reason: It has the Lowest Average Waiting Time.")