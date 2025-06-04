def calculate_love_score(name1, name2):
    # Combine both names into one string (lowercase for uniformity)
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of the letters in "TRUE"
    true_count = sum(combined_names.count(char) for char in "true")

    # Count occurrences of the letters in "LOVE"
    love_count = sum(combined_names.count(char) for char in "love")

    # Combine the counts into a two-digit number
    love_score = int(str(true_count) + str(love_count))

    return love_score

# Example usage
print(calculate_love_score("Kanye West", "Kim Kardashian"))  # Output: 42
