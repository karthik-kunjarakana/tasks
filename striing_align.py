def left_align(words, width):
    """
    Aligns words to the left within the specified width.

    Parameters:
    words (list): List of words to be aligned.
    width (int): The width for the alignment.

    Returns:
    list: List of aligned lines.
    """
    # Initialize an empty list to store the lines and the current line being built
    # 'lines' will hold the final aligned text, while 'current_line' accumulates words until they fit the width
    lines = []
    current_line = []
    current_length = 0

    # Iterate over each word in the list of words
    # This loop processes each word to determine how it fits into the current line
    for word in words:
        # Check if adding the current word would exceed the width
        # If it would, we need to handle it appropriately
        if current_length + len(word) + len(current_line) > width:
            # Handle numbers by pushing them to a new line
            # Numbers are treated as atomic units and are not split
            if word.isdigit():
                if current_line:
                    # Join the current line and add to the lines list
                    lines.append(' '.join(current_line))
                # Start a new line with the current word
                current_line = [word]
                current_length = len(word)
            else:
                # Handle overflow for non-numbers
                while current_length + len(word) + len(current_line) > width:
                    # Calculate space left in the current line
                    space_left = width - current_length - len(current_line)
                    if space_left > 0:
                        # Split the word to fit the remaining space and add a hyphen
                        current_line.append(word[:space_left] + '-')
                        word = word[space_left:]
                    # Join the current line and add to the lines list
                    lines.append(' '.join(current_line))
                    # Reset the current line and length
                    current_line = []
                    current_length = 0
                # Add the remaining part of the word to the new line
                current_line.append(word)
                current_length += len(word)
        else:
            # If the word fits, add it to the current line
            current_line.append(word)
            current_length += len(word)

    # Add the last line if there's any content left
    if current_line:
        lines.append(' '.join(current_line))

    return lines

# Function to right align words within the specified width
def right_align(words, width):
    # Call the left_align function to get the lines
    lines = left_align(words, width)
    # Right align each line using the rjust method
    return [line.rjust(width) for line in lines]
# Function to center align words within the specified width
def center_align(words, width):
    # Call the left_align function to get the lines
    lines = left_align(words, width)
    # Center align each line using the center method
    return [line.center(width) for line in lines]
 
def justify_align(words, width):
    """
    Aligns words to justify within the specified width.

    Parameters:
    words (list): List of words to be aligned.
    width (int): The width for the alignment.

    Returns:
    list: List of aligned lines.
    """
    # Initialize an empty list to store the lines and the current line being built
    # 'lines' will hold the final aligned text, while 'current_line' accumulates words until they fit the width
    lines = []
    current_line = []
    current_length = 0

    # Iterate over each word in the list of words
    # This loop processes each word to determine how it fits into the current line
    for word in words:
        # Check if adding the current word would exceed the width
        # If it would, we need to handle it appropriately
        if current_length + len(word) + len(current_line) > width:
            # Handle numbers by pushing them to a new line
            # Numbers are treated as atomic units and are not split
            if word.isdigit():
                if current_line:
                    # Join the current line and add to the lines list
                    lines.append(' '.join(current_line))
                # Start a new line with the current word
                current_line = [word]
                current_length = len(word)
            else:
                # Handle overflow for non-numbers
                while current_length + len(word) + len(current_line) > width:
                    # Calculate space left in the current line
                    space_left = width - current_length - len(current_line)
                    if space_left > 0:
                        # Split the word to fit the remaining space and add a hyphen
                        current_line.append(word[:space_left] + '-')
                        word = word[space_left:]
                    # Join the current line and add to the lines list
                    lines.append(' '.join(current_line))
                    # Reset the current line and length
                    current_line = []
                    current_length = 0
                # Add the remaining part of the word to the new line
                current_line.append(word)
                current_length += len(word)
        else:
            # If the word fits, add it to the current line
            current_line.append(word)
            current_length += len(word)

    # Add the last line if there's any content left
    if current_line:
        lines.append(' '.join(current_line))

    return lines
def align_text(text, width, alignment):
    """
    Aligns the input text based on the specified width and alignment type.

    Parameters:
    text (str): The input text to be aligned.
    width (int): The width for the alignment.
    alignment (str): The type of alignment ('left', 'right', 'center', 'justify').

    Returns:
    str: The aligned text as a single string.
    """
    # Split the input text into individual lines
    # This ensures we handle multiline text correctly
    lines = text.split('\n')
    
    # Initialize an empty list to store the aligned lines
    # This will contain the final output after processing each line
    aligned_lines = []

    # Process each line individually
    # This loop handles each line separately to ensure proper alignment
    for line in lines:
        # Split each line into words
        # This allows us to manage word wrapping and alignment
        words = line.split()

        # Check the specified alignment type and call the corresponding function
        # We delegate the actual alignment to specialized functions for clarity
        if alignment == 'left':
            aligned_lines.extend(left_align(words, width))
        elif alignment == 'right':
            aligned_lines.extend(right_align(words, width))
        elif alignment == 'center':
            aligned_lines.extend(center_align(words, width))
        elif alignment == 'justify':
            aligned_lines.extend(justify_align(words, width))
        else:
            # Raise an error if an invalid alignment type is provided
            raise ValueError("Invalid alignment type")
    
    # Join the aligned lines into a single string and return
    # This combines the processed lines into the final output
    return '\n'.join(aligned_lines)

# Read multiline input from the user
print("Enter the text (end with an empty line):")
user_input = []
while True:
    line = input()
    if line == "":
        break
    user_input.append(line)

text = "\n".join(user_input)
width = int(input("Enter the width: "))
alignment = input("Enter the alignment (left, right, center, justify): ")

print(f"\n{alignment.capitalize()} Aligned:")
print(align_text(text, width, alignment))