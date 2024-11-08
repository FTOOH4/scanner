import re


class Token:
    def __init__(self, category, content):
        # Type of the token (e.g., keyword, number, or operator)
        self.category = category
        # Actual value of the token
        self.content = content


class Scanner:
    def __init__(self, text):
        # Input text to be analyzed
        self.text = text
        # Current character to be analyzed
        self.current = text[0]
        # Position of the current character
        self.index = 0

    def move_next(self):
        # Move to the next character in the input text
        self.index += 1
        if self.index < len(self.text):
            self.current = self.text[self.index]
        else:
            self.current = None  # End of input

    def is_space(self, char):
        # Check if the character is a whitespace
        return re.match(r'\s', char)

    def is_alpha(self, char):
        # Check if the character is a letter (A-Z, a-z)
        return re.match(r'[a-zA-Z]', char)

    def is_numeric(self, char):
        # Check if the character is a digit (0-9)
        return re.match(r'\d', char)

    def is_operator_symbol(self, char):
        # Check if the character is an operator symbol
        return char in ['+', '-', '=', '<', '>', '==', '!=', '<=', '>=']

    def fetch_token(self):
        # Main function to identify and return the next token
        while self.current is not None:
            if self.is_space(self.current):
                # Skip whitespace characters
                self.move_next()
                continue

            elif self.is_alpha(self.current):
                # Handle keywords and identifiers
                keyword_list = [
                    'False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
                    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'False', 'finally',
                    'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'None',
                    'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield'
                ]
                text_fragment = ''
                while self.is_alpha(self.current) or self.is_numeric(self.current):
                    text_fragment += self.current
                    self.move_next()

                if text_fragment in keyword_list:
                    return Token('KEYWORD', text_fragment)  # Return as keyword
                else:
                    return Token('IDENTIFIER', text_fragment)  # Return as identifier

            elif self.is_numeric(self.current):
                # Handle numbers
                number_value = ''
                while self.is_numeric(self.current):
                    number_value += self.current
                    self.move_next()
                return Token('NUMBER', number_value)  # Return as number

            elif self.is_operator_symbol(self.current):
                # Handle operators
                operator = ''
                while self.is_operator_symbol(self.current):
                    operator += self.current
                    self.move_next()
                return Token('OPERATOR', operator)  # Return as operator

            else:
                # Handle special characters
                unique_char = self.current
                self.move_next()
                return Token('SPECIAL_CHAR', unique_char)  # Return as special character

        return Token('EOF', None)  # End of input


# Run the scanner on input
code_input = input('Please enter a statement:\n')
lexer = Scanner(code_input)
print('*' * 50)

token_names, token_types = [], []
current_token = lexer.fetch_token()
while current_token.category != 'EOF':
    token_names.append(current_token.content)
    token_types.append(current_token.category)
    print(f'<Token Type: {current_token.category}, Value: {current_token.content}>')
    current_token = lexer.fetch_token()

print('*' * 50)
print(token_names, '\n', token_types)
print('*' * 50)
