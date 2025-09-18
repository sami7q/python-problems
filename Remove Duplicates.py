def remove_duplicates(numbers):
    unique_num = set()

    for number in numbers:
        if number not in unique_num:
            unique_num.add(number)
    return sorted(unique_num)
