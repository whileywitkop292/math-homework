def is_palindrome(word):
    """
    Check if a word is a palindrome.
    
    A palindrome reads the same backward as forward. For example, 'madam' and 'radar'.
    """
    return word == word[::-1]

# Example usage:
word = "madam"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
