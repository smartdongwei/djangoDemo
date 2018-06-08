from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length= 30)
    address = models.CharField(max_length= 50)
    city = models.CharField(max_length= 50)
    state_province = models.CharField(max_length= 50)
    country = models.CharField(max_length= 50)
    website = models.URLField()

    def __unicode__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length= 50)
    last_name =models.CharField(max_length= 50)
    email = models.EmailField(blank= True,verbose_name="电子邮箱")
    def __unicode__(self):
        return u'%s %s ' % (self.first_name, self.last_name)

class Book(models.Model):
    title =  models.CharField(max_length= 50)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.SET_NULL,blank= True , null= True)
    publication_date = models.DateField()
    def __unicode__(self):
        return self.title

