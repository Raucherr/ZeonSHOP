from rest_framework import generics, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .models import News, AboutUs, HelpQA, OurAdvantages, SliderMainPage,\
    PublicOffer, CallBack, FooterHeaderObjects
from .serializers import *


class ListNewsPagination(PageNumberPagination):
    """
    нумерация страниц
    """
    page_size = 8


class ListNews(generics.ListAPIView):
    """
    список новостей в системе.
    """
    queryset = News.objects.all().order_by('-publish')
    serializer_class = NewsSerializer
    pagination_class = ListNewsPagination


class AboutUsView(generics.ListAPIView):
    """
    about us
    """
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class HelpQAView(generics.ListAPIView):
    """
    q/a
    """
    queryset = HelpQA.objects.all()
    serializer_class = HelpQASeralizer


class OurAdvantagesView(generics.ListAPIView):
    """
    список преимуществ
    """
    queryset = OurAdvantages.objects.all()
    serializer_class = OurAdvantagesSeralizer


class SliderMainPageView(generics.ListAPIView):
    """
    ссылки на изображения слайдера на главной 
    """
    queryset = SliderMainPage.objects.all()
    serializer_class = SliderMainPageSeralizer


class PublicOfferView(generics.ListAPIView):
    """
    публичная оферта
    """
    queryset = PublicOffer.objects.all()
    serializer_class = PublicOfferSeralizer


class CallBackViewSet(viewsets.ModelViewSet):
    """
    обратный вызов
    """
    queryset = CallBack.objects.all()
    serializer_class = CallBackSerializer
    permission_classes = [AllowAny, ]


class FooterHeaderObjectsView(generics.ListAPIView):
    """
    футеры и хедеры 
    """
    queryset = FooterHeaderObjects.objects.all()
    serializer_class = FooterHeaderObjectsSerializer