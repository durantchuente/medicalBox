from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
import psycopg2

class PostgresAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Connexion à PostgreSQL pour valider les identifiants
            conn = psycopg2.connect(
                dbname='box_medication',
                user=username,
                password=password,
                host='localhost',
                port='5432'
            )
            conn.close()  # Connexion réussie
            
            # Vérifier si l'utilisateur existe dans Django
            user, created = User.objects.get_or_create(username=username)
            if created:
                user.set_unusable_password()  # Mot de passe inutilisable côté Django
                user.save()
            return user
        except psycopg2.OperationalError:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
