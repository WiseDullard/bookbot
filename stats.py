def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    counts = {}
    for c in text:
        c = c.lower()
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
    return counts

def sort_on(dict):
    return dict["num"]

def sort_list(characters):
    sorted_list = []
    for ch in characters:
        count = characters[ch]
        sorted_list.append({"char":ch, "num":count})
        sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list