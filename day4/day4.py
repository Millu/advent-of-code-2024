def day4_pt1(file_name):
    input_word_search = []
    with open(file_name) as file:
        for line in file:
            input_word_search.append(list(line.strip()))

    valid_letter_positions = []

    dim_x = len(input_word_search[0])
    dim_y = len(input_word_search)
    possible_directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    for i in range(len(dim_x)):
        possible_valid_letter_positions = []
        for j in range(len(dim_y)):
            if input[i][j] == 'X':
                for direction in possible_directions:
                    x, y = i, j
                    for _ in range(4):
                        x += direction[0]
                        y += direction[1]
                        if x < 0 or x >= len(input) or y < 0 or y >= len(input[i]) or input[x][y] == '.':
                            break
                        input[x][y] = 'X'
    


if __name__ == "__main__":
    file_name = 'day4_example.txt'
    day4_pt1(file_name)
    