myfile = open("day1.txt","r") #open day1.txt, which contains input from AoC
arr = [] #create a blank array
for line in myfile: #go through each line in the file
    line = line.strip()
    num1 = int(line[:5])
    num2 = int(line[-5:])
    arr.append([num1,num2]) #add each line to the array as an individual item. .strip() removes unnecessary characters (e.g. new line character)

# Create dictionaries to store counts of each number
first_half_counts = {}
second_half_counts = {}

# Count occurrences in first half
for sublist in arr:
    num = sublist[0]
    first_half_counts[num] = first_half_counts.get(num, 0) + 1

# Count occurrences in second half
for sublist in arr:
    num = sublist[1]
    second_half_counts[num] = second_half_counts.get(num, 0) + 1

# Find duplicates by comparing dictionaries above
duplicates = 0
for num in first_half_counts:
    if num in second_half_counts:
        # Add the minimum count from either array to get total duplicates
        duplicates += min(first_half_counts[num], second_half_counts[num])
        print(f"Duplicate found: {num} appears {first_half_counts[num]} times in first array and {second_half_counts[num]} times in second array")

print(f"Total duplicates found: {duplicates}")

# Calculate total distance
sorted_first_half = []
for sublist in arr:
    sorted_first_half.append(sublist[0])
sorted_first_half.sort()

sorted_second_half = []
for sublist in arr:
    sorted_second_half.append(sublist[1])
sorted_second_half.sort()

total_dist = 0
for i in range(len(sorted_first_half)):
    a = sorted_first_half[i]
    b = sorted_second_half[i]
    total_dist += abs(a-b)
print("Total:", total_dist)
