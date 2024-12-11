from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import Minerva_Professor, User

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            professor = Minerva_Professor.objects.get(usuario=username)
            if check_password(password, professor.senha):
                user, created = User.objects.get_or_create(professor_matricula=professor)
                return user
        except Minerva_Professor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
