# Envíoclick: code-challenge

## Overview

This repository contains the scripts to solve the code challenge technical test. 

## Table of contents

1.  [Project Structure](#project-structure)
2.  [Installation](#installation)
2.  [Execution](#execution)
3.  [Examples](#examples)

## Project Structure
```
code-challenge/
├── README.md
├── main.py
├── problems
|       ├── problem_1.py
|       ├── problem_2.py
|       ├── utils
|             ├── operations.py
├── test_problem_1.py
└── test_problem_2.py
```

## Features

- Problem 1 consists of getting the frequency of a substring inside another subtring.
- Problem 2 consists of an array parser to order values that fulfill a set of conditions by priority.

## Installation

Make sure you have installed [Python 3.9+](https://www.python.org/downloads).

Clone this repository with the following command:

```sh
git clone git@github.com:Barbie-44/code-challenge.git
```

## Execution

To run python scripts, execute `main.py`. 
Default values are given, but parameters might be changed manually depending on the functionality.
```sh
python main.py
```
A message will be displayed to select the script to run
```sh
Enter a the number of a problem to solve (1 or 2): 
```

To run tests the script must be specified.
Example to run test cases for problem 1:
```sh
python test_problem_1.py
```

## Examples
### Problem 1.
target to find in paragraph
```sh
target = "logística"
```
paragraph to analyze
```sh
paragraph = (
    "La logística Digital es un concepto que surge de la integración "
    "de la logística tradicional y la era digital. Con el auge del correo "
    "electrónico y las descargas digitales reemplazando productos físicos, "
    "podríamos estar hablando de un golpe devastador para la industria de la "
    "logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de "
    "la logística ha introducido las innovaciones digitales."
)
```
output
```sh
4 ocurrencias encontradas.
```

### Problem 2.
criteria to match
```sh
criteria = [("weight", "=", 3)]
```
Original input array
```sh
data = [
    {
        "id": 12340,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 125,
        "priority": 2,
    },
    {
        "id": 12341,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 127,
        "priority": 4,
    },
    {
        "id": 12342,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 129,
        "priority": 6,
    },
    {
        "id": 12343,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 131,
        "priority": 0,
    },
    {
        "id": 12344,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 133,
        "priority": 0,
    },
    {
        "id": 12345,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 135,
        "priority": 0,
    },
    {
        "id": 12346,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 137,
        "priority": -1,
    },
    {
        "id": 12347,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 139,
        "priority": 0,
    },
    {
        "id": 12348,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 141,
        "priority": 2,
    },
    {
        "id": 12349,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 143,
        "priority": 0,
    },
    {
        "id": 12350,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 145,
        "priority": 0,
    },
    {
        "id": 12351,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 147,
        "priority": 10,
    },
    {
        "id": 12352,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 149,
        "priority": 0,
    },
    {
        "id": 12353,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 151,
        "priority": 0,
    },
    {
        "id": 12354,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 153,
        "priority": 0,
    },
    {
        "id": 12355,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 155,
        "priority": 0,
    },
    {
        "id": 12356,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 157,
        "priority": 0,
    },
    {
        "id": 12357,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 159,
        "priority": 0,
    },
    {
        "id": 12358,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 161,
        "priority": 0,
    },
    {
        "id": 12359,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 135,
        "priority": 0,
    },
    {
        "id": 12360,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 137,
        "priority": 0,
    },
    {
        "id": 12361,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 139,
        "priority": 0,
    },
    {
        "id": 12362,
        "weight": 3,
        "width": 3,
        "height": 1,
        "length": 10,
        "cost": 141,
        "priority": -2,
    },
    {
        "id": 12363,
        "weight": 3,
        "width": 3,
        "height": 1,
        "length": 10,
        "cost": 153,
        "priority": -2,
    },
    {
        "id": 12364,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 145,
        "priority": -6,
    },
    {
        "id": 12366,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 147,
        "priority": 0,
    },
    {
        "id": 12367,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 149,
        "priority": 0,
    },
    {
        "id": 12365,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 151,
        "priority": 2,
    },
    {
        "id": 12368,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 181,
        "priority": 2,
    },
    {
        "id": 12369,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 183,
        "priority": 0,
    },
]
```

output
```sh
[
    {
        "id": 12365,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 151,
        "priority": 2,
    },
    {
        "id": 12368,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 181,
        "priority": 2,
    },
    {
        "id": 12360,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 137,
        "priority": 0,
    },
    {
        "id": 12361,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 139,
        "priority": 0,
    },
    {
        "id": 12366,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 147,
        "priority": 0,
    },
    {
        "id": 12367,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 149,
        "priority": 0,
    },
    {
        "id": 12369,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 183,
        "priority": 0,
    },
    {
        "id": 12362,
        "weight": 3,
        "width": 3,
        "height": 1,
        "length": 10,
        "cost": 141,
        "priority": -2,
    },
    {
        "id": 12363,
        "weight": 3,
        "width": 3,
        "height": 1,
        "length": 10,
        "cost": 153,
        "priority": -2,
    },
    {
        "id": 12364,
        "weight": 3,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 145,
        "priority": -6,
    },
    {
        "id": 12340,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 125,
        "priority": 2,
    },
    {
        "id": 12341,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 127,
        "priority": 4,
    },
    {
        "id": 12342,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 129,
        "priority": 6,
    },
    {
        "id": 12343,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 131,
        "priority": 0,
    },
    {
        "id": 12344,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 133,
        "priority": 0,
    },
    {
        "id": 12345,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 135,
        "priority": 0,
    },
    {
        "id": 12346,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 137,
        "priority": -1,
    },
    {
        "id": 12347,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 139,
        "priority": 0,
    },
    {
        "id": 12348,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 141,
        "priority": 2,
    },
    {
        "id": 12349,
        "weight": 1,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 143,
        "priority": 0,
    },
    {
        "id": 12350,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 145,
        "priority": 0,
    },
    {
        "id": 12351,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 147,
        "priority": 10,
    },
    {
        "id": 12352,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 149,
        "priority": 0,
    },
    {
        "id": 12353,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 151,
        "priority": 0,
    },
    {
        "id": 12354,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 1,
        "cost": 153,
        "priority": 0,
    },
    {
        "id": 12355,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 155,
        "priority": 0,
    },
    {
        "id": 12356,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 157,
        "priority": 0,
    },
    {
        "id": 12357,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 159,
        "priority": 0,
    },
    {
        "id": 12358,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 161,
        "priority": 0,
    },
    {
        "id": 12359,
        "weight": 2,
        "width": 1,
        "height": 1,
        "length": 10,
        "cost": 135,
        "priority": 0,
    },
]
```