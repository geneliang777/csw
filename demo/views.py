from django.shortcuts import render

def demo_view(request):
    """
    A simple view to demonstrate rendering a template.
    """
    # context = {
    #     'message': 'Hello, this is a demo view!'
    # }
    # return render(request, 'demo/demo_template.html', context) 
    return render(request, 'demo_django.html',{'data':'This is demo page'}
                  )
# Create your views here.
