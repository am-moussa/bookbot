def word_count(string_input):
    return len(string_input.split())


def char_count(string_input):
    char_dict = {}
    for char in string_input:
        if char.lower() not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    return char_dict

def sort_on(items):
    return items["num"]

def char_count_sorted(char_count_dict):
    modified_char_count = []
    for i in char_count_dict:
        modified_char_count.append({
            "char":i, "num":char_count_dict[i]
        })
        
    modified_char_count.sort(reverse=True, key=sort_on)
    
    return modified_char_count
