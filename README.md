# ReqRes API Testing Framework

## Overview
This framework is designed to test the ReqRes API (https://reqres.in) using Python and Pytest. It includes comprehensive test coverage, detailed reporting, and CI/CD integration.

## Features
- Modular and maintainable test structure
- Detailed HTML reports
- Logging system
- CI/CD integration with GitHub Actions
- Parallel test execution support
- Environment configuration management

## Setup
1. Clone the repository
2. Create virtual environment: `python -m venv venv`
3. Activate virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Running Tests
- Run all tests: `pytest`
- Generate HTML report: `pytest --html=reports/report.html`
- Run tests in parallel: `pytest -n auto`
- Run specific test file: `pytest tests/test_users.py`

## Project Structure
- `src/`: Source code and utilities
- `tests/`: Test cases
- `reports/`: Test reports and logs
- `.github/workflows/`: CI/CD configuration

## Contributing
1. Fork the repository
2. Create feature branch
3. Commit changes
4. Create pull request
