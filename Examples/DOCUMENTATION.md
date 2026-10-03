# Tupy

**Tupy**

It uses a minimal syntax with variables, arithmetic operations, comparisons, `if` statements, `while` loops, and output through `print`.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Syntax](#syntax)
  - [Variables](#variables)
  - [Numbers](#numbers)
  - [Arithmetic Operators](#arithmetic-operators)
  - [Comparison Operators](#comparison-operators)
  - [Modulo](#modulo)
- [Output](#output)
  - [Printing Numbers](#printing-numbers)
  - [Printing Text](#printing-text)
- [Control Flow](#control-flow)
  - [If Statements](#if-statements)
  - [While Loops](#while-loops)
- [Comments](#comments)
- [Examples](#examples)
  - [Basic Arithmetic](#basic-arithmetic)
  - [Counting](#counting)
  - [FizzBuzz](#fizzbuzz)
- [Data Types](#data-types)
- [Operators Reference](#operators-reference)
- [Limitations](#limitations)

---

# Getting Started

Tupy programs are executed from a file.

For example, a file named:

```text
program.tupy
```

can be executed by the interpreter.

The interpreter reads the source code line by line and executes each instruction.

Blank lines are ignored.

---

# Syntax

## Variables

Variables are created using the `=` operator.

```tupy
x = 10
y = 20
```

Variables can be used in expressions:

```tupy
x = 10
y = 20
result = x + y

print result
```

Output:

```text
30
```

Variables can also be strings:

```tupy
x = 'Hello, '
y = 'World!'
result = x + y

print result
```

Output:

```text
Hello, World!
```

Tupy stores variables internally by name. If a variable does not exist, its value is `0`. 

---

## Numbers

Tupy currently supports integer values.

```tupy
x = 42
y = -10
z = 0
```

Negative integers are supported.

---

# Arithmetic Operators

Tupy supports the following arithmetic operators:

| Operator | Operation | Example |
|---|---|---|
| `+` | Addition | `5 + 3` |
| `-` | Subtraction | `5 - 3` |
| `*` | Multiplication | `5 * 3` |
| `/` | Integer division | `5 / 2` |
| `%` | Modulo | `5 % 2` |

### Example

```tupy
a = 10
b = 3

print a + b
print a - b
print a * b
print a / b
print a % b
```

Output:

```text
13
7
30
3
1
```

Division is converted to an integer using `int()`, so fractional results are discarded.

---

# Comparison Operators

Comparisons return either:

```text
1
```

for **true**, or:

```text
0
```

for **false**.

Tupy supports:

| Operator | Meaning |
|---|---|
| `==` | Equal |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |
| `>` | Greater than |
| `<` | Less than |

Example:

```tupy
x = 10

print x == 10
print x > 5
print x < 5
```

Output:

```text
1
1
0
```

Comparisons are implemented as numeric `1`/`0` values.

---

# Modulo

The `%` operator returns the remainder of a division.

```tupy
print 10 % 3
```

Output:

```text
1
```

Modulo is particularly useful for checking whether numbers are divisible by another number.

For example:

```tupy
x = 15
result = x % 3

print result
```

Output:

```text
0
```

---

# Output

## Printing Numbers

Use `print` followed by an expression:

```tupy
x = 42

print x
```

Output:

```text
42
```

Expressions can also be printed directly:

```tupy
print 10 + 5
```

Output:

```text
15
```

The interpreter evaluates the expression before printing it.

---

## Printing Text

Text can be printed using single quotes:

```tupy
print 'Hello, Tupy!'
```

Output:

```text
Hello, Tupy!
```

The interpreter detects text inside single quotes and removes the quotes before printing.

For example:

```tupy
print 'Fizz'
print 'Buzz'
print 'FizzBuzz'
```

Output:

```text
Fizz
Buzz
FizzBuzz
```

---

# Control Flow

## If Statements

Tupy supports conditional execution using `if`.

```tupy
x = 10

if x > 5
    print 'x is greater than 5'
endif
```

The expression after `if` is evaluated.

If its value is not `0`, the block is executed.

If its value is `0`, the interpreter skips the block until `endif`.

### Example

```tupy
x = 10

if x == 10
    print 'Correct!'
endif
```

Output:

```text
Correct!
```

---

## While Loops

Tupy supports `while` loops.

```tupy
x = 1

while x <= 5
    print x
    x = x + 1
endwhile
```

Output:

```text
1
2
3
4
5
```

The condition is evaluated every time the loop is reached.

If the condition is non-zero, the loop body executes.

If the condition is `0`, the interpreter searches for the corresponding `endwhile` and continues after it.

---

# FizzBuzz

FizzBuzz can be implemented using Tupy's arithmetic, modulo, variables, comparisons, `if`, and `while`.

```tupy
n = 1

while n <= 100

    r3 = n % 3
    r5 = n % 5

    fizz = r3 == 0
    buzz = r5 == 0

    code = fizz * 2 + buzz

    if code == 3
        print 'FizzBuzz'
    endif

    if code == 2
        print 'Fizz'
    endif

    if code == 1
        print 'Buzz'
    endif

    if code == 0
        print n
    endif

    n = n + 1

endwhile
```

This works because comparisons produce `1` or `0`.

```text
fizz = 1  → divisible by 3
fizz = 0  → not divisible by 3

buzz = 1  → divisible by 5
buzz = 0  → not divisible by 5
```

The resulting code is:

| `fizz` | `buzz` | `code` | Meaning |
|---:|---:|---:|---|
| 0 | 0 | 0 | Number |
| 0 | 1 | 1 | Buzz |
| 1 | 0 | 2 | Fizz |
| 1 | 1 | 3 | FizzBuzz |

---

# Data Types

Tupy currently has two practical forms of values:

### Integers

```tupy
x = 123
```

Variables and expressions are primarily handled as integers.

### Text

Text can be passed directly to `print` using single quotes:

```tupy
print 'Hello'
```

Text is currently handled specially by the `print` instruction rather than as a general-purpose string value.

---

# Operators Reference

## Arithmetic

```text
+    Addition
-    Subtraction
*    Multiplication
/    Integer division
%    Modulo
```

## Comparison

```text
==   Equal
>=   Greater than or equal
<=   Less than or equal
>    Greater than
<    Less than
```

---

# Program Structure

A typical Tupy program can combine variables, calculations, conditions, loops, and output.

Example:

```tupy
counter = 1

while counter <= 10

    if counter % 2 == 0
        print 'Even'
    endif

    if counter % 2 != 0
        print 'Odd'
    endif

    counter = counter + 1

endwhile
```

The language is intentionally small: programs are interpreted sequentially, and the interpreter maintains a simple variable table and program counter.

---

# Limitations

Tupy is currently a minimal language and does not provide many features found in larger programming languages.

The current interpreter does **not** implement:

- Functions
- Arrays
- Objects
- User-defined types
- `else`
- Boolean keywords such as `true` and `false`
- Logical operators such as `and` and `or`
- String concatenation
- Floating-point numbers
- Input from the user
- A standard library
- Error handling
- Comments

The expression evaluator works by splitting expressions into whitespace-separated tokens, so operators and operands should be separated by spaces.

For example:

```tupy
x = 10 + 5
```

is valid, while:

```tupy
x = 10+5
```

is not interpreted in the same way by the current evaluator.

---

# Design Philosophy

Tupy is built around a simple idea:

> **A programming language should be easy to understand, easy to interpret, and easy to extend.**

Its syntax intentionally avoids complex features and focuses on a small set of fundamental programming concepts:

```text
Variables
    ↓
Expressions
    ↓
Conditions
    ↓
Loops
    ↓
Output
```

Despite its small size, these features are enough to implement basic algorithms such as counters, mathematical calculations, conditional programs, and FizzBuzz.

---

# Quick Reference

```tupy
# Variables
x = 10

# Arithmetic
x = 10 + 5
x = x * 2

# Comparison
if x > 10
    print 'Greater'
endif

# Loop
while x > 0
    print x
    x = x - 1
endwhile

# Text
print 'Hello, Tupy!'

# Number
print x

# Modulo
remainder = x % 2
```

---

## Tupy at a Glance

| Feature | Supported |
|---|---|
| Variables | Yes |
| Integers | Yes |
| Addition | Yes |
| Subtraction | Yes |
| Multiplication | Yes |
| Division | Yes |
| Modulo | Yes |
| Comparisons | Yes |
| `if` | Yes |
| `while` | Yes |
| Number output | Yes |
| Text output | Yes |
| Strings as variables | Yes |
| Functions | No |
| Arrays | No |
| User input | No |
| `else` | No |
| Logical operators | No |