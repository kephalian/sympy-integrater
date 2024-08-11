from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
)
from PySide6.QtGui import QPalette, QColor
from PySide6.QtCore import Qt
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

class IntegrationApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up the layout
        self.layout = QVBoxLayout()
        
        # Set up the palette for light green background and black text
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('green'))
        palette.setColor(QPalette.WindowText, Qt.black)
        self.setPalette(palette)
        
        # Expression input
        self.expression_label = QLabel("Enter the expression:")
        self.expression_input = QLineEdit()
        self.expression_input.setPlaceholderText("e.g., x**2 + 3*x + 2, sin(x), exp(x)")
        self.expression_input.setStyleSheet("""
        font-size: 16px;
        background-color: lightblue;""") 
        self.layout.addWidget(self.expression_label)
        self.layout.addWidget(self.expression_input)
        
        # Lower limit input
        self.lower_limit_label = QLabel("Enter the lower limit:")
        self.lower_limit_input = QLineEdit()
        self.lower_limit_input.setPlaceholderText("e.g., 0")
        self.lower_limit_input.setStyleSheet("""
        font-size: 16px;
        background-color: lightblue;""") 
        self.layout.addWidget(self.lower_limit_label)
        self.layout.addWidget(self.lower_limit_input)
        
        # Upper limit input
        self.upper_limit_label = QLabel("Enter the upper limit:")
        self.upper_limit_input = QLineEdit()
        self.upper_limit_input.setStyleSheet("""
        font-size: 16px;
        background-color: lightblue;""")  # Adjust font size and background color
        self.upper_limit_input.setPlaceholderText("e.g., 1")
        self.layout.addWidget(self.upper_limit_label)
        self.layout.addWidget(self.upper_limit_input)
        
        # Button to calculate integral
        self.integrate_button = QPushButton("Calculate Integral")
        self.integrate_button.setStyleSheet("""
        font-size: 16px;
        color:blue;
        background-color: blue;""") 
        self.integrate_button.clicked.connect(self.calculate_integral)
        self.layout.addWidget(self.integrate_button)
        
        # Button to show plot
        self.plot_button = QPushButton("Plot Expression")
        self.plot_button.setStyleSheet("""
        font-size: 16px;
        color:blue;
        background-color: blue;""") 
        self.plot_button.clicked.connect(self.plot_expression)
        self.layout.addWidget(self.plot_button)
        
        # Output display
        self.output_display = QTextEdit()
        self.output_display.setStyleSheet("""
        font-size: 12px;
        font-weight:italics;
        color:blue;
        background-color: lightblue;""") 
        self.output_display.setReadOnly(True)
        self.layout.addWidget(self.output_display)
        
        # Set the layout and window title
        self.setLayout(self.layout)
        self.setWindowTitle("Integration Calculator")
    
    def calculate_integral(self):
        expression = self.expression_input.text()
        lower_limit = self.lower_limit_input.text()
        upper_limit = self.upper_limit_input.text()
        
        # Define the symbol x
        x = sp.Symbol('x')
        
        # Parse the expression
        try:
            f = sp.sympify(expression)
        except Exception as e:
            self.output_display.setText(f"Error in expression: {e}")
            return
        
        # Compute the indefinite integral
        try:
            indefinite_integral = sp.integrate(f, x)
            result_text = f"∫({expression}) dx = {indefinite_integral}\n\n"
        except Exception as e:
            self.output_display.setText(f"Error in indefinite integration: {e}")
            return
        
        # Compute the definite integral if limits are provided
        if lower_limit and upper_limit:
            try:
                lower_limit = float(lower_limit)
                upper_limit = float(upper_limit)
                definite_integral = sp.integrate(f, (x, lower_limit, upper_limit))
                result_text += f"∫({expression}) dx from {lower_limit} to {upper_limit} = {definite_integral}"
            except ValueError:
                result_text += "Error: Limits must be numbers."
            except Exception as e:
                result_text += f"Error in definite integration: {e}"
        else:
            result_text += "No definite integral calculated. Provide limits for a definite integral."
        
        # Display the results
        self.output_display.setText(result_text)
    
    def plot_expression(self):
        expression = self.expression_input.text()
        lower_limit = self.lower_limit_input.text()
        upper_limit = self.upper_limit_input.text()
        
        # Define the symbol x
        x = sp.Symbol('x')
        
        # Parse the expression
        try:
            f = sp.sympify(expression)
        except Exception as e:
            self.output_display.setText(f"Error in expression: {e}")
            return
        
        # Check if limits are provided and valid
        if lower_limit and upper_limit:
            try:
                lower_limit = float(lower_limit)
                upper_limit = float(upper_limit)
                
                # Generate x values
                x_vals = np.linspace(lower_limit, upper_limit, 400)
                # Generate y values by evaluating the expression
                y_vals = [float(f.subs(x, val)) for val in x_vals]
                
                # Plot the expression
                plt.figure()
                plt.plot(x_vals, y_vals, label=str(f))
                plt.title(f"Plot of {expression}")
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.legend()
                plt.grid(True)
                plt.show()
            except ValueError:
                self.output_display.setText("Error: Limits must be numbers.")
            except Exception as e:
                self.output_display.setText(f"Error in plotting: {e}")
        else:
            self.output_display.setText("Provide valid limits to plot the expression.")

# Running the application
if __name__ == "__main__":
    app = QApplication([])
    window = IntegrationApp()
    window.show()
    app.exec()