"""
Entropy Calculator Module
-------------------------
This module evaluates the strength of a password based on its Shannon entropy.
It returns a normalized score between 0 (weak) and 1 (strong).
Higher entropy indicates a more unpredictable password.
"""

import math
from collections import Counter

# Entropy thresholds
MIN_ENTROPY = 20      # less than = weak
IDEAL_ENTROPY = 60    # greater than = strong

def calculate_entropy(password: str) -> float:
    """
    Calculate Shannon entropy of a password.

    Parameters:
        password (str): The password to evaluate.

    Returns:
        float: Shannon entropy of the password.
    """
    if not password:
        return 0.0

    length = len(password)
    counts = Counter(password)
    entropy = 0.0

    for count in counts.values():
        p = count / length
        entropy -= p * math.log2(p)

    return entropy * length # Scale by length to reflect more randomness in longer passwords

def normalize_entropy(entropy: float) -> float:
    """
    Normalize entropy score to a value between 0 and 1 based on thresholds.

    Parameters:
        entropy (float): Shannon entropy of a password.

    Returns:
        float: Normalized score (0 = weak, 1 = strong)
    """
    if entropy <= MIN_ENTROPY:
        return 0.0
    elif entropy >= IDEAL_ENTROPY:
        return 1.0
    else:
        return (entropy - MIN_ENTROPY) / (IDEAL_ENTROPY - MIN_ENTROPY) # Linear interpolation between MIN_ENTROPY and IDEAL_ENTROPY

def check_entropy(password: str) -> float:
    """
    Compute normalized entropy score for a single password.
    
    Parameters:
        password (str): Password to evaluate.
    
    Returns:
        float: Normalized entropy score (0-1)
    """
    entropy = calculate_entropy(password)
    return normalize_entropy(entropy)

def evaluate(passwords: list) -> dict:
    """
    Evaluate a list of passwords and return a dictionary mapping
    passwords to their normalized entropy scores.

    Parameters:
        passwords (list): List of passwords to evaluate.

    Returns:
        dict: {password: entropy_score}
    """
    scores = {}
    for pwd in passwords:
        scores[pwd] = check_entropy(pwd)
    return scores