with open("input.txt") as f:
    lines = [l.strip() for l in f.readlines()]

trees = [[int(t) for t in line] for line in lines]
print(trees)


def get_visibility(trees):
    visible = [False for tree in trees]
    forward_highest = -1
    backward_highest = -1
    for i in range(len(trees)):
        forward_current = trees[i]
        backward_current = trees[-1-i]
        if forward_current > forward_highest:
            visible[i] = True
            forward_highest = forward_current
        if backward_current > backward_highest:
            visible[-1-i] = True
            backward_highest = backward_current
    return visible

print(list(zip(*trees)))

left_right_visibility = [get_visibility(row) for row in trees]
up_down_visibility = [get_visibility(col) for col in zip(*trees)]

count = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        if left_right_visibility[i][j] or up_down_visibility[j][i]:
            count += 1

print(count)

def get_scenic_score(trees):
    scores = [0 for tree in trees]

    for i in range(1, len(trees)-1):
        forward_score = 0
        backward_score = 0
        for f in range(i-1, -1, -1):
            if trees[i] <= trees[f]:
                forward_score = i - f
                break
        if forward_score == 0:
            forward_score = i
        for b in range(i+1, len(trees)):
            if trees[i] <= trees[b]:
                backward_score = b - i
                break
        if backward_score == 0:
            backward_score = len(trees) - i - 1
        scores[i] = forward_score * backward_score
    return scores

left_right_score = [get_scenic_score(row) for row in trees]
up_down_score = [get_scenic_score(col) for col in zip(*trees)]
max_score = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        cur_score = left_right_score[i][j] * up_down_score[j][i]
        if cur_score > max_score:
            # print(left_right_score[i][j] , up_down_score[j][i])
            max_score = cur_score
print(max_score)
