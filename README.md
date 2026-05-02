# Bhasha-Script

**Bhasha-Script** is a custom LALR compiler and Integrated Development Environment (IDE) designed to let users write programs using Bengali keywords and native Bengali digits. This project was developed as part of the **CSE 430 (Compiler Design)** coursework.

## Key Features

*   **Native Keyword Support**: Use natural language keywords like `dhoro` (variable), `dekhao` (print), `jodi` (if), `tahole` (then), and `nahole` (else).
*   **Unicode Integration**: Full support for Bengali digits (`০-৯`) which are automatically mapped to integers for calculation.
*   **LALR Parsing**: Built using the Python Lex-Yacc (PLY) library to handle complex grammar and operator precedence.
*   **Smart Highlighting**: The built-in editor features real-time syntax highlighting for keywords to improve code readability.
*   **Localized Error Handling**: Provides user-friendly feedback in Bangla (e.g., "Syntax bhul hoyeche!") when errors occur.

## Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/bhasha-script.git
   cd bhasha-script
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Editor**:
   ```bash
   python amar_editor.py
   ```

## Usage Example

Type the following code into the **Amar Bangla Editor** to see the logic in action:
```text
dhoro x = ১০
dhoro y = ৫
jodi x > y tahole dekhao ১০০ nahole dekhao ০
```

*Expected Output in Console:* `> 100`

## Project Structure

*   **`bangla_compiler.py`**: The core compiler logic containing the Lexer and Parser definitions.
*   **`amar_editor.py`**: The Tkinter-based GUI providing a user-friendly coding interface.
*   **`requirements.txt`**: Contains the dependency list (PLY).

## Academic Context
This project demonstrates the full front-end pipeline of a compiler:
1. **Lexical Analysis**: Converting Unicode strings into distinct tokens.
2. **Syntax Analysis**: Using Context-Free Grammar (CFG) to validate statement structures.
3. **Semantic Analysis**: Managing a symbol table for variable storage and retrieval during execution.
