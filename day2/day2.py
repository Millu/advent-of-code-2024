def day2_pt1(file_path):
    # https://adventofcode.com/2024/day/2#part1
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

def day2_pt2(file_path):
    # https://adventofcode.com/2024/day/2#part2

    # Psuedo code:
    # If a number makes the level unsafe:
    # Delete the number from the list, add 1 to the unsafe level counter and check the list again
    # If the level is found unsafe and the unsafe level counter is > 1 then the level is unsafe



    total_safe_levels = 0

    with open(file_path, 'r') as file:
        for line in file:
            
            level = line.strip().split(" ")
            direction = ''
            is_level_safe = False
            num_unsafe_levels = 0

            if int(level[1]) > int(level[0]):
                direction = 'increasing'
            else:
                direction = 'decreasing'
            
            for i in range(1,len(level)):
                
                diff = abs(int(level[i]) - int(level[i-1]))
                
                if diff >= 1 and diff <= 3:
                    if i > 1 and direction == 'increasing' and int(level[i]) > int(level[i-1]):
                        print('increasing')
                        is_level_safe = True
                    elif i > 1 and direction == 'decreasing' and int(level[i]) < int(level[i-1]):
                        print('descreasing')
                        is_level_safe = True
                    elif i == 1:
                         pass
                    else:
                        print('diff:', diff, 'i:', level[i], 'i-1:', level[i-1]) 
                        num_unsafe_levels += 1
                        if num_unsafe_levels > 1:
                            print('unsafe levels in count:', num_unsafe_levels, level,)
                            is_level_safe = False
                            break
                else:                   
                    num_unsafe_levels += 1
                    print('unsafe levels:', num_unsafe_levels, level, )
                    if num_unsafe_levels > 1:
                        print('break')
                        is_level_safe = False
                        break
            
            if is_level_safe:
                print('level is safe:', is_level_safe, level, '\n')
                total_safe_levels += 1

    print("Safe levels including 1 bad level: ", total_safe_levels)
                                                

if __name__ == "__main__":
    
    file_path = 'day2_example.txt'
    day2_pt1(file_path)
    day2_pt2(file_path)

        
    

    