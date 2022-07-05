from email import message
from re import template
from django.shortcuts import render,redirect
from .models import RetailStore
import csv,io
from django.contrib import messages
from .forms import RetailModelForm
from django.db.models import Q
# Create your views here.

def upload_retail_csv(request):
    #serach functionality
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    retail_data = RetailStore.objects.filter(
            Q(store_id__icontains=q)|
            Q(product_name__icontains=q)|
            Q(sku__icontains = q)|
            Q(price__icontains = q)|
            Q(date__icontains =q)
        )
    template = 'retail_details.html'
    

    mydata = {
        'retail_data': retail_data,
    }
    # GET request would returns the  value of the data as appeared in CSV
    if request.method == 'GET':
        return render(request,template,mydata)
    
    #CSV read and write start here
    csv_file = request.FILES['file']

    # Check for csv file 
    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a CSV file")
        return render(request,template,mydata)

    data_set = csv_file.read().decode('UTF-8')

    #setting up stream for looping through each line of data in csv as a stream
    mystring = io.StringIO(data_set)
    next(mystring) # skip the header of csv file
    

    for column in csv.reader(mystring,delimiter=",", quotechar="|"):
        _, created = RetailStore.objects.get_or_create(
            store_id = column[0],
            sku = column[1],
            product_name = column[2],
            price = column[3],
            date = column[4]

        )
        
    retail_data = RetailStore.objects.all()   
    return redirect('csv-data')
    #return render(request,template,{'retail_data':retail_data})  


def update_details(request,pk):
    retailData = RetailStore.objects.get(id=pk)
    form = RetailModelForm(instance=retailData)

    if request.method == 'POST':
        form = RetailModelForm(request.POST, instance=retailData)
        if form.is_valid():
            form.save()
            return redirect('csv-data')
    context = {'form':form}
    return render(request,'update_detail.html',context)

