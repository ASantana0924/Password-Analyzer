# Password Analyzer

A comprehensive password strength analysis tool with a beautiful web interface.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://password-analyzer.streamlit.app/)

## Features

- **Multi-criteria Analysis**: Checks length, entropy, patterns, frequency in common lists, and personal names
- **Visual Web Interface**: Interactive Streamlit app with charts and feedback
- **Command-line Demo**: Simple script for testing
- **Modular Design**: Easy to extend with new analyzers

## Live Demo

Try the app live at: [https://password-analyzer.streamlit.app/](https://password-analyzer.streamlit.app/)

## Installation (Local)

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the web app: `streamlit run app.py`

## Usage

### Web Interface
Enter a password to get:
- Overall strength score (0-1)
- Component breakdown with bar chart
- Color-coded feedback (strong/moderate/weak)
- Specific improvement suggestions

### Command Line
Run `python test_score.py` for a demo analysis

## Architecture

- `src/analyzer/`: Core analysis modules
- `src/utils/`: Helper functions for normalization and APIs
- `tests/`: Unit tests
- `data/`: Static data files (patterns, names, blocklists)

## Deployment

This app is deployed on Streamlit Cloud. To deploy your own version:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub account
4. Select this repository and the `main` branch
5. Click Deploy!

## Contributing

Feel free to open issues or submit pull requests to improve the analyzer!
