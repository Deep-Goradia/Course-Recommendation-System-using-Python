import re

def clean_text(text):
    """Lowercase and remove special characters from text"""
    if not isinstance(text, str):
        return ""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text
