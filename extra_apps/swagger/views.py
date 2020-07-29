import os

from django.shortcuts import render
from django.views.generic.base import View
from django.conf import settings


class DocIndexView(View):

    def get(self, *args):
        base_dir = settings.BASE_DIR
        doc_dir = getattr(settings, 'DOC_DIR', None)
        if not doc_dir:
            doc_dir = os.path.join(base_dir, 'docs')

        filenames = [(filename, filename.split('.')[0]) for filename in os.listdir(doc_dir)]
        return render(
            request=self.request,
            template_name='swagger-index.html',
            context={'filenames': filenames},
        )
