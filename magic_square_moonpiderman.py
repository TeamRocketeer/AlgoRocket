def solution(dirs) :
    cmd = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    road = set()
    cur_x, cur_y = (0, 0)

    for rou in dirs :
        next_x, next_y = cur_x + cmd[rou][0], cur_y + cmd[rou][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5 :
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2

if __name__ == '__main__' :
    dirs_1 = "ULURRDLLU"
    dirs_2 = "LULLLLLLU"

    print(solution(dirs_1))
    print(solution(dirs_2))
