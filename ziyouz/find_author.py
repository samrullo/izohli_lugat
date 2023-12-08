import re

def extract_author_and_title(filename):
    # Add a space before a capital letter followed by a lowercase letter
    spaced_filename = re.sub(r'([a-z])([A-Z])', r'\1 \2', filename)

    # Replace underscore with an apostrophe if it's surrounded by letters
    cleaned_filename = re.sub(r'(?<=[a-zA-Z])_(?=[a-zA-Z])', "'", spaced_filename)

    # Split the cleaned filename into words
    words = cleaned_filename.split()

    # Find the index of the first capital letter followed by a lowercase letter or space
    split_index = None
    for i, word in enumerate(words[1:], start=1):
        if re.match(r'[A-Z][a-z]', word) or " " in word:
            split_index = i
            break

    if split_index is None:
        return None, None

    author_name = " ".join(words[:split_index])
    book_title = " ".join(words[split_index:])

    return author_name, book_title

# Replace 'filenames' with your list of filenames
filenames = ["abbos_said_qariya_qissalar_hikoyalar", "g_afur_g_ulom_mukammal_asarlar_to_plami_5_jild_1986_start_100"]
for filename in filenames:
    author, title = extract_author_and_title(filename)
    print(f"Author: {author}\nTitle: {title}\n")
