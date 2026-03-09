
# CSYE 7220 – DevOps In-Class Lab

**Course:** CSYE 7220 – Development and Operation of Software Applications  
**Instructor:** Jiazhen Zhu  
**Duration:** 60 minutes  
**Type:** Individual Hands-on Lab  
**Tools:** Git, GitHub, GitHub Actions, Python

---

# Lab Overview

In this lab you will simulate a **real DevOps workflow**.

You will:

1. Create a Git feature branch
2. Debug application code
3. Fix failing tests
4. Repair a broken CI pipeline
5. Create and merge a Pull Request

The goal is to ensure the **CI pipeline passes successfully**.

---

# Scenario

You have joined a DevOps team.

A developer submitted a feature but the **CI pipeline is failing**.

Your task is to:

- fix the code
- fix the tests
- fix the CI pipeline
- successfully merge the Pull Request

---

# Starter Repository

You will receive a repository from the instructor:

```
devops-lab-app
```

Repository structure:

```
devops-lab-app
│
├── app.py
├── test_app.py
├── requirements.txt
├── README.md
└── .github/workflows/ci.yml
```

---

# Part 1 – Git Workflow (20 points)

### Task 1 — Clone the repository

```bash
git clone <repo-url>
cd devops-lab-app
```

### Task 2 — Create a feature branch

Create a new branch called:

```
feature/fix-login
```

Command:

```bash
git checkout -b feature/fix-login
```

### Task 3 — Push the branch

```bash
git push origin feature/fix-login
```

---

# Part 2 – Debug the Application Code (30 points)

Open:

```
app.py
```

Current code:

```python
def login(username, password):
    if username == "admin" and password == "1234"
        return True
    return False
```

The CI pipeline fails because there is a **syntax error**.

### Fix the code

Correct version:

```python
def login(username, password):
    if username == "admin" and password == "1234":
        return True
    return False
```

### Commit the fix

```bash
git add .
git commit -m "Fix syntax error in login function"
```

---

# Part 3 – Fix the Tests (20 points)

Open:

```
test_app.py
```

Current test:

```python
from app import login

def test_login():
    assert login("admin","wrong") == True
```

Expected behavior:

```
wrong password should return False
```

### Correct test

```python
from app import login

def test_login():
    assert login("admin","wrong") == False
```

### Commit the change

```bash
git add .
git commit -m "Fix incorrect test expectation"
```

---

# Part 4 – Fix the CI Pipeline (20 points)

Open the CI workflow file:

```
.github/workflows/ci.yml
```

Current pipeline:

```yaml
name: CI

on: push

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

### Problem

`pytest` is not installed.

The pipeline fails when running tests.

### Fix the pipeline

Update the dependency step:

```yaml
- name: Install dependencies
  run: |
    pip install -r requirements.txt
    pip install pytest
```

### Push your changes

```bash
git add .
git commit -m "Fix CI pipeline dependency"
git push
```

---

# Part 5 – Create a Pull Request (10 points)

Create a Pull Request:

```
feature/fix-login → main
```

Verify:

- CI pipeline runs
- Tests pass
- No errors remain

### Merge the Pull Request

Once CI passes, merge your PR into the `main` branch.

---

# Expected CI Pipeline

```
Push Code
   ↓
Checkout Repository
   ↓
Install Dependencies
   ↓
Run Tests
   ↓
Pipeline Status: PASS
```

---

# Grading Rubric

| Task | Points |
|-----|------|
| Git branch workflow | 20 |
| Fix application code | 30 |
| Fix test cases | 20 |
| Repair CI pipeline | 20 |
| Create Pull Request | 10 |

**Total: 100 points**

---

# Learning Objectives

By completing this lab you will learn how to:

- Use Git branching workflows
- Debug application code
- Fix failing test cases
- Repair CI pipelines
- Work with Pull Request workflows
- Understand DevOps automation practices

---

# Submission

Submit the following:

1. GitHub repository link
2. Screenshot of successful CI pipeline
3. Pull Request URL
