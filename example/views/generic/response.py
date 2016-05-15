from example.views.generic.base import BaseView
from django.http import JsonResponse as DjangoJsonResponse


class JsonResponse(BaseView):
  """ Generic view for processing the response
  of a view into a JSON response.
  """
  
  def prepare_response(self, response, **kwargs):
    # Some conversion of the response data might be necessary
    # here to enable converting it to JSON.
    return super().prepare_response(DjangoJsonResponse(response), **kwargs)
