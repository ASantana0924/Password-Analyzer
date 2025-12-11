"""
Aggregate scores from all analyzers to compute a final password strength score.
"""

def aggregate_scores(results_dict, weights=None):
    """
    Compute a final normalized password strength score based on individual analyzer results.

    Parameters:
        results_dict (dict): Dictionary with keys corresponding to analyzers
            and values being analyzer-specific scores in [0,1] (or 0 if not present).
            Example:
            {
                "length": 0.5,
                "entropy": 0.75,
                "patterns": 1.0,
                "frequency": 0.8,
                "names": 0.0
            }
        weights (dict, optional): Dictionary to weight each component.
            Defaults to equal weights for all present components.

    Returns:
        float: final score normalized to [0,1], higher = stronger password
    """

    if not results_dict:
        return 0.0

    # Default weights: equal weight for each component
    if weights is None:
        weights = {k: 1 for k in results_dict.keys()}

    # Ensure only keys in results_dict are considered
    weights = {k: weights.get(k, 1) for k in results_dict.keys()}

    # Compute weighted sum
    weighted_score = 0.0
    total_weight = 0.0
    for key, score in results_dict.items():
        w = weights.get(key, 1)
        weighted_score += score * w
        total_weight += w

    if total_weight == 0:
        return 0.0

    final_score = weighted_score / total_weight

    # Clip to [0,1]
    return min(max(final_score, 0.0), 1.0)


def combine_results(analyzer_results):
    """
    Combine all individual analyzer results into a final dictionary per password.

    Parameters:
        analyzer_results (dict): Dictionary mapping analyzer names to their
        outputs (e.g., results from length_checker, entropy_calculator, etc.)
        Each output should have a numeric score (0-1).

    Returns:
        dict: {
            "final_score": 0.0-1.0,
            "components": {
                "length": ...,
                "entropy": ...,
                "patterns": ...,
                "frequency": ...,
                "names": ...
            }
        }
    """
    components = {}
    for name, result in analyzer_results.items():
        # Assume each analyzer result dict has 'score' or '<analyzer>_score'
        if isinstance(result, dict):
            if "score" in result:
                components[name] = result["score"]
            else:
                # fallback for custom score keys
                key = next((k for k in result.keys() if k.endswith("_score")), None)
                components[name] = result.get(key, 0.0)
        else:
            # if result is already a numeric score
            components[name] = float(result)

    final_score = aggregate_scores(components)
    return {
        "final_score": final_score,
        "components": components
    }