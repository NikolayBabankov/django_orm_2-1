from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article,Category,ArticleCategory

class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        list_main = []
        for form in self.forms:
            form.cleaned_data
            if form.cleaned_data == {}:
                break
            main = form.cleaned_data['is_main']
            if main:
                list_main.append(1)
        if len(list_main) > 1:
            raise ValidationError('У статьи может быть только одна основная категория')
        return super().clean()

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

class RelationshipInline(admin.TabularInline):
    model = ArticleCategory
    formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]