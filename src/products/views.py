from django.shortcuts import render
from products.models import Product, Purchase
import pandas as pd
# Create your views here.
def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    print(product_df)
    context={
        'products' : product_df.to_html,
        'purchases' : purchase_df.to_html,
    }
    return render(request, 'products/main.html',context)