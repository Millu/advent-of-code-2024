def day2_pt1(file_path):
    safe_levels = 0

    with open(file_path, 'r') as file:
        for line in file:
            level = line.strip().split(" ")
            direction = ''
            i = 1
            for i in range(3):
                diff = abs(int(level[i]) - int(level[i-1]))
                if diff >= 1 and diff <= 3:
                    if int(level[i]) > int(level[i-1]):
                        direction = 'increasing'
                    else:
                        direction = 'decreasing'                    
                if i > 1 and direction == 'increasing' and int(level[i]) > int(level[i-2]):
                        safe_levels += 1
                        print("safe", level)
                elif i > 1 and direction == 'decreasing' and int(level[i]) < int(level[i-2]):
                        safe_levels += 1
                        print("safe", level)

    print("Safe Levels: ", safe_levels)
                        

if __name__ == "__main__":
    
    file_path = 'day2_example.txt'
    day2_pt1(file_path)

        
    