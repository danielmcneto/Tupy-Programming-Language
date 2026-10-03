# Tupy

A lightweight, imperative scripting language interpreter built in Python from scratch, featuring manual program counter flow control and expression evaluation.

## Why?

I built this project to challenge my understanding of computer science fundamentals behind programming language engineering, implementing a custom DSL (Domain-Specific Language) without relying on any external libraries.

## Built With

* **Core Language:** Python 3.10+
* **Key Concepts:**
  * Flow control via manual Program Counter (`pc`) tracking
  * Stack-based evaluation for math expressions
  * Python Structural Pattern Matching (`match/case`)
  * Command-line argument parsing and file I/O

## Features

- [x] **Variable:** Supports global/local variable scoping (`x = 10`).
- [x] **Arithmetic & Comparison:** Evaluates `+`, `-`, `*`, `/`, and `>=` operations.
- [x] **Control (`while` / `end`):** Conditional looping with dynamic line jumping.
- [x] **Output (`print`):** Standard output for variables and expression evaluations.

## Codes Exemples

- **FizzBuzz:** 0 = normal | 1 = Fizz or Buzz | 2 = FizzBuzz
- **Math:** A simple calculus output
- **Condition:** Outputs if the variable is even or odd number

---

## Syntax Example

Here is a quick look at a program written in **Tupy**:


```text
n = 5
a = 1

while n >= 1
    a = a * 2
    n = n - 1
    print a
endwhile
```
Indentation is optional in Tupy and is used here solely for clarity.

---

## Getting Started

1. **Clone the repository:**

2. **Run an example script:**
   ```bash
   python3 interpreter.py Examples/ExampleName
   ```

---
