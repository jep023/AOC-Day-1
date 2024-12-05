myfile = open("day1.txt","r") #open day1.txt, which contains input from AoC
arr = [] #create a blank array
for line in myfile: #go through each line in the file
    line = line.strip()
    num1 = int(line[:5])
    num2 = int(line[-5:])
    arr.append([num1,num2]) #add each line to the array as an individual item. .strip() removes unnecessary characters (e.g. new line character)

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

i = 0# array_index_1
j = 0# array_index_2
o = i+1# array_index_1+1
k = j+1# array_index_2+1
opt = True
duplicates = 0

while opt == True:
    if i >= len(sorted_first_half) or j >= len(sorted_second_half):
        break  # Exit the loop if either index goes out of bounds
    
    a = sorted_first_half[i]
    b = sorted_second_half[j]
    if a == b:
        duplicates += 1
        print("Duplicates found", duplicates, sorted_second_half[i], sorted_first_half[j])
        i += 1  # Optionally, increment the index to avoid checking the same pair
        j += 1  # Optionally, increment the index to avoid checking the same pair
    else:
        if a < b:  # Increment the index for the smaller value
            i += 1
        else:
            j += 1
