import tkinter as tk
from tkinter import ttk
import requests
import json
import api_call

organizations = api_call.get_edu_organ_api()
teachers = api_call.get_teacher_api()
masters = api_call.get_master_api()
students = api_call.get_student_api()
high_students = api_call.get_high_student_api()
college_students = api_call.get_college_student_api()
elementaries = api_call.get_elementary_api()
first_highs = api_call.get_first_high_api()
second_highs = api_call.get_second_high_api()
colleges = api_call.get_college_api()
class_rooms = api_call.get_class_room_api()
snacks = api_call.get_snack_api()
vending_machines = api_call.get_vending_machine_api()
shops = api_call.get_shop_api()

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("Model Browser")
root.geometry("500x500")
root.resizable = True, True

# تابع برای باز کردن پنجره جدید با قابلیت جستجو و فیلتر
def open_model_window(model_name, objects, fields):
    new_window = tk.Toplevel(root)
    new_window.title(f"{model_name} List")
    new_window.geometry("1350x400")
    
    # فیلد جستجو
    search_label = tk.Label(new_window, text="Search:")
    search_label.pack(pady=5)
    
    search_entry = tk.Entry(new_window)
    search_entry.pack(pady=5)
    
    # جدول برای نمایش object‌ها
    tree = ttk.Treeview(new_window, columns=fields, show="headings")
    for field in fields:
        tree.heading(field, text=field)
    tree.pack(fill="both", expand=True)
    
    # تابع برای بروزرسانی لیست بر اساس جستجو و فیلتر
    def update_list():
        query = search_entry.get().lower()
        tree.delete(*tree.get_children())
        
        for obj in objects:
            values = [str(obj.get(field, "")) for field in fields]
            if any(query in value.lower() for value in values):
                tree.insert("", "end", values=values)
    
    # دکمه فیلتر
    filter_button = tk.Button(new_window, text="Filter", command=update_list)
    filter_button.pack(pady=5)
    
    # نمایش اولیه لیست
    update_list()

# تعریف مدل‌ها و فیلدها برای هر دکمه
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

# ایجاد دکمه‌ها برای هر مدل
for i, (model_name, objects, fields) in enumerate(models):
    button = tk.Button(root, text=model_name, command=lambda m=model_name, o=objects, f=fields: open_model_window(m, o, f))
    button.grid(row=i//2, column=i%2, padx=10, pady=5)

# اجرای برنامه
root.mainloop()
