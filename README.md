"""
This code provides functions for aligning text based on the specified width and alignment type.

Functions:
- `left_align(words, width)`: Aligns the words to the left within the specified width.
- `right_align(words, width)`: Aligns the words to the right within the specified width.
- `center_align(words, width)`: Aligns the words to the center within the specified width.
- `justify_align(words, width)`: Aligns the words using justified alignment within the specified width.
- `align_text(text, width, alignment)`: Aligns the text based on the specified width and alignment type.

Usage:
1. Call the `align_text()` function with the text, width, and alignment type as parameters to align the text.


```

The code starts here...

```python
def left_align(words, width):
    """
    Aligns the words to the left within the specified width.

    Args:
    - words (list): A list of words to be aligned.
    - width (int): The width of the alignment.

    Returns:
    - lines (list): A list of aligned lines.

    """
    # Implementation details...

def right_align(words, width):
    """
    Aligns the words to the right within the specified width.

    Args:
    - words (list): A list of words to be aligned.
    - width (int): The width of the alignment.

    Returns:
    - lines (list): A list of aligned lines.

    """
    # Implementation details...

def center_align(words, width):
    """
    Aligns the words to the center within the specified width.

    Args:
    - words (list): A list of words to be aligned.
    - width (int): The width of the alignment.

    Returns:
    - lines (list): A list of aligned lines.

    """
    # Implementation details...

def justify_align(words, width):
    """
    Aligns the words using justified alignment within the specified width.

    Args:
    - words (list): A list of words to be aligned.
    - width (int): The width of the alignment.

    Returns:
    - lines (list): A list of aligned lines.

    """
    # Implementation details...

def align_text(text, width, alignment):
    """
    Aligns the text based on the specified width and alignment type.

    Args:
    - text (str): The text to be aligned.
    - width (int): The width of the alignment.
    - alignment (str): The type of alignment (left, right, center, justify).

    Returns:
    - aligned_text (str): The aligned text.

    Raises:
    - ValueError: If an invalid alignment type is provided.

    """
Example:
```python
text = "Hi everyone, Iam Karthika Krishna K, I am a student of VCET Puttur. I hope you all are doing fine. Have a great day!!"
width = 20
alignment = "justified"
aligned_text = align_text(text, width, alignment)
print(aligned_text)
# Output:
Hi  everyone,  I  am
Karthika  Krishna  K,
I  am  a  student  of
VCET  Puttur.  I  hope
you  all  are  doing
fine.  Have  a  great
day!!

How the code works for the function - justify

- **Text**: "Hi everyone, I am Karthika Krishna K, I am a student of VCET Puttur. I hope you all are doing fine. Have a great day!!"
- **Width**: 20

We'll focus on the lines before and after adding the word "Karthika" since the line will be justified at this point:

### First Line
Words: `["Hi", "everyone,", "I", "am"]`
- `current_length` is 14 (before adding "Karthika")

#### Justifying "Hi everyone, I am"
- `total_spaces = width - current_length = 20 - 14 = 6`
- `space_between_words = total_spaces // (len(current_line) - 1) = 6 // 3 = 2`
- `extra_spaces = total_spaces % (len(current_line) - 1) = 6 % 3 = 0`
- Spaces distribution:
  - "Hi" + 2 spaces + "everyone," + 2 spaces + "I" + 2 spaces + "am"

**Justified Line:**
```
"Hi  everyone,  I  am"
```

### Second Line
Words: `["Karthika", "Krishna", "K,"]`
- `current_length` is 17 (before adding "I")

#### Justifying "Karthika Krishna K,"
- `total_spaces = width - current_length = 20 - 17 = 3`
- `space_between_words = total_spaces // (len(current_line) - 1) = 3 // 2 = 1`
- `extra_spaces = total_spaces % (len(current_line) - 1) = 3 % 2 = 1`
- Spaces distribution:
  - "Karthika" + 2 spaces + "Krishna" + 1 space + "K,"

**Justified Line:**
```
"Karthika  Krishna K,"
```

1. **First Line**:
```
"Hi  everyone,  I  am"
```
2. **Second Line**:
```
"Karthika  Krishna  K,"
```

