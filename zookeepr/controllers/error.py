from zookeepr.lib.base import *
from paste import fileapp
from pylons.middleware import media_path, error_document_template, run_wsgi
import os.path
from pylons.util import get_prefix

class ErrorController(BaseController):
    """
    Class to generate error documents as and when they are required. This behaviour of this
    class can be altered by changing the parameters to the ErrorDocuments middleware in 
    your config/middleware.py file.
    """

    def document(self):
        """
        Change this method to change how error documents are displayed
        """
        page = error_document_template % {
            'prefix':get_prefix(request.environ),
            'code':params.get('code', ''), 
            'message':params.get('message', ''),
        }
        m.write(page)

    def img(self, id):
        self._serve_file(os.path.join(media_path, 'img', id))
        
    def style(self, id):
        self._serve_file(os.path.join(media_path, 'style', id))

    def _serve_file(self, path):
        run_wsgi(fileapp.FileApp(path), m, request)