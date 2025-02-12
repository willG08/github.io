from django.db import models

# Create your models here.
class Hobbies(models.Model):
    hobby_name = models.CharField(max_length=200)
    hobby_description = models.TextField()
    hobby_years = models.DecimalField(max_digits=10, decimal_places=1)
    hobby_image = models.CharField(max_length=500, default="https://th.bing.com/th/id/OIP.Uj-WLdfpgM4fBj8dhWe5VAHaHd?w=197&h=199&c=7&r=0&o=5&pid=1.7")
    #override the string method, 2 under scores before and after str
    #def __str__(self):
    #    return f"I have done {self.hobby_name} as a hobby for {self.hobby_years} years. {self.hobby_name} is {self.hobby_description}."


class PortfolioModel(models.Model):
    portfolio_name = models.CharField(max_length=200)
    portfolio_description = models.TextField()
    portfolio_created = models.CharField(max_length=100, default="January, 2025")
    portfolio_image = models.CharField(max_length=500, default="https://th.bing.com/th/id/OIP.Uj-WLdfpgM4fBj8dhWe5VAHaHd?w=197&h=199&c=7&r=0&o=5&pid=1.7")
     #override the string method, 2 under scores before and after str
    #def __str__(self):
    #    return f"I created a {self.portfolio_name} project. {self.portfolio_description}."

#PortfolioModel.objects.create(portfolio_name='Russell Detailing', portfolio_description ='I created a website for a company in Ogden. I created the layout and revisions with the company owner and delivered a project that exceeded expectations.')

