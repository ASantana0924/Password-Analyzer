# 🔐 Password Analyzer

A comprehensive password strength analysis tool with multiple deployment options.

## ✨ Features

- **🔍 Multi-Criteria Analysis**: Evaluates length, entropy, patterns, frequency in common lists, and personal names
- **🌐 Client-Side Demo**: Fast JavaScript-based analysis on GitHub Pages (no backend required)
- **🐍 Full Python Backend**: Advanced analysis with Flask web server for comprehensive evaluation
- **📊 Interactive Visualizations**: Real-time charts showing component strength scores
- **🛡️ Breach Detection**: Checks against common password databases
- **🎯 Smart Suggestions**: Personalized improvement recommendations
- **📱 Responsive Design**: Works on desktop and mobile devices
- **🔧 Modular Architecture**: Easy to extend with new analyzers

## 🚀 Quick Start

### Option 1: Try the Client-Side Demo (No Installation Required)
Visit: **[https://asantana0924.github.io/Password-Analyzer/](https://asantana0924.github.io/Password-Analyzer/)**

- Instant analysis using JavaScript
- Good for quick password checks
- Works offline once loaded

### Option 2: Full Python Backend (Recommended for Advanced Analysis)

#### Prerequisites
- Python 3.8+
- pip package manager

#### Installation
```bash
# Clone the repository
git clone https://github.com/ASantana0924/Password-Analyzer.git
cd Password-Analyzer

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Running the Application
```bash
# Start the Flask web server
python flask_app.py

# Open your browser to: http://localhost:5000
```

## 📖 Usage

### Web Interface
1. Enter a password in the input field
2. Click "Analyze Password"
3. View comprehensive results including:
   - **Overall strength score** (0-100%)
   - **Component breakdown** with individual scores
   - **Interactive bar chart** visualization
   - **Security warnings** for breached passwords
   - **Improvement suggestions**

### Analysis Components

| Component | Description | Scale |
|-----------|-------------|-------|
| **Length** | Password length evaluation | 0-100% |
| **Entropy** | Randomness/complexity measure | 0-100% |
| **Patterns** | Detection of weak sequences/patterns | 0-100% |
| **Frequency** | Check against common password lists | 0-100% |
| **Names** | Personal name detection | 0-100% |

### Command Line Demo
```bash
python test_score.py
```

## 🏗️ Architecture

```
Password-Analyzer/
├── src/analyzer/           # Core analysis modules
│   ├── length_checker.py   # Password length evaluation
│   ├── entropy_calculator.py # Entropy/complexity analysis
│   ├── pattern_detector.py # Pattern recognition
│   ├── frequency_checker.py # Common password detection
│   ├── name_detector.py    # Personal name detection
│   └── score_aggregator.py # Score combination logic
├── src/utils/              # Helper utilities
├── data/                   # Static data files
│   ├── common_patterns.json
│   ├── common-names.txt
│   └── blocklists/
├── docs/                   # GitHub Pages static site
├── templates/              # Flask HTML templates
├── tests/                  # Unit tests
├── flask_app.py           # Flask web application
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🔧 Development

### Running Tests
```bash
python -m pytest tests/
```

### Adding New Analyzers
1. Create a new module in `src/analyzer/`
2. Implement an `evaluate(passwords)` function
3. Update `score_aggregator.py` to include the new component
4. Add tests in `tests/`

### Code Quality
- Follow PEP 8 style guidelines
- Add type hints for function parameters
- Include comprehensive docstrings
- Write unit tests for new features

## 🚀 Deployment

### GitHub Pages (Client-Side Only)
The static demo is automatically deployed to GitHub Pages from the `docs/` folder.

### Flask App Deployment
For production deployment with the full Python backend:

#### Local Development
```bash
python flask_app.py
```

#### Production Servers
- **Railway**: Connect GitHub repo for automatic deployment
- **Heroku**: Use the included `Procfile` (if created)
- **Docker**: Build from the included `Dockerfile` (if created)

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Ensure all tests pass: `python -m pytest`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Submit a pull request

### Areas for Contribution
- Additional analysis modules
- Improved pattern detection algorithms
- Better UI/UX design
- Performance optimizations
- Internationalization support
- Mobile app development

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## ⚠️ Security Notice

- **Never** use real passwords for testing
- This tool is for educational purposes only
- Passwords entered are processed locally (client-side demo) or temporarily on the server (Flask version)
- No passwords are stored or transmitted externally

## 🙏 Acknowledgments

- Built with Flask, Chart.js, and Python's data analysis libraries
- Pattern data sourced from various security research projects
- Inspired by password security best practices from OWASP and NIST

---

**Made with ❤️ for better password security awareness**
