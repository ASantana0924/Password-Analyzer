import os
from src.utils import normalization

ROCKYOU_FILE = os.path.join(os.path.dirname(__file__), "../../data/blocklists/rockyou_sample.txt")
TOP_10K_FILE = os.path.join(os.path.dirname(__file__), "../../data/blocklists/top_10k_passwords.txt")

rockyou_set = set()
top1k_set = set()

def load_frequency_lists():
    """Load password frequency lists into memory."""
    global rockyou_set, top1k_set

    if not rockyou_set:
        with open(ROCKYOU_FILE, "r", encoding="utf-8", errors="ignore") as f:
            rockyou_set = set(line.strip().lower() for line in f if line.strip())

    if not top1k_set:
        with open(TOP_10K_FILE, "r", encoding="utf-8", errors="ignore") as f:
            top1k_set = set(line.strip().lower() for line in f if line.strip())

def check_frequency(password: str) -> dict:
    """
    Check if the password exists in common password lists.
    Returns a dictionary with score and which list matched.
    """
    load_frequency_lists()
    normalized_pw = normalization.normalize(password)

    if normalized_pw in top1k_set:
        return {
            "password": password,
            "frequency_score": 1.0,
            "matched_list": "top_1k"
        }
    elif normalized_pw in rockyou_set:
        return {
            "password": password,
            "frequency_score": 0.8,
            "matched_list": "rockyou"
        }
    else:
        return {
            "password": password,
            "frequency_score": 0.0,
            "matched_list": None
        }

def evaluate(passwords: list) -> list:
    """
    Evaluate a list of passwords against the frequency lists.
    Returns a list of dictionaries for each password.
    """
    results = []
    for pw in passwords:
        results.append(check_frequency(pw))
    return results