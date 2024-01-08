from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['GET'])
def get_book(request):
    book_obj = Books.objects.all()
    serialized_data = BookSerializer(book_obj, many = True)
    return Response({"status": 200, "data": serialized_data.data})

def home(request):
    return HttpResponse("Server is up and runing!!!")

class Register_user(APIView):
    def post(self, request):
        data = request.data

        serialized_data = UserSerializer(data = data)

        if not serialized_data.is_valid():
            return Response({"status": 403, "errors": serialized_data.errors, "message": "Something went wrong!"})

        serialized_data.save()
        print(serialized_data.data.get("username"))

        user_obj = User.objects.get(username=serialized_data.data.get("username"))

        refresh = RefreshToken.for_user(user_obj)

        return Response({
            "status": 200, 
            "data": serialized_data.data, 
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Data saved successfully"
        })
    
class StudentsApi(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        print(request.user)
        student_obj = Student.objects.all()
        serialized_data = StudentSerializer(student_obj, many = True)
        return Response({"status": 200, "data": serialized_data.data})

    def post(self, request):
        data = request.data
        serialized_data = StudentSerializer(data = data)
       
        if not serialized_data.is_valid():
            return Response({"status": 403, "errors": serialized_data.errors, "message": "Something went wrong!"})

        serialized_data.save()
        return Response({"status": 200, "data": serialized_data.data, "message": "Data saved successfully"}) 

    def put(self, request):
        pass

    def patch(self, request):
        data = request.data
        try:
            student_obj = Student.objects.get(id = request.GET.get('id'))
            serialized_data = StudentSerializer(student_obj, data = data, partial=True)
        except:
            return Response({"status": 403, "message": "Student not found!"})
        else:
            
            if not serialized_data.is_valid():
                return Response({"status": 403, "errors": serialized_data.errors, "message": "Something went wrong!"})

            serialized_data.save()
            return Response({"status": 200, "data": serialized_data.data, "message": "Data saved successfully"}) 

    def delete(self, request):
        try:
            student_obj = Student.objects.get(id = request.GET.get('id'))
            student_obj.delete()
            return Response({"status": 200, "message": "Student deleted successfully"})
        except:
            return Response({"status": 403, "message": "Student not Found!"})


class ProductApi(APIView):
    
    def get(self, request):
        products_id = request.GET.get('id')
        gender = request.GET.get('gender')
        print(products_id)

        if products_id:
            products_obj = Product.objects.get(id=products_id)
            serialized_data = ProductSerializer(products_obj)
        else:
            if gender:
                products_obj = Product.objects.filter(gender=gender)
            else:
                products_obj = Product.objects.all()
            serialized_data = ProductSerializer(products_obj, many = True)
            
        return Response({"status": 200, "data": serialized_data.data})