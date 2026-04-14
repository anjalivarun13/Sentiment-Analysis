# preprocessing_file.py

import re

# Remove HTML tags
def remove_html(text):
    pattern = re.compile("<.*?>")
    return pattern.sub("", str(text))

# Convert to lowercase
def to_lower(text):
    return str(text).lower()

# Final pipeline function (BEST PRACTICE)
def preprocess_text(text):
    text = remove_html(text)
    text = to_lower(text)
    return text
    

