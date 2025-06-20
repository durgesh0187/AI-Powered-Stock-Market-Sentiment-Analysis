import re

def clean_text(text):
    """
    Cleans tweet text by removing URLs, mentions, hashtags, emojis, and extra symbols.

    Args:
        text (str): Raw tweet text

    Returns:
        str: Cleaned lowercase text
    """
    text = re.sub(r"http\S+", "", text)          # Remove URLs
    text = re.sub(r"@\w+", "", text)             # Remove mentions
    text = re.sub(r"#", "", text)                # Remove hashtag symbols but keep the words
    text = re.sub(r"[^A-Za-z\s]", "", text)      # Remove non-alphabetic characters (emojis, symbols)
    return text.lower().strip()                  # Convert to lowercase and remove extra spaces
