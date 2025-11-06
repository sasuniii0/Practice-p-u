import re
text = "The rain in Spain stays mainly in the plain."

match = re.search("ain", text)
print(match)  # This will print a match object if found, else None
if match:
    print("Match found")
    print("Start:", match.start())
    print("End:", match.end())

    matches = re.findall("ain", text,re.IGNORECASE)
    print("All matches:", matches)

new_text = re.sub("fox","cat", text)
print("New text:", new_text)

pattern = re.compile(r"\b\w+\b") # Matches whole words
words = pattern.findall(text)
print("Words:", words)