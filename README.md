# Wordle Clone  

This script lets you play a Wordle-style game using random words from a `words.txt` file.  

## Requirements  
- **ANSI Escape Character Support**  
  The program uses ANSI escape codes for colored output. Most modern terminals (Linux, macOS, Windows Terminal, etc.) support this by default.  

  - If your console **does not** support ANSI escape codes and you still want to run the program, simply open the script and change the variable:  
    ```python
    ansi = True  # change this to False
    ```  
    (This is on **line 4** of the script.)  

## How It Works  
- A random word is chosen from `words.txt`.  
- You try to guess the word using Wordle-style rules until you solve it.  

## Running the Program  
```bash
python wordle.py
