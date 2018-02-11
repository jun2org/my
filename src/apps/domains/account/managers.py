from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(email=self.normalize_email(email), is_staff=False, is_active=True, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.model(email=self.normalize_email(email), is_staff=True, is_superuser=True, is_active=True, **kwargs)
        user.set_password(password)
        user.save()
        return user
