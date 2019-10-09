from os import listdir


def find_end(matrix, start):
    start_row = start[0] + 2
    start_column = start[1] + 2
    while matrix[start_row][start_column] != 'W':
        start_row = start_row + 1
    start_row = start_row - 1;
    while matrix[start_row][start_column] != 'W':
        start_column = start_column + 1
    start_column = start_column - 1
    end = [start_row+2, start_column+2]
    return end


def file_writer(matrix, start_point, end_point, file_name):
    with open(file_name, 'w') as file:
        for r_indx in range(start_point[0], end_point[0]+1):
            for c_indx in range(start_point[1], end_point[1]+1):
                file.write(matrix[r_indx][c_indx])
            if r_indx != end_point[0]:
                file.write('\n')


def spliter(file_name):
    name = file_name[0:len(file_name) - 4] + '_room_'
    file = open(file_name, 'r')
    data = file.readlines()
    file.close()
    lines = []
    for line in data:
        lines.append(line)
    lines_shape = [len(lines), len(lines[0])]
    i = 0
    room_id = 1
    while i < lines_shape[0]:
        start = []
        end = []
        j = 0
        while j < lines_shape[1]:
            if len(start) == 0 and lines[i][j] == 'W':
                start = [i, j]
                end = find_end(lines, start)
                file_writer(lines, start, end, name + str(room_id)+ '.txt')
                room_id = room_id + 1
                j = end[1]
                start = []
            j = j + 1
        if len(end) > 0:
            i = end[0]
        i = i + 1


def handler(path):
    files = listdir(path)
    for file in files:
        spliter(path + '/' + file)