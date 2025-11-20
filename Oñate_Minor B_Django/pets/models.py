from django.db import models

class Pet(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Male"
        FEMALE = "female", "Female"

    class Status(models.TextChoices):
        AVAILABLE = "available", "Available"
        ADOPTED = "adopted", "Adopted"
        INACTIVE = "inactive", "Inactive"

    class PetType(models.TextChoices):
        DOG = "dog", "Dog"
        CAT = "cat", "Cat"
        OTHER = "other", "Other"

    name = models.CharField(max_length=50)
    pet_type = models.CharField(
        max_length=10,
        choices=PetType.choices,
        default=PetType.OTHER,
        blank=True,
        null=True,
    )
    other_pet_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Specify if pet_type is 'Other' (e.g., Rabbit, Bird)"
    )
    breed = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    birth_date = models.DateField(blank=True, null=True)
    health = models.TextField(blank=True)
    favorite_food = models.CharField(max_length=100, blank=True)
    favorite_toy = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AVAILABLE)
    likes = models.CharField(max_length=100, blank=True)
    hates = models.CharField(max_length=100, blank=True)

    def __str__(self):
        if self.pet_type == self.PetType.OTHER and self.other_pet_type:
            return f"{self.name} ({self.other_pet_type})"
        return f"{self.name} ({self.pet_type})"

    class Meta:
        ordering = ["name"]
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
