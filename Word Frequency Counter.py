def word_frequency(text):
    
    cleaned_text = text.lower()
    for char in ".,!?":
        cleaned_text = cleaned_text.replace(char, "")

    
    words = cleaned_text.split()

    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count