from rest_framework import status, generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, TeamSerializer, AccountsSerializer, MovementsSerializer
from .models import User, Accounts, Movements, Team
from .authentication import JWTAuthentication, JWTAuthenticationDispatch
import datetime
import jwt



class UserView(JWTAuthenticationDispatch, viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer
    userData = None

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active = True).first()

    def list(self,request):
        if not self.userData['is_staff']:
            return Response({'AuthError':'You cant see all users'},status = status.HTTP_401_UNAUTHORIZED)
        serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        if not self.userData['is_staff']:
            return Response({'AuthError':'You cant create users'},status = status.HTTP_401_UNAUTHORIZED)
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Team was created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        if not self.userData['is_staff']:
            return Response({'AuthError':'You cant destroy users'},status = status.HTTP_401_UNAUTHORIZED)
        dest = self.get_queryset().filter(id = pk).first()
        if dest:
            dest.is_active = False
            dest.save()
            return Response({'message':'User erased'},status = status.HTTP_200_OK)
        return Response({'error':'Theres no team with associated'},status = status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()

        if user is None:
#            raise AuthenticationFailed('Auth Error')
            raise AuthenticationFailed('User Error')

        if not user.check_password(password):
            raise AuthenticationFailed('pass Error')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class TeamViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = TeamSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def list(self,request):
        serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Team was created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        team = self.get_queryset().filter(id = pk).first()
        if team:
            team.state = False
            team.save()
            return Response({'message':'Team erased'},status = status.HTTP_200_OK)
        return Response({'error':'Theres no team with associated'},status = status.HTTP_400_BAD_REQUEST)

class AccountsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = AccountsSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def list(self,request):
        serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Account was created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_200_OK)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        destroy = self.get_queryset().filter(id = pk).first()
        if destroy:
            destroy.state = False
            destroy.save()
            return Response({'message':'Account erased'},status = status.HTTP_200_OK)
        return Response({'error':'Theres no account with associated'},status = status.HTTP_400_BAD_REQUEST)

class MovementsViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    serializer_class = MovementsSerializer

    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()

    def list(self,request):
        serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Account was created'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk=None):
        pass

    def destroy(self,request,pk=None):
        pass

class MovementsRetrieveView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = MovementsSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

class MovementsListCreateView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = MovementsSerializer
    queryset = MovementsSerializer.Meta.model.objects.all()

    def post(self, request):
        serializer= self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Movement was created"})
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
