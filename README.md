# Chalice View

Extension classes for develop  [chalice](https://github.com/awslabs/chalice)

## installation
```sh
$ pip install chalice_view
```

## how to use

**Chalice View** load your .chalice directory and set your project name and development mode.

you should only create custom view class and register route to custom manager class.

```python
from chalice_view.manager import AppManager
from chalice_view.view import View


# define custom view based on chalice_view.View class
class SampleView(View):
  def get(self, request, name):
    return {'hello': name}


# initialize app manager to generate chalice application
manager = AppManager(debug=True)
manager.register('/version1/{name}', SampleView)
# chalice will read following app instance
app = manager.generate_app()
```

## testing
```python
import unittest
from chalice_view.test import ChaliceRequestFactory

class TestCustomResponse(unittest.TestCase):
  def setUp(self):
    # 1. initialize request factory
    self.factory = ChaliceRequestFactory()
    # 2. generate custom request parser
    self.view = manager.as_view()

  def test_sample(self):
    # 3. create request and call view method
    request = factory.get('/version1/{name}', uri_params={'name': 'kate'})
    response = view(request)
    # call test
    self.assertTrue({'hello': 'kate'}, response)

if __name__ == '__main__':
  unittest.main()
```

## todo

```python
from . import App, View, serializers, router

class SampleSerializer(serializers.Serializer):
  country = serializers.StringField(max_length=20)
  zipcode = serializers.IntegerField(required=False)

class SampleView(View)
  def post(self, request, *args):
    serializer = SampleSerializer(request.json_body)
    if serializer.is_valid:
      return serializer.data
    else:
      return {'error': 'country is required'}
```

```python
from pynamodb.models import Model
from pynamodb.attributes import (
  UnicodeAttribute, NumberAttribute
)

class AddressModel(Model):
  class Meta:
        table_name = 'Address'

    zipcode = NumberAttribute(hash_key=True)
    prefecture = UnicodeAttribute(range_key=True)

class AddressSerializer(new_serializer.Serializer):
  class Meta:
    model = AddressSerializer

class AddressView(ModelView):
  queries = Address.objects.all()
  serializer = AddressSerializer
```
