def text_indentation(text):
    """
    Prints text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Define the characters to split the text
    split_chars = ['.', '?', ':']

    # Split the text based on the defined characters
    lines = []
    line = ''
    for char in text:
        line += char
        if char in split_chars:
            lines.append(line.strip())
            lines.append('')  # Add two new lines
            line = ''
    # Add the last line if it's not empty
    if line:
        lines.append(line.strip())

    # Print the processed text
    print('\n'.join(lines))

