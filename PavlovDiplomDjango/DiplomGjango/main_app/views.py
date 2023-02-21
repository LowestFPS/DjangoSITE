from django.shortcuts import render
from django.views import View
from loguru import logger


class HomePageView(View):
    #Представление начальной страницы сайта

    @logger.catch
    def get(self, request):
       #Отображает шаблон главной страницы сайта

        return render(request, "main_app/home_page.html")
