from example.views.generic.base import BaseView
from example.mock import SomeVeryClearError

class ParamRequest(BaseView):
  """ Generic view for API views which
  respond with JSON based on some POST parameter values. 
  """
  params = []
  
  def prepare_request(self, request, *args, **kwargs):
    payload = request.GET.dict()
    processed_params = []
    
    for param in self.params:
      key, expected_type = param
      
      front_end_param = ParamRequest.extract(key, payload)
      back_end_param = ParamRequest.transform(key, front_end_param, expected_type)

      processed_params.append(back_end_param)
      
    # Call next request preparator with injected processed parameters
    return super().prepare_request(request, *processed_params, **kwargs)
  
  @classmethod
  def extract(cls, key, payload):
    try:
      return payload.pop(key)
    except KeyError:
      raise SomeVeryClearError('Parameter ({}) missing!'.format(key))
  
  @classmethod
  def transform(cls, key, param, expected_type):
    try:
      return expected_type(param)        
    except ValueError:
      raise SomeVeryClearError('Parameter ({}) is not of type {}'.format(key, expected_type.__name__))
        
