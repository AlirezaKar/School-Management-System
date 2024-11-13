from django.urls import path
from school.views import (my_api_view, 
                          home,
                          education_organization_view,
                          student_view,
                          teacher_view,
                          master_view,
                          class_room_view,
                          high_student_view,
                          college_student_view,
                          elementary_view,
                          first_high_view,
                          second_high_view,
                          college_view,
                          snack_view,
                          vending_machine_view,
                          shop_view,
                          )

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', home, name='home'),
    path('api/', my_api_view, name='my_api_view'),
    path('education-organization/', education_organization_view, name='education_organization_view'),
    path('student/', student_view, name='student_view'),
    path('teacher/', teacher_view, name='teacher_view'),
    path('master/', master_view, name='master_view'),
    path('class-room/', class_room_view, name='class_room_view'),
    path('high-student/', high_student_view, name='high_student_view'),
    path('college-student/', college_student_view, name='college_student_view'),
    path('elementary/', elementary_view, name='elementary_view'),
    path('first-high/', first_high_view, name='first_high_view'),
    path('second-high/', second_high_view, name='second_high_view'),
    path('college/', college_view, name='college_view'),
    path('shop/', shop_view, name='shop_view'),
    path('snack/', snack_view, name='snack_view'),
    path('vending-machine/', vending_machine_view, name='vending_machine_view'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]