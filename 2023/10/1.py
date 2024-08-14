def read_map(file):
    with open(file, "r") as f:
        read_map = f.readlines()
    return read_map


directions_dictionary = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(0, -1), (1, 0)],
    "F": [(1, 0), (0, 1)],
    "S": [(-1, 0), (0, 1), (1, 0), (0, -1)],
    ".": [],
}


def get_starting_point(find_map):
    for s in find_map:
        if s.find("S") != -1:
            return find_map.index(s), s.index("S")


def get_related_pos(stand_pos, next_pos):
    return next_pos[0] - stand_pos[0], next_pos[1] - stand_pos[1]


def wait():
    input("Press to continue")


def find_furthest_pos(input_map, cur_point):
    height, width = len(input_map), len(input_map[0])
    passed_map = [[-1] * width for _ in range(height)]

    passed_map[cur_point[0]][cur_point[1]] = 0
    # print(passed_map)

    passed_pos = [cur_point]

    furthest_pos = 0

    while len(passed_pos) > 0:
        cur_x, cur_y = passed_pos[0]
        passed_pos.pop(0)

        cur_point = passed_map[cur_x][cur_y]
        cur_pipe = input_map[cur_x][cur_y]
        empty_str = ''

        print(
            f'cur pos:\n {input_map[cur_x - 1][cur_y] if cur_x >= 1 else empty_str}\n{input_map[cur_x][cur_y - 1] if cur_y > 0 else empty_str}{input_map[cur_x][cur_y]}{input_map[cur_x][cur_y + 1] if cur_y + 1 < width else empty_str}\n {input_map[cur_x + 1][cur_y] if cur_x + 1 < height else empty_str}')

        for t_x, t_y in directions_dictionary[cur_pipe]:
            n_x, n_y = cur_x + t_x, cur_y + t_y
            related_pos = (-t_x, -t_y)
            next_pipe = input_map[n_x][n_y]
            next_dir = directions_dictionary[next_pipe]
            print(f'related pos: {related_pos}, next dir: {next_dir}')
            if not (related_pos in next_dir) or passed_map[n_x][n_y] != -1:
                continue
            print(f'cur_pos: {(cur_x, cur_y)}, cur pos: {cur_point}, next pos: {(n_x, n_y)}, next pipe: {next_pipe}, '
                  f'next dir: {next_dir}')
            passed_map[n_x][n_y] = cur_point + 1
            passed_pos.append((n_x, n_y))
            furthest_pos = max(furthest_pos, cur_point + 1)
            # wait()
        # print(f'new passed map: {passed_map}')

    return furthest_pos


def part_1():
    input_file = "input.txt"
    pipe_map = read_map(input_file)
    starting_point = get_starting_point(pipe_map)
    print(find_furthest_pos(pipe_map, starting_point))
