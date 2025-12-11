"""
Password Analyzer Flask Application

A comprehensive password strength analysis web application built with Flask.
Provides both web interface and REST API for password analysis.
"""

from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os
from src.analyzer import (
    length_checker,
    entropy_calculator,
    pattern_detector,
    frequency_checker,
    name_detector,
    score_aggregator
)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    """
    Render the main password analyzer web interface.
    """
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
    REST API endpoint for password analysis.

    Expects JSON payload: {"password": "password_to_analyze"}

    Returns JSON response with analysis results.
    """
    try:
        data = request.get_json()
        password = data.get('password', '').strip()

        if not password:
            return jsonify({'error': 'No password provided'}), 400

        # Run comprehensive analysis using all analyzer modules
        length_res = length_checker.evaluate([password])
        entropy_res = entropy_calculator.evaluate([password])
        patterns_res = pattern_detector.evaluate([password])[0]
        freq_res = frequency_checker.evaluate([password])[0]
        names_res = name_detector.NameDetector().analyze(password)

        # Convert raw scores to strength scores (0-1 scale)
        results = {
            "length": length_res[password],
            "entropy": entropy_res[password],
            "patterns": 1 - min(patterns_res["pattern_score"] / 5, 1),  # Convert penalty to strength
            "frequency": 1 - freq_res["frequency_score"],  # Convert penalty to strength
            "names": 1 - min(names_res["name_score"] / 5, 1)  # Convert penalty to strength
        }

        # Aggregate all component scores into final result
        final_result = score_aggregator.combine_results(results)

        # Generate breach warning
        breach_warning = ""
        if freq_res["frequency_score"] > 0.5:
            breach_warning = "⚠️ This password appears in common password lists and may have been compromised in data breaches."

        # Generate personalized suggestions
        suggestions = []
        if results['length'] < 0.8:
            suggestions.append("Make it longer (at least 12 characters recommended)")
        if results['entropy'] < 0.6:
            suggestions.append("Add more variety (mix uppercase, lowercase, numbers, and symbols)")
        if results['patterns'] < 0.8:
            suggestions.append("Avoid common patterns like sequences (123), repeats (aaa), or keyboard patterns (qwerty)")
        if results['frequency'] < 0.8:
            suggestions.append("Avoid passwords that appear in common password dictionaries")
        if results['names'] < 0.8:
            suggestions.append("Avoid using personal names, dates, or easily guessable information")

        # Prepare comprehensive response
        response = {
            'overall_score': round(final_result['final_score'], 3),
            'components': {k: round(v, 3) for k, v in final_result['components'].items()},
            'strength': 'Strong' if final_result['final_score'] >= 0.8
                      else 'Moderate' if final_result['final_score'] >= 0.6
                      else 'Weak',
            'breach_warning': breach_warning,
            'suggestions': suggestions
        }

        return jsonify(response)

    except Exception as e:
        app.logger.error(f"Analysis error: {str(e)}")
        return jsonify({'error': 'Analysis failed. Please try again.'}), 500

@app.route('/health')
def health():
    """
    Health check endpoint for monitoring.
    """
    return jsonify({'status': 'healthy', 'service': 'password-analyzer'})

if __name__ == '__main__':
    # Development server configuration
    app.run(
        debug=True,
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000))
    )