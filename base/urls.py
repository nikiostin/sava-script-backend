from django.urls import path
from base.Views.CodeViews import CodeListAPIView, CodeDetailAPIView

urlpatterns = [
    path('codes/', CodeListAPIView.as_view(), name='code-list'),
    path('codes/<int:pk>/', CodeDetailAPIView.as_view(), name='code-detail'),
]