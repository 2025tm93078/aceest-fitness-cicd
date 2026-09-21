# ACEest Fitness & Gym

## What is this project
This is a Flask web app for ACEest Fitness and Gym. It has API endpoints for fitness programs, diet plans, workouts and calorie calculation. I also set up a full CI/CD pipeline using GitHub Actions and Jenkins.

## How to run locally
```bash
git clone https://github.com/2025tm93078/aceest-fitness-cicd.git
cd aceest-fitness-cicd
pip install -r requirements.txt
python app.py
```
Open http://localhost:5000 in browser

## API Endpoints
- GET / — checks if app is running
- GET /programs — shows all fitness programs
- GET /programs/<id> — shows one program
- GET /programs/<id>/diet — shows diet plan
- GET /programs/<id>/workout — shows workout plan
- POST /calories — calculates daily calories based on weight
- GET /metrics — shows gym details

## Running tests
```bash
pytest test_app.py -v
```
18 tests, all passing.

## Docker
```bash
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```

![Docker](screenshots/docker.png)

## GitHub Actions
Pipeline runs automatically on every push to main. It does 3 things - lint check, docker build, and runs all tests.

![GitHub Actions](screenshots/github-actions.png)

## Jenkins
Jenkins pulls code from GitHub and runs the build. Stages are checkout, install, lint and test.

![Jenkins 1](screenshots/jenkins1.png)
![Jenkins 2](screenshots/jenkins2.png)
![Jenkins 3](screenshots/jenkins3.png)