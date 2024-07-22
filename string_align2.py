def left_align(words, width):
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            if word.isdigit():
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
            else:
                while current_length + len(word) + len(current_line) > width:
                    space_left = width - current_length - len(current_line)
                    if space_left > 0:
                        current_line.append(word[:space_left] + '-')
                        word = word[space_left:]
                    lines.append(' '.join(current_line))
                    current_line = []
                    current_length = 0
                current_line.append(word)
                current_length += len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def right_align(words, width):
    lines = left_align(words, width)
    right_aligned_lines = []

    for line in lines:
        space_to_add = width - len(line)
        right_aligned_line = ' ' * space_to_add + line
        right_aligned_lines.append(right_aligned_line)

    return right_aligned_lines

def center_align(words, width):
    lines = left_align(words, width)
    centered_lines = []

    for line in lines:
        total_padding = width - len(line)
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
        centered_line = ' ' * left_padding + line + ' ' * right_padding
        centered_lines.append(centered_line)

    return centered_lines

def justify_align(words, width):
    lines = left_align(words, width)
    justified_lines = []

    for line in lines[:-1]:
        words_in_line = line.split()
        if len(words_in_line) == 1:
            justified_lines.append(words_in_line[0])
            continue

        total_spaces_needed = width - len(''.join(words_in_line))
        spaces_between_words = total_spaces_needed // (len(words_in_line) - 1)
        extra_spaces = total_spaces_needed % (len(words_in_line) - 1)

        justified_line = ''
        for i in range(len(words_in_line) - 1):
            justified_line += words_in_line[i] + ' ' * (spaces_between_words + (1 if i < extra_spaces else 0))
        justified_line += words_in_line[-1]
        justified_lines.append(justified_line)

    justified_lines.append(lines[-1])  # The last line should be left-aligned
    return justified_lines

def align_text(text, width, alignment):
    lines = text.split('\n')
    aligned_lines = []

    for line in lines:
        words = line.split()
        if alignment == 'left':
            aligned_lines.extend(left_align(words, width))
        elif alignment == 'right':
            aligned_lines.extend(right_align(words, width))
        elif alignment == 'center':
            aligned_lines.extend(center_align(words, width))
        elif alignment == 'justify':
            aligned_lines.extend(justify_align(words, width))
        else:
            raise ValueError("Invalid alignment type")

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
