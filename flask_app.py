from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from src.analyzer import length_checker, entropy_calculator, pattern_detector, frequency_checker, name_detector, score_aggregator

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')

    if not password:
        return jsonify({'error': 'No password provided'}), 400

    # Run individual analyzer modules
    length_res = length_checker.evaluate([password])
    entropy_res = entropy_calculator.evaluate([password])
    patterns_res = pattern_detector.evaluate([password])[0]
    freq_res = frequency_checker.evaluate([password])[0]
    names_res = name_detector.NameDetector().analyze(password)

    # Convert to strength scores
    results = {
        "length": length_res[password],
        "entropy": entropy_res[password],
        "patterns": 1 - min(patterns_res["pattern_score"] / 5, 1),
        "frequency": 1 - freq_res["frequency_score"],
        "names": 1 - min(names_res["name_score"] / 5, 1)
    }

    final_result = score_aggregator.combine_results(results)

    # Check for breaches (simplified)
    breach_warning = ""
    if freq_res["frequency_score"] > 0.5:
        breach_warning = "This password appears in common password lists and may have been compromised."

    response = {
        'overall_score': final_result['final_score'],
        'components': final_result['components'],
        'strength': 'Strong' if final_result['final_score'] >= 0.8 else 'Moderate' if final_result['final_score'] >= 0.6 else 'Weak',
        'breach_warning': breach_warning,
        'suggestions': []
    }

    # Generate suggestions
    if results['length'] < 0.8:
        response['suggestions'].append("Make it longer (at least 12 characters)")
    if results['entropy'] < 0.6:
        response['suggestions'].append("Add more variety (uppercase, lowercase, numbers, symbols)")
    if results['patterns'] < 0.8:
        response['suggestions'].append("Avoid common patterns like sequences or repeats")
    if results['frequency'] < 0.8:
        response['suggestions'].append("Avoid common passwords")
    if results['names'] < 0.8:
        response['suggestions'].append("Avoid using personal names")

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)