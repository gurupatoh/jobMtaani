from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
# user and client
class CustomUser(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    user_location = models.CharField(max_length = 150)
    email=models.EmailField(unique=True)
    email=models.EmailField(default='patrickn0023@gmail.com',unique=True)
    client_location = models.CharField(max_length=255,default='ruiru')
    client_description = models.TextField(default="There is currently no description available for this company.")
    def __str__(self):
        return self.first_name

  
# class Client(models.Model):
#     """
#     Simply contains company details, referenced by Placement model
#     """

#     client_name = models.CharField(max_length=120,default='clientname')
#     email=models.EmailField(default='patrickn0023@gmail.com',unique=True)
#     client_location = models.CharField(max_length=255)
#     client_description = models.TextField(default="There is currently no description available for this company.")
#     password=models.CharField(max_length=100)
#     Confirmpassword=models.CharField(max_length=100)


#     username = None

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     def __str__(self):
#         return self.client_name



class Placement(models.Model):
    """
    A placement allows investors to bid on company capital raise
    """

    placement_title = models.CharField(max_length=255)
    placement_slug = models.SlugField()
    placement_location = models.CharField(max_length=150)
    placement_quote = models.DecimalField(max_digits=10, decimal_places=2)

    placement_description = models.TextField(default=None)
    placement_category = models.CharField(max_length=200, default="welding")

    placement_created = models.DateTimeField(auto_now_add=True)
    placement_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.placement_title


class Bid(models.Model):
    """
    The bid, synonmous with 'order'
    """
    bid_status = models.BooleanField(default=False)

    bid_created = models.DateTimeField(auto_now_add=True)
    bid_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} -{}'.format(self.user, self.bid_status)


class PlacementBid(models.Model):
    """
    The junction table for placement and bid models/tables. Contains every instance of a bid for a placement
    """

    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    offer = models.IntegerField()
    shares = models.IntegerField()
    confirmed = models.BooleanField(default=False)

    placementbid_created = models.DateTimeField(auto_now_add=True)
    placementbid_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-placementbid_modified']

    def __str__(self):
        return '{} - {} - {}'.format(self.shares, self.offer, self.user)
