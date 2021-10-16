from django.db import models
from django.contrib.auth.models import User
from .utils import generate_sku


class Category(models.Model):
    """ Define structure of Category model in db """
    class Meta:
        """ Define verbose name of this model for admin display """
        verbose_name_plural = "Categories"

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


class Product(models.Model):
    """ Define structure of Product model in db """
    # category is foreign key to Category model
    # If category deleted, its product's category will be null
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=True, blank=True, default=generate_sku)
    # Only name, description, price and required
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    # String method takes in Product model, returns model name
    def __str__(self):
        return self.name


# Each comment will be added according to this model
class Comment(models.Model):
    """ Define structure of Comment model in db """
    # product is foreign key to Product model
    # If a product is deleted, associated comments will also be deleted
    product = models.ForeignKey(
        "Product", related_name="comments", on_delete=models.CASCADE)
    name = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    # Automatically add date to comment
    date = models.DateTimeField(auto_now_add=True)
    # Parent field indicates if comment is being replied to, or is in reply to
    parent = models.ForeignKey(
        "self", related_name="+", on_delete=models.CASCADE, blank=True, null=True)

    @property
    def children(self):
        """ Return list of child comments of a parent comment
            to be accessed in the template """
        return Comment.objects.filter(parent=self).order_by('-date').all()

    @property
    def is_parent(self):
        """ Determine if comment is parent or child comment """
        # If there is nothing in the parent field/has no parent
        if self.parent is None:
            # the comment is a parent comment
            return True
        # Otherwise, the comment has a parent/is a child comment
        else:
            return False

    # String method takes in Comment model, returns related product & user names
    def __str__(self):
        return '%s' % (self.pk)
