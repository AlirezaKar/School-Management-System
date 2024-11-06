import settings
import requests
import json



def get_edu_organ_api():
    organization_url = settings.DOMAIN + "/education-organization"
    payload = {}
    headers = {}
    organization_response = requests.request("GET", organization_url, headers=headers, data=payload)
    return json.loads(organization_response.text)

def get_student_api():
    students_url  = settings.DOMAIN + "/student"
    payload = {}
    headers = {}
    students_response = requests.request("GET", students_url, headers=headers, data=payload)
    return json.loads(students_response.text)
    
def get_teacher_api():
    teachers_url = settings.DOMAIN + "/teacher"
    payload = {}
    headers = {}
    teachers_response = requests.request("GET", teachers_url, headers=headers, data=payload)
    return json.loads(teachers_response.text)


def get_master_api():
    masters_url = settings.DOMAIN + "/master"
    payload = {}
    headers = {}
    masters_response = requests.request("GET", masters_url, headers=headers, data=payload)
    return json.loads(masters_response.text)


def get_class_room_api():
    class_rooms_url = settings.DOMAIN + "/class-room"
    payload = {}
    headers = {}
    class_rooms_response = requests.request("GET", class_rooms_url, headers=headers, data=payload)
    return json.loads(class_rooms_response.text)


def get_high_student_api():
    high_students_url = settings.DOMAIN + "/high-student"
    payload = {}
    headers = {}
    high_students_response = requests.request("GET", high_students_url, headers=headers, data=payload)
    return json.loads(high_students_response.text)

def get_college_student_api():
    college_students_url = settings.DOMAIN + "/college-student"
    payload = {}
    headers = {}
    college_students_response = requests.request("GET", college_students_url, headers=headers, data=payload)
    return json.loads(college_students_response.text)

def get_elementary_api():
    elementaries_url = settings.DOMAIN + "/elementary"
    payload = {}
    headers = {}
    elementaries_response = requests.request("GET", elementaries_url, headers=headers, data=payload)
    return json.loads(elementaries_response.text)


def get_first_high_api():
    first_highs_url = settings.DOMAIN + "/first-high"
    payload = {}
    headers = {}
    first_highs_response = requests.request("GET", first_highs_url, headers=headers, data=payload)
    return json.loads(first_highs_response.text)

    
def get_second_high_api():
    second_highs_url = settings.DOMAIN + "/second-high"
    payload = {}
    headers = {}
    second_highs_response = requests.request("GET", second_highs_url, headers=headers, data=payload)
    return json.loads(second_highs_response.text)


def get_college_api():
    colleges_url = settings.DOMAIN + "/college"
    payload = {}
    headers = {}
    colleges_response = requests.request("GET", colleges_url, headers=headers, data=payload)
    return json.loads(colleges_response.text)


def get_snack_api():
    snacks_url = settings.DOMAIN + "/shop"
    payload = {}
    headers = {}
    snacks_response = requests.request("GET", snacks_url, headers=headers, data=payload)
    return json.loads(snacks_response.text)

def get_vending_machine_api():
    vending_machines_url = settings.DOMAIN + "/snack"
    payload = {}
    headers = {}
    vending_machines_response = requests.request("GET", vending_machines_url, headers=headers, data=payload)
    return json.loads(vending_machines_response.text)

def get_shop_api():
    shops_url = settings.DOMAIN + "/vending-machine"
    payload = {}
    headers = {}
    shops_response = requests.request("GET", shops_url, headers=headers, data=payload)
    return json.loads(shops_response.text)



    
    
    


    
    
    
    
    
    
    
    
