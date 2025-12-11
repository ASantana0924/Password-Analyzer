# Password Analyzer

A comprehensive password strength analysis tool with multiple interface options.

## Features

- **Multi-criteria Analysis**: Checks length, entropy, patterns, frequency in common lists, and personal names
- **Client-Side Web Interface**: Fast JavaScript-based analysis on GitHub Pages
- **Full Python Backend**: Advanced analysis with Flask web server for local use
- **Command-line Demo**: Simple script for testing
- **Modular Design**: Easy to extend with new analyzers

## Live Demo

Try the client-side analysis at: [https://asantana0924.github.io/Password-Analyzer/](https://asantana0924.github.io/Password-Analyzer/)

*Note: The live demo uses JavaScript for instant analysis. For the full Python-powered experience with advanced features, run locally.*

## Installation & Usage

### Option 1: Client-Side Analysis (GitHub Pages)
- Visit [https://asantana0924.github.io/Password-Analyzer/](https://asantana0924.github.io/Password-Analyzer/)
- Analysis runs instantly in your browser
- Good for quick checks and demonstrations

### Option 2: Full Python Backend (Local)
For the complete experience with advanced analysis:

1. Clone the repository:
   ```bash
   git clone https://github.com/ASantana0924/Password-Analyzer.git
   cd Password-Analyzer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask web application:
   ```bash
   python flask_app.py
   ```

4. Open your browser to `http://localhost:5000`

### Option 3: Command Line Demo
Run `python test_score.py` for a simple analysis demo

## Analysis Features

### Client-Side (JavaScript)
- Length and entropy calculation
- Basic pattern detection
- Visual charts with Chart.js
- Instant feedback

### Full Backend (Python)
- All client-side features plus:
- Advanced pattern recognition
- Breach detection against common password lists
- Personal name detection
- More accurate entropy calculations
- Comprehensive improvement suggestions

## Architecture

- `src/analyzer/`: Core Python analysis modules
- `src/utils/`: Helper functions for normalization and APIs
- `docs/`: GitHub Pages static site with client-side analysis
- `templates/`: Flask HTML templates
- `tests/`: Unit tests
- `data/`: Static data files (patterns, names, blocklists)

## Contributing

Feel free to open issues or submit pull requests to improve the analyzer!
