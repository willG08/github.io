from django.shortcuts import render, HttpResponse
from .models import PortfolioModel, Hobbies

#in case I can figure out how to implement it
# def index(request):
#      context={}
#      return render(request, 'PortfolioDatabase/home.html', context)

# Create your views here.
def home(request):
    hobbies_list = Hobbies.objects.all()
    portfolio_list = PortfolioModel.objects.all()
    context = {
          'hobbies_list': hobbies_list,
          'portfolio_list': portfolio_list,
    }
    return render(request, 'PortfolioDatabase/home.html', context)
    #return HttpResponse("Hello, I'm Will Gunther! Welcome to my Portfolio made with Django! I got married in August to the love of my life. I am geared up to graduate in August. Luckily, I only need to take 1 regular class during the summer but I am still working hard to find an internship.")
    

def hobbies(request):
    #  hobbies_list = Hobbies.objects.all()
    #  return HttpResponse(hobbies_list)
    hobbies_list = Hobbies.objects.all()
    context = {
          'hobbies_list': hobbies_list,
    }
    return render(request, 'PortfolioDatabase/hobbies.html', context)
    

def portfolio(request):
    # portfolio_list = PortfolioModel.objects.all()
    # return HttpResponse(portfolio_list)
    portfolio_list = PortfolioModel.objects.all()
    context = {
          'portfolio_list': portfolio_list,
    }
    return render(request, 'PortfolioDatabase/portfolio.html', context)

def contact(request):
        context={
             'name': 'Will Gunther',
             'phone': '801-555-5555',
             'email': 'willgunther9@gmail.com',
             'address': '3848 Harrison Blvd, Ogden, UT',
             'description': 'Motivated and detail oriented software developer with a solid foundation in computer science principles and experience in developing scalable projects. Proficient in C#, Javascript, Java, C++, and other languages. Knowledgeable in Windows, Linux, Ubuntu, web development, web applications, full stack development, API’s, version control, database management, machine learning, virtual machine, unit tests, debugging, code reviews, object oriented design, software development lifecycle, Agile methodology, and design documentation. Known for critical listening skills, actively engaging in group discussions to ensure clear understanding and effective solutions. A quick learner who thrives in collaborative environments, ready to apply technical skills and a passion for problem-solving to aid your engineering team.', 
        }
        #return HttpResponse("Hello! My name is Will Gunther and my email is willgunther@mail.weber.edu. Contact me to learn more about my coding experience.")
        return render(request, 'PortfolioDatabase/contact.html', context)

def details(request, hobby_id):
    hobby = Hobbies.objects.get(pk=hobby_id)
    context = {
        'hobby': hobby,
    }
    return render(request, 'PortfolioDatabase/details.html', context)

def portfolioDetails(request, portfolio_id):
    portfolio = PortfolioModel.objects.get(pk=portfolio_id)
    context = {
        'portfolio': portfolio,
    }
    return render(request, 'PortfolioDatabase/portfolioDetails.html', context)