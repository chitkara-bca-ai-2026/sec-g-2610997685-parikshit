print("=" * 42)
print("          STRING UTILITY ANALYZER")
print("=" * 42)

# Accept a sentence from the user
text = input("Enter a line of text: ")

print("\n--- Analysis Output ---")

# Character indexing
idx = int(input("Enter index to check character: "))

if 0 <= idx < len(text):
    print("Character at index", idx, "   :",
          repr(text[idx]))
else:
    print("Invalid index!")

# String slicing
begin = int(input("Enter starting index for slice: "))
stop = int(input("Enter ending index for slice: "))

if 0 <= begin <= len(text) and 0 <= stop <= len(text):
    print(f"Sliced text [{begin}:{stop}]   :",
          repr(text[begin:stop]))
else:
    print("Invalid slice indices!")

# Convert to uppercase
print("Uppercase             :", text.upper())

# Convert to lowercase
print("Lowercase             :", text.lower())

# Replace a word
target = input("Enter word to find: ")
substitute = input("Enter new word: ")

updated_text = text.replace(target, substitute)

print("After replacement     :", updated_text)

# Find length
print("Total length          :", len(text))

print("\n" + "=" * 42)
print("Processing Finished!")
print("=" * 42)
