def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    num_words = file_contents.split().__len__()
    return num_words

def get_letter_counts(filepath):
    characters = {}
    with open(filepath) as f:
        file_contents = f.read().lower()
    for l in file_contents:
        if l in characters:
            characters[l] += 1
        else:
            characters[l] = 1
    return characters

def get_sorted_report(characters:dict):
    list_from_dict = list(characters.items())
    sorted_list = sorted(list_from_dict, key=lambda tup: tup[1], reverse=True)
    for i in range(sorted_list.__len__()):
        print(f"{sorted_list[i][0]}: {sorted_list[i][1]}")