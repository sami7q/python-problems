def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    unique_vowels = set()   
    
    for char in text:
        if char in vowels:
            count += 1
            unique_vowels.add(char)
    
    return count, unique_vowels
