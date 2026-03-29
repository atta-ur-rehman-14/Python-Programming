import tkinter as tk
from tkinter import messagebox, ttk

from storage import load_data, save_data


class ClassManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Class Management System")
        self.root.geometry("1150x720")
        self.root.minsize(980, 620)

        self.data = load_data()

        self.student_form_mode = None
        self.class_form_mode = None
        self.selected_student_id = None
        self.selected_class_id = None
        self.selected_enrollment_id = None

        self.build_styles()
        self.build_ui()
        self.refresh_all()

    def build_styles(self):
        style = ttk.Style()
        style.theme_use("clam")

        self.root.configure(bg="#f2f6fb")

        style.configure("TNotebook", background="#f2f6fb", borderwidth=0)
        style.configure("TNotebook.Tab", padding=(16, 10), font=("Segoe UI", 10, "bold"))
        style.configure("Card.TFrame", background="#ffffff", relief="flat")
        style.configure("Header.TLabel", background="#ffffff", font=("Segoe UI", 16, "bold"), foreground="#1f2a44")
        style.configure("SubHeader.TLabel", background="#ffffff", font=("Segoe UI", 10), foreground="#56627a")
        style.configure("Metric.TLabel", background="#ffffff", font=("Segoe UI", 20, "bold"), foreground="#10375c")
        style.configure("MetricTitle.TLabel", background="#ffffff", font=("Segoe UI", 10, "bold"), foreground="#5e6c84")
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        style.configure("TButton", font=("Segoe UI", 10), padding=8)

    def build_ui(self):
        container = ttk.Frame(self.root, padding=16)
        container.pack(fill="both", expand=True)

        title = ttk.Label(container, text="Class Management System", style="Header.TLabel")
        title.pack(anchor="w")

        subtitle = ttk.Label(
            container,
            text="Manage students, courses, enrollments, and attendance in one place.",
            style="SubHeader.TLabel",
        )
        subtitle.pack(anchor="w", pady=(4, 12))

        self.notebook = ttk.Notebook(container)
        self.notebook.pack(fill="both", expand=True)

        self.dashboard_tab = ttk.Frame(self.notebook, padding=12, style="Card.TFrame")
        self.students_tab = ttk.Frame(self.notebook, padding=12, style="Card.TFrame")
        self.classes_tab = ttk.Frame(self.notebook, padding=12, style="Card.TFrame")
        self.enrollment_tab = ttk.Frame(self.notebook, padding=12, style="Card.TFrame")

        self.notebook.add(self.dashboard_tab, text="Dashboard")
        self.notebook.add(self.students_tab, text="Students")
        self.notebook.add(self.classes_tab, text="Classes")
        self.notebook.add(self.enrollment_tab, text="Enrollments")

        self.build_dashboard_tab()
        self.build_students_tab()
        self.build_classes_tab()
        self.build_enrollment_tab()

    def build_dashboard_tab(self):
        metric_row = ttk.Frame(self.dashboard_tab, style="Card.TFrame")
        metric_row.pack(fill="x", pady=(0, 16))

        self.student_metric = self.create_metric_card(metric_row, "Total Students")
        self.class_metric = self.create_metric_card(metric_row, "Total Classes")
        self.enrollment_metric = self.create_metric_card(metric_row, "Total Enrollments")
        self.attendance_metric = self.create_metric_card(metric_row, "Present Rate")

        for card in (
            self.student_metric["frame"],
            self.class_metric["frame"],
            self.enrollment_metric["frame"],
            self.attendance_metric["frame"],
        ):
            card.pack(side="left", fill="both", expand=True, padx=6)

        bottom = ttk.Frame(self.dashboard_tab, style="Card.TFrame")
        bottom.pack(fill="both", expand=True)
        bottom.columnconfigure(0, weight=1)
        bottom.columnconfigure(1, weight=1)

        left = ttk.Frame(bottom, padding=14, style="Card.TFrame")
        right = ttk.Frame(bottom, padding=14, style="Card.TFrame")
        left.grid(row=0, column=0, sticky="nsew", padx=(0, 8))
        right.grid(row=0, column=1, sticky="nsew", padx=(8, 0))

        ttk.Label(left, text="Recent Students", style="Header.TLabel").pack(anchor="w")
        self.recent_students = tk.Listbox(left, height=12, font=("Segoe UI", 10), borderwidth=0, highlightthickness=0)
        self.recent_students.pack(fill="both", expand=True, pady=(12, 0))

        ttk.Label(right, text="Class Overview", style="Header.TLabel").pack(anchor="w")
        self.class_overview = tk.Listbox(right, height=12, font=("Segoe UI", 10), borderwidth=0, highlightthickness=0)
        self.class_overview.pack(fill="both", expand=True, pady=(12, 0))

    def create_metric_card(self, parent, title):
        frame = ttk.Frame(parent, padding=16, style="Card.TFrame")
        title_label = ttk.Label(frame, text=title, style="MetricTitle.TLabel")
        value_label = ttk.Label(frame, text="0", style="Metric.TLabel")
        title_label.pack(anchor="w")
        value_label.pack(anchor="w", pady=(8, 0))
        return {"frame": frame, "value": value_label}

    def build_students_tab(self):
        wrapper = ttk.Frame(self.students_tab, style="Card.TFrame")
        wrapper.pack(fill="both", expand=True)
        wrapper.columnconfigure(0, weight=2)
        wrapper.columnconfigure(1, weight=1)

        left = ttk.Frame(wrapper, padding=(0, 0, 12, 0), style="Card.TFrame")
        right = ttk.Frame(wrapper, padding=(12, 0, 0, 0), style="Card.TFrame")
        left.grid(row=0, column=0, sticky="nsew")
        right.grid(row=0, column=1, sticky="nsew")
        left.rowconfigure(1, weight=1)

        ttk.Label(left, text="Student Records", style="Header.TLabel").grid(row=0, column=0, sticky="w")

        columns = ("id", "name", "age", "email")
        self.student_tree = ttk.Treeview(left, columns=columns, show="headings", height=16)
        for column, title, width in (
            ("id", "ID", 60),
            ("name", "Name", 180),
            ("age", "Age", 80),
            ("email", "Email", 220),
        ):
            self.student_tree.heading(column, text=title)
            self.student_tree.column(column, width=width, anchor="center")
        self.student_tree.grid(row=1, column=0, sticky="nsew", pady=(12, 0))
        self.student_tree.bind("<<TreeviewSelect>>", self.on_student_select)

        student_buttons = ttk.Frame(left, style="Card.TFrame")
        student_buttons.grid(row=2, column=0, sticky="ew", pady=(12, 0))
        ttk.Button(student_buttons, text="New Student", command=self.prepare_new_student).pack(side="left", padx=(0, 8))
        ttk.Button(student_buttons, text="Delete Student", command=self.delete_student).pack(side="left")

        self.build_student_form(right)

    def build_student_form(self, parent):
        ttk.Label(parent, text="Student Form", style="Header.TLabel").pack(anchor="w")
        ttk.Label(parent, text="Create or update a student profile.", style="SubHeader.TLabel").pack(anchor="w", pady=(4, 14))

        self.student_name_var = tk.StringVar()
        self.student_age_var = tk.StringVar()
        self.student_email_var = tk.StringVar()

        self.create_labeled_entry(parent, "Name", self.student_name_var)
        self.create_labeled_entry(parent, "Age", self.student_age_var)
        self.create_labeled_entry(parent, "Email", self.student_email_var)

        button_row = ttk.Frame(parent, style="Card.TFrame")
        button_row.pack(fill="x", pady=(16, 0))
        ttk.Button(button_row, text="Save Student", command=self.save_student).pack(side="left", padx=(0, 8))
        ttk.Button(button_row, text="Clear", command=self.clear_student_form).pack(side="left")

    def build_classes_tab(self):
        wrapper = ttk.Frame(self.classes_tab, style="Card.TFrame")
        wrapper.pack(fill="both", expand=True)
        wrapper.columnconfigure(0, weight=2)
        wrapper.columnconfigure(1, weight=1)

        left = ttk.Frame(wrapper, padding=(0, 0, 12, 0), style="Card.TFrame")
        right = ttk.Frame(wrapper, padding=(12, 0, 0, 0), style="Card.TFrame")
        left.grid(row=0, column=0, sticky="nsew")
        right.grid(row=0, column=1, sticky="nsew")
        left.rowconfigure(1, weight=1)

        ttk.Label(left, text="Class Records", style="Header.TLabel").grid(row=0, column=0, sticky="w")

        columns = ("id", "title", "teacher", "schedule")
        self.class_tree = ttk.Treeview(left, columns=columns, show="headings", height=16)
        for column, title, width in (
            ("id", "ID", 60),
            ("title", "Class Title", 180),
            ("teacher", "Teacher", 180),
            ("schedule", "Schedule", 200),
        ):
            self.class_tree.heading(column, text=title)
            self.class_tree.column(column, width=width, anchor="center")
        self.class_tree.grid(row=1, column=0, sticky="nsew", pady=(12, 0))
        self.class_tree.bind("<<TreeviewSelect>>", self.on_class_select)

        class_buttons = ttk.Frame(left, style="Card.TFrame")
        class_buttons.grid(row=2, column=0, sticky="ew", pady=(12, 0))
        ttk.Button(class_buttons, text="New Class", command=self.prepare_new_class).pack(side="left", padx=(0, 8))
        ttk.Button(class_buttons, text="Delete Class", command=self.delete_class).pack(side="left")

        self.build_class_form(right)

    def build_class_form(self, parent):
        ttk.Label(parent, text="Class Form", style="Header.TLabel").pack(anchor="w")
        ttk.Label(parent, text="Set up a course and assign a teacher.", style="SubHeader.TLabel").pack(anchor="w", pady=(4, 14))

        self.class_title_var = tk.StringVar()
        self.class_teacher_var = tk.StringVar()
        self.class_schedule_var = tk.StringVar()

        self.create_labeled_entry(parent, "Class Title", self.class_title_var)
        self.create_labeled_entry(parent, "Teacher", self.class_teacher_var)
        self.create_labeled_entry(parent, "Schedule", self.class_schedule_var)

        button_row = ttk.Frame(parent, style="Card.TFrame")
        button_row.pack(fill="x", pady=(16, 0))
        ttk.Button(button_row, text="Save Class", command=self.save_class).pack(side="left", padx=(0, 8))
        ttk.Button(button_row, text="Clear", command=self.clear_class_form).pack(side="left")

    def build_enrollment_tab(self):
        top = ttk.Frame(self.enrollment_tab, style="Card.TFrame")
        top.pack(fill="x", pady=(0, 16))

        ttk.Label(top, text="Enrollment Management", style="Header.TLabel").grid(row=0, column=0, columnspan=4, sticky="w")
        ttk.Label(top, text="Enroll students in classes and mark attendance.", style="SubHeader.TLabel").grid(
            row=1, column=0, columnspan=4, sticky="w", pady=(4, 12)
        )

        self.enrollment_student_var = tk.StringVar()
        self.enrollment_class_var = tk.StringVar()
        self.attendance_var = tk.StringVar(value="Present")

        ttk.Label(top, text="Student").grid(row=2, column=0, sticky="w", padx=(0, 10))
        ttk.Label(top, text="Class").grid(row=2, column=1, sticky="w", padx=(0, 10))
        ttk.Label(top, text="Attendance").grid(row=2, column=2, sticky="w", padx=(0, 10))

        self.student_combo = ttk.Combobox(top, textvariable=self.enrollment_student_var, state="readonly", width=24)
        self.class_combo = ttk.Combobox(top, textvariable=self.enrollment_class_var, state="readonly", width=24)
        self.attendance_combo = ttk.Combobox(
            top, textvariable=self.attendance_var, state="readonly", width=16, values=["Present", "Absent"]
        )

        self.student_combo.grid(row=3, column=0, sticky="ew", padx=(0, 10))
        self.class_combo.grid(row=3, column=1, sticky="ew", padx=(0, 10))
        self.attendance_combo.grid(row=3, column=2, sticky="ew", padx=(0, 10))

        action_row = ttk.Frame(top, style="Card.TFrame")
        action_row.grid(row=3, column=3, sticky="e")
        ttk.Button(action_row, text="Save Enrollment", command=self.save_enrollment).pack(side="left", padx=(0, 8))
        ttk.Button(action_row, text="Delete Enrollment", command=self.delete_enrollment).pack(side="left")

        table_frame = ttk.Frame(self.enrollment_tab, style="Card.TFrame")
        table_frame.pack(fill="both", expand=True)

        columns = ("id", "student", "class", "attendance")
        self.enrollment_tree = ttk.Treeview(table_frame, columns=columns, show="headings")
        for column, title, width in (
            ("id", "ID", 60),
            ("student", "Student", 240),
            ("class", "Class", 240),
            ("attendance", "Attendance", 120),
        ):
            self.enrollment_tree.heading(column, text=title)
            self.enrollment_tree.column(column, width=width, anchor="center")
        self.enrollment_tree.pack(fill="both", expand=True)
        self.enrollment_tree.bind("<<TreeviewSelect>>", self.on_enrollment_select)

    def create_labeled_entry(self, parent, label_text, variable):
        ttk.Label(parent, text=label_text).pack(anchor="w", pady=(0, 4))
        entry = ttk.Entry(parent, textvariable=variable, width=32)
        entry.pack(fill="x", pady=(0, 12))
        return entry

    def refresh_all(self):
        self.refresh_students()
        self.refresh_classes()
        self.refresh_enrollments()
        self.refresh_dashboard()
        self.refresh_comboboxes()

    def refresh_students(self):
        self.student_tree.delete(*self.student_tree.get_children())
        for student in self.data["students"]:
            self.student_tree.insert("", "end", iid=str(student["id"]), values=(
                student["id"],
                student["name"],
                student["age"],
                student["email"],
            ))

    def refresh_classes(self):
        self.class_tree.delete(*self.class_tree.get_children())
        for class_item in self.data["classes"]:
            self.class_tree.insert("", "end", iid=str(class_item["id"]), values=(
                class_item["id"],
                class_item["title"],
                class_item["teacher"],
                class_item["schedule"],
            ))

    def refresh_enrollments(self):
        self.enrollment_tree.delete(*self.enrollment_tree.get_children())
        for enrollment in self.data["enrollments"]:
            student = self.find_by_id("students", enrollment["student_id"])
            class_item = self.find_by_id("classes", enrollment["class_id"])
            if not student or not class_item:
                continue
            self.enrollment_tree.insert("", "end", iid=str(enrollment["id"]), values=(
                enrollment["id"],
                student["name"],
                class_item["title"],
                enrollment["attendance"],
            ))

    def refresh_dashboard(self):
        students = self.data["students"]
        classes = self.data["classes"]
        enrollments = self.data["enrollments"]

        present_count = sum(1 for item in enrollments if item["attendance"] == "Present")
        attendance_rate = f"{(present_count / len(enrollments) * 100):.0f}%" if enrollments else "0%"

        self.student_metric["value"].config(text=str(len(students)))
        self.class_metric["value"].config(text=str(len(classes)))
        self.enrollment_metric["value"].config(text=str(len(enrollments)))
        self.attendance_metric["value"].config(text=attendance_rate)

        self.recent_students.delete(0, tk.END)
        for student in students[-8:][::-1]:
            self.recent_students.insert(tk.END, f"{student['name']} | Age: {student['age']} | {student['email']}")

        self.class_overview.delete(0, tk.END)
        for class_item in classes:
            total = sum(1 for item in enrollments if item["class_id"] == class_item["id"])
            self.class_overview.insert(tk.END, f"{class_item['title']} | Teacher: {class_item['teacher']} | Enrolled: {total}")

    def refresh_comboboxes(self):
        student_values = [f"{item['id']} - {item['name']}" for item in self.data["students"]]
        class_values = [f"{item['id']} - {item['title']}" for item in self.data["classes"]]
        self.student_combo["values"] = student_values
        self.class_combo["values"] = class_values

    def save_student(self):
        name = self.student_name_var.get().strip()
        age_text = self.student_age_var.get().strip()
        email = self.student_email_var.get().strip()

        if not name or not age_text or not email:
            messagebox.showerror("Missing Data", "Please complete all student fields.")
            return

        if not age_text.isdigit():
            messagebox.showerror("Invalid Age", "Age must be a whole number.")
            return

        if self.student_form_mode == "edit" and self.selected_student_id is not None:
            student = self.find_by_id("students", self.selected_student_id)
            if not student:
                return
            student["name"] = name
            student["age"] = int(age_text)
            student["email"] = email
        else:
            new_id = self.data["next_ids"]["student"]
            self.data["students"].append({
                "id": new_id,
                "name": name,
                "age": int(age_text),
                "email": email,
            })
            self.data["next_ids"]["student"] += 1

        self.persist_and_refresh()
        self.clear_student_form()

    def save_class(self):
        title = self.class_title_var.get().strip()
        teacher = self.class_teacher_var.get().strip()
        schedule = self.class_schedule_var.get().strip()

        if not title or not teacher or not schedule:
            messagebox.showerror("Missing Data", "Please complete all class fields.")
            return

        if self.class_form_mode == "edit" and self.selected_class_id is not None:
            class_item = self.find_by_id("classes", self.selected_class_id)
            if not class_item:
                return
            class_item["title"] = title
            class_item["teacher"] = teacher
            class_item["schedule"] = schedule
        else:
            new_id = self.data["next_ids"]["class"]
            self.data["classes"].append({
                "id": new_id,
                "title": title,
                "teacher": teacher,
                "schedule": schedule,
            })
            self.data["next_ids"]["class"] += 1

        self.persist_and_refresh()
        self.clear_class_form()

    def save_enrollment(self):
        student_value = self.enrollment_student_var.get().strip()
        class_value = self.enrollment_class_var.get().strip()
        attendance = self.attendance_var.get().strip()

        if not student_value or not class_value:
            messagebox.showerror("Missing Data", "Please select a student and a class.")
            return

        student_id = int(student_value.split(" - ", 1)[0])
        class_id = int(class_value.split(" - ", 1)[0])

        if self.selected_enrollment_id is not None:
            enrollment = self.find_by_id("enrollments", self.selected_enrollment_id)
            if not enrollment:
                return
            enrollment["student_id"] = student_id
            enrollment["class_id"] = class_id
            enrollment["attendance"] = attendance
        else:
            duplicate = next(
                (
                    item for item in self.data["enrollments"]
                    if item["student_id"] == student_id and item["class_id"] == class_id
                ),
                None,
            )
            if duplicate:
                messagebox.showerror("Duplicate Enrollment", "This student is already enrolled in the selected class.")
                return

            new_id = self.data["next_ids"]["enrollment"]
            self.data["enrollments"].append({
                "id": new_id,
                "student_id": student_id,
                "class_id": class_id,
                "attendance": attendance,
            })
            self.data["next_ids"]["enrollment"] += 1

        self.persist_and_refresh()
        self.clear_enrollment_form()

    def delete_student(self):
        if self.selected_student_id is None:
            messagebox.showinfo("Select Student", "Please select a student to delete.")
            return

        self.data["students"] = [item for item in self.data["students"] if item["id"] != self.selected_student_id]
        self.data["enrollments"] = [item for item in self.data["enrollments"] if item["student_id"] != self.selected_student_id]
        self.persist_and_refresh()
        self.clear_student_form()
        self.clear_enrollment_form()

    def delete_class(self):
        if self.selected_class_id is None:
            messagebox.showinfo("Select Class", "Please select a class to delete.")
            return

        self.data["classes"] = [item for item in self.data["classes"] if item["id"] != self.selected_class_id]
        self.data["enrollments"] = [item for item in self.data["enrollments"] if item["class_id"] != self.selected_class_id]
        self.persist_and_refresh()
        self.clear_class_form()
        self.clear_enrollment_form()

    def delete_enrollment(self):
        if self.selected_enrollment_id is None:
            messagebox.showinfo("Select Enrollment", "Please select an enrollment to delete.")
            return

        self.data["enrollments"] = [item for item in self.data["enrollments"] if item["id"] != self.selected_enrollment_id]
        self.persist_and_refresh()
        self.clear_enrollment_form()

    def on_student_select(self, _event):
        selected = self.student_tree.selection()
        if not selected:
            return

        self.selected_student_id = int(selected[0])
        student = self.find_by_id("students", self.selected_student_id)
        if not student:
            return

        self.student_form_mode = "edit"
        self.student_name_var.set(student["name"])
        self.student_age_var.set(str(student["age"]))
        self.student_email_var.set(student["email"])

    def on_class_select(self, _event):
        selected = self.class_tree.selection()
        if not selected:
            return

        self.selected_class_id = int(selected[0])
        class_item = self.find_by_id("classes", self.selected_class_id)
        if not class_item:
            return

        self.class_form_mode = "edit"
        self.class_title_var.set(class_item["title"])
        self.class_teacher_var.set(class_item["teacher"])
        self.class_schedule_var.set(class_item["schedule"])

    def on_enrollment_select(self, _event):
        selected = self.enrollment_tree.selection()
        if not selected:
            return

        self.selected_enrollment_id = int(selected[0])
        enrollment = self.find_by_id("enrollments", self.selected_enrollment_id)
        if not enrollment:
            return

        student = self.find_by_id("students", enrollment["student_id"])
        class_item = self.find_by_id("classes", enrollment["class_id"])
        if student:
            self.enrollment_student_var.set(f"{student['id']} - {student['name']}")
        if class_item:
            self.enrollment_class_var.set(f"{class_item['id']} - {class_item['title']}")
        self.attendance_var.set(enrollment["attendance"])

    def prepare_new_student(self):
        self.clear_student_form()

    def prepare_new_class(self):
        self.clear_class_form()

    def clear_student_form(self):
        self.student_form_mode = "new"
        self.selected_student_id = None
        self.student_name_var.set("")
        self.student_age_var.set("")
        self.student_email_var.set("")
        self.student_tree.selection_remove(self.student_tree.selection())

    def clear_class_form(self):
        self.class_form_mode = "new"
        self.selected_class_id = None
        self.class_title_var.set("")
        self.class_teacher_var.set("")
        self.class_schedule_var.set("")
        self.class_tree.selection_remove(self.class_tree.selection())

    def clear_enrollment_form(self):
        self.selected_enrollment_id = None
        self.enrollment_student_var.set("")
        self.enrollment_class_var.set("")
        self.attendance_var.set("Present")
        self.enrollment_tree.selection_remove(self.enrollment_tree.selection())

    def persist_and_refresh(self):
        save_data(self.data)
        self.refresh_all()

    def find_by_id(self, key, item_id):
        return next((item for item in self.data[key] if item["id"] == item_id), None)


def main():
    root = tk.Tk()
    app = ClassManagementApp(root)
    app.clear_student_form()
    app.clear_class_form()
    app.clear_enrollment_form()
    root.mainloop()


if __name__ == "__main__":
    main()
