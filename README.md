# Password Analyzer

A comprehensive password strength analysis tool that evaluates passwords based on multiple security criteria.

## Features

- **Multi-criteria Analysis**: Checks length, entropy, patterns, frequency in common lists, and personal names
- **Visual Web Interface**: Interactive Streamlit app with charts and feedback
- **Command-line Demo**: Simple script for testing
- **Modular Design**: Easy to extend with new analyzers

## Installation

1. Clone the repository
2. Install dependencies: `pip install streamlit matplotlib`
3. Run the web app: `streamlit run app.py`

## Usage

### Web Interface
Run `streamlit run app.py` and enter a password to get:
- Overall strength score (0-1)
- Component breakdown with bar chart
- Color-coded feedback (strong/moderate/weak)
- Specific improvement suggestions

### Command Line
Run `python test_score.py` for a demo analysis of "MyP@ssw0rd123"

## Architecture

- `src/analyzer/`: Core analysis modules
- `src/utils/`: Helper functions for normalization and APIs
- `tests/`: Unit tests
- `data/`: Static data files (patterns, names, blocklists)

## Enhancements Made

- Added Streamlit web interface for better user experience
- Included data visualizations with matplotlib
- Added intelligent improvement suggestions
- Improved code documentation with inline comments
