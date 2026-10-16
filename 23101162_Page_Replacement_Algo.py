pages = [1, 2, 3, 4, 2, 3, 1]
frames = []
size = 3
hit = 0
fault = 0

for page in pages:
    if page in frames:
        hit += 1
        print(page, frames, "Hit")
    else:
        fault += 1

        if len(frames) == size:
            frames.pop(0)

        frames.append(page)
        print(page, frames, "Fault")

print("\nTotal Page Hits:", hit)
print("Total Page Faults:", fault)
print("Hit Ratio:", round(hit / len(pages), 2))
print("Fault Ratio:", round(fault / len(pages), 2))

