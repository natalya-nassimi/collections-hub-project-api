from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers.auth import SignUpSerializer, SignInSerializer
from .serializers.common import UserSerializer
from .serializers.tokens import MyTokenObtainPairSerializer

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'User created successfully'})
    
class SignInView(APIView):
    def post(self, request):
        serializer = SignInSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        refresh = MyTokenObtainPairSerializer.get_token(user)
        return Response({
            'message': 'Login successful',
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh':str(refresh),
                'access':str(refresh.access_token),
            }
        })