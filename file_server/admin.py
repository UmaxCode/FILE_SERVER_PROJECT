from django.contrib import admin

from .models import Document

# Register your models here.

class AdminDocument(admin.ModelAdmin):
    
    list_display = (
        "title",
        "description",
        "file",
        "num_downloads"
    )


admin.site.register(Document, AdminDocument)

