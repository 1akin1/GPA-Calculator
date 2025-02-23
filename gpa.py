from tkinter import *
from tkinter import messagebox

def submit():
    """Calculates the weighted average and displays it."""
    total_credit = 0
    total_weighted_score = 0

    try:
        num_courses = int(num_courses_entry.get())
        if num_courses <= 0:
            messagebox.showerror("Error", "Enter a valid number of courses!")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number of courses!")
        return

    for i in range(num_courses):
        try:
            credit = float(credit_entries[i].get())
            score = float(grade_entries[i].get())
            total_credit += credit
            total_weighted_score += credit * score
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
            return

    if total_credit == 0:
        messagebox.showerror("Error", "Total credits cannot be zero!")
        return

    # Calculate the average
    average = total_weighted_score / total_credit

    # Display the result
    result_label.config(text=f"Your GPA: {average:.2f}", fg="white", bg="#4CAF50")


def generate_fields():
    """Creates input fields based on the entered number of courses."""
    global grade_entries, credit_entries

    # Clear previous entries
    for widget in input_frame.winfo_children():
        widget.destroy()

    try:
        num_courses = int(num_courses_entry.get())
        if num_courses <= 0:
            messagebox.showerror("Error", "Enter a valid number of courses!")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number of courses!")
        return

    grade_entries = []
    credit_entries = []

    # Create headers
    Label(input_frame, text="Course No", font=('Arial', 12, 'bold'), bg="#eeeeee").grid(row=0, column=0, padx=10, pady=5)
    Label(input_frame, text="Grade", font=('Arial', 12, 'bold'), bg="#eeeeee").grid(row=0, column=1, padx=10, pady=5)
    Label(input_frame, text="Credit", font=('Arial', 12, 'bold'), bg="#eeeeee").grid(row=0, column=2, padx=10, pady=5)

    for i in range(num_courses):
        Label(input_frame, text=f"{i + 1}", font=('Arial', 12), bg="#eeeeee").grid(row=i + 1, column=0, padx=10, pady=5)
        
        grade_entry = Entry(input_frame, font=('Arial', 12))
        grade_entry.grid(row=i + 1, column=1, padx=10, pady=5)
        grade_entries.append(grade_entry)

        credit_entry = Entry(input_frame, font=('Arial', 12))
        credit_entry.grid(row=i + 1, column=2, padx=10, pady=5)
        credit_entries.append(credit_entry)

    # Submit button
    submit_button = Button(input_frame, text="Calculate GPA", command=submit, font=('Arial', 14, 'bold'), bg="#007BFF", fg="white", width=15)
    submit_button.grid(row=num_courses + 1, column=0, columnspan=3, pady=15)


# Create the main window
window = Tk()
window.title("GPA Calculator")
window.geometry("600x600")
window.configure(bg="#f8f9fa")

# Title label
Label(window, text="GPA Calculator", font=('Arial', 20, 'bold'), fg="black", bg="#f8f9fa").pack(pady=10)

# Entry for number of courses
Label(window, text="Enter number of courses:", font=('Arial', 14), bg="#f8f9fa").pack(pady=5)
num_courses_entry = Entry(window, font=('Arial', 14), width=10, justify="center")
num_courses_entry.pack(pady=5)

# Generate fields button
Button(window, text="Generate Fields", command=generate_fields, font=('Arial', 14, 'bold'), bg="#28a745", fg="white", width=15).pack(pady=5)

# Frame to hold input fields
input_frame = Frame(window, bg="#eeeeee", bd=2, relief=SOLID)
input_frame.pack(pady=10, padx=20, fill="both", expand=True)

# Result label
result_label = Label(window, text="", font=('Arial', 16, 'bold'), bg="#f8f9fa", fg="black", pady=10)
result_label.pack()

window.mainloop()
