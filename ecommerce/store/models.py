from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=250, db_index=True)

    slug = models.SlugField(max_length=250, unique=True)


    class Meta:

        verbose_name_plural = 'categories'


    def __str__(self):

        return self.name


    def get_absolute_url(self):

        return reverse('list-category', args=[self.slug])


class ProductManager(models.Manager):
    def ascending_price(self):
        return self.all().order_by('price')

    def descending_price(self):
        return self.all().order_by('-price')


class Product(models.Model):

    #FK 

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True, verbose_name="category")


    title = models.CharField(_("title"), max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    image = models.ImageField(upload_to='images/')

    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now())
    
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now=True)

    class Meta:

        verbose_name_plural = _('products')


    def __str__(self):

        return self.title



    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])

    objects = ProductManager()

