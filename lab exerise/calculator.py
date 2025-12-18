import tkinter as tk

def on_click(event):
    """Handles button clicks."""
    text = event.widget.cget("text")
    if text == "=":
        try:
            # Evaluate the expression in the display
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        # Clear the display
        screen.set("")
    else:
        # Append the clicked button text to the current expression
        screen.set(screen.get() + text)

# --- Set up the main window ---
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400") # Set a default window size

# Variable to hold the screen's text
screen = tk.StringVar()

# --- Create the display entry (read-only) ---
entry = tk.Entry(root, textvar=screen, font="lucida 20 bold", bd=5, relief=tk.SUNKEN, justify='right')
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# --- Create button frames ---
button_frame = tk.Frame(root)
button_frame.pack()

# Define the buttons layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]
row_val = 0
col_val = 0

for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font="lucida 15 bold", padx=20, pady=20, bd=5)
    button.grid(row=row_val, column=col_val)
    button.bind('<Button-1>', on_click) # Bind the left mouse click event to the on_click function
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# --- Start the GUI event loop ---
root.mainloop()
