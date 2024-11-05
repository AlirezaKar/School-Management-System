import tkinter as tk
from tkinter import ttk
import requests
import json

# url = "http://127.0.0.1:8000/"

organization_url = "http://127.0.0.1:8000/education-organization"
students_url  = "http://127.0.0.1:8000/student"
teachers_url = "http://127.0.0.1:8000/teacher"
masters_url = "http://127.0.0.1:8000/master"
class_rooms_url = "http://127.0.0.1:8000/class-room"
high_students_url = "http://127.0.0.1:8000/high-student"
college_students_url = "http://127.0.0.1:8000/college-student"
elementaries_url = "http://127.0.0.1:8000/elementary"
first_highs_url = "http://127.0.0.1:8000/first-high"
second_highs_url = "http://127.0.0.1:8000/second-high"
colleges_url = "http://127.0.0.1:8000/college"
snacks_url = "http://127.0.0.1:8000/shop"
vending_machines_url = "http://127.0.0.1:8000/snack"
shops_url = "http://127.0.0.1:8000/vending-machine"

payload = {}
headers = {}

organization_response = requests.request("GET", organization_url, headers=headers, data=payload)
students_response = requests.request("GET", students_url, headers=headers, data=payload)
teachers_response = requests.request("GET", teachers_url, headers=headers, data=payload)
masters_response = requests.request("GET", masters_url, headers=headers, data=payload)
class_rooms_response = requests.request("GET", class_rooms_url, headers=headers, data=payload)
high_students_response = requests.request("GET", high_students_url, headers=headers, data=payload)
college_students_response = requests.request("GET", college_students_url, headers=headers, data=payload)
elementaries_response = requests.request("GET", elementaries_url, headers=headers, data=payload)
first_highs_response = requests.request("GET", first_highs_url, headers=headers, data=payload)
second_highs_response = requests.request("GET", second_highs_url, headers=headers, data=payload)
colleges_response = requests.request("GET", colleges_url, headers=headers, data=payload)
snacks_response = requests.request("GET", snacks_url, headers=headers, data=payload)
vending_machines_response = requests.request("GET", vending_machines_url, headers=headers, data=payload)
shops_response = requests.request("GET", shops_url, headers=headers, data=payload)

# print(response.text)

organizations_res = json.loads(organization_response.text)
import pdb;pdb.set_trace()
organizations = organizations_res['data']
import pdb;pdb.set_trace()
students_res = json.loads(students_response.text)
students = students_res['data']
teachers_res = json.loads(teachers_response.text)
teachers = teachers_res['data']
masters_res = json.loads(masters_response.text)
masters = masters_res['data']
class_rooms_res = json.loads(class_rooms_response.text)
class_rooms = class_rooms_res['data']
high_students_res = json.loads(high_students_response.text)
high_students = high_students_res['data']
college_students_res = json.loads(college_students_response.text)
college_students = college_students_res['data']
elementaries_res = json.loads(elementaries_response.text)
elementaries = elementaries_res['data']
first_highs_res = json.loads(first_highs_response.text)
first_highs = first_highs_res['data']
second_highs_res = json.loads(second_highs_response.text)
second_highs = second_highs_res['data']
colleges_res = json.loads(colleges_response.text)
colleges= colleges_res['data']
snacks_res = json.loads(snacks_response.text)
snacks = snacks_res['data']
vending_machines_res = json.loads(vending_machines_response.text)
vending_machines = vending_machines_res['data']
shops_res = json.loads(shops_response.text)
shops = shops_res['data']



# مدل‌های فرضی با داده‌های نمونه
# students = [
#     {"first_name": "Alice", "last_name": "Smith", "has_school_bus": True, "grade": "A"},
#     {"first_name": "Bob", "last_name": "Jones", "has_school_bus": False, "grade": "B"},
#     {"first_name": "Charlie", "last_name": "Brown", "has_school_bus": True, "grade": "A"},
# ]

# high_students = [
#     {"first_name": "Dave", "last_name": "Davis", "has_school_bus": False, "grade": "10", "major": "Science"},
#     {"first_name": "Eve", "last_name": "Evans", "has_school_bus": True, "grade": "11", "major": "Arts"},
# ]

# college_students = [
#     {"first_name": "Fay", "last_name": "Johnson", "student_id": 123, "has_dorm": True, "grade": "Sophomore", "education_type": "Full-Time", "major": "CS", "sub_major": "AI"},
# ]

# teachers = [
#     {"first_name": "Grace", "last_name": "Williams", "salary_per_day": 100, "working_days": 20},
# ]

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
