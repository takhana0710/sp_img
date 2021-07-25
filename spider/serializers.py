from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import PixivArt
class PivixSerializers(DocumentSerializer):
    class Meta:
        model=PixivArt
