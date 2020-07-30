from django.db import models

from models import BaseModel


class FileModel(BaseModel):

    name = models.CharField(verbose_name="文件名", max_length=255)
    file = models.FileField(verbose_name="文件", upload_to="upload/%Y/%m/%d")

    class Meta:
        db_table = "cms_files"
        verbose_name = "文件"
        verbose_name_plural = verbose_name

    @classmethod
    def read_iter_file(cls, path, max_size=512):
        with open(path, 'rb') as f:
            while True:
                data = f.read(max_size)
                if data:
                    yield data
                else:
                    break
