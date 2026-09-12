def remove_fourth_character(word: str) -> str:
    first_part = word[:3]
    second_part = word[4:]
    new_word = first_part + second_part
    return new_word

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
