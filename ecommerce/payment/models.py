from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from store.models import Product

# Create your models here.



class ShippingAddress(models.Model):

    full_name = models.CharField(_("full_name"), max_length=300)

    email = models.EmailField(_("email"), max_length=255)

    address1 = models.CharField(_("address1"), max_length=300)

    address2 = models.CharField(_("address2"), max_length=300)

    city = models.CharField(_("city"), max_length=255)


    # Optional

    state = models.CharField(_("state"), max_length=255, null=True, blank=True)

    zipcode = models.CharField(_("zipcode"), max_length=255, null=True, blank=True)


    # FK

    # Authenticated / not authenticated users (bear in mind)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))


    class Meta:

        verbose_name_plural = _('Shipping Address')
        verbose_name = _('Shipping Address')



    def __str__(self):

        return 'Shipping Address - ' + str(self.id)
    


class Order(models.Model):

    full_name = models.CharField(_("full_name"), max_length=300)

    email = models.EmailField(_("email"), max_length=255)

    shipping_address = models.TextField(_("shipping_address"), max_length=10000)

    amount_paid = models.BigIntegerField(_("amount_paid"), default=1)

    date_ordered = models.DateTimeField(_("date_ordered"), auto_now_add=True)


    # FK

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))


    class Meta:

        verbose_name_plural = _('Orders')
        verbose_name = _('Order')

    def __str__(self):

        return 'Order - #' + str(self.id)




class OrderItem(models.Model):

    # FK -> 

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name=_("order"))

    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("product"))


    quantity = models.PositiveBigIntegerField(_("quantity"), default=1)

    price = models.DecimalField(_("price"), max_digits=8, decimal_places=2)    

    datetime_created = models.DateTimeField(_('datetime_created'), default=timezone.now())

    # FK

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("user"))

    class Meta:

        verbose_name_plural = _('Order Items')
        verbose_name = _('Order Item')


    def __str__(self):

        return 'Order Item - #' + str(self.id)


