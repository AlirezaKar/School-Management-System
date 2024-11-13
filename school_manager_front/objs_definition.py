import asyncio
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


async def get_organizations():
    return await get_edu_organ_api()

async def get_teachers():
    return await get_teacher_api()

async def get_masters():
    return await get_master_api()

async def get_students():
    return await get_student_api()

async def get_high_students():
    return await get_high_student_api()

async def get_college_students():
    return await get_college_student_api()

async def get_elementaries():
    return await get_elementary_api()

async def get_first_highs():
    return await get_first_high_api()

async def get_second_highs():
    return await get_second_high_api()

async def get_colleges():
    return await get_college_api()

async def get_class_rooms():
    return await get_class_room_api()

async def get_snacks():
    return await get_snack_api()

async def get_vending_machines():
    return await get_vending_machine_api()

async def get_shops():
    return await get_shop_api()


async def main():
    tasks = [
        get_organizations(),
        get_teachers(),
        get_masters(),
        get_students(),
        get_high_students(),
        get_college_students(),
        get_elementaries(),
        get_first_highs(),
        get_second_highs(),
        get_colleges(),
        get_class_rooms(),
        get_snacks(),
        get_vending_machines(),
        get_shops(),
    ]

    results = await asyncio.gather(*tasks)


    (organizations, teachers, masters, students, high_students,
     college_students, elementaries, first_highs, second_highs,
     colleges, class_rooms, snacks, vending_machines, shops) = results

    # print("Organizations:", organizations)
    # print("Teachers:", teachers)

if __name__ == "__main__":
    asyncio.run(main())
