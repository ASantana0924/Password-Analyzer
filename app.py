import streamlit as st  # Web app framework for creating interactive interfaces
import matplotlib.pyplot as plt  # Library for creating visualizations like bar charts
from src.analyzer import length_checker, entropy_calculator, pattern_detector, frequency_checker, name_detector, score_aggregator

st.title("Password Strength Analyzer")  # Sets the main title of the web app

password = st.text_input("Enter a password to analyze:", type="password")  # Creates a password input field that hides the text

if password:  # Only run analysis if a password is entered
    # Run individual analyzer modules on the password
    length_res = length_checker.evaluate([password])  # Checks password length strength
    entropy_res = entropy_calculator.evaluate([password])  # Calculates randomness/entropy
    patterns_res = pattern_detector.evaluate([password])[0]  # Detects weak patterns
    freq_res = frequency_checker.evaluate([password])[0]  # Checks against common password lists
    names_res = name_detector.NameDetector().analyze(password)  # Detects personal names

    # Convert analyzer results to strength scores (0-1, higher is better)
    results = {
        "length": length_res[password],  # Length score (0-1)
        "entropy": entropy_res[password],  # Entropy score (0-1)
        "patterns": 1 - min(patterns_res["pattern_score"] / 5, 1),  # Invert pattern penalty to strength
        "frequency": 1 - freq_res["frequency_score"],  # Invert frequency penalty to strength
        "names": 1 - min(names_res["name_score"] / 5, 1)  # Invert name penalty to strength
    }

    final_result = score_aggregator.combine_results(results)  # Aggregate all scores into final result

    st.subheader(f"Overall Strength Score: {final_result['final_score']:.2f}")  # Display overall score

    # Display individual component scores
    st.write("Component Scores:")
    for key, value in final_result['components'].items():
        st.write(f"- {key.capitalize()}: {value:.2f}")

    # Create and display a bar chart of the component scores
    fig, ax = plt.subplots()
    ax.bar(final_result['components'].keys(), final_result['components'].values())
    ax.set_ylim(0, 1)
    ax.set_ylabel('Strength Score')
    ax.set_title('Password Strength Components')
    st.pyplot(fig)  # Embed the matplotlib figure in the Streamlit app

    # Provide color-coded feedback based on overall score
    score = final_result['final_score']
    if score >= 0.8:
        st.success("Strong password!")  # Green success message
    elif score >= 0.6:
        st.warning("Moderate password. Consider improvements.")  # Yellow warning
    else:
        st.error("Weak password. Please strengthen it.")  # Red error message

    # Generate and display specific improvement suggestions
    suggestions = []
    if results['length'] < 1:
        suggestions.append("Make it longer (at least 12 characters).")
    if results['entropy'] < 0.5:
        suggestions.append("Add more variety (uppercase, lowercase, numbers, symbols).")
    if results['patterns'] < 1:
        suggestions.append("Avoid common patterns like sequences or repeats.")
    if results['frequency'] < 1:
        suggestions.append("Avoid common passwords.")
    if results['names'] < 1:
        suggestions.append("Avoid using personal names.")

    if suggestions:
        st.subheader("Suggestions to improve:")
        for sug in suggestions:
            st.write(f"- {sug}")