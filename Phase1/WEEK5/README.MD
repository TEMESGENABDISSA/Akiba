# Akiba Technologies: Week 5 Python OOP Tasks

A collection of five Python exercises that introduce the core concepts of Object-Oriented Programming (OOP): classes, objects, constructors, instance methods, class attributes, and string representation.

---

## Table of Contents

- [Overview](#overview)
- [Learning Objectives](#learning-objectives)
- [Repository Structure](#repository-structure)
- [Tasks](#tasks)
  - [Easy](#easy-tasks)
  - [Medium](#medium-tasks)

---

## Overview

| Detail            | Value                         |
|-------------------|-------------------------------|
| Program           | Akiba Technologies            |
| Module            | Week 5: Python OOP            |
| Total Tasks       | 5                             |
| Language          | Python 3                      |
| Submission Method | GitHub repository             |

All five solutions live in a single file, `week5_oop_tasks.py`, with each task separated by clear comment headers.

---

## Learning Objectives

By completing these tasks, you should be able to:

- Create classes and instantiate objects
- Use constructors (`__init__()`) and instance methods
- Distinguish between class attributes and instance attributes
- Represent objects as readable text using `__str__()`
- Implement basic object behavior with validation (e.g., preventing overdrafts)

---

## Repository Structure

```
.
├── README.md
├── week5_oop_tasks.py        # All five task solutions
└── week5_oop_answers.txt     # Conceptual answers (optional if answered as comments)
```

---

## Tasks

### Easy Tasks

#### Task 1: Student Information System

Create a `Student` class that:

- Defines the attributes `name`, `age`, and `department`
- Initializes them with `__init__()`
- Provides a `display_info()` method that shows the student's details

Then create **three** student objects with different information and display each one.

#### Task 2: Rectangle Calculator

Create a `Rectangle` class that:

- Initializes `length` and `width` with `__init__()`
- Provides an `area()` method
- Provides a `perimeter()` method

Then create **two** rectangles with different dimensions and display the area and perimeter of each.

---

### Medium Tasks

#### Task 3: Student Score Management

Create a `Student` class that:

- Defines a class attribute `school_name = "Akiba Academy"`
- Defines instance attributes `name`, `score`, and `department`
- Provides a `display()` method that shows all student information

Then:

1. Create at least **three** student objects.
2. Update the score of one student and display the updated information.
3. Demonstrate that each student has an independent score.

**Questions**

- What is the difference between a class attribute and an instance attribute?
- Why does updating one student's score not automatically change the scores of other students?

#### Task 4: Product Information System

Create a `Product` class that:

- Defines the attributes `name`, `price`, and `quantity`
- Initializes them with `__init__()`
- Implements `__str__()` to return a readable description of the product
- Provides a `total_value()` method that returns `price × quantity`

Then create at least **three** products and print each one directly using `print()`.

**Question**

- What is the purpose of the `__str__()` method?

#### Task 5: Bank Account Management

Create a `BankAccount` class that:

- Defines the attributes `owner` and `balance`
- Initializes them with `__init__()`
- Provides `deposit(amount)`, `withdraw(amount)`, and `display_balance()` methods
- **Prevents withdrawals** when the requested amount exceeds the available balance

Then create **two** accounts with different owners and balances, and perform multiple deposits and withdrawals on each.

**Example scenario**

1. Create an account with a balance of 1,000 birr.
2. Deposit 500 birr.
3. Withdraw 300 birr.
4. Attempt to withdraw 2,000 birr (this must be rejected).
5. Display the final balance and explain what should happen when a withdrawal exceeds the balance.

---


# Run the solutions
python week5_oop_tasks.py
```
