from userpost.models import UserPost
from userpost.serializer import UserSerializer

from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication

class UserPostViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes =[IsAdminUser]

    queryset=UserPost.objects.all().order_by('id')
    serializer_class=UserSerializer

    filter_backends = [SearchFilter]
    search_fields = ('title', 'body',)

    def get_queryset(self):
        qs=super().get_queryset()
        #qs=qs.filter(author__id=4)
        if self.request.user.is_authenticated:
            qs=qs.filter(author=self.request.user)
        else:
            qs=qs.none()
        return qs

    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
    