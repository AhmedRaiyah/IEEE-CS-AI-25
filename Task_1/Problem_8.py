
word = input()

if word[::-1] == word: 
    print(f"\"{word}\" is a palindrome")
else:
    print(f"\"{word}\" is NOT a palindrome")