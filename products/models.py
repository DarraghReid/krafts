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


# Each product will be added according to this model
class Products(models.Model):
    # category is foreign key to Category model
    # If category deleted, its products' category will be null
    # Only name, description, price and required
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # String method takes in Category model, returns model name
    def __str__(self):
        return self.name
