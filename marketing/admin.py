from django.contrib import admin

from marketing.models import MarketingPreference


# Register your models here.
class MarketingPreferenceAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subscribed', 'updated']
    readonly_fields = ['mailchimp_msg', 'mailchimp_subscribed', 'timestamp', 'updated']
    class Meta:
        model = MarketingPreference
        fields = [
            'user',
            'subscrbed',
            'mailchimp_msg',
            'mailchimp_subscribed',
            'timestamp',
            'updated'
        ]


admin.site.register(MarketingPreference, MarketingPreferenceAdmin)