from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('adopter', 'Adopter'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    contact_number = models.CharField(max_length=20, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='fixed_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='fixed_user_permissions',
        blank=True
    )

    def is_adopter(self):
        return self.role == 'adopter'

    def is_staff_user(self):
        return self.role == 'staff'

    def is_admin(self):
        return self.role == 'admin'


class UserAccount(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='account'
    )
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)

class UserSignup(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='signup',
        null=True,
        blank=True
    )
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    contact_number = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Application(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')]
    adopter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'adopter'},
        related_name='applications'
    )
    pet = models.ForeignKey('pets.Pet', on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    submitted_at = models.DateTimeField(auto_now_add=True)

class Donation(models.Model):
    donor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='donations'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    item_description = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

class DonationMethod(models.Model):
    METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('check', 'Check'),
        ('paymaya', 'PayMaya'),
        ('gcash', 'GCash'),
        ('cebuana', 'Cebuana'),
        ('bank_transfer', 'Bank Transfer'),
        ('credit_card', 'Credit Card'),
        ('other_online', 'Other Online'),
    ]

    donation = models.ForeignKey(Donation, on_delete=models.CASCADE, related_name='methods')
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    details = models.TextField(blank=True)

class Trial(models.Model):
        pets = models.OneToOneField('pets.Pet', on_delete=models.CASCADE)
        adopter = models.ForeignKey(
            User,
            on_delete=models.CASCADE,
            limit_choices_to={'role': 'adopter'},
            related_name='trials'
        )
        start_date = models.DateField()
        end_date = models.DateField(null=True, blank=True)
        feedback = models.TextField(blank=True)