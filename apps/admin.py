from django.contrib import admin

from apps.models import Galaxy, Planet, Group, Star, Gallery, Exploration, About, Holes_Matter, Register

# from apps.models import Product, Category
#
# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Galaxy)
admin.site.register(Planet)
admin.site.register(Group)
admin.site.register(Star)
admin.site.register(Gallery)
admin.site.register(Exploration)
admin.site.register(About)
admin.site.register(Holes_Matter)
admin.site.register(Register)

from django.contrib import admin
from .models import Fakt_turi, Faktlar


class FaktlarInline(admin.TabularInline):
    model = Faktlar
    extra = 1


@admin.register(Fakt_turi)
class FaktTuriAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [FaktlarInline]


@admin.register(Faktlar)
class FaktlarAdmin(admin.ModelAdmin):
    list_display = ('title', 'fakt')
    list_filter = ('fakt',)
