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
            
            checked_levels = level.copy()
            i = 1
            print('level: ', level)
            while i < len(checked_levels):
                print('level_being_checked:', checked_levels)
                diff = abs(int(level[i]) - int(level[i-1]))
                
                if diff >= 1 and diff <= 3:
                    if i > 1 and direction == 'increasing' and int(checked_levels[i]) > int(checked_levels[i-1]):
                        is_level_safe = True
                    elif i > 1 and direction == 'decreasing' and int(checked_levels[i]) < int(checked_levels[i-1]):
                        is_level_safe = True
                    elif i == 1:
                        pass
                    else:
                        if num_unsafe_levels == 0:
                            checked_levels.pop(i)
                            print('0000   ','i:', i, 'level:', checked_levels)
                            num_unsafe_levels += 1
                        elif num_unsafe_levels == 1:
                            checked_levels = level.copy()
                            checked_levels.pop(i)
                            print('1111   ','i:', i, 'level:', checked_levels)
                            num_unsafe_levels += 1
                        elif num_unsafe_levels == 2:
                            print('2222   ','i:', i, 'level:', checked_levels)
                            is_level_safe = False
                            print('Unsafe level:', level, '\n')
                            break
                        
                        i = 1

                else:                   
                    if num_unsafe_levels == 0:
                            checked_levels.pop(i)
                            print('0000   ','i:', i, 'level:', checked_levels)
                            num_unsafe_levels += 1
                    elif num_unsafe_levels == 1:
                        checked_levels = level.copy()
                        checked_levels.pop(i)
                        print('1111   ','i:', i, 'level:', checked_levels)
                        num_unsafe_levels += 1
                    elif num_unsafe_levels == 2:
                        print('2222   ','i:', i, 'level:', checked_levels)
                        is_level_safe = False
                        print('Unsafe level:', level, '\n')
                        break
                    
                    i = 1

                i += 1
            
            if is_level_safe:
                total_safe_levels += 1

    print("Safe levels including 1 bad level: ", total_safe_levels)
                                                

if __name__ == "__main__":
    
    file_path = 'day2_example.txt'
    print(file_path, '\n')
    day2_pt1(file_path)
    day2_pt2(file_path)

        
    

    