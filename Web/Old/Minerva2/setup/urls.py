from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('users.urls')),
    path('professor/', include('professor.urls')),
    path('aluno/', include('aluno.urls')),
]

# # project/urls.py
# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('user/', include('user.urls')),
#     path('professor/', include('professor.urls')),
#     path('aluno/', include('aluno.urls')),
# ]
