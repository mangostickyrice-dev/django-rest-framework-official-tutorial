from django.urls import path
from rest_api import views

urlpatterns = [
    
    # #! class base
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
    path('', views.api_root),
    
    # #! Authentication
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    
    # #! procedurl function
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail), 
]