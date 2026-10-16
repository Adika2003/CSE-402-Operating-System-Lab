queue = [3, 60, 10, 25, 30, 4]
head = 41
# SSTF
requests = queue.copy()
current = head
total_sstf = 0
sstf_sequence = [head]
while requests:
    nearest = requests[0]

    for r in requests:
        if abs(current - r) < abs(current - nearest):
            nearest = r

    movement = abs(current - nearest)
    print(current, "->", nearest, "=", movement)

    total_sstf += movement
    current = nearest
    sstf_sequence.append(current)
    requests.remove(nearest)

print("Total Movement:", total_sstf)
print("Sequence", sstf_sequence)

# FCFS
current = head
total_fcfs = 0
fcfs_sequence = [head]
print()
for r in queue:
    movement = abs(current - r)
    print(current, "->", r, "=", movement)
    total_fcfs += movement
    current = r
    fcfs_sequence.append(current)
print("Total Movement:", total_fcfs)
print("Sequence", fcfs_sequence)

# Comparison
print("\nComparison")
print("SSTF Total Movement:", total_sstf)
print("FCFS Total Movement:", total_fcfs)
if total_sstf < total_fcfs:
    print("SSTF is more efficient than FCFS.")
elif total_fcfs < total_sstf:
    print("FCFS is more efficient than SSTF.")
else:
    print("Both algorithms are equally efficient.")
print("Movement Saved:", abs(total_fcfs - total_sstf))
