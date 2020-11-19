from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import User, Group
from .serializers import *

@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        data = User.objects.all()

        serializer = UserSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def groups_list(request):
    if request.method == 'GET':
        data = Group.objects.all()

        serializer = GroupSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])
def groups_detail(request, pk):
    try:
        group = Group.objects.get(pk=pk)
    except Group.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = GroupSerializer(group, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class UserGroupListView(generics.ListAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# class UserGroupCreateView(generics.CreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# class UserGroupEditView(generics.RetrieveUpdateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer


# class UserGroupDeleteView(generics.DestroyAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

#     def delete(self, request, *args, **kwargs):
#         obj = self.get_object()
#         user = User.objects.filter(group_id=kwargs['pk']).first()
#         if user:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         else:
#             obj.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)