# chalice-utils (Olympia Beta)

## how to use
```python
from . import App, View, serializers, router


class SampleSerializer(serializers.Serializer):
  country = serializers.StringField(max_length=20)
  zipcode = serializers.IntegerField(required=False)


class SampleView(View):
  def get(self, request, name):
    return {'hello': name}

  def post(self, request, *args):
    serializer = SampleSerializer(request.query_params)
    if serializer.is_valid:
      return serializer.data
    else:
      return {'error': 'country is required'}


app = App(app_name='shepherd')
app.register(path='/version1/{name}', SampleView)
```

## todo
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
