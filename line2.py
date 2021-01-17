import copy
from prob import *

# tree_inv = [set(), set(), {0}, {0, 1}, {1}, {2},
#             {5}, {3, 4}, {7}, {4}, {6, 8, 9}]
# times = [3, 6, 7, 5, 2, 4, 5, 7, 1, 6, 4]
tree_inv = TREE_INV
times = TIMES
cycle_time = CYCLE_TIME
N = len(times)

# (すでに終わったタスクのリスト, 今作業してる人の作業時間) → 次にできる仕事のリスト


def available_tasks(past, time):
    tasks = []
    past_set = set(past)
    for i in range(N):
        if not i in past and tree_inv[i].issubset(past_set) and time + times[i] <= cycle_time:
            tasks.append(i)
    return tasks

# タスクのリスト → タスク全部の時間


def Time(tasks):
    time = 0
    for task in tasks:
        time += times[task]
    return time

# (前の人までに終わったタスクのリスト, 今作業中の人のタスクのリストのリスト)
# → 次にできるタスクまで含めたタスクのリストのリスト


def next_step(past, sequences_b):
    sequences = []
    for past_per in sequences_b:
        if available_tasks(past + past_per, Time(past_per)) == []:
            sequences.append(past_per)
        else:
            for task in available_tasks(past + past_per, Time(past_per)):
                past_per_next = copy.copy(past_per)
                past_per_next.append(task)
                sequences.append(past_per_next)
    for li in sequences:
        li.sort()
    return get_unique_list(sequences)

# ２重リストの一意化


def get_unique_list(seq):
    seen = []
    return [x for x in seq if x not in seen and not seen.append(x)]


# すでに終わったタスクのリスト → 次の人がする全タスクのリストのリスト
def next_person(past):
    sequences_b = [[]]
    while True:
        sequences_b = next_step(past, sequences_b)
        if sequences_b == next_step(past, sequences_b):
            break
    return sequences_b
