from django.core.paginator import Paginator
from django.views import generic
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.utils.translation import activate
# def store(request, page=1):
#     all_products = Product.objects.all()
#     paginator = Paginator(all_products, 1)
#     page_number = request.get(page)
#     page_obj = paginator.get_page(page_number)
#     context = {'my_products': page_obj}
#     return render(request, 'store/store.html', context=context)

def change_language(request):

    activate(request.GET.get('lang'))

    return redirect(request.GET.get('next'))


class Store(generic.ListView):
    queryset = Product.objects.all()

    template_name = 'store/store.html'

    context_object_name = 'my_products'

    paginate_by = 5


class AscendingPrice(generic.ListView):
    queryset = Product.objects.all().order_by('price')

    template_name = 'store/store.html'

    context_object_name = 'my_products'

    paginate_by = 5
    
# def ascending_price(request):
#     all_products = Product.objects.all().order_by('price')
#     return render(request, 'store/store.html', { "my_products" : all_products})

class DescendingPrice(generic.ListView):
    queryset = Product.objects.all().order_by('-price')

    template_name = 'store/store.html'

    context_object_name = 'my_products'

    paginate_by = 5


class AscendingTime(generic.ListView):
    queryset = Product.objects.all().order_by('datetime_created')

    template_name = 'store/store.html'

    context_object_name = 'my_products'

    paginate_by = 5



class DescendingTime(generic.ListView):
    queryset = Product.objects.all().order_by('-datetime_created')

    template_name = 'store/store.html'

    context_object_name = 'my_products'

    paginate_by = 5





def categories(request):
    all_categories = Category.objects.all()
    return {'all_categories': all_categories}





def list_category(request, category_slug=None):

    category = get_object_or_404(Category, slug=category_slug)

    products = Product.objects.filter(category=category)


    return render(request, 'store/list-category.html', {'category':category, 'products':products})

def product_info(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    contex={'product': product}
    return render(request, 'store/product-info.html', contex)


# Create Your ProductSearchListView By classbased.
class SearchProduct(generic.ListView):
    paginate_by = 2
    template_name = 'store/search_product.html'
    def get_queryset(self):
        search = self.request.GET.get('q')
        return Product.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        search = self.request.GET.get('q')

        context['search'] = search
        
        context['my_products'] = Product.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))
        
        return context

