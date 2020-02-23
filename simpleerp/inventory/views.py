from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Inventory, Sales, InventoryChangeLog
from .forms import JobForm
from .forms import SkuForm
from .forms import UpdateForm
from datetime import datetime
import traceback


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
            #selected_item = get_object_or_404(Item, pk=request.POST.get('item_id')) #use this to get sku from id
            #print(request.POST)
            sku = request.POST.get('select_sku')

            #save to POS
            post = form.save(commit=False)
            post.sku = sku
            post.job_date = datetime.now()
            post.operator = 'admin' #This should update automatically the username logged in.
            post.save()

            #deduct from inventory
            change_inventory(sku, post.qty)
        else:
            print("Form invalid")
            print(form.errors)


    inventory_list = Inventory.objects.all()

    form = JobForm()
    context = {
        'form' : form,
        'inventory_list' : inventory_list 
    }
    return render(request, 'inventory/sales_create_job.html', context)


def dashboard(request):
    return HttpResponse("This is dashboard page.")

def add_sku(request):
    #return HttpResponse("Add new SKU") 
    if request.method == 'POST':
        form = SkuForm(request.POST)
        if form.is_valid():
            #print('form is valid')

            #save to Inventory
            post = form.save(commit=False)
            post.save()
        else:
            print("Form invalid")
            print(form.errors)


    form = SkuForm()
    context = {
        'form' : form 
    }
    return render(request, 'inventory/add_new_sku.html', context)

def update_sku(request, sku):
    #return HttpResponse("Update x units for %s" % sku)
    if request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            change_type = form.cleaned_data['action']
            comment = form.cleaned_data['comment']

            #update inventory
            change_inventory(sku, quantity, change_type)

            #log in InventoryChangeLog
            print(quantity)
            print(change_type)
            
            i = InventoryChangeLog()
            i.sku = sku
            i.quantity = quantity
            i.change_type = change_type
            i.change_by = 'admin' #This should update automatically the username logged in.
            i.change_date = datetime.now()
            i.comment = comment
            i.save()

        return inventory(request)
    else:
        form = UpdateForm()
        context = {
            'sku' : sku,
            'form' : form
        }

        return render(request, 'inventory/update_sku.html', context)


def inventory_changelog(request):
    inventory_changelog_list = InventoryChangeLog.objects.order_by('-id').all()
    context = {'inventory_changelog_list' : inventory_changelog_list}
    return render(request, 'inventory/inventory_changelog.html', context)

def delete_sku(request, sku):
    context = {'sku' : sku}
    return render(request, 'inventory/confirm_sku_deletion.html', context)

def confirm_delete_sku(request, sku):
    change_inventory(sku, 0, change_type = 'delete')
    return inventory(request)    

def sales_log(request):
    sales_log = Sales.objects.order_by('-id').all()
    context = {'sales_log' : sales_log}
    return render(request, 'inventory/sales_log.html', context)

       
'''
Helper functions
'''


def change_inventory(input_sku, input_quantity, change_type = 'subtract'):
    '''
    Subtracts the given quantity from given sku in database
    '''
    try:
        print(input_sku)
        print(change_type)

        if change_type == 'subtract':
            #Default change type. Applicable for POS as well.
            i = Inventory.objects.get(sku = input_sku)
            i.quantity = i.quantity - input_quantity
            i.save()
        elif change_type == 'add':
            i = Inventory.objects.get(sku = input_sku)
            i.quantity = i.quantity + input_quantity
            i.save()
        elif change_type == 'update':
            i = Inventory.objects.get(sku = input_sku)
            i.quantity = input_quantity
            i.save()
        elif change_type == 'delete':
            i = Inventory.objects.get(sku = input_sku)
            i.delete()
    except:
        #print("Error in change_inventory")
        print(traceback.format_exc())

