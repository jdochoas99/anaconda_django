from django.shortcuts import render
from pandas.core.reshape.merge import merge
from django.contrib.auth.models import User
from products.models import Product, Purchase
import pandas as pd
# Create your views here.
def chart_select_view(request):
    product_df = pd.DataFrame(Product.objects.all().values())
    product_df['product_id']= product_df['id']
    purchase_df = pd.DataFrame(Purchase.objects.all().values())
    df = pd.merge(purchase_df,product_df, on='product_id',).drop(['id_y','date_y'],axis=1).rename({'id_x': 'id', 'date_x':'date'},axis=1)
    print(product_df)
    context={
        'df': df.to_html(),
        'products' : product_df.to_html(),
        'purchases' : purchase_df.to_html(),
    }
    return render(request, 'products/main.html',context)