from collections import defaultdict


def count_paths(source_path: str) -> int:
    """
    Counts the different possible paths through a cave system.
    Each valid path has to contain a start and an end point.
    A path may contain multiple entries of the came capital cave but only one instance
    per minor cave.

    :param source_path: File path to the routing info of a cave system.
    :returns: The sum of counted valid paths. Each path increments the sum by 1.
    """
    # Create dictionary
    connections = defaultdict(list)

    for line in open(source_path, 'r'):
        # Write combinations of entry end destination point per path to the dictionary
        entry, destination = line.strip().split('-')
        connections[entry].append(destination)
        connections[destination].append(entry)

    next_cave = [['start']]
    valid_paths = 0

    # As long as there are valid paths available
    while next_cave:
        # Take the next path
        current_path = next_cave.pop(0)

        # If the cave coming after the current one
        for follow_up in connections[current_path[-1]]:
            # If next cave is an end cave increment the path counter
            if follow_up == 'end':
                valid_paths += 1
            # Else append it to the list of coming caves
            # Only when it is a capital cave or has not been visited yet
            elif not follow_up.islower() or follow_up not in current_path:
                next_cave.append(current_path + [follow_up])

    return valid_paths


print('Solution for first test task 01: ', count_paths('resources/test_1'))
print('Solution for second test task 01: ', count_paths('resources/test_2'))
print('Solution for validation task 01: ', count_paths('resources/val'))
