# Create your views here.
from rest_framework.viewsets import ModelViewSet

from students.models import Student
from students.serializers import StudentSerializer


class StudentListView(ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
