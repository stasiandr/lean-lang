from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    @staticmethod
    def validate_input(email, password, first_name, last_name):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        if not first_name:
            raise ValueError("User must have a first name")
        if not last_name:
            raise ValueError("User must have a last name")

    def create_user(self, email, password, first_name="", last_name="", staff=False, admin=False):

        user = self.model(
            email=self.normalize_email(email)
        )
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)  # change password to hash
        user.is_admin = admin
        user.is_staff = staff
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password=None):
        return self.create_user(email, first_name, last_name, password, True, True)

    def create_staffuser(self, email, first_name, last_name, password=None):
        return self.create_user(email, first_name, last_name, password, True, False)


class CustomUser(AbstractBaseUser):
    ADMIN = 'admin'
    STAFF = 'staff'
    STATUS = [
        (ADMIN, 'Admin User'),
        [STAFF, 'Staff User'],
    ]

    class YearInSchool(models.TextChoices):
        TEACHER = 'TE', 'Teacher'
        STUDENT = 'ST', 'Student'

    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=30, default="")
    last_name = models.CharField('last name', max_length=30, default="")

    role = models.CharField(
        max_length=2,
        choices=YearInSchool.choices,
        default=YearInSchool.STUDENT,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # a admin user; non super-user
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['role']

    objects = CustomUserManager()

    @staticmethod
    def has_perm(perm, obj=None):
        # "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    @staticmethod
    def has_module_perms(app_label):
        # "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def __str__(self):
        return "{}".format(self.email)
