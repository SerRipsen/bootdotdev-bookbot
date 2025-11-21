def count_words(text):
    return len(text.split())

def count_characters(text):
    character_count = {}
    
    # select each character
    for i in range(0,len(text)):
        char = text[i].lower()
        
        if char not in character_count:
            character_count[char] = 0
        character_count[char] += 1

    return character_count

def sort_on(items):
    return items["count"]

def create_report(dict_of_characters):
    list_of_dicts = []

    for character in dict_of_characters:
        count = dict_of_characters[character]
        working_dict = {"char": character, "count": count}

        list_of_dicts.append(working_dict)
    
    list_of_dicts.sort(reverse = True, key = sort_on)
    return list_of_dicts