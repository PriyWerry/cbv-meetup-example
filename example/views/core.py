from example.views import ParamRequest, JsonResponse


class ExampleView(ParamRequest, JsonResponse):
  
  params = [
      ('param1', int),
      ('param2', int)
  ]
  
  def process_get(self, request, param1, param2):
    value = param1 + param2
    return {'result': value}
    
  
