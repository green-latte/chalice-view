# Chalice View

Extension classes for develop  [chalice](https://github.com/awslabs/chalice)

## how to use

**Chalice View** load your .chalice directory and set your project name and development mode.

you should only create custom view class and register route to custom manager class.

```python
from chalice_view.manager import AppManager
from chalice_view.view import View


class SampleView(View):
  def get(self, request, name):
    return {'hello': name}

  def post(self, request, *args):
    serializer = SampleSerializer(request.query_params)
    if serializer.is_valid:
      return serializer.data
    else:
      return {'error': 'country is required'}

manager = AppManager())
manager.register('/version1/{name}', SampleView)

app = manager.generate_app()
```

## todo

```python
from . import App, View, serializers, router

class SampleSerializer(serializers.Serializer):
  country = serializers.StringField(max_length=20)
  zipcode = serializers.IntegerField(required=False)
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
