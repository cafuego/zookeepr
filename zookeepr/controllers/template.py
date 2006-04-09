from zookeepr.lib.base import *

class TemplateController(BaseController):
    def view(self, url):
        """
        This is the last place which is tried during a request to try to find a 
        file to serve. It could be used for example to display a template::
        
            def view(self, url):
                from pkg_resources import resource_exists
                if resource_exists('zookeepr', url+'.myt'):
                    m.subexec(url+'.myt')
                else:
                    m.abort(404, "File not found")
        
        The default is just to abort the request with a 404 File not found
        status message.
        """
        m.abort(404, "File not found")