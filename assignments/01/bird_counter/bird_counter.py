"""Bird Counter Program"""

import pickle

def load_birds_count(file: str) -> dict:
    """Unpickle the given file and return a dictionary."""
    try:
        with open(file, 'rb') as birds_count_file:
            return pickle.load(birds_count_file)
    except (FileNotFoundError, PermissionError) as e:
        return {}

def dump_birds_count(birds: dict, file: str) -> None:
    """Pickle the given birds dict to the given file."""
    with open(file, 'wb') as birds_count_file:
        pickle.dump(birds, birds_count_file)

def _find_longest_key_length(dictionary: dict) -> int:
    """Returns the longest string length of a key in the given dictionary."""
    length: int = 0
    for key in dictionary.keys():
        if len(key) > length: length = len(str(key))
    return length

def _add_padding(data: str, width: int, padding_char: str = ' ') -> str:
    """Return data with added padding for tabulation using given width."""
    return data + padding_char*(width - len(data))

def display_results_table(birds_count_dict: dict, longest_length: int, name_header: str = 'Name', count_header: str = 'Count') -> None:
    """Display the results of the bird counting to the user."""
    print()
    if len(name_header) > longest_length or len(count_header) > longest_length:
        longest_length = len(name_header) if len(name_header) > len(count_header) else len(count_header) 
    print(_add_padding(name_header, longest_length), _add_padding(count_header, longest_length))
    print('='*longest_length, '='*longest_length)
    birds: list = list(birds_count_dict.keys())
    birds.sort()
    for bird in birds:
        print(_add_padding(bird.title(), longest_length), birds_count_dict[bird])

def bird_counter_splash() -> None:
    """The start or splash of bird counter."""
    print('Bird Counter Program\n')
    print('Enter \'x\' to exit\n')

def bird_counter_loop(birds: dict, save_file: str) -> None:
    """Primary loop of bird counter."""
    bird: str = ''
    while bird != 'x':
        bird: str = input('Enter name of bird: ').lower()
        if bird == 'x':
            continue
        # If a new bird
        if bird not in birds.keys():
            birds[bird] = 1
        else:
            birds[bird] += 1
        dump_birds_count(birds, save_file)
    length = _find_longest_key_length(birds)
    display_results_table(birds, length)

def main() -> None:
    """Bird counter main control function."""
    bird_counter_splash()
    birds = load_birds_count(BIRD_FILE)
    bird_counter_loop(birds, BIRD_FILE)
    
if __name__ == '__main__':
    BIRD_FILE = 'birds.pickle'
    main()