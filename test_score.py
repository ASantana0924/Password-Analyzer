from src.analyzer import length_checker, entropy_calculator, pattern_detector, frequency_checker, name_detector, score_aggregator

password = "MyP@ssw0rd123"

results = {
    "length": length_checker.evaluate([password])[0],
    "entropy": entropy_calculator.evaluate([password])[0],
    "patterns": pattern_detector.evaluate([password])[0],
    "frequency": frequency_checker.evaluate([password])[0],
    "names": name_detector.NameDetector().analyze(password)
}

final_result = score_aggregator.combine_results(results)
print(final_result)