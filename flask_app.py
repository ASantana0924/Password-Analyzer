from flask import Flask, render_template, request, jsonify
import os
from src.analyzer import length_checker, entropy_calculator, pattern_detector, frequency_checker, name_detector, score_aggregator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    password = request.json.get('password', '')
    
    if not password:
        return jsonify({'error': 'No password provided'}), 400
    
    # Run analysis (same as before)
    length_res = length_checker.evaluate([password])
    entropy_res = entropy_calculator.evaluate([password])
    patterns_res = pattern_detector.evaluate([password])[0]
    freq_res = frequency_checker.evaluate([password])[0]
    names_res = name_detector.NameDetector().analyze(password)

    results = {
        "length": length_res[password],
        "entropy": entropy_res[password],
        "patterns": 1 - min(patterns_res["pattern_score"] / 5, 1),
        "frequency": 1 - freq_res["frequency_score"],
        "names": 1 - min(names_res["name_score"] / 5, 1)
    }

    final_result = score_aggregator.combine_results(results)
    
    return jsonify({
        'overall_score': final_result['final_score'],
        'components': final_result['components'],
        'strength': 'Strong' if final_result['final_score'] >= 0.8 else 'Moderate' if final_result['final_score'] >= 0.6 else 'Weak'
    })

if __name__ == '__main__':
    app.run(debug=True)