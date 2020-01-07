
from post.models import Post
from post.serializer import PostSerializer

from rest_framework import viewsets

from rest_framework import renderers
from rest_framework.decorators import action
from django.http import HttpResponse

from post.pagination import Mypagination


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset=Post.objects.all().order_by('id')
    serializer_class=PostSerializer
    pagination_class=Mypagination

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self,request,*args,**kwargs):
        return HttpResponse('얍')


'''
#3주차 -3
from rest_framework import generics

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
'''

'''
#3주차 -2
from rest_framework import generics
from rest_framework import mixins 


class PostList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def get(self, request,*args,**kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    
class PostDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer

    def get(self, request,*args,**kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request,*args,**kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request,*args,**kwargs):
        return self.destroy(request, *args, **kwargs)
    
'''

'''
#3주차 -1
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

from rest_framework.views import APIView

class PostList(APIView):
    def get(self, request):
        posts=Post.objects.all()
        serializer=PostSerializer(posts,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer=PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class PostDetail(APIView):
    def get_object(self,pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        post=self.get_object(pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        post=self.get_object(pk)
        serializer=PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        post=self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
#2주차
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
'''