from django.shortcuts import render
from .models import Myskill,Contactinfo


def index(request):
    my_item = Myskill.objects.all()

    title = 'WELCOME TO OUR SERVICES'
    desc = 'Mobile phones and other digital media and platforms to promote products and services internet and online based digital technologies such as desktop computers, '
    context ={
        'my_title':title, 
        'description':desc,
        'data':my_item
    }
    return render(request , 'index.html', context)

def about(request):
    title='About Page'
    desc='Master the basics of digital marketing with our free course accredited by Interactive Advertising Bureau Europe and The Open University. There are 26 modules to explore, all created by Google trainers, packed full of practical exercises and real-world examples to help you turn knowledge into action.'

    context = {
        'about_title' : title,
        'descive': desc,
    }
    return render(request, 'about.html', context)



def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('comments')

        mydata = Contactinfo(cname=name,cemail=email,cquery=query)
        mydata.save()
   
    return render(request, 'contact.html')