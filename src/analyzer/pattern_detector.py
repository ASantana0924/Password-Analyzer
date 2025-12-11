import json
import re
from pathlib import Path

PATTERNS_FILE = Path(__file__).parent.parent.parent / "data" / "common_patterns.json"
with open(PATTERNS_FILE, "r") as f:
    PATTERNS = json.load(f)

# Define weights for each pattern (how much they reduce password strength)
PATTERN_WEIGHTS = {
    "sequential_numbers": 1.0,
    "sequential_letters": 1.0,
    "keyboard_pattern": 0.8,
    "repeated_chars": 0.5,
    "repeated_substring": 0.5,
    "date_numeric": 0.7,
    "date_alphanumeric": 0.7
}

def detect_patterns(password):
    """Detect weak patterns in a password and calculate a pattern score."""
    detected = []
    score = 0.0

    # Numeric sequences
    for seq in PATTERNS.get("sequences_numeric", []):
        for i in range(len(seq) - 2):
            if seq[i:i+3] in password or seq[i:i+3][::-1] in password:
                detected.append("sequential_numbers")
                score += PATTERN_WEIGHTS["sequential_numbers"]
                break
        if "sequential_numbers" in detected:
            break

    # Alphabetic sequences
    for seq in PATTERNS.get("sequences_alpha", []):
        for i in range(len(seq) - 2):
            sub = seq[i:i+3]
            if sub.lower() in password.lower() or sub[::-1].lower() in password.lower():
                detected.append("sequential_letters")
                score += PATTERN_WEIGHTS["sequential_letters"]
                break
        if "sequential_letters" in detected:
            break

    # Keyboard patterns
    for seq in PATTERNS.get("keyboard_patterns", []):
        if seq.lower() in password.lower():
            detected.append("keyboard_pattern")
            score += PATTERN_WEIGHTS["keyboard_pattern"]
            break

    # Repeated characters
    for pattern in PATTERNS.get("repeated_chars", []):
        if re.search(pattern, password):
            detected.append("repeated_chars")
            score += PATTERN_WEIGHTS["repeated_chars"]
            break

    # Repeated substrings
    for pattern in PATTERNS.get("repeated_substrings", []):
        if re.search(pattern, password):
            detected.append("repeated_substring")
            score += PATTERN_WEIGHTS["repeated_substring"]
            break

    # Dates numeric
    for pattern in PATTERNS.get("dates_numeric", []):
        if re.search(pattern, password):
            detected.append("date_numeric")
            score += PATTERN_WEIGHTS["date_numeric"]
            break

    # Dates alphanumeric
    for pattern in PATTERNS.get("dates_alphanumeric", []):
        if re.search(pattern, password, re.IGNORECASE):
            detected.append("date_alphanumeric")
            score += PATTERN_WEIGHTS["date_alphanumeric"]
            break

    return {"patterns": detected, "pattern_score": score}


def evaluate(passwords):
    """Evaluate a list of passwords for patterns and return pattern scores."""
    results = []
    for pw in passwords:
        result = detect_patterns(pw)
        results.append({
            "password": pw,
            "patterns": result["patterns"],
            "pattern_score": result["pattern_score"]
        })
    return results