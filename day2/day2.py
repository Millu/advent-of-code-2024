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

    print("Total Safe Reports: ", total_safe_levels)

def day2_pt2(file_path):
    # https://adventofcode.com/2024/day/2#part2

    total_safe_levels = 0

    with open(file_path, 'r') as file:
        for line in file:
            
            level = line.strip().split(" ")
            num_unsafe_levels = 0
            direction = ''
            total_safe_levels = 0
            
            i = 0
            while i < len(level):
                if i == 0:
                    if int(level[1]) > int(level[0]):
                        direction = 'increasing' 
                        i += 1
                    elif int(level[1]) < int(level[0]):
                        direction = 'decreasing'
                        i += 1
                    else:
                        del level.copy()[i]
                        num_unsafe_levels += 1
                        if num_unsafe_levels > 2:
                            break
                        i = 0
                else:
                    diff = abs(int(level[i]) - int(level[i-1]))
                    if diff >= 1 and diff <= 3:
                        if i > 1 and direction == 'increasing' and int(level[i]) > int(level[i-1]):
                            i += 1
                        elif i > 1 and direction == 'decreasing' and int(level[i]) < int(level[i-1]):
                            i += 1
                        elif i == 1:
                            i += 1
                        else:
                            del level.copy()[i]
                            num_unsafe_levels += 1
                            if num_unsafe_levels > 2:
                                break
                            i = 0
                    else:
                        del level.copy()[i]
                        num_unsafe_levels += 1
                        if num_unsafe_levels > 2:
                            break
                        i = 0
            
            if num_unsafe_levels < 2:
                total_safe_levels += 1
        print('Total Safe Reports:', total_safe_levels)

if __name__ == "__main__":
    
    file_path = 'day2_example.txt'
    print(file_path, '\n')
    day2_pt1(file_path)
    day2_pt2(file_path)

        
    

    





# direction = ''
#             is_level_safe = False
#             num_unsafe_levels = 0
                        
#             checked_levels = level.copy()
#             i = 1
#             print('level:', level)
#             while i < len(checked_levels):
                
#                 if i == 1:
#                     direction_diff = int(checked_levels[1]) - int(checked_levels[0])
                    
#                     print('i',i, 'direction_diff:', direction_diff, '1_value:', checked_levels[1], '0_value:', checked_levels[0], checked_levels)
#                     if direction_diff == 0:
#                         checked_levels = level.copy()
#                         checked_levels.pop(i-1)
#                         num_unsafe_levels += 1
#                         i = 1

#                     elif direction_diff > 0:
#                         direction = 'increasing'    
#                     elif direction_diff < 0:
#                         direction = 'decreasing'

#                     print('direction_check:',direction, checked_levels, )
#                 diff = abs(int(checked_levels[i]) - int(checked_levels[i-1]))

#                 if diff >= 1 and diff <= 3:
#                     if i > 1 and direction == 'increasing' and int(checked_levels[i]) > int(checked_levels[i-1]):
#                         is_level_safe = True
#                         i += 1
#                     elif i > 1 and direction == 'decreasing' and int(checked_levels[i]) < int(checked_levels[i-1]):
#                         is_level_safe = True
#                         i += 1
#                     elif i == 1:
#                         pass
#                         i += 1
#                     else:
#                         if num_unsafe_levels == 0:
#                             print('0000   ','i:', i, 'level:', checked_levels, 'direction:', direction)
#                             checked_levels.pop(i-1)
#                             num_unsafe_levels += 1
#                         elif num_unsafe_levels == 1:
#                             print('1111   ','i:', i, 'level:', checked_levels, 'direction:', direction)
#                             checked_levels = level.copy()
#                             checked_levels.pop(i-1)
#                             num_unsafe_levels += 1
#                         elif num_unsafe_levels >= 2:
#                             print('2222   ','i:', i, 'level:', checked_levels, 'direction:', direction)
#                             is_level_safe = False
#                             print('Unsafe level:', level,'direction:', direction, '\n')
#                             break
                        
#                         i = 1
#                         print(i)

#                 else:                   
#                     if num_unsafe_levels == 0:
#                         print('0000diff   ','diff:', diff, 'i:', i, 'level:', checked_levels)
#                         checked_levels.pop(i-1)
#                         num_unsafe_levels += 1
#                     elif num_unsafe_levels == 1:
#                         print('1111diff   ','diff:', diff, 'i:', i, 'level:', checked_levels)
#                         checked_levels = level.copy()
#                         checked_levels.pop(i-1)
#                         num_unsafe_levels += 1
#                     elif num_unsafe_levels >= 2:
#                         print('2222diff   ','diff:', diff, 'i:', i, 'level:', checked_levels)
#                         is_level_safe = False
#                         print('Unsafe level:', level,'direction:', direction, '\n')
#                         break
                    
#                     i = 1
            
#             if is_level_safe:
#                 total_safe_levels += 1
#                 print('\n')

#     print("Safe levels including 1 bad level: ", total_safe_levels)