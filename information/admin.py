
from django.contrib import admin
from .models import *


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish')


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):

    list_display = ('title',)

    def has_add_permission(self, request):
        """функция лимита для - 'About us'."""
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(HelpQA)
class ImageHelpQAAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        """лимит для фото в - helpQA."""
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class HelpQAAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('type_of_treatment', 'called_status', 'published',)
    search_fields = ('user_name', 'user_phone',)
    list_filter = ('called_status',)


@admin.register(SocialTypes)
class SocialTypesAdmin(admin.ModelAdmin):
    list_display = ('contact_type', 'link_to')


@admin.register(FooterHeaderObjects)
class FooterHeaderObjectsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """ограничение для добавления объектов нижнего колонтитула Верхнего колонтитула."""
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(PublicOffer)
class PublicOfferAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """лимит на добавление Публичной оферты."""
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


@admin.register(SliderMainPage)
class SliderMainPageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        """лимит для главной страницы добавления слайдера."""
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


admin.site.register(OurAdvantages)
admin.site.register(ImageHelpQA, ImageHelpQAAdmin)