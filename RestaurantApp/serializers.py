from rest_framework import serializers
from .models import MenuItem

class MenuItemSerializers(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','title','price','inventory']
        extra_kwargs = {
            'price':{'min_value':2},
            'inventory':{'min_value':0}
        }