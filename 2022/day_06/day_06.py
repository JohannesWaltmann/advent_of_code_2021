
test_path = '../resources/test/06.txt'
validation_path = '../resources/validation/06.txt'

def import_data(file_path: object) -> list[str]:
    return [content.strip() for content in open(file_path, 'r').readlines()]


def has_repeated_characters(sequence) -> bool:
    return len(set(sequence)) != len(sequence)


def task(file_path, stream_length: int) -> list[int]:
    signal_streams = import_data(file_path)
    start_of_packet_markers = []

    for stream in signal_streams:
        # Get the first three characters of the signal
        initial_three = stream[:stream_length]
        additional_counter = 1

        for character in range(stream_length, len(stream)):

            if not has_repeated_characters(initial_three) and not initial_three.__contains__(stream[character]):
                start_of_packet_markers.append(character + 1)
                break
            elif initial_three.__contains__(stream[character]) or has_repeated_characters(initial_three):
                initial_three = stream[additional_counter:stream_length + additional_counter]
                additional_counter += 1

    return start_of_packet_markers


# Print Solutions:
print(f'Task 01 testing: {task(test_path, 3)}')
print(f'Task 01 validation: {task(validation_path, 3)}')
print('---')
print(f'Task 02 testing: {task(test_path, 13)}')
print(f'Task 02 validation: {task(validation_path, 13)}')
