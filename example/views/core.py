from example.views import ParamRequest, JsonResponse

class ExampleView(ParamRequest, JsonResponse):
  
  params = [
      ('param1', int),
      ('param2', int)
  ]
  
  def process_get(self, request, param1, param2):
    value = param1 + param2
    return {'result': value}
    
  

from example.mock import SomeVeryClearError
import json
from django.http import HttpResponse

def bad_example_view(request):
  params = request.GET.dict()
  param1 = params.get('param1')
  param2 = params.get('param2')
  
  if param1 is None:
    raise SomeVeryClearError('param1 not found!')
  if param2 is None:
    raise SomeVeryClearError('param2 not found!')
    
  try:
    param1 = int(param1)
  except ValueError:
    raise SomeVeryClearError('param1 is not of type int')
  try:
    param2 = int(param2)
  except ValueError:
    raise SomeVeryClearError('param2 is not of type int')
    
  value = param1 + param2
  
  json_result = json.dumps({'result': value})
  return HttpResponse(json_result, content_type="application/json")
  
  
  
