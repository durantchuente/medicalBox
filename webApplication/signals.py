from django.contrib.auth.signals import user_logged_in
from django.db import connections
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

@receiver(user_logged_in)
def switch_database_user(sender, request, user, **kwargs):
    """
    Modifie les paramètres de connexion à la base de données après qu'un utilisateur s'est connecté.
    Cette version gère les erreurs d'encodage dans le nom d'utilisateur.
    """
    try:
        # Récupérer le nom d'utilisateur
        postgres_user = user.username

        # Corriger l'encodage si nécessaire
        postgres_user = clean_username(postgres_user)

        # Mot de passe utilisateur (assurez-vous de gérer cela en toute sécurité)
        password = user.password  # Remplacez par une méthode sécurisée pour gérer les mots de passe

        # Modifier les paramètres de connexion de la base de données 'default'
        db_connection = connections['default']
        db_connection.settings_dict['USER'] = "userP"
        db_connection.settings_dict['PASSWORD'] = "qwerty"
        db_connection.close()  # Fermer l'ancienne connexion si elle existe

        logger.info(f"Connexion à la base de données modifiée pour l'utilisateur {postgres_user}.")
    except UnicodeDecodeError as e:
        logger.error(f"Erreur d'encodage avec l'utilisateur {user.username}: {e}")
    except Exception as e:
        logger.error(f"Erreur lors de la modification de la connexion : {e}")

def clean_username(username):
    """
    Fonction pour corriger les problèmes d'encodage dans le nom d'utilisateur.
    Elle remplace les caractères invalides par des caractères de remplacement.
    """
    try:
        # Essayons de décoder correctement en utf-8
        return username.encode("latin1").decode("utf-8", errors="replace")
    except UnicodeDecodeError:
        # En cas d'échec, forcer l'encodage en utf-8 avec remplacement
        return username.encode("utf-8", errors="replace").decode("utf-8")
