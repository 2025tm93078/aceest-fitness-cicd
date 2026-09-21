import pytest
import json
from app import app, PROGRAMS, GYM_METRICS, calculate_calories

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client
      
def test_get_diet_endpoint(client):
    response = client.get("/programs/fat_loss/diet")
    assert response.status_code == 200

def test_get_workout_endpoint(client):
    response = client.get("/programs/muscle_gain/workout")
    assert response.status_code == 200

def test_get_diet_invalid_program(client):
    response = client.get("/programs/invalid/diet")
    assert response.status_code == 404

def test_get_workout_invalid_program(client):
    response = client.get("/programs/invalid/workout")
    assert response.status_code == 404
    
def test_home_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home_status_running(client):
    response = client.get("/")
    data = json.loads(response.data)
    assert data["status"] == "running"

def test_get_all_programs(client):
    response = client.get("/programs")
    assert response.status_code == 200

def test_programs_count(client):
    response = client.get("/programs")
    data = json.loads(response.data)
    assert data["count"] == 3

def test_fat_loss_program(client):
    response = client.get("/programs/fat_loss")
    assert response.status_code == 200

def test_muscle_gain_program(client):
    response = client.get("/programs/muscle_gain")
    assert response.status_code == 200

def test_beginner_program(client):
    response = client.get("/programs/beginner")
    assert response.status_code == 200

def test_invalid_program_404(client):
    response = client.get("/programs/invalid")
    assert response.status_code == 404

def test_calorie_calculation(client):
    response = client.post("/calories",
        json={"weight_kg": 70, "program": "fat_loss"},
        content_type="application/json")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert data["daily_calories"] == 1540

def test_calorie_missing_fields(client):
    response = client.post("/calories",
        json={"weight_kg": 70},
        content_type="application/json")
    assert response.status_code == 400

def test_metrics_endpoint(client):
    response = client.get("/metrics")
    assert response.status_code == 200

def test_metrics_capacity(client):
    response = client.get("/metrics")
    data = json.loads(response.data)
    assert data["capacity"] == 150

def test_calculate_calories_helper():
    assert calculate_calories(70, "fat_loss") == 1540

def test_calculate_calories_invalid():
    assert calculate_calories(70, "invalid") is None