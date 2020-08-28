from rest_framework.request import Request
from rest_framework_jwt.views import ObtainJSONWebToken, jwt_response_payload_handler

from views import APIView
from user.models import Account
from user.serializers import AccountSerializer
from response import JSONResponse
from websocket.jobs import send_message, mass_message


class TestView(APIView):

    def get(self, request: Request, **kwargs) -> dict:
        user_id = request.user.id
        data = {'text': 'websocket成功'}
        send_message.delay(user_id, data)
        return JSONResponse.success()

    def post(self, request, **kwargs):
        user_ids = request.data.get("user_ids")
        data = {'text': 'websocket成功'}
        mass_message(user_ids, data)
        return JSONResponse.success()


class RegisterView(APIView):

    def post(self, *args) -> dict:
        serializer = AccountSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
        else:
            return JSONResponse.badrequest(serializer.errors)
        return JSONResponse.success()


class LoginView(ObtainJSONWebToken):

    def post(self, request, *args, **kwargs) -> dict:
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            token = serializer.object.get('token')
            data = jwt_response_payload_handler(token, user, request)
            return JSONResponse.success(data)
        else:
            return JSONResponse.noauth(serializer.errors)
