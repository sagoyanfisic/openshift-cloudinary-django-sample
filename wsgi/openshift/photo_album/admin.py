from django.contrib import admin
from .models import Profile
from django.contrib.admin import DateFieldListFilter

admin.site.register(Profile)

'''
@admin.register(Profile)
class DishAdmin(admin.ModelAdmin):
    pass

    exclude = ()
    list_display = ()#,'priority')
    list_editable = ()#,'priority')
    actions = ['guardado']
    list_filter = (
        ('create_time', DateFieldListFilter),
    )

'''

