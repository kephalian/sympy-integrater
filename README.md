# sympy-integrater
GUI Graphical front end that automatically performs integration on supplied expression and graphs the expression 

# Integration Calculator with PySide6 and Sympy

This repository contains a PySide6-based GUI application for calculating the indefinite and definite integrals of mathematical expressions. The application supports polynomials, trigonometric functions, exponential functions, and allows users to plot these expressions within specified limits.

# A stand alone EXE program version is also available under release for Windows.

# Many Antivirus will flag this open source project as malware or suspected malware as this is an unsigned executable and I refuse to pay the software mobsters any money for buying a code signing certificate. The source code is hosted here for anyone to peruse and judge.


## Features

- **Indefinite Integral Calculation**: Compute and display the indefinite integral of the input expression.
- **Definite Integral Calculation**: Calculate the definite integral if limits are provided by the user.
- **Expression Plotting**: Visualize the input expression within user-specified limits using `matplotlib`.
- **User-Friendly Interface**: The application features a light green background with black text for improved readability.

## Prerequisites

- **Python 3.x**
- Python Packages:
  - `PySide6`
  - `sympy`
  - `matplotlib`
  - `numpy`

You can install the required packages with:

```bash
pip install PySide6 sympy matplotlib numpy
```

How to Run the Application

simplest way is to download the EXE file in Windows
and double click to launch.

You can also Clone the repository 
git https://github.com/kephalian/sympy-integrater

cd sympy-integrater



Run the application:

python sympy-integrater.py

Usage:Enter the expression you wish to integrate in the provided text field (e.g., x**2 + 3*x + 2, sin(x), exp(x)).

Specify the limits for definite integration, if desired.
Click "Calculate Integral" to display the indefinite or definite integral.
Click "Plot Expression" to visualize the function within the specified limits.
Example Expressions
Polynomial: x**2 + 3*x + 2Trigonometric: sin(x)Exponential: exp(x)

License LGPL3
Attribution mandatory and derivative works must be released under same license and open source LGPL3 only.

