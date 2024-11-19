from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
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
from django.views.generic import View, DetailView


def into(request):
    return render(request, 'home.html')

def homepage(request):
    return render(request, 'homepage.html', {})

def school_view(request):
    elementaries = Elementary.objects.all()
    first_highs = FirstHigh.objects.all()
    second_highs = SecondHigh.objects.all()
    
    data = {
        'elementaries': elementaries,
        'first_highs': first_highs,
        'second_highs': second_highs,
    }
    return render(request, 'school_view.html', {'data':data})

class SchoolDetailView(DetailView):
    model = Elementary, FirstHigh, SecondHigh
    template_name = 'school_detail_view.html'

    
def my_api_view(request):  
    return JsonResponse({'text':"hello world"})


@api_view(['GET'])
def education_organization_view(request):
    q = request.GET.get('q', None)
    if q is not None:
        organization_serializer = EducationOrganizationSerializer(
            EducationOrganization.objects.filter(Q(name__icontains=q) | Q(description__icontains=q)), many=True
            )
    else:
        organization_serializer = EducationOrganizationSerializer(EducationOrganization.objects.all(), many=True)
    return Response(organization_serializer.data)

@api_view(['GET'])
def student_view(request):
    q = request.GET.get('q', None)
    if q is not None:
        student_serializer = StudentSerializer(
            Student.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q)), many=True
            )
    else:
        student_serializer = StudentSerializer(Student.objects.all(), many=True)
    return Response(student_serializer.data)

@api_view(['GET'])
def teacher_view(request):
    q = request.GET.get('q', None)
    if q is not None:
        teacher_serializer = TeacherSerializer(
            Teacher.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q)), many=True
            )
    else:   
        teacher_serializer = TeacherSerializer(Teacher.objects.all(), many=True)
    return Response(teacher_serializer.data)

@api_view(['GET'])
def master_view(request):
    q = request.GET.get('q', None)
    if q is not None:
        master_serializer = MasterSerializer(Master.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q)), many=True)
    else:
        master_serializer = MasterSerializer(Master.objects.all(), many=True)    
    return Response(master_serializer.data)

@api_view(['GET'])
def class_room_view(request):
    class_room_serializer = ClassRoomSerializer(ClassRoom.objects.all(), many=True)
    return Response(class_room_serializer.data)

@api_view(['GET'])
def high_student_view(request):
    q = request.GET.get('q', None)
    if q is not None:
        high_student_serializer = HighStudentSerializer(HighStudent.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q)), many=True)
    else:
        high_student_serializer = HighStudentSerializer(HighStudent.objects.all(), many=True)
    return Response(high_student_serializer.data)

@api_view(['GET'])
def college_student_view(request):
    q = request.GET.get('q', None)
    if q is not None:
        college_student_serializer = CollegeStudentSerializer(CollegeStudent.objects.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q)), many=True)
    else:
        college_student_serializer = CollegeStudentSerializer(CollegeStudent.objects.all(), many=True)
    return Response(college_student_serializer.data)

@api_view(['GET'])
def elementary_view(request):
    elementary_serializer = ElementarySerializer(Elementary.objects.all(), many=True)
    return Response(elementary_serializer.data)

@api_view(['GET'])
def first_high_view(request):
    first_high_serializer = FirstHighSerializer(FirstHigh.objects.all(), many=True)
    return Response(first_high_serializer.data)

@api_view(['GET'])
def second_high_view(request):
    second_high_serializer = SecondHighSerializer(SecondHigh.objects.all(), many=True)
    return Response(second_high_serializer.data)

@api_view(['GET'])
def college_view(request):
    college_serializer = CollegeSerializer(College.objects.all(), many=True)
    return Response(college_serializer.data)

@api_view(['GET'])
def snack_view(request):
    q = request.GET.get('q' , None)
    if q is not None:
        snack_serializer = SnackSerializer(Snack.objects.filter(name__icontains=q), many=True)
    else:
        snack_serializer = SnackSerializer(Snack.objects.all(), many=True)
    return Response(snack_serializer.data)

@api_view(['GET'])
def vending_machine_view(request):
    q = request.GET.get('q', None)
    if q is not None:
        vending_machine_serializer = VendingMachineSerializer(VendingMachine.objects.filter(shopkeeper__icontains=q), many=True)
    else:
        vending_machine_serializer = VendingMachineSerializer(VendingMachine.objects.all(), many=True)
    return Response(vending_machine_serializer.data)

@api_view(['GET'])
def shop_view(request):
    q = request.GET.get('q', None)
    if q is not None:
        shop_serializer = ShopSerializer(Shop.objects.filter(shopkeeper__icontains=q), many=True)
    else:
        shop_serializer = ShopSerializer(Shop.objects.all(), many=True)
    return Response(shop_serializer.data)