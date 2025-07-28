import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "school", "department", "institute"]
    return not any(word.lower() in affiliation.lower() for word in academic_keywords)

def extract_email(text: str) -> str:
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None
