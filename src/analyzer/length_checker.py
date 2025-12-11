"""
Length Checker Module
---------------------
This module evaluates the strength of a password based on its length.
It returns a normalized score between 0 and 1, where 1 indicates
an ideal password length according to best practices.
"""

MIN_LENGTH = 8       # below this is very weak
IDEAL_LENGTH = 12    # above this is very strong

def check_length(password: str) -> float:
    """
    Check password length and return a normalized score.
    
    Parameters:
        password (str): The password to evaluate.
    
    Returns:
        float: Score between 0 (very weak) and 1 (strong).

    """

    length = len(password)

    if length < MIN_LENGTH:
        return 0.0
    elif length >= IDEAL_LENGTH:
        return 1.0
    else:
        return (length - MIN_LENGTH) / (IDEAL_LENGTH - MIN_LENGTH) # Linear interpolation between MIN_LENGTH and IDEAL_LENGTH

def evaluate(passwords: list) -> dict:
    """
    Evaluate a list of passwords and return a dictionary
    mapping passwords to their length scores.

    Parameters:
        passwords (list): List of passwords to evaluate.
    
    Returns:
        dict: {password: length_score}

    """
    scores = {}
    for pwd in passwords:
        scores[pwd] = check_length(pwd)
    return scores