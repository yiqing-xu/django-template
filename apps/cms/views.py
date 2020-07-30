from django.http import FileResponse

from views import APIView
from response import JSONResponse
from cms.serializers import FileSerializer, FileModel


class FileCreateView(APIView):

    def post(self, request):
        serializer = FileSerializer(data=request.data, context=dict(request=request))
        if serializer.is_valid():
            serializer.save()
        else:
            return JSONResponse.badrequest(serializer.errors)
        return JSONResponse.success(serializer.data)


class FileRetrieveDestroyView(APIView):

    def get(self, request, **kwargs):
        file_id = kwargs.get("id")
        try:
            file = FileModel.objects.get(id=file_id)
        except FileModel.DoesNotExist:
            return JSONResponse.notfound("{}不指向任何文件".format(file_id))
        path = file.file.path
        name = file.name
        data = FileModel.read_iter_file(path)
        response = FileResponse(data)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format(name).encode("utf-8")
        return response

    def delete(self, request, **kwargs):
        file_id = kwargs.get("id")
        FileModel.objects.filter(id=file_id).delete()
        return JSONResponse.success()
