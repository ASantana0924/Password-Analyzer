#!/usr/bin/env python3
"""
Password Analyzer - Command Line Demo

This script demonstrates the password analysis capabilities
by analyzing sample passwords and displaying detailed results.
"""

from src.analyzer import (
    length_checker,
    entropy_calculator,
    pattern_detector,
    frequency_checker,
    name_detector,
    score_aggregator
)

def analyze_password(password: str) -> dict:
    """
    Analyze a single password using all analyzer modules.

    Args:
        password (str): The password to analyze

    Returns:
        dict: Complete analysis results
    """
    # Run all analysis modules
    length_res = length_checker.evaluate([password])
    entropy_res = entropy_calculator.evaluate([password])
    patterns_res = pattern_detector.evaluate([password])[0]
    freq_res = frequency_checker.evaluate([password])[0]
    names_res = name_detector.NameDetector().analyze(password)

    # Convert to strength scores (0-1 scale)
    results = {
        "length": length_res[password],
        "entropy": entropy_res[password],
        "patterns": 1 - min(patterns_res["pattern_score"] / 5, 1),  # Convert penalty to strength
        "frequency": 1 - freq_res["frequency_score"],  # Convert penalty to strength
        "names": 1 - min(names_res["name_score"] / 5, 1)  # Convert penalty to strength
    }

    # Get final aggregated result
    final_result = score_aggregator.combine_results(results)

    return {
        'password': password,
        'final_score': final_result['final_score'],
        'components': final_result['components'],
        'raw_data': {
            'length': length_res[password],
            'entropy': entropy_res[password],
            'patterns': patterns_res,
            'frequency': freq_res,
            'names': names_res
        }
    }

def print_analysis(result: dict):
    """Pretty print analysis results."""
    print(f"\n{'='*60}")
    print(f"🔐 Password Analysis: '{result['password']}'")
    print(f"{'='*60}")

    # Overall score
    score_pct = result['final_score'] * 100
    strength = "🟢 Strong" if result['final_score'] >= 0.8 else "🟡 Moderate" if result['final_score'] >= 0.6 else "🔴 Weak"
    print(f"Overall Strength: {score_pct:.1f}% - {strength}")

    # Component scores
    print(f"\n📊 Component Scores:")
    for component, score in result['components'].items():
        pct = score * 100
        bar = "█" * int(pct / 10) + "░" * (10 - int(pct / 10))
        print(f"  {component.capitalize():>10}: {pct:5.1f}% [{bar}]")

    # Raw data insights
    raw = result['raw_data']
    print(f"\n🔍 Detailed Analysis:")
    print(f"  Length: {len(result['password'])} characters")
    print(f"  Entropy: {raw['entropy']:.2f} bits")
    print(f"  Pattern Score: {raw['patterns']['pattern_score']:.2f} (lower is better)")
    print(f"  Frequency Score: {raw['frequency']['frequency_score']:.2f} (lower is better)")
    print(f"  Name Matches: {raw['names']['name_score']} detected names")

    # Breach warning
    if raw['frequency']['frequency_score'] > 0.5:
        print(f"\n⚠️  SECURITY WARNING: This password appears in common password lists!")

    print(f"{'='*60}\n")

def main():
    """Main demo function."""
    print("🔐 Password Analyzer - Command Line Demo")
    print("Analyzing sample passwords...\n")

    # Test passwords of varying strength
    test_passwords = [
        "password",           # Very weak
        "123456",             # Very weak
        "qwerty123",          # Weak
        "MyPassword123",      # Moderate
        "Tr0ub4dor&3",        # Strong
        "X9$kL2mP8qR5nT1wV4yZ",  # Very strong
    ]

    for password in test_passwords:
        result = analyze_password(password)
        print_analysis(result)

    print("💡 Tip: Run 'python flask_app.py' for the full web interface!")
    print("🌐 Or visit: https://asantana0924.github.io/Password-Analyzer/ for client-side analysis")

if __name__ == "__main__":
    main()