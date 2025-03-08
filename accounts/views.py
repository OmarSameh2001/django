from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny

User = get_user_model()

# Custom Login View using JWT
class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response(
            {"message": "Login successful!", "tokens": response.data},
            status=status.HTTP_200_OK,
        )

# Register View
class RegisterView(APIView):
    permission_classes = [AllowAny]  # Allow anyone to register

    def post(self, request):
        data = request.data
        if User.objects.filter(email=data.get("email")).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(
            email=data["email"],
            username=data["username"],
            password=data["password"],
            first_name=data.get("first_name", ""),
            last_name=data.get("last_name", ""),
            phone_number=data.get("phone_number", ""),
        )
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)
