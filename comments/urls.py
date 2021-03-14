
from django.urls import path
from comments import views

urlpatterns = [
    path('create/', views.CommentCreateView.as_view()),
    path('list/', views.CommentListView.as_view()),
    path('update/<int:pk>/', views.CommentUpdateView.as_view()),
    path('delete/<int:pk>/', views.CommentDeleteView.as_view()),
    path('retrieve/<int:pk>/', views.CommentDetailListView.as_view()),
    path('get-all-comments/', views.CommentListAllView.as_view()),
    path('sub-comment/create/', views.SubCommentCreateView.as_view()),
    path('sub-comment/delete/<int:pk>/', views.SubCommentDeleteView.as_view()),

]
