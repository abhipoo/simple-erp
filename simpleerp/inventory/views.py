from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory, Sales
from .forms import JobForm
from datetime import datetime

# Create your views here.

def inventory(request):
    #return HttpResponse("This is inventory page")
    inventory_list = Inventory.objects.all()
    context = {'inventory_list' : inventory_list}
    return render(request, 'inventory/inventory_master.html', context)


def sales(request):
    #return HttpResponse("This is sales page.")
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            #print('form is valid')

            #save to POS
            post = form.save(commit=False)
            post.job_date = datetime.now()
            post.save()

            #deduct from inventory
            change_inventory(post.sku, post.qty)

        else:
            print("Form invalid")
            print(form.errors)

    form = JobForm()
    context = {
        'form' : form 
    }
    return render(request, 'inventory/sales_create_job.html', context)


def dashboard(request):
    return HttpResponse("This is dashboard page.")



'''
Helper functions
'''


def change_inventory(input_sku, input_quantity):
    '''
    Subtracts the given quantity from given sku in database
    '''
    try:
        i = Inventory.objects.get(sku = input_sku)
        i.quantity = i.quantity - input_quantity
        i.save()
    except:
        print("Error in change_inventory")
