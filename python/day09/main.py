with open("example.txt") as f:
    lines = [l.strip() for l in f.readlines()]

def move_from_line(l):
    tup = l.split(" ")
    return tup[0], int(tup[1])

moves = [move_from_line(l) for l in lines]
# print(moves)

def move(position, direction):
    match direction:
        case "R": return (position[0] + 1, position[1])
        case "L": return (position[0] - 1, position[1])
        case "U": return (position[0], position[1] + 1)
        case "D": return (position[0], position[1] - 1)

def update_link(head_position, tail_position):
    delta = head_position[0] - tail_position[0], head_position[1] - tail_position[1]
    distance = (delta[0]**2 + delta[1]**2)**0.5
    if distance < 2:
        return tail_position
    elif distance == 2:
        return tail_position[0] + delta[0] / 2, tail_position[1] + delta[1] / 2
    else:
        return (
            tail_position[0] + delta[0] / abs(delta[0]),
            tail_position[1] + delta[1] / abs(delta[1])
        )


rope = [(0, 0) for _ in range(10)]
tail_positions = set([rope[-1]])
for direction, n in moves:
    for _ in range(n):
        rope[0] = move(rope[0], direction)
        for i in range(1, len(rope)):
            rope[i] = update_link(rope[i-1], rope[i])
        tail_positions.add(rope[-1])

print(len(tail_positions))
