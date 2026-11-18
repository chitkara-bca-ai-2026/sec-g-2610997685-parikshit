line = input("Enter a line of text: ")

# Count different characters
char_total = len(line)
word_count = len(line.split())

vowel_count = 0
consonant_count = 0
digit_count = 0
space_count = 0
symbol_count = 0

for ch in line:
    if ch.lower() in "aeiou":
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch == " ":
        space_count += 1
    else:
        symbol_count += 1

# Summary
letter_total = vowel_count + consonant_count

if letter_total > 0:
    vowel_ratio = (vowel_count / letter_total) * 100
else:
    vowel_ratio = 0

# Display report
print("\n" + "=" * 48)
print("          TEXT METRICS SUMMARY")
print("=" * 48)

print("Text:", line)
print("Total characters:", char_total)

print("\n--- Character Details ---")
print("Words:", word_count)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Digits:", digit_count)
print("Spaces:", space_count)
print("Special characters:", symbol_count)

print("\n--- Overview ---")
print("Total letters:", letter_total)
print(f"Vowel percentage: {vowel_ratio:.2f}%")

print("\n" + "=" * 48)
print("Report Finished!")
print("=" * 48)
