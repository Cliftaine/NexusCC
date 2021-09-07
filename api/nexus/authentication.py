import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import BaseAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authentication import get_authorization_header
from .models import User
from .serializers import UserTokenSerializer



class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        try:
            payload = jwt.decode(token, 'secret', algorithm='HS256')

        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')


class JWTAuthenticationDispatch(object):
    userData = None
    
    def get_userData(self,request):
        token = request.COOKIES.get('jwt')

        if not token:
            return None

        else:
            try:
                payload = jwt.decode(token, 'secret', algorithm='HS256')
                user = User.objects.filter(id=payload['id']).first()
                userSerialized = UserTokenSerializer(user)
                userData = userSerialized.data

                if userData != None:
                    self.userData = userData
                    return userData
                return None

            except jwt.ExpiredSignatureError:
                return None
#                raise AuthenticationFailed('Unauthenticated!')
        return None

    def dispatch(self, request, *args, **kwargs):

        user = self.get_userData(request)
        if user is not None:
            return super().dispatch(request, *args, **kwargs)
 
        response = Response({'Error': 'Unauthenticated.'},status = status.HTTP_401_UNAUTHORIZED
)
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = 'application/json'
        response.renderer_context = {}
        return response


