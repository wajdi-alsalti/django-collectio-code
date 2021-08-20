from django.db import models
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='categoryPhoto/')
    def __str__(self):
        return self.name



class Cards(models.Model):
    owner = models.CharField(max_length=50)
    header = models.CharField(max_length=100)

    # drop box with options from category 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # on delete delete all data
    
    language_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photo/')
    description = models.TextField(max_length=500)

    # code blog
    code_blog = models.TextField(max_length=5000)

    # date field to show when is the code wrote
    publish_at = models.DateField(auto_now_add=True)

    # slug used to rename the url in website like google/title.com
    slug = models.SlugField(blank=True, null=True)
    
    # function change the save button behavior in admin site override
    def save(self,*args, **kwargs):
        self.slug = slugify(self.header) #slugify convert the spaces in title to (-)
        super(Cards,self).save(*args, **kwargs)

    def __str__(self):
        return self.header


class AddNewCode(models.Model):
    code = models.ForeignKey(Cards, related_name='insert_code', on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # on delete delete all data
    upload_img = models.ImageField(upload_to='uploadImg/')
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return 
