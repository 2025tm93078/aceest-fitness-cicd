# ACEest Fitness & Gym — CI/CD Pipeline

![GitHub Actions](https://github.com/2025tm93078/aceest-fitness-cicd/actions/workflows/main.yml/badge.svg)

## Project Overview
ACEest Fitness & Gym is a Flask-based REST API that serves fitness programs, diet plans, workout schedules, and calorie calculations. This project demonstrates a complete DevOps pipeline including version control, containerization, automated testing, and CI/CD automation.

## Tech Stack
- **Backend:** Python, Flask
- **Testing:** Pytest
- **Containerization:** Docker
- **CI/CD:** GitHub Actions, Jenkins
- **Version Control:** Git/GitHub

## Local Setup
```bash
git clone https://github.com/2025tm93078/aceest-fitness-cicd.git
cd aceest-fitness-cicd
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Health check |
| GET | /programs | List all fitness programs |
| GET | /programs/<id> | Get specific program details |
| GET | /programs/<id>/diet | Get diet plan for a program |
| GET | /programs/<id>/workout | Get workout plan for a program |
| POST | /calories | Calculate daily calorie target |
| GET | /metrics | Gym capacity and metrics |

## Running Tests Manually
```bash
pytest test_app.py -v
```
Currently 18 tests covering all endpoints.

## Docker
```bash
docker build -t aceest-fitness .
docker run -p 5000:5000 aceest-fitness
```
Uses `python:3.10-slim` for optimized image size.

![Docker Build](screenshots/docker.png)

## GitHub Actions Pipeline
Triggers automatically on every push and pull request to main branch.

**Stages:**
1. **Build and Lint** — installs dependencies, checks syntax with flake8
2. **Docker Build** — builds and verifies the Docker image
3. **Run Pytest** — runs all 18 tests inside the container

![GitHub Actions](screenshots/github-actions.png)

## Jenkins Pipeline
Jenkins pulls the latest code from GitHub and runs a clean build.

**Stages:**
1. **Checkout** — clones the repository from GitHub
2. **Install Dependencies** — installs all Python packages
3. **Lint** — runs flake8 for code quality check
4. **Run Tests** — executes all 18 pytest cases

![Jenkins 1](screenshots/jenkins1.png)
![Jenkins 2](screenshots/jenkins2.png)
![Jenkins 3](screenshots/jenkins3.png)