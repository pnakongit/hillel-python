# https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python

def sum_of_intervals(intervals):
    intervals_set = set()
    for i in intervals:
        for y in range(*i):
            intervals_set.add((y, y + 1))

    return len(intervals_set)


assert (sum_of_intervals([(1, 5)]) == 4)
assert (sum_of_intervals([(1, 5), (6, 10)]) == 8)
assert (sum_of_intervals([(1, 5), (1, 5)]) == 4)
assert (sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)

print('SUCCESS')


# перший варіант валився на великих числах, тому зробив ще в одноме варіанті
def sum_of_intervals(intervals):
    sort_intervals = sorted(intervals)

    correct_intervals = [sort_intervals[0]]
    for interval in sort_intervals[1:]:
        if interval[0] < correct_intervals[-1][1] and interval[1] <= correct_intervals[-1][1]:
            continue
        elif interval[0] < correct_intervals[-1][1] and interval[1] >= correct_intervals[-1][1]:
            correct_intervals.append((correct_intervals[-1][1], interval[1]))
        else:
            correct_intervals.append(interval)

    return sum([j - i for i, j in correct_intervals])


assert (sum_of_intervals([(1, 5)]) == 4)
assert (sum_of_intervals([(1, 5), (6, 10)]) == 8)
assert (sum_of_intervals([(1, 5), (1, 5)]) == 4)
assert (sum_of_intervals([(1, 4), (7, 10), (3, 5)]) == 7)
assert (sum_of_intervals([(-1_000_000_000, 1_000_000_000)]) == 2_000_000_000)
assert (sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]) == 100_000_030)

print('SUCCESS')
