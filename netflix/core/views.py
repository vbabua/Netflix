from django.shortcuts import render

# View function to display the index page.abs
def index(request):
    return render(request, 'index.html')
