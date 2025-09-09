import tkinter as tk
from tkinter import messagebox, ttk

students = []


def add_student():
    # Validation
    try:
        student_id = int(entry_id.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ ID must be an integer.")
        return

    name = entry_name.get().strip()
    instructor = entry_instructor.get().strip()
    if not name.isalpha():
        messagebox.showerror("Invalid Input", "❌ Name must contain only letters.")
        return
    if not instructor.isalpha():
        messagebox.showerror("Invalid Input", "❌ Instructor must contain only letters.")
        return

    if not course_var.get():
        messagebox.showerror("Invalid Input", "❌ Please select a Course.")
        return
    if not mode_var.get():
        messagebox.showerror("Invalid Input", "❌ Please select Mode (Online/On Campus).")
        return
    if not timing_var.get():
        messagebox.showerror("Invalid Input", "❌ Please select Timings (Morning/Evening/Night).")
        return

    try:
        fee = int(entry_fee.get())
        fee = f"Rs {fee}"
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ Fee must be a number.")
        return

    student = {
        "ID": str(student_id),
        "Name": name,
        "Course": course_var.get(),
        "Mode": mode_var.get(),
        "Instructor": instructor,
        "Duration": entry_duration.get(),
        "Fee": fee,
        "Timings": timing_var.get()
    }

    students.append(student)
    refresh_table()
    clear_fields()
    messagebox.showinfo("Success", "✅ Student added successfully!")


def edit_student():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Student", "Please select a student to edit.")
        return

    index = int(tree.item(selected, "text"))
    student = students[index]

    # Update fields with same validation as add
    try:
        student_id = int(entry_id.get()) if entry_id.get() else int(student["ID"])
    except ValueError:
        messagebox.showerror("Invalid Input", "❌ ID must be an integer.")
        return

    name = entry_name.get().strip() or student["Name"]
    instructor = entry_instructor.get().strip() or student["Instructor"]
    if not name.isalpha():
        messagebox.showerror("Invalid Input", "❌ Name must contain only letters.")
        return
    if not instructor.isalpha():
        messagebox.showerror("Invalid Input", "❌ Instructor must contain only letters.")
        return

    fee_val = entry_fee.get().strip()
    if fee_val:
        try:
            fee = int(fee_val)
            fee = f"Rs {fee}"
        except ValueError:
            messagebox.showerror("Invalid Input", "❌ Fee must be a number.")
            return
    else:
        fee = student["Fee"]

    student.update({
        "ID": str(student_id),
        "Name": name,
        "Course": course_var.get() or student["Course"],
        "Mode": mode_var.get() or student["Mode"],
        "Instructor": instructor,
        "Duration": entry_duration.get() or student["Duration"],
        "Fee": fee,
        "Timings": timing_var.get() or student["Timings"]
    })

    refresh_table()
    clear_fields()
    messagebox.showinfo("Updated", "✅ Student details updated successfully!")


def delete_student():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Select Student", "Please select a student to delete.")
        return

    index = int(tree.item(selected, "text"))
    students.pop(index)
    refresh_table()
    messagebox.showinfo("Deleted", "✅ Student deleted successfully!")


def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for i, student in enumerate(students):
        tree.insert("", "end", text=i, values=(
            student["ID"], student["Name"], student["Course"], student["Mode"],
            student["Instructor"], student["Duration"], student["Fee"], student["Timings"]
        ))


def clear_fields():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_instructor.delete(0, tk.END)
    entry_duration.delete(0, tk.END)
    entry_fee.delete(0, tk.END)
    course_var.set("")
    mode_var.set("")
    timing_var.set("")


# --- UI Setup ---
root = tk.Tk()
root.title("🎓 Student Management System")
root.geometry("1050x700")
root.configure(bg="#eaf6f6")

# Heading Banner
header = tk.Label(root, text="🎓 STUDENT MANAGEMENT SYSTEM 🎓",
                  font=("Arial", 22, "bold"),
                  bg="#003366", fg="white", pady=15)
header.pack(fill="x")

sub_header = tk.Label(root, text="Development/Designing by (M.Masab Hassan)",
                      font=("Arial", 11, "italic"),
                      bg="#003366", fg="lightyellow", pady=5)
sub_header.pack(fill="x")

# Form Section
frame_form = tk.LabelFrame(root, text=" Student Information ",
                           font=("Arial", 12, "bold"),
                           bg="#f0faff", padx=15, pady=10, fg="#003366")
frame_form.pack(pady=10, padx=10, fill="x")

# ID
tk.Label(frame_form, text="ID", font=("Arial", 10, "bold"), bg="#f0faff").grid(row=0, column=0, padx=5, pady=5,
                                                                               sticky="w")
entry_id = tk.Entry(frame_form, width=30, font=("Arial", 10))
entry_id.grid(row=0, column=1, padx=5, pady=5)

# Name
tk.Label(frame_form, text="Name", font=("Arial", 10, "bold"), bg="#f0faff").grid(row=1, column=0, padx=5, pady=5,
                                                                                 sticky="w")
entry_name = tk.Entry(frame_form, width=30, font=("Arial", 10))
entry_name.grid(row=1, column=1, padx=5, pady=5)

# Course (OptionMenu)
tk.Label(frame_form, text="Course", font=("Arial", 10, "bold"), bg="#f0faff").grid(row=2, column=0, padx=5, pady=5,
                                                                                   sticky="w")
course_var = tk.StringVar()
course_menu = ttk.Combobox(frame_form, textvariable=course_var, values=["AI", "CCNA", "Language"], state="readonly",
                           width=28)
course_menu.grid(row=2, column=1, padx=5, pady=5)

# Mode (Radio Buttons)
tk.Label(frame_form, text="Mode", font=("Arial", 10, "bold"), bg="#f0faff").grid(row=3, column=0, padx=5, pady=5,
                                                                                 sticky="w")
mode_var = tk.StringVar()
tk.Radiobutton(frame_form, text="Online", variable=mode_var, value="Online", bg="#f0faff").grid(row=3, column=1,
                                                                                                sticky="w")
tk.Radiobutton(frame_form, text="On Campus", variable=mode_var, value="On Campus", bg="#f0faff").grid(row=3, column=1,
                                                                                                      padx=120,
                                                                                                      sticky="w")

# Instructor
tk.Label(frame_form, text="Instructor", font=("Arial", 10, "bold"), bg="#f0faff").grid(row=4, column=0, padx=5, pady=5,
                                                                                       sticky="w")
entry_instructor = tk.Entry(frame_form, width=30, font=("Arial", 10))
entry_instructor.grid(row=4, column=1, padx=5, pady=5)

# Duration
tk.Label(frame_form, text="Duration", font=("Arial", 10, "bold"), bg="#f0faff").grid(row=5, column=0, padx=5, pady=5,
                                                                                     sticky="w")
entry_duration = tk.Entry(frame_form, width=30, font=("Arial", 10))
entry_duration.grid(row=5, column=1, padx=5, pady=5)

# Fee
tk.Label(frame_form, text="Fee", font=("Arial", 10, "bold"), bg="#f0faff").grid(row=6, column=0, padx=5, pady=5,
                                                                                sticky="w")
entry_fee = tk.Entry(frame_form, width=30, font=("Arial", 10))
entry_fee.grid(row=6, column=1, padx=5, pady=5)

# Timings (Radio Buttons)
tk.Label(frame_form, text="Timings", font=("Arial", 10, "bold"), bg="#f0faff").grid(row=7, column=0, padx=5, pady=5,
                                                                                    sticky="w")
timing_var = tk.StringVar()
tk.Radiobutton(frame_form, text="Morning", variable=timing_var, value="Morning", bg="#f0faff").grid(row=7, column=1,
                                                                                                    sticky="w")
tk.Radiobutton(frame_form, text="Evening", variable=timing_var, value="Evening", bg="#f0faff").grid(row=7, column=1,
                                                                                                    padx=100,
                                                                                                    sticky="w")
tk.Radiobutton(frame_form, text="Night", variable=timing_var, value="Night", bg="#f0faff").grid(row=7, column=1,
                                                                                                padx=200, sticky="w")

# Buttons
btn_frame = tk.Frame(root, bg="#eaf6f6")
btn_frame.pack(pady=10)

style_btn = {"font": ("Arial", 10, "bold"), "width": 15, "height": 2, "bd": 0}

tk.Button(btn_frame, text="➕ Add Student", command=add_student, bg="#28a745", fg="white", **style_btn).grid(row=0,
                                                                                                            column=0,
                                                                                                            padx=10)
tk.Button(btn_frame, text="✏️ Edit Student", command=edit_student, bg="#ffc107", fg="black", **style_btn).grid(row=0,
                                                                                                               column=1,
                                                                                                               padx=10)
tk.Button(btn_frame, text="❌ Delete Student", command=delete_student, bg="#dc3545", fg="white", **style_btn).grid(row=0,
                                                                                                                  column=2,
                                                                                                                  padx=10)
tk.Button(btn_frame, text="🧹 Clear Fields", command=clear_fields, bg="#17a2b8", fg="white", **style_btn).grid(row=0,
                                                                                                              column=3,
                                                                                                              padx=10)

# Table
tree_frame = tk.Frame(root, bg="#eaf6f6")
tree_frame.pack(pady=20, padx=20, fill="both", expand=True)

columns = ["ID", "Name", "Course", "Mode", "Instructor", "Duration", "Fee", "Timings"]
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=12)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120, anchor="center")

tree.pack(fill="both", expand=True)

root.mainloop()
