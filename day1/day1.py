file_path = 'day1.txt'

def day1_pt1():
    
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

    print("Total Distance: ",sum(distances)) 
    return left_list, right_list

def day1_pt2(left_list, right_list):
    similarity_score = 0
    seen_dict = {}
    for i in left_list: 
        if i not in seen_dict:
            seen_dict[i] = right_list.count(i)
            similarity_score += int(i) * seen_dict[i]
        else:
            similarity_score += int(i) * seen_dict[i]

    print("Similarity Score: ", similarity_score)
    

if __name__ == "__main__":
    left_list, right_list = day1_pt1()
    day1_pt2(left_list, right_list)