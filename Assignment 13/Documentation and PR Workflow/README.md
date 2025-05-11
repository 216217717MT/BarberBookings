## How to run tests locally. How the CI/CD pipeline works

## CI/CD Pipeline

This project uses GitHub Actions to automate testing and artifact deployment.

### Running Tests Locally

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
How to run tests locally. How the CI/CD pipeline works
Documentation & PR Workflow
