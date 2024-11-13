import tkinter as tk
from tkinter import ttk
from objs_definition import (
    get_organizations,
    get_teachers,
    get_masters,
    get_students,
    get_high_students,
    get_college_students,
    get_elementaries,
    get_first_highs,
    get_second_highs,
    get_colleges,
    get_class_rooms,
    get_snacks,
    get_vending_machines,
    get_shops,
)

organizations = get_organizations()
teachers = get_teachers()
masters = get_masters()
students = get_students()
high_students = get_high_students()
college_students = get_college_students()
elementaries = get_elementaries()
first_highs = get_first_highs()
second_highs = get_second_highs()
colleges = get_colleges()
class_rooms = get_class_rooms()
snacks = get_snacks()
vending_machines = get_vending_machines()
shops = get_shops()


root = tk.Tk()
root.title("Model Browser")
root.geometry("500x500")
root.resizable = True, True


def open_model_window(model_name, objects, fields):
    new_window = tk.Toplevel(root)
    new_window.title(f"{model_name} List")
    new_window.geometry("1350x400")
    
    
    search_label = tk.Label(new_window, text="Search:")
    search_label.pack(pady=5)
    
    search_entry = tk.Entry(new_window)
    search_entry.pack(pady=5)
    
    
    tree = ttk.Treeview(new_window, columns=fields, show="headings")
    for field in fields:
        tree.heading(field, text=field)
    tree.pack(fill="both", expand=True)
    
    
    # def update_list():
    #     query = search_entry.get().lower()
    #     tree.delete(*tree.get_children())

    #     for obj in objects:
    #         values = [str(obj.get(field, "")) for field in fields]
    #         if any(query in value.lower() for value in values):
    #             tree.insert("", "end", values=values)
    
    
    # filter_button = tk.Button(new_window, text="Filter", command=update_list)
    # filter_button.pack(pady=5)
    
    
    # update_list()


models = [
    ("Student", students, ["first_name", "last_name", "grade"]),
    ("HighStudent", high_students, ["first_name", "last_name", "grade", "major"]),
    ("CollegeStudent", college_students, ["first_name", "last_name", "grade", "education_type", "major", "sub_major"]),
    ("Elementary", elementaries, ['grade', 'class_room', 'students', 'teachers']),
    ("FirstHigh", first_highs, ['grade', 'class_room', 'students', 'teachers']),
    ("SecondHigh", second_highs, ['grade', 'class_room', 'students', 'teachers']),
    ("College", colleges, ['semester', 'grade', 'class_rooms', 'students', 'masters', 'major', 'sub_major']),
    ("ClassRoom", class_rooms, ['name', 'students', 'teacher']),
    ("Snack", snacks, ['name', 'cost']),
    ("VendingMachine", vending_machines, ['shopkeeper', 'snacks']),
    ("Shop", shops, ['shopkeeper', 'snacks']),
    ("Teacher", teachers, ["first_name", "last_name"]),
    ("Master", masters, ["first_name", "last_name"]),
    ("EducationOrganization", organizations, ['name', 'gender', 'year_of_foundation', 'school_type', 'education_level']),
]


for i, (model_name, objects, fields) in enumerate(models):
    button = tk.Button(root, text=model_name, command=lambda m=model_name, o=objects, f=fields: open_model_window(m, o, f))
    button.grid(row=i//2, column=i%2, padx=10, pady=5)


root.mainloop()
