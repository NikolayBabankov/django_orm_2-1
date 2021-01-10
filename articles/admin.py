from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article,Category,ArticleCategory

# class RelationshipInlineFormset(BaseInlineFormSet):
#     def clean(self):
#         for form in self.forms:
#             # В form.cleaned_data будет словарь с данными
#             # каждой отдельной формы, которые вы можете проверить
#             form.cleaned_data = 1
#             # вызовом исключения ValidationError можно указать админке о наличие ошибки
#             # таким образом объект не будет сохранен,
#             # а пользователю выведется соответствующее сообщение об ошибке
#             raise ValidationError('Тут всегда ошибка')
#         return super().clean()  # вызываем базовый код переопределяемого метода

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

class RelationshipInline(admin.TabularInline):
    model = ArticleCategory
    # formset = RelationshipInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]