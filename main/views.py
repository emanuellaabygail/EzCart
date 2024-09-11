from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'project_name' : 'EzCart',
        'name' : 'Emanuella Abygail',
        'npm' : '2306152185',
        'class' : 'PBP C',
        'product_name' : 'Buku The Poppy War',
        'price': 250000,
        'description': 'A historical fantasy novel about a war orphan fighting everyone in her way while getting more and more unhinged'
    }

    return render(request, "main.html", context)