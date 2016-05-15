from django.views.generic import View

class BaseView(View):
  """ Base view for views which need 
  request preparation and/or response preparation.
  """
  
  def post(self, request, *args, **kwargs):
    (request, args, kwargs) = self.prepare_request(request, *args, **kwargs)
    response = self.process_post(request, *args, **kwargs)
    return self.prepare_response(response, **kwargs)
    
  def get(self, request, *args, **kwargs):
    response = self.process_get()
    return self.prepare_response(response)
    
  def prepare_request(self, request, *args, **kwargs):
    """ Boilerplate function to end the request preparation"""
    return request, args, kwargs
    
  def prepare_response(self, response, **kwargs):
    """ Boilerplate function to end the response preparation"""
    return response
