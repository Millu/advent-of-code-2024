def day2_pt1(file_path):
    
    total_safe_levels = 0

    with open(file_path, 'r') as file:
        for line in file:
            level = line.strip().split(" ")
            direction = ''
            is_level_safe = False
            
            if int(level[1]) > int(level[0]):
                direction = 'increasing'
            else:
                direction = 'decreasing'

            for i in range(1,len(level)):

                diff = abs(int(level[i]) - int(level[i-1]))
                
                if diff >= 1 and diff <= 3:
                    if i > 1 and direction == 'increasing' and int(level[i]) > int(level[i-1]):
                        is_level_safe = True
                    elif i > 1 and direction == 'decreasing' and int(level[i]) < int(level[i-1]):
                        is_level_safe = True
                    elif i == 1:
                         pass
                    else: 
                        is_level_safe = False
                        break
                else:
                    is_level_safe = False
                    break
            
            if is_level_safe:
                total_safe_levels += 1

    print("Safe Levels: ", total_safe_levels)
                        

if __name__ == "__main__":
    
    file_path = 'day2.txt'
    day2_pt1(file_path)

        
    

    