from example.views.generic.base import BaseView
from example.mock import SomeVeryClearError
import json


class PostParamRequest(BaseView):
  """ Generic view for API views which
  respond with JSON based on some POST parameter values. 
  """
  params = []
  
  def prepare_request(self, request, *args, **kwargs):
    payload = request.GET.dict()
    processed_params = []
    
    for param in self.params:
      try:
        processed_params.append(payload.pop(param))
      except KeyError:
        raise SomeVeryClearError('Parameter ({}) missing!'.format(param))
        
    # Call next request preparator with injected processed parameters
    return super().prepare_request(request, *processed_params, **kwargs)
        
