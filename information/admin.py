from django.contrib import admin
from .models import News, AboutUs, HelpQA, OurAdvantages, SliderMainPage, \
    PublicOffer, CallBack, SocialTypes, FooterHeaderObjects


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish')


class AboutUsAdmin(admin.ModelAdmin):

    list_display = ('title',)

    def has_add_permission(self, request):
        """ limit for add info."""
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)


class HelpQAAdmin(admin.ModelAdmin):
    list_display = ('question', )


@admin.register(CallBack)
class CallBackAdmin(admin.ModelAdmin):
    list_display = ('type_of_treatment', 'called_status', 'published',)
    search_fields = ('user_name', 'user_phone',)
    list_filter = ('called_status',)


@admin.register(SocialTypes)
class SocialTypesAdmin(admin.ModelAdmin):
    list_display = ('contact_type', 'link_to')


admin.site.register(News, NewsAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(HelpQA, HelpQAAdmin)
admin.site.register(OurAdvantages)
admin.site.register(SliderMainPage)
admin.site.register(PublicOffer)
admin.site.register(FooterHeaderObjects)