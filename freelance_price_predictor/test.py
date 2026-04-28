import pytest
from fastapi.testclient import TestClient
from main import app
from price_model import predict_price, SKILL_PROJECTS

client = TestClient(app)

# --- Logic Tests (The AI Model) ---

def test_prediction_logic_success():
    """Verify the model returns a valid price for a standard combo."""
    # Pick a valid pair from the shared configuration
    skill = "python"
    project = SKILL_PROJECTS[skill][0] # "script"
    
    price = predict_price(
        skill=skill, 
        experience="intermediate", 
        project_type=project, 
        complexity="medium", 
        hours=20
    )
    
    assert isinstance(price, float)
    assert price > 0
    print(f"✅ Prediction Logic OK: ${price}")

def test_invalid_skill_combination():
    """Verify the backend blocks project types not allowed for a specific skill."""
    # 'blockchain' does not have 'landing_page' in its list
    with pytest.raises(ValueError) as excinfo:
        predict_price("blockchain", "expert", "landing_page", "high", 10)
    
    assert "not valid for skill" in str(excinfo.value)
    print("✅ Skill/Project Validation OK")


# --- Web Tests (The FastAPI App) ---

def test_home_page_loads():
    """Ensure the landing page renders with the correct form fields."""
    response = client.get("/")
    assert response.status_code == 200
    assert 'id="skillSelect"' in response.text
    assert 'id="projectSelect"' in response.text

def test_web_prediction_flow():
    """Simulate a user filling out the form and clicking 'Predict'."""
    form_data = {
        "skill": "web_dev",
        "experience": "beginner",
        "project_type": "landing_page",
        "complexity": "low",
        "hours": 15
    }
    response = client.post("/predict", data=form_data)
    
    assert response.status_code == 200
    # Check if the result-box appears in the HTML output
    assert "Recommended Price" in response.text
    # Verify the price is passed to the template
    assert "price" in response.context
    print(f"✅ Web Flow OK: Recommended ${response.context['price']}")

def test_web_error_handling():
    """Ensure errors (like bad inputs) are shown to the user in the UI."""
    bad_data = {
        "skill": "python",
        "experience": "beginner",
        "project_type": "smart_contract", # Python can't do smart contracts in your logic
        "complexity": "low",
        "hours": 5
    }
    response = client.post("/predict", data=bad_data)
    
    assert response.status_code == 200
    assert "error-box" in response.text
    assert "not valid for skill" in response.text
    print("✅ Error UI display OK")

if __name__ == "__main__":
    # This allows you to run it via 'python test.py' manually
    print("🚀 Starting manual test run...")
    try:
        test_prediction_logic_success()
        test_home_page_loads()
        test_web_prediction_flow()
        print("\n✨ ALL CORE TESTS PASSED ✨")
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
