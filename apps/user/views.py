from rest_framework_jwt.views import ObtainJSONWebToken, jwt_response_payload_handler
from rest_framework_jwt.settings import api_settings

from views import APIView
from user.models import Account
from user.serializers import AccountSerializer
from response import JSONResponse

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER  # 生成token
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER  # 解析token


class TestView(APIView):

    def get(self, *args, **kwargs):
        print(self.request.user)
        query_params = self.request.query_params
        print(query_params)
        return JSONResponse.success()

    def post(self, request, **kwargs):
        print(self.request.user.id)
        return JSONResponse.success()


class RegisterView(APIView):

    def post(self, *args):
        serializer = AccountSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return JSONResponse.badrequest(serializer.errors)
        return JSONResponse.success()


class LoginView(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            data = jwt_response_payload_handler(token, user, request)
            return JSONResponse.success(data)
        else:
            return JSONResponse.noauth(serializer.errors)
