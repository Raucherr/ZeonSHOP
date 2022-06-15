from rest_framework import serializers
from .models import *

"сериялайзер для новостей"
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

"сериялайзер для 'About us'"
class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

"сериялайзер для q/a"
class HelpQASeralizer(serializers.ModelSerializer):
    class Meta:
        model = HelpQA
        fields = '__all__'

"сериялайзер для фото q/a"
class ImageHelpQASeralizer(serializers.ModelSerializer):
    class Meta:
        model = ImageHelpQA
        fields = ['image']

"сериялайзер для наши преимущества"
class OurAdvantagesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = OurAdvantages
        fields = '__all__'

"сериялайзер для слайдеров"
class SliderMainPageSeralizer(serializers.ModelSerializer):
    class Meta:
        model = SliderMainPage
        fields = '__all__'

"сериялайзер для  публичной оферты"
class PublicOfferSeralizer(serializers.ModelSerializer):
    class Meta:
        model = PublicOffer
        fields = '__all__'

"сериялайзер для обратного звонка"
class CallBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallBack
        fields = ('user_name', 'user_phone', 'type_of_treatment')

"сериялайзер для объектов футера и хедера"
class FooterHeaderObjectsSerializer(serializers.ModelSerializer):
    social_type = serializers.StringRelatedField(many=True)

    class Meta:
        many = True
        model = FooterHeaderObjects
        fields = '__all__'