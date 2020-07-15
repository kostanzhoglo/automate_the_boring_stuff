def create_phrase(list):
    phrase = ''
    list_length = len(list)
    for i in range(len(list)):
        if i < list_length-2:
            phrase += list[i] + ', '
        elif i < list_length-1:
            phrase += list[i] + ', and '
        else:
            phrase += list[i]

    print(phrase)
    return phrase

example = ['apples', 'bananas', 'tofu', 'cats']
marvel = ["Captain America", "Spiderman", "Thor", "Iron Man", "Black Widow", "Mockingbird"]
create_phrase(example)
create_phrase(marvel)