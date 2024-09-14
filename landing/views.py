from django.shortcuts import render

# Create your views here.
ctx = {
    'footer': [{
            'link': 'https://www.facebook.com/itstep.tashkent',
            'img': 'https://tashkent.itstep.org/dist/images/src/images/academy/footer/f.svg',
            'class': 'footer-new__link footer-new__link--fb'
        },{
            'link': 'https://www.instagram.com/itstep.tashkent/',
            'img': 'https://tashkent.itstep.org/dist/images/src/images/academy/footer/ins.svg',
            'class': 'footer-new__link footer-new__link--insta'
        },{
            'link': 'https://t.me/itstep_tashkent',
            'img': 'https://tashkent.itstep.org/dist/images/src/images/icons/social-links/2.svg',
            'class': 'footer-new__link footer-new__link--telega'
        },]
    }

def index(request):
    return render(request, 'landing/index.html', ctx)

def about(request):
    return render(request, 'landing/about.html', ctx)

def contact(request):
    return render(request, 'landing/contact.html', ctx)