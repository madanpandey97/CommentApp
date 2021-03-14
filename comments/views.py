import logging
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.settings import api_settings as pagination_settings
from .models import (Comment, SubComment)
from comments import serializers

logger = logging.getLogger(__name__)


class CommentCreateView(generics.CreateAPIView):
    __doc__ = """
    Create View for the Main Comment Thread Section
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CommentSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data["user"] = user.id
        logger.info(f"{user} request to create comment thread with data  {data}")
        serializer = self.serializer_class(data=data)

        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"status": False, "message": serializer.errors},
                status=status.HTTP_200_OK,
            )

        serializer.save()
        return Response(
            {"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED
        )


class CommentListView(generics.ListAPIView):
    __doc__= """
    List View for the main comment thread 
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CommentDetailsSerializer
    pagination_class = pagination_settings.DEFAULT_PAGINATION_CLASS

    def get_queryset(self, request, user):
        queryset = Comment.objects.filter(user=user).order_by("-id")
        return queryset

    def get(self, request, *args, **kwargs):
        user = request.user
        logger.info(f"{user} request to list  of Comment Thread")

        queryset = self.get_queryset(request, user)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)


class CommentUpdateView(generics.UpdateAPIView):
    __doc__ = """
    Update View for the  comment thread 
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CommentSerializer

    queryset = Comment.objects.all()

    def put(self, request, *args, **kwargs):
        user = request.user
        data = self.partial_update(request, *args, **kwargs)
        logger.info(f"{user} request update the comment section {request.data}")
        return Response(
            {"status": True, "data": data.data},
            status=status.HTTP_200_OK,
        )


class CommentDetailListView(generics.RetrieveAPIView):
    __doc__="""
    Retrive View for the mail broadcast
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CommentDetailsSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        logger.info(f"{user} request to get details  of Comment thread")
        queryset = Comment.objects.get(id=kwargs.get("pk"), user=user)
        serializer = self.serializer_class(queryset)
        return Response(
            {"status": True, "data": serializer.data}, status=status.HTTP_200_OK
        )


class CommentDeleteView(generics.DestroyAPIView):
    __doc__ = """
    Delete View for the mail broadcast
    """

    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        logger.info(f"{user} request to delete comment thread {kwargs}")
        queryset = Comment.objects.filter(user=user)
        if not queryset.filter(id=kwargs.get("pk")).exists():
            return Response(
                {"status": False, "message": "Comment thread not found"},
                status=status.HTTP_200_OK,
            )

        instance = queryset.get(id=kwargs.get("pk"))
        instance.delete()
        return Response(
            {"status": True, "message": "Comment thread deleted"},
            status=status.HTTP_200_OK,
        )


class CommentListAllView(generics.ListAPIView):
    __doc__="""
    List View of all the comment created
    """

    permission_classes = (AllowAny,)
    serializer_class = serializers.CommentDetailsSerializer
    pagination_class = pagination_settings.DEFAULT_PAGINATION_CLASS

    def get_queryset(self, request):
        queryset = Comment.objects.all().order_by("-id")
        return queryset

    def get(self, request, *args, **kwargs):
        user = request.user
        logger.info(f"request to list  of all Comment Thread")

        queryset = self.get_queryset(request)
        page = self.paginate_queryset(queryset)
        serializer = self.serializer_class(page, many=True)
        return self.get_paginated_response(serializer.data)


class SubCommentCreateView(generics.CreateAPIView):
    __doc__ = """
    Create View for the reply of Main Comment Thread Section
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SubCommentSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        data = request.data
        data["user"] = user.id
        comment_id = data.get('comment_id')
        logger.info(f"{user} request to create reply of comment thread with data  {data}")
        serializer = self.serializer_class(data=data)

        if not serializer.is_valid(raise_exception=True):
            return Response(
                {"status": False, "message": serializer.errors},
                status=status.HTTP_200_OK,
            )

        sub_comment = serializer.save()
        comment = Comment.objects.get(id=comment_id)
        comment.sub_comment.add(sub_comment)
        return Response(
            {"status": True, "data": serializer.data}, status=status.HTTP_201_CREATED
        )


class SubCommentDeleteView(generics.DestroyAPIView):
    __doc__ = """
    Delete View for the mail broadcast
    """

    permission_classes = (IsAuthenticated,)

    def destroy(self, request, *args, **kwargs):
        user = request.user
        logger.info(f"{user} request to delete comment thread {kwargs}")
        queryset = SubComment.objects.filter(user=user)
        if not queryset.filter(id=kwargs.get("pk")).exists():
            return Response(
                {"status": False, "message": "Comment not found"},
                status=status.HTTP_200_OK,
            )

        instance = queryset.get(id=kwargs.get("pk"))
        instance.delete()
        return Response(
            {"status": True, "message": "Comment  deleted"},
            status=status.HTTP_200_OK,
        )


class SubCommentUpdateView(generics.UpdateAPIView):
    __doc__ = """
    Update View for the  reply of comment thread 
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.SubCommentSerializer

    queryset = SubComment.objects.all()

    def put(self, request, *args, **kwargs):
        user = request.user
        data = self.partial_update(request, *args, **kwargs)
        logger.info(f"{user} request update the reply of  comment section {request.data}")
        return Response(
            {"status": True, "data": data.data},
            status=status.HTTP_200_OK,
        )
