
# Quality Assurance Case Study Implementation

## Introduction

This repository is dedicated to the implementation of a quality assurance case study for both backend API and frontend interface of a demo flight application. The case study includes automated tests designed to validate the functionality, reliability and correctness of the application.

## Overview

The case study is divided into two main parts with three files:
##### Backend Testing
- `backend_tests.py`: The code I used to test backend API.
- `backend_tests_pytest.py`: API testing with using a test framework.
##### Frontend Testing
- `frontend_tests_playwright.py`: Frontend testing using Playwright.

## Prerequisites

- [Python 3.8 or newer](https://www.python.org/downloads/)
- [Playwright for Python](https://playwright.dev/python/docs/intro)
- [PyTest](https://docs.pytest.org/en/latest/)
- [Requests Library](https://requests.readthedocs.io/en/master/)

## How 2 Run

**Clone the Repository**:

```bash
git clone https://github.com/borawhocodess/QA-case-study.git
```

### Run

**Backend API tests**: with pure python:
  ```bash
  python backend_tests.py
  ```
**Backend API tests**: with PyTest:
  ```bash
  pytest backend_tests_pytest.py
  ```
**Frontend tests**: with Playwright:
  ```bash
  python frontend_tests_playwright.py
  ```

## Disclaimer

This project is for a case study for a QA internship position and it demonstrates QA practices on a demo application. It is not used in real world and is not intended for production use.


