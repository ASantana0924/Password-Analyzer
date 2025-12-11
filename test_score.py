from src.analyzer import length_checker, entropy_calculator, pattern_detector, frequency_checker, name_detector, score_aggregator

password = "MyP@ssw0rd123"

length_res = length_checker.evaluate([password])
entropy_res = entropy_calculator.evaluate([password])
patterns_res = pattern_detector.evaluate([password])[0]
freq_res = frequency_checker.evaluate([password])[0]
names_res = name_detector.NameDetector().analyze(password)

results = {
    "length": length_res[password],
    "entropy": entropy_res[password],
    "patterns": 1 - min(patterns_res["pattern_score"] / 5, 1),  # assume max penalty 5
    "frequency": 1 - freq_res["frequency_score"],
    "names": 1 - min(names_res["name_score"] / 5, 1)  # assume max 5 names
}

final_result = score_aggregator.combine_results(results)
print(final_result)