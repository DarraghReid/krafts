from django.db import models


# Each message will be added according to this model
class Message(models.Model):
    # Name of user sending message
    full_name = models.CharField(max_length=254, null=False, blank=False)
    # User's email address
    email = models.EmailField(max_length=254, null=False, blank=False)
    # Message user is sending
    message = models.TextField(max_length=500, null=False, blank=False)

    # String method takes in Message model, returns model name
    def __str__(self):
        return self.full_name
