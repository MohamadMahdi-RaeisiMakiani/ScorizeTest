from django.contrib import admin
from .models import Countries_to_apply, Cities_to_apply, University_to_apply


class countries_sendto_admin(admin.ModelAdmin):
    list_display = ('id', 'Country_Name',)


class cities_sendto_admin(admin.ModelAdmin):
    list_display = ('id', 'from_country', 'City_Name')


class universities_sendto_admin(admin.ModelAdmin):
    list_display = ('id', 'from_city', 'Uni_Name', 'Uni_Acronym', 'Uni_Logo', 'Uni_Type',
                    'Uni_EstablishedYear', 'Uni_All_Students', 'Uni_International_Students', 'Uni_Website', 'Uni_ApplyRate')


admin.site.register(Countries_to_apply, countries_sendto_admin)
admin.site.register(Cities_to_apply, cities_sendto_admin)
admin.site.register(University_to_apply, universities_sendto_admin)
