from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    """This class base function for creating a Custom User model."""

    def create_user(self, email, username, password=None):
        if not username:
            raise ValueError("User must have a unique username.")

        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password=None):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(
            email=email,
            username=username,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
