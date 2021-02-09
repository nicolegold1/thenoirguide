from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Business(models.Model):
    name = models.CharField(max_length=50)

    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=60, blank=True)
    state = models.CharField(max_length=30, blank=True)
    zipcode = models.CharField(max_length=5, blank=True)
    

    phone_number = models.CharField(max_length=22, blank=True )
    description = models.TextField(max_length=700)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length= 100, blank=True)
    # user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    verified= models.BooleanField(default=False)

    # {% if verified == true%}
    # <p>resource.name</p>
    # {%endif%}
    # details page
    


    def __str__(self):
       return self.name


    BUSINESS_CATEGORIES = [
        ('REST', 'Restaurant'),
        ('HAIR', 'Hair Salon'),
        ('BARB', 'Barber Shop'),
        ('ESTH', 'Esthetician'),
        ('NAIL',   'Nail Salon'),
        ('DERM', 'Dermatologist'),
        ('APPL', 'Appliance Repair'),
        ('LAWY', 'Lawyer'),
        ('EVEN', 'Event Planner'),
        ('REAL', 'REALTOR'),
        ('SKIN',  'Skincare'),
        ('CLOT',  'Clothing')
    ]

    business_type = models.CharField(
    # business_list = models.ForeignKey(Business, on_delete=models.CASCADE)
        max_length=4,
        choices=BUSINESS_CATEGORIES,
        default=BUSINESS_CATEGORIES[0][0]
        
    )

   


class Review(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #adding star rating with a template tag



    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.URLField(max_length=100)

#     def __str__(self):
#             return self.user.username
    









    










   



    
  
    





