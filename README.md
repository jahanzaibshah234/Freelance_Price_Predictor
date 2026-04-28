# Freelance Price Predictor 💰

👥 Developed by **Jahanzaib Shah & Maria Rashid**

A machine learning-powered web application that predicts freelance project pricing based on project characteristics and market factors.

## 📋 Overview

The Freelance Price Predictor is an intelligent tool designed to help freelancers and clients estimate fair project pricing. Using advanced machine learning algorithms, the predictor analyzes project requirements, complexity, and market data to provide accurate price recommendations for freelance work.

## ✨ Features

- **Smart Price Prediction** - ML-based pricing model for accurate estimates
- **User-Friendly Interface** - Intuitive web interface for easy interaction  
- **Real-Time Analysis** - Instant price predictions based on project parameters
- **Responsive Design** - Works seamlessly on desktop and mobile devices
- **Data-Driven Insights** - Backed by comprehensive market data analysis
- **Detailed Breakdown** - View factors influencing the predicted price
- **Custom Filters** - Filter predictions by skill type, experience level, and more

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python |
| Frontend | HTML & CSS |
| Framework | FastAPI (Asynchronous API) |
| ML Libraries | Scikit-learn |
| Data Processing | Pandas |

## 📊 Language Composition

- Python: 52.4%
- HTML: 30.3%
- CSS: 17.3%

## 📁 Project Structure

```
FREELANCE_PRICE_PREDICTOR/           # Root Directory
├── .github/workflows/               # GitHub Actions CI/CD
│   └── ci.yml
├── freelance_price_predictor/       # Core Project Folder
│   ├── static/                      # CSS files
│   │   └── style.css
│   ├── templates/                   # HTML templates
│   │   └── index.html
│   ├── dataset.csv                  # Training data
│   ├── main.py                      # FastAPI routes & server
│   ├── price_model.py               # ML Logic & training script
│   ├── test.py                      # Pytest suite
│   ├── requirements.txt             # Project dependencies
│   └── .gitignore                   # Ignored files (like myenv/ and .joblib)
└── README.md                        # Documentation
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10
- pip (Python package installer)
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jahanzaibshah234/Freelance_Price_Predictor.git
   cd Freelance_Price_Predictor
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv myenv
   ```

3. **Activate Virtual Environment**
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux:**
     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   # Move into the project folder
   cd freelance_price_predictor
   # Run using uvicorn
   uvicorn main:app --reload
   ```

6. **Access the Application**
   - Open your web browser and navigate to: `http://localhost:8000`
   - The application should now be running and ready to use

## 📝 Usage

### Basic Usage

1. **Fill in Project Details:**
   - Select Skill: Choose your primary technical domain (e.g., Python, Web Dev, etc.)
   - Experience Level: Select your expertise (Beginner, Intermediate, or Expert).
   - Choose a specific category (this list updates dynamically based on your selected Skill)
   - Complexity: Rate the difficulty of the task (Low, Medium, or High)
   - Estimated Hours: Enter the total time you expect the project to take

2. **Get Price Prediction:**
   - Click the "Predict Price" button
   - The system will process your inputs through the Random Forest model

3. **View Results:**
   - Recommended Price: See the total suggested project cost in USD
   - Market Context: Pricing is based on calculated 2026 market rates
   - Error Handling: If an invalid combination is selected, the UI will provide instant feedback

### Example Input

```
Skill: Python
Experience Level: Intermediate
Project Type: Automation
Complexity: Medium
Estimated Hours:
```

### Expected Output

```
💰 Recommended Price: $1063.09
Based on 2026 Market Rates
```

## 🤖 Machine Learning Model

### Model Architecture

The price prediction engine uses a **Random Forest Regressor** (with 200 estimators). This ensemble learning method was chosen for its ability to handle non-linear relationships between project complexity, experience levels, and market rates.

**Input Features:**
The model processes five specific features to generate a prediction:
- Skill: The core technical domain (Categorical - Label Encoded)
- Experience Level: The freelancer's expertise (Beginner, Intermediate, Expert).
- Project Type: The specific deliverable (updates dynamically based on skill)
- Complexity: The difficulty tier of the project (Low, Medium, High)
- Estimated Hours: The total duration of the engagement

**Output:**
- Predicted freelance project price (USD)

### Training Data

