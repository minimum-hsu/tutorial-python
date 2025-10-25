#!/usr/bin/env python3

def format_text(text: str) -> str:
    """
    Format the input text by trimming whitespace and converting to lowercase.

    Args:
        text (str): The input text to format.

    Returns:
        str: The formatted text.
    """

    def trim(s: str) -> str:
        """
        The inner function to trim whitespace from both ends of the string.
        """

        return s.strip()

    def to_lower(s: str) -> str:
        """
        The inner function to convert the string to lowercase.
        """

        return s.lower()

    return to_lower(trim(text))

if __name__ == '__main__':
    sample = "   Hello World!   "
    formatted = format_text(sample)
    print(f"Original: '{sample}'")
    print(f"Formatted: '{formatted}'")
