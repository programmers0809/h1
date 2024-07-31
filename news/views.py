# from django.shortcuts import render
# from django.views import View
# from .models import CategoryModel,NewsModel

# class HomeView(View):
#     def get(self, request):
#         category_list = CategoryModel.objects.all()
#         all_news_list = NewsModel.manager.all().order_by('-publish_time')
#         context = {
#             'category_list': category_list  # Kalitlar string bo'lishi kerak
#                         'all_news_list': all_news_list

            
#         }
#         return render(request, 'news/home.html', context)


# class ContactView(View):
#     def get(self, request):
#         context = {}  # Add any context data if needed
#         return render(request=request, template_name='news/contact.html', )

# class NewsDetailView(View):
#     def get(self, request):
#         context = {}  # Add any context data if needed
#         return render(request=request, template_name='news/news_detail.html', )

# from django.shortcuts import render
# from django.views import View
# from .models import CategoryModel, NewsModel

# class HomeView(View):
#     def get(self, request):
#         category_list = CategoryModel.objects.all()
#         all_news_list = NewsModel.manager.all().order_by('-publish_time')
#         uzb_news_list =NewsModel.manager.all.filter(category_name="O'zbekiston").order_by('-publish_time')[:6]
#         context = {
#             'category_list': category_list,  # Kalitlar string bo'lishi kerak
#             'all_news_list': all_news_list,
#             'uzb_news_list' :uzb_news_list
#         }
#         return render(request, 'news/home.html', context)
from django.shortcuts import render
from django.views import View
from .models import CategoryModel, NewsModel

class HomeView(View):
    def get(self, request):
        category_list = CategoryModel.objects.all()
        all_news_list = NewsModel.objects.all().order_by('-publish_time')  # 'manager' o'rniga 'objects' ishlatilmoqda
        uzb_news_list = NewsModel.objects.filter(category__name="O'zbekiston").order_by('-publish_time')[:6]  # 'all' chaqiruvini olib tashlang

        context = {
            'category_list': category_list,
            'all_news_list': all_news_list,
            'uzb_news_list': uzb_news_list
        }
        return render(request, 'news/home.html', context)


class ContactView(View):
    def get(self, request):
        context = {}  # Kerak bo'lsa, har qanday kontekst ma'lumotlarini qo'shing
        return render(request, 'news/contact.html', context)


class NewsDetailView(View):
    def get(self, request):
        context = {}  # Kerak bo'lsa, har qanday kontekst ma'lumotlarini qo'shing
        return render(request, 'news/news_detail.html', context)