- Dataset Size: 10,000+ historical freelance project entries.
- Time Period: Data reflects market trends up to 2026
- Features: 5 core input features (Skill, Experience, Project Type, Complexity, and Hours)
- Target Variable: Project Price (USD) — The total recommended project fee

## 🔄 API Endpoints

While the primary interface is the web UI, the backend processes requests through the following structure:

### Predict Price

**Endpoint:** `POST /api/predict`
**Content-Type:** application/x-www-form-urlencoded

**Request:**
```json
{
  "skill": "python",
  "experience": "intermediate",
  "project_type": "automation",
  "complexity": "medium",
  "hours": 20
}
```

**Response:**
```json
{
  "status": "success",
  "recommended_price": 1063.09,
  "currency": "USD",
  "market_year": 2026
}
```


## 🧪 Testing

Run the test suite:

```bash
pytest test.py
```

### Test Coverage

- Logic Tests (test_prediction_logic_success): Confirms the AI model successfully processes inputs and returns a valid price
- Validation Tests (test_invalid_skill_combination): Ensures the backend logic correctly blocks impossible skill/project pairings
- Web Integration (test_home_page_loads): Verifies that the FastAPI server renders the homepage and form fields correctly
- End-to-End Flow (test_web_prediction_flow): Simulates a full user interaction from form submission to price display
- Error Handling (test_web_error_handling): Checks that the UI properly displays error messages when invalid data is submitted

## 📈 Future Enhancements

- [ ] User authentication and project history
- [ ] Advanced visualization dashboard
- [ ] Mobile app development
- [ ] Blockchain integration for payment
- [ ] Multilingual support
- [ ] Real-time market data integration
- [ ] Browser extension for price suggestions
- [ ] Integration with major freelance platforms

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
   ```bash
   git clone https://github.com/yourusername/Freelance_Price_Predictor.git
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Make Your Changes**
   - Keep code clean and documented
   - Follow PEP 8 style guidelines for Python
   - Add comments for complex logic

4. **Commit Your Changes**
   ```bash
   git commit -m "Add: Brief description of your changes"
   ```

5. **Push to the Branch**
   ```bash
   git push origin feature/YourFeatureName
   ```

6. **Open a Pull Request**
   - Provide clear description of changes
   - Reference any related issues
   - Ensure all tests pass

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports & Feature Requests

Found a bug or have a feature request? Please open an issue on GitHub:
- [Create an Issue](https://github.com/jahanzaibshah234/Freelance_Price_Predictor/issues)

Include:
- Detailed description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

## 📞 Contact & Support

- **Email**: jahanzaib1234510@gmail.com
- **GitHub**: [@jahanzaibshah234](https://github.com/jahanzaibshah234)
- **LinkedIn**: https://www.linkedin.com/in/jahanzaib-khalid/

For quick questions, feel free to open a discussion or contact via email.

## 👥 Team

### **Jahanzaib Shah**
- Role: Machine Learning Engineer & Backend Developer
- Contributions:
  - Built and trained the ML model (Random Forest Regressor)
  - Developed FastAPI backend and API endpoints
  - Integrated model with web application

### **Maria Rashid**
- Role: Python Developer & UI Support
- Contributions:
  - Assisted in Python development and project logic
  - Worked on frontend integration (HTML/CSS templates)
  - Supported testing and overall project structuring

## 🙏 Acknowledgments

- Thanks to all contributors and supporters
- Inspired by freelance marketplace ecosystems
- Built with dedication for the freelance community

**Special Thanks:**
- Maria Rashid for her valuable contribution in development and support
- Scikit-learn and machine learning community
- Open-source contributors

## 📚 Resources & References

- [Scikit-learn Documentation](https://scikit-learn.org/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Machine Learning Best Practices](https://ml.mastery.com/)

## 📋 Changelog

### v1.0.0 (2026-04-28)
- Initial release
- Core price prediction model
- Basic web interface
- API endpoints

### Upcoming
- v1.1.0: User authentication system
- v1.2.0: Advanced analytics dashboard
- v2.0.0: Mobile application launch

---

<div align="center">

**Made with ❤️ by Jahanzaib Shah & Maria Rashid**

⭐ If this project helped you, please consider giving it a star!

[Report Bug](https://github.com/jahanzaibshah234/Freelance_Price_Predictor/issues) · [Request Feature](https://github.com/jahanzaibshah234/Freelance_Price_Predictor/issues)

</div>
