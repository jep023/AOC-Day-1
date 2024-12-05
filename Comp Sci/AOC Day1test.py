# Open the file and read input
myfile = open("day1.txt", "r")  # open day1.txt, which contains input from AoC
arr = []  # create a blank array

# Read each line in the file, strip whitespace, and extract the two numbers
for line in myfile:  # go through each line in the file
    line = line.strip()
    num1 = int(line[:5])
    num2 = int(line[-5:])
    arr.append([num1, num2])  # add each line to the array as an individual item

# Compare pairs directly to find duplicates
duplicates = 0
seen_pairs = set()  # Set to track already seen pairs
for pair in arr:
    pair_tuple = tuple(pair)  # Convert the pair to a tuple to store in the set
    if pair_tuple in seen_pairs:  # Check if the pair is already seen
        duplicates += 1
        print(f"Duplicate found: {pair}")
    else:
        seen_pairs.add(pair_tuple)  # Add the pair to the seen set

print(f"Total duplicates: {duplicates}")
