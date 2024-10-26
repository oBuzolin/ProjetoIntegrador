import hashlib
from django.contrib.auth.backends import BaseBackend
from .models import Minerva_Professor, User

class EmailBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            professor = Minerva_Professor.objects.get(email=username)
            # Realiza o hashing da senha com SHA-256
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

            # Verifica se a senha hash corresponde
            if professor.senha == hashed_password:
                user, created = User.objects.get_or_create(professor_matricula=professor)
                return user
        except Minerva_Professor.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
