from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('professor/', include('professor.urls')),
    path('aluno/', include('aluno.urls')),
    # outras URLs
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
