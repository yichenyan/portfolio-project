from django.shortcuts import render

# Create your views here.
def bloghome(request):
	return render(request, 'blog/bloghome.html')