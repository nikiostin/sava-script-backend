from django.contrib import admin
from base.models.Code import Code
# Register your models here.
@admin.register(Code)
class CodeAdmin(admin.ModelAdmin):
    pass