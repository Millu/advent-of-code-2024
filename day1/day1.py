file_path = 'pt1_input.txt'

distances = []
left_list  = []
right_list = []

with open(file_path, 'r') as file:
    for line in file:
        row = line.strip().split("   ")
        left_list.append(row[0])
        right_list.append(row[1])
        
left_list.sort()
right_list.sort()

for i in range(len(left_list)):
    left = left_list[i]
    right = right_list[i]
    distance = abs(int(left) - int(right))
    distances.append(distance)

print(sum(distances))