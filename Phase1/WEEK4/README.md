# Week 4 Python Task: Mutability, References, and Memory Model
## Repository Structure

week-4-python-task/
├── README.md
├── questions.py
└── student_marks_manager.py


## How to Run

python questions.py
python student_marks_manager.py

## Answers

### Question 1: Mutable and Immutable Objects
- **Mutable** objects can be changed in place and keep the same identity (e.g. `list`, `dict`, `set`).
- **Immutable** objects cannot be changed after creation; "modifying" them creates a new object (e.g. `int`, `str`, `tuple`).

### Question 2: References and Object Identity
- Output: `True`, `False`, `True`.
- `==` compares values; `is` compares identity (same object in memory).
- `a` and `c` have equal values but are two separate list objects, so their identities differ.

### Question 3: Shared References and Side Effects
- Output: `[1, 2, 3, 4]` printed twice.
- `values = numbers` copies the reference, not the list, so both names point to one object.
- Fix: `values = numbers.copy()`.

### Question 4: Function Arguments and Mutability
- Output: `[50, 60, 70, 100]`.
- The function receives a reference to the same mutable list, so `append` changes the original.
- Fix: `return items + [100]`.

### Question 5: Memory Management and Garbage Collection
- Python uses reference counting; when an object's count reaches zero its memory is freed. A cyclic garbage collector handles reference cycles.
- `del` removes a name, not necessarily the object.
- The object survives while other references to it exist.
- An object with no references is eligible for garbage collection.


## Project Reflection

**1. Why does modifying a shared reference affect the original list?**
Both variables point to the same list object, so a change through one is visible through the other.

**2. Why does modifying the copied list not affect the original list?**
A copy is a separate object in its own memory location.

**3. What is the difference between equality and identity?**
Equality (`==`) checks whether values are the same; identity (`is`) checks whether they are the same object.