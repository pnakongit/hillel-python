def depth_of_the_lake(coordinates: list) -> int:
    if not coordinates:
        return 0

    coordinates = list(enumerate(coordinates))

    min_point = coordinates[0]
    max_point = coordinates[0]
    depths_list = [0]
    for i in range(0, len(coordinates) - 1):
        if coordinates[i][1] <= coordinates[i + 1][1] and max_point[1] <= coordinates[i + 1][1]:
            if coordinates[i + 1][0] - max_point[0] == 1:
                max_point = coordinates[i + 1]
                min_point = coordinates[i + 1]
            else:
                depths_list.append(max_point[1] - min_point[1])
                max_point = coordinates[i + 1]
                min_point = coordinates[i + 1]
        elif coordinates[i][1] > coordinates[i + 1][1] and min_point[1] > coordinates[i + 1][1]:
            min_point = coordinates[i + 1]

    return max(depths_list)


assert (depth_of_the_lake([1, 2, 5, 6, 1, 2, 2, 3, 0, 1, 5, 6, 7, 5, 5, 7, 8, 8, 2]) == 6)
assert (depth_of_the_lake([]) == 0)
assert (depth_of_the_lake([1, 2, 3, 2, 1, 2, 3, 2, 1, 4, 0, 4]) == 4)
assert (depth_of_the_lake([1, 2, 3, 2, 1, 2, 3, 2]) == 2)
assert (depth_of_the_lake([1, 2]) == 0)

print('SUCCESS')
