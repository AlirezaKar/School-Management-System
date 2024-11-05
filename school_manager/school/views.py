from django.shortcuts import render
from django.http import JsonResponse
from school.models import (
    EducationOrganization,
    Student,
    Teacher,
    Master,
    ClassRoom,
    HighStudent,
    CollegeStudent,
    Elementary,
    FirstHigh,
    SecondHigh,
    College,
    Snack,
    Shop,
    VendingMachine,
)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from school.api.serializers import (
        EducationOrganizationSerializer,
        StudentSerializer,
        TeacherSerializer,
        MasterSerializer,
        ClassRoomSerializer,
        HighStudentSerializer,
        CollegeStudentSerializer,
        ElementarySerializer,
        FirstHighSerializer,
        SecondHighSerializer,
        CollegeSerializer,
        SnackSerializer,
        ShopSerializer,
        VendingMachineSerializer,
)

def home(request):
    return render(request, 'home.html')


def my_api_view(request):  
    return JsonResponse({'text':"hello world"})


@api_view(['GET'])
def education_organization_view(request):
    # organizations_from_db = EducationOrganization.objects.values('name', 'gender', 'year_of_foundation', 'school_type', 'education_level')
    # organizations = {
    #     'data': [item for item in organizations_from_db]
    # }
    # return JsonResponse(organizations)
    organization_serializer = EducationOrganizationSerializer(EducationOrganization.objects.all(), many=True)
    return Response(organization_serializer.data)

@api_view(['GET'])
def student_view(request):
    # students_from_db = Student.objects.values('first_name', 'last_name', 'grade')
    # students = {
    #     'data': [item for item in students_from_db]
    # }
    # return JsonResponse(students)
    student_serializer = StudentSerializer(Student.objects.all(), many=True)
    return Response(student_serializer.data)

@api_view(['GET'])
def teacher_view(request):
#     teachers_from_db = Teacher.objects.values('first_name', 'last_name')
#     teachers = {
#         'data': [item for item in teachers_from_db]
#     }
#     return JsonResponse(teachers)
    teacher_serializer = TeacherSerializer(Teacher.objects.all(), many=True)
    return Response(teacher_serializer.data)

@api_view(['GET'])
def master_view(request):
    # masters_from_db = Master.objects.values('first_name', 'last_name')
    # masters = {
    #     'data': [item for item in masters_from_db]
    # }
    # return JsonResponse(masters)
    master_serializer = MasterSerializer(Master.objects.all(), many=True)
    return Response(master_serializer.data)

@api_view(['GET'])
def class_room_view(request):
    # class_rooms_from_db = ClassRoom.objects.values('name', 'students', 'teacher')
    # class_rooms = {
    #     'data': [item for item in class_rooms_from_db]
    # }
    # return JsonResponse(class_rooms)
    class_room_serializer = ClassRoomSerializer(ClassRoom.objects.all(), many=True)
    return Response(class_room_serializer.data)

@api_view(['GET'])
def high_student_view(request):
    # high_students_from_db = HighStudent.objects.values('first_name', 'last_name', 'grade', 'major')
    # high_students = {
    #     'data': [item for item in high_students_from_db]
    # }
    # return JsonResponse(high_students)
    high_student_serializer = HighStudentSerializer(HighStudent.objects.all(), many=True)
    return Response(high_student_serializer.data)

@api_view(['GET'])
def college_student_view(request):
    # college_students_from_db = CollegeStudent.objects.values('first_name', 'last_name', 'grade', 'major', 'sub_major')
    # college_students = {
    #     'data': [item for item in college_students_from_db]
    # }
    # return JsonResponse(college_students)
    college_student_serializer = CollegeStudentSerializer(CollegeStudent.objects.all(), many=True)
    return Response(college_student_serializer.data)

@api_view(['GET'])
def elementary_view(request):
    # elementaries_from_db = Elementary.objects.values('grade', 'class_room', 'students', 'teachers')
    # elementaries = {
    #     'data': [item for item in elementaries_from_db]
    # }
    # return JsonResponse(elementaries)
    elementary_serializer = ElementarySerializer(Elementary.objects.all(), many=True)
    return Response(elementary_serializer.data)

@api_view(['GET'])
def first_high_view(request):
    # first_highs_from_db = FirstHigh.objects.values('grade', 'class_room', 'students', 'teachers')
    # first_highs = {
    #     'data': [item for item in first_highs_from_db]
    # }
    # return JsonResponse(first_highs)
    first_high_serializer = FirstHighSerializer(FirstHigh.objects.all(), many=True)
    return Response(first_high_serializer.data)

@api_view(['GET'])
def second_high_view(request):
    # second_highs_from_db = SecondHigh.objects.values('grade', 'class_room', 'students', 'teachers')
    # second_highs = {
    #     'data': [item for item in second_highs_from_db]
    # }
    # return JsonResponse(second_highs)
    second_high_serializer = SecondHighSerializer(SecondHigh.objects.all(), many=True)
    return Response(second_high_serializer.data)

@api_view(['GET'])
def college_view(request):
    # colleges_from_db = College.objects.values('semester', 'grade', 'class_rooms', 'students', 'masters', 'major', 'sub_major')
    # colleges = {
    #     'data': [item for item in colleges_from_db]
    # }
    # return JsonResponse(colleges)
    college_serializer = CollegeSerializer(College.objects.all(), many=True)
    return Response(college_serializer.data)

@api_view(['GET'])
def snack_view(request):
    # snacks_from_db = Snack.objects.values('name', 'cost')
    # snacks = {
    #     'data': [item for item in snacks_from_db]
    # }
    # return JsonResponse(snacks)
    snack_serializer = SnackSerializer(Snack.objects.all(), many=True)
    return Response(snack_serializer.data)

@api_view(['GET'])
def vending_machine_view(request):
    # vending_machines_from_db = VendingMachine.objects.values('shopkeeper', 'snacks')
    # vending_machines = {
    #     'data': [item for item in vending_machines_from_db]
    # }
    # return JsonResponse(vending_machines)
    vending_machine_serializer = VendingMachineSerializer(VendingMachine.objects.all(), many=True)
    return Response(vending_machine_serializer.data)

@api_view(['GET'])
def shop_view(request):
    # shops_from_db = Shop.objects.values('shopkeeper', 'snacks')
    # shops = {
    #     'data': [item for item in shops_from_db]
    # }
    # return JsonResponse(shops)
    shop_serializer = ShopSerializer(Shop.objects.all(), many=True)
    return Response(shop_serializer.data)