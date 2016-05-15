from django.test import TestCase
from example.views import ExampleView

class ExampleTestCase(TestCase):
  
  def test_example_correct(self):
    request = {}
    param1 = 1
    param2 = 2
    
    result = ExampleView().process_post(request, param1, param2)
    
    self.assertEqual(result['key'], param1+param2)
