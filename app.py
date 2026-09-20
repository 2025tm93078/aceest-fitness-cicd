from flask import Flask, jsonify, request

app = Flask(__name__)

PROGRAMS = {
    "fat_loss": {
        "name": "Fat Loss (FL)",
        "workout": [
            "Mon: Back Squat 5x5 + Core",
            "Tue: EMOM 20min Assault Bike",
            "Wed: Bench Press + 21-15-9",
            "Thu: Deadlift + Box Jumps",
            "Fri: Zone 2 Cardio 30min"
        ],
        "diet": {
            "breakfast": "3 Egg Whites + Oats",
            "lunch": "Grilled Chicken + Brown Rice",
            "dinner": "Fish Curry + Millet Roti",
            "target_kcal": 2000
        },
        "calorie_factor": 22
    },
    "muscle_gain": {
        "name": "Muscle Gain (MG)",
        "workout": [
            "Mon: Squat 5x5",
            "Tue: Bench Press 5x5",
            "Wed: Deadlift 4x6",
            "Thu: Front Squat 4x8",
            "Fri: Incline Press 4x10",
            "Sat: Barbell Rows 4x10"
        ],
        "diet": {
            "breakfast": "4 Eggs + Peanut Butter Oats",
            "lunch": "Chicken Biryani (250g chicken)",
            "dinner": "Mutton Curry + Jeera Rice",
            "target_kcal": 3200
        },
        "calorie_factor": 35
    },
    "beginner": {
        "name": "Beginner (BG)",
        "workout": [
            "Full Body Circuit: Air Squats, Ring Rows, Push-ups",
            "Focus: Technique Mastery & Form"
        ],
        "diet": {
            "breakfast": "Idli + Sambar",
            "lunch": "Rice + Dal + Vegetables",
            "dinner": "Chapati + Curry",
            "target_kcal": 2400
        },
        "calorie_factor": 28
    }
}

GYM_METRICS = {
    "capacity": 150,
    "area_sqft": 10000,
    "breakeven_members": 250,
    "name": "ACEest Functional Fitness"
}

def calculate_calories(weight_kg, program_key):
    if program_key not in PROGRAMS:
        return None
    factor = PROGRAMS[program_key]["calorie_factor"]
    return round(weight_kg * factor)

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "app": "ACEest Fitness & Gym",
        "version": "1.0.0"
    })

@app.route("/programs")
def get_programs():
    return jsonify({
        "programs": list(PROGRAMS.keys()),
        "count": len(PROGRAMS)
    })

@app.route("/programs/<program_id>")
def get_program(program_id):
    if program_id not in PROGRAMS:
        return jsonify({"error": "Program not found"}), 404
    return jsonify(PROGRAMS[program_id])

@app.route("/calories", methods=["POST"])
def get_calories():
    data = request.get_json()
    if not data or "weight_kg" not in data or "program" not in data:
        return jsonify({"error": "Provide weight_kg and program"}), 400
    calories = calculate_calories(data["weight_kg"], data["program"])
    if calories is None:
        return jsonify({"error": "Invalid program"}), 400
    return jsonify({
        "weight_kg": data["weight_kg"],
        "program": data["program"],
        "daily_calories": calories
    })

@app.route("/metrics")
def get_metrics():
    return jsonify(GYM_METRICS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)