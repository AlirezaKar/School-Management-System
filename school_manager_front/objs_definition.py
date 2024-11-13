from api_call import (
    get_edu_organ_api,
    get_teacher_api,
    get_master_api,
    get_student_api,
    get_high_student_api,
    get_college_student_api,
    get_elementary_api,
    get_first_high_api,
    get_second_high_api,
    get_college_api,
    get_class_room_api,
    get_snack_api,
    get_vending_machine_api,
    get_shop_api,
)

if __name__ == '__main':
    organizations = get_edu_organ_api()
    teachers = get_teacher_api()
    masters = get_master_api()
    students = get_student_api()
    high_students = get_high_student_api()
    college_students = get_college_student_api()
    elementaries = get_elementary_api()
    first_highs = get_first_high_api()
    second_highs = get_second_high_api()
    colleges = get_college_api()
    class_rooms = get_class_room_api()
    snacks = get_snack_api()
    vending_machines = get_vending_machine_api()
    shops = get_shop_api()