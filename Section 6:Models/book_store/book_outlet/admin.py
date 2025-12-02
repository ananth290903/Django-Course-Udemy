from django.contrib import admin
from .models import Book,Author,Address,Country




class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("title",)}
    list_display=("title","author",)


class AuthorAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name",)

class CountryAdmin(admin.ModelAdmin):
    list_display=("name","code",)


admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Address)
admin.site.register(Country,CountryAdmin)
































# from django.contrib import admin
# from .models import Book 
# # Register your models here.



# class BookAdmin(admin.ModelAdmin):
#     # readonly_fields=("slug",)
#     # prepopulated_fields={"slug":("title",)}
#     list_filter=("rating","author",)
#     list_display=("title","author",)


# admin.site.register(Book,BookAdmin)

