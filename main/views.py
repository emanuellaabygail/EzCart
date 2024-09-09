from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'project_name' : 'EzCart',
        'name' : 'Emanuella Abygail',
        'class' : 'PBP C',
        'product_name' : 'Anjay',
        'price': 1000000,
        'description': 'Anjay'
    }

    return render(request, "main.html", context)