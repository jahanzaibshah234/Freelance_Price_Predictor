import os
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

MODEL_PATH = "freelance_model.joblib"

# Skill -> valid project types mapping (used by frontend & validation)
SKILL_PROJECTS = {
    "python":            ["script", "automation", "ai_model", "api_endpoint", "web_scraper", "saas_mvp"],
    "web_dev":           ["landing_page", "full_website", "ecommerce", "api_endpoint", "saas_mvp", "web_scraper"],
    "data_science":      ["ai_model", "script", "automation", "api_endpoint", "technical_whitepaper", "saas_mvp"],
    "app_dev":           ["saas_mvp", "ecommerce", "api_endpoint", "full_website", "landing_page", "automation"],
    "cyber_security":    ["script", "api_endpoint", "technical_whitepaper", "saas_mvp", "automation", "web_scraper"],
    "cloud_computing":   ["automation", "api_endpoint", "saas_mvp", "script", "technical_whitepaper", "full_website"],
    "blockchain":        ["smart_contract", "saas_mvp", "api_endpoint", "technical_whitepaper", "automation", "web_scraper"],
    "graphic_design":    ["landing_page", "full_website", "ecommerce", "technical_whitepaper", "saas_mvp", "growth_hacking"],
    "ui_ux_design":      ["landing_page", "full_website", "ecommerce", "saas_mvp", "web_scraper", "automation"],
    "content_writing":   ["technical_whitepaper", "landing_page", "growth_hacking", "full_website", "ecommerce", "script"],
    "digital_marketing": ["growth_hacking", "landing_page", "ecommerce", "full_website", "technical_whitepaper", "saas_mvp"],
}


def train_and_save():
    """Train model on dataset and persist to disk."""
    df = pd.read_csv("dataset.csv")

    le_skill = LabelEncoder()
    le_exp   = LabelEncoder()
    le_proj  = LabelEncoder()
    le_comp  = LabelEncoder()

    df["skill"]        = le_skill.fit_transform(df["skill"])
    df["experience"]   = le_exp.fit_transform(df["experience"])
    df["project_type"] = le_proj.fit_transform(df["project_type"])
    df["complexity"]   = le_comp.fit_transform(df["complexity"])

    X = df[["skill", "experience", "project_type", "complexity", "hours"]]
    y = df["price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=42)
    model = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)

    score = model.score(X_test, y_test)
    print(f"Model R² on test set: {score:.4f}")

    joblib.dump({
        "model": model,
        "encoders": {
            "skill":        le_skill,
            "experience":   le_exp,
            "project_type": le_proj,
            "complexity":   le_comp,
        }
    }, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")


def _load():
    """Load model and encoders from disk, training first if needed."""
    if not os.path.exists(MODEL_PATH):
        print("Model not found — training now...")
        train_and_save()
    bundle = joblib.load(MODEL_PATH)
    return bundle["model"], bundle["encoders"]


# Load once at module import
_model, _encoders = _load()


def predict_price(skill: str, experience: str, project_type: str, complexity: str, hours: int) -> float:
    """Return predicted freelance price (USD).  Raises ValueError on bad inputs."""
    enc = _encoders

    for field, value, encoder in [
        ("skill",        skill,        enc["skill"]),
        ("experience",   experience,   enc["experience"]),
        ("project_type", project_type, enc["project_type"]),
        ("complexity",   complexity,   enc["complexity"]),
    ]:
        if value not in encoder.classes_:
            raise ValueError(
                f"Unknown {field}: '{value}'. Valid: {list(encoder.classes_)}"
            )

    # Also validate the skill↔project_type combo
    if skill in SKILL_PROJECTS and project_type not in SKILL_PROJECTS[skill]:
        raise ValueError(
            f"Project type '{project_type}' is not valid for skill '{skill}'."
        )

    row = pd.DataFrame([[
        enc["skill"].transform([skill])[0],
        enc["experience"].transform([experience])[0],
        enc["project_type"].transform([project_type])[0],
        enc["complexity"].transform([complexity])[0],
        hours,
    ]], columns=["skill", "experience", "project_type", "complexity", "hours"])

    return round(float(_model.predict(row)[0]), 2)


if __name__ == "__main__":
    train_and_save()
