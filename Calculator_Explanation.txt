This Python script implements a simple graphical calculator using the Tkinter library.

1. Import:
- The script imports the tkinter module as tk to create the GUI.

2. Functions:
- append_to_display(value): Appends the given value (number/operator) to the current display text.
- clear_display(): Clears the calculator display.
- evaluate_expression(): Tries to evaluate the mathematical expression shown on the display using Python's eval function. If evaluation fails, shows "Invalid Input".
- on_key_press(event): Handles keyboard input. Allows numbers, operators, and special keys (Return to evaluate, Escape to clear).

3. GUI Setup:
- Creates the main window with title "Calculator" and a dark background color.
- Defines a StringVar() called display to hold the current input/expression.
- Adds a Label widget as the display area for showing current input or results.

4. Buttons:
- A set of buttons representing digits 0-9, decimal point, arithmetic operators (+, -, *, /), equals (=) button for evaluation, and 'A' button.
- Buttons are styled with colors and font.
- The '=' button triggers evaluate_expression function.
- The 'C' button (appears to be intended but not in current buttons list) triggers clear_display function.
- Other buttons append their respective text to the display when clicked.

5. Layout:
- The buttons are laid out in a grid.
- Row and column weights are configured to allow the buttons to expand and fill the window evenly.

6. Keyboard Bindings:
- The script binds any keypress to the on_key_press function to allow keyboard input.

7. Main Loop:
- The Tk event loop is started with root.mainloop() to display the window and interact with the user.

Note: The 'C' button for clear is defined in the if-else in the code but not included in the buttons list, so effectively no clear button is shown except clearing by pressing Escape key on keyboard.
