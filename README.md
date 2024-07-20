
# Text Alignment Simulator

This project simulates text alignment operations for a given string and width. It supports four types of alignments:
- Left
- Right
- Center
- Justify

## Features
- Overflowing characters precede with '-' and are pushed to a new line.
- Numbers are handled properly, with overflowing numbers pushed to a new line entirely.
- Supports multiple lines of input text.

## Requirements
- Python 3.x

## Usage

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/text-alignment-simulator.git
   cd text-alignment-simulator
   ```

2. Run the script:
   ```sh
   python align_text.py
   ```

3. Follow the prompts to enter the text, width, and alignment type.

## Example
### Input:
```
Enter the text (end with an empty line):
This is an example of text alignment simulation.
Overflowing words and numbers are handled appropriately.
123456789012345 should be on a new line if it overflows.
```
### Output:
```
Enter the width: 20
Enter the alignment (left, right, center, justify): justify

Justify Aligned:
This is an example-
of text alignment-
simulation.
Overflowing words-
and numbers are-
handled-
appropriately.
123456789012345-
should be on a new-
line if it overflows.
```

## Functions

### `left_align(words, width)`
Aligns the text to the left.

### `right_align(words, width)`
Aligns the text to the right.

### `center_align(words, width)`
Centers the text.

### `justify_align(words, width)`
Justifies the text.

### `align_text(text, width, alignment)`
Aligns the text based on the specified alignment.

## Time Complexity Analysis

- The time complexity for all alignment functions is O(n), where n is the total number of characters in the input text.
- Each word is processed once, and operations like string joining and slicing are linear in nature.
- Overall, the algorithm efficiently handles the text alignment within linear time.

## Trace Example

### Input Line:
```
This is an example of text alignment simulation.
```
### Process:

1. **Left Align (`width=20`):**
   - Current line: "This is an" (length 10)
   - Current line: "example of" (length 10)
   - Current line: "text alignment-" (length 14, overflows and breaks at width)
   - Current line: "simulation." (length 11)

   **Output:**
   ```
   This is an example of-
   text alignment-
   simulation.
   ```

2. **Right Align (`width=20`):**
   - Uses the left-aligned output and right-aligns each line:
   
   **Output:**
   ```
   This is an example-
              of text-
   alignment-
            simulation.
   ```

3. **Center Align (`width=20`):**
   - Uses the left-aligned output and centers each line:
   
   **Output:**
   ```
   This is an example-
       of text-
       alignment-
      simulation.
   ```

4. **Justify Align (`width=20`):**
   - Similar to left align but spreads words to fill the width where possible:
   
   **Output:**
   ```
   This is an example-
   of text alignment-
   simulation.
   ```

---

This example demonstrates how the program processes a single line of input for each alignment type. For more complex cases with multiple lines and varying content, the program's logic ensures proper alignment and handling of overflowing text.

### Contact
For any issues or feature requests, please open an issue on the GitHub repository.