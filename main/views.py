from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'store' : 'Shopaholic',
        'name': 'Olav Dendy Christian Manullang',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)