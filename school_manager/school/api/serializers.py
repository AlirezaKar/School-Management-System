from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
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

class EducationOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationOrganization
        fields = ['id', 'name', 'description' ,'gender', 'year_of_foundation', 'school_type', 'education_level']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'grade']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name']


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = ['first_name', 'last_name']


class ClassRoomSerializer(serializers.ModelSerializer):
    students = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()

    def get_students(self, obj):
        return StudentSerializer(obj.students.all(), many=True).data
    
    def get_teacher(self, obj):
        return TeacherSerializer(obj.teacher.all(), many=True).data
    
    class Meta:
        model = ClassRoom
        fields = ['id', 'name', 'students', 'teacher']


class HighStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = HighStudent
        fields = ['first_name', 'last_name', 'grade', 'major']


class CollegeStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeStudent
        fields = ['first_name', 'last_name', 'grade', 'major', 'sub_major']


class ElementarySerializer(serializers.ModelSerializer):
    class_room = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    def get_class_room(self, obj):
        return ClassRoomSerializer(obj.class_room.all(), many=True).data

    def get_students(self, obj):
        return StudentSerializer(obj.students.all(), many=True).data
    
    def get_teachers(self, obj):
        return TeacherSerializer(obj.teachers.all(), many=True).data
    
    class Meta:
        model = Elementary
        fields = ['id', 'grade', 'class_room', 'students', 'teachers']


class FirstHighSerializer(serializers.ModelSerializer):
    class_room = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    def get_class_room(self, obj):
        return ClassRoomSerializer(obj.class_room.all(), many=True).data

    def get_students(self, obj):
        return StudentSerializer(obj.students.all(), many=True).data
    
    def get_teachers(self, obj):
        return TeacherSerializer(obj.teachers.all(), many=True).data
    
    class Meta:
        model = FirstHigh
        fields = ['id', 'grade', 'class_room', 'students', 'teachers']


class SecondHighSerializer(serializers.ModelSerializer):
    class_room = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    teachers = serializers.SerializerMethodField()

    def get_class_room(self, obj):
        return ClassRoomSerializer(obj.class_room.all(), many=True).data

    def get_students(self, obj):
        return StudentSerializer(obj.students.all(), many=True).data
    
    def get_teachers(self, obj):
        return TeacherSerializer(obj.teachers.all(), many=True).data
    
    class Meta:
        model = SecondHigh
        fields = ['id', 'grade', 'class_room', 'students', 'teachers']


class CollegeSerializer(serializers.ModelSerializer):
    class_rooms = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    masters = serializers.SerializerMethodField()

    def get_class_rooms(self, obj):
        return ClassRoomSerializer(obj.class_rooms.all(), many=True).data

    def get_students(self, obj):
        return StudentSerializer(obj.students.all(), many=True).data
    
    def get_masters(self, obj):
        return MasterSerializer(obj.masters.all(), many=True).data
    
    class Meta:
        model = College
        fields = ['id', 'semester', 'grade', 'class_rooms', 'students', 'masters', 'major', 'sub_major']


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ['id', 'name', 'cost']


class ShopKeeperSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ShopSerializer(serializers.ModelSerializer):
    shopkeeper = serializers.SerializerMethodField()

    def get_shopkeeper(self, obj):
        return ShopKeeperSerializer(obj.shopkeeper.all()).data
    
    class Meta:
        model = Shop
        fields = ['id', 'shopkeeper', 'snacks']


class VendingMachineSerializer(serializers.ModelSerializer):
    shopkeeper = serializers.SerializerMethodField()

    def get_shopkeeper(self, obj):
        return ShopKeeperSerializer(obj.shopkeeper.all()).data
    
    class Meta:
        model = VendingMachine
        fields = ['id', 'shopkeeper', 'snacks']