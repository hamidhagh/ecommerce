from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from translated_fields import TranslatedField


class Category(models.Model):

    name = TranslatedField(models.CharField(_("name"),max_length=250, db_index=True))

    slug = models.SlugField(_("slug"),max_length=250, unique=True)


    class Meta:

        verbose_name_plural = _('categories')
        verbose_name = _('category')


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

    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True, verbose_name=_("category"))


    title = TranslatedField(models.CharField(_("title"), max_length=250,))

    brand = models.CharField(_("brand"), max_length=250, default='un-branded')

    description = TranslatedField(models.TextField(_("description"), blank=True, null=True))

    slug = models.SlugField(_("slug"), max_length=255)

    price = models.BigIntegerField(_("price"), default=1)

    image = models.ImageField(_("image"), upload_to='images/')

    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now())
    
    datetime_modified = models.DateTimeField(_('datetime_modified'), auto_now=True)

    class Meta:

        verbose_name_plural = _('products')
        verbose_name = _('product')


    def __str__(self):

        return self.title



    def get_absolute_url(self):

        return reverse('product-info', args=[self.slug])

    objects = ProductManager()

