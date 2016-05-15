from example.views import PostParamRequest, JsonResponse


class ExampleView(PostParamRequest, JsonResponse):
  
  params = ['param1', 'param2']
  
  def process_post(self, request, param1, param2):
    value = param1 + param2
    return {'key': value}
    
