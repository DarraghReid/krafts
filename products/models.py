from django.db import models


# Each product will have a category which follows this model
class Category(models.Model):
    # Character field representing programmatic name
    name = models.CharField(max_length=254)
    # Friendly name for front end is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    # String method takes in Category model, returns model name
    def __str__(self):
        return self.name

    # Model method returns friendly name
    def get_friendly_name(self):
        return self.friendly_name
