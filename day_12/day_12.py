from collections import defaultdict


def count_paths_small_once(source_path: str) -> int:
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


def count_paths_one_small_double(source_path: str) -> int:
    """
    Counts the different possible paths through a cave system.
    Each valid path has to contain a start and an end point.
    A path may contain multiple entries of the came capital cave and up to two instances
    per minor cave.

    :param source_path: File path to the routing info of a cave system.
    :returns: The sum of counted valid paths. Each path increments the sum by 1.
    """
    # Create dictionary and fill with cave connections
    connections = defaultdict(list)
    for line in open(source_path, 'r'):
        entry, destination = line.strip().split('-')
        connections[entry].append(destination)
        connections[destination].append(entry)

    valid_paths = 0
    _next = [['start']]
    # As long as paths are available
    while _next:
        # Take the next path as current
        current_path = _next.pop(0)

        # For each cave in the current path
        for coming in connections[current_path[-1]]:
            # Mark the cave as multi occurance of minor cave
            revisit = coming.islower() and coming in current_path

            if coming == 'end':
                valid_paths += 1
            # If the path is not the starting cave and it is not a multi revisit of a minor cave
            elif coming != 'start' and not (current_path[0] == '*' and revisit):
                # Add it to the following caves of the current path
                _next.append((['*'] if revisit else []) + current_path + [coming])

    return valid_paths


# Output for task 01
print('Solution for first test task 01: ', count_paths_small_once('resources/test_1'))
print('Solution for second test task 01: ', count_paths_small_once('resources/test_2'))
print('Solution for validation task 01: ', count_paths_small_once('resources/val'))

print('-------------------------------')

# Output for task 02
print('Solution for first test task 02: ', count_paths_one_small_double('resources/test_3'))
print('Solution for second test task 02: ', count_paths_one_small_double('resources/test_2'))
print('Solution for validation task 02: ', count_paths_one_small_double('resources/val'))
