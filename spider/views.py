from rest_framework.views import APIView
from rest_framework.response import Response
from .spiderptt import sp_ptt
from .models import PixivArt
from .serializers import PivixSerializers
from .spiderpivix import sp_pixiv,sendDC
webhook_url = ''

class SpiderPtt(APIView):
    def post(self, request, *args, **kwargs):
        sp_ptt()
        return Response('ok')

class SpiderPivix(APIView):
    def get(self,request,*args,**kwargs):
        data = PixivArt.objects.filter(tag='ナイスネイチャ(ウマ娘)').order_by('-cdate')[:10]
        ser=PivixSerializers(data,many=True).data
        return Response({'code':0,'data':ser})
    def post(self,request,*args,**kwargs):
        sp_pixiv()
        data=PixivArt.objects.filter(tag='ナイスネイチャ(ウマ娘)').order_by('-cdate')[:10]
        # data=PixivArt.objects.all().order_by('title')[:5]
        for i in data:
            sendobj={'content':'%s,p站網址:%s'%(i['title'],i['artUrl']),'img':i['imgUrl']}
            print(sendobj)
            sendDC(sendobj)
        return Response('ok')

class testVue(APIView):
    def get(self,request,*args,**kwargs):
        return Response({'code':0,'data':'hello vue'})