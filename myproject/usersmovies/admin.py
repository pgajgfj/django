from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    # Відображення колонок у списку
    list_display = ('title', 'release_date', 'id')  # Колонки, які відображатимуться в таблиці
    list_display_links = ('title',)  # Поля, які є посиланнями
    list_editable = ('release_date',)  # Поля, які можна редагувати зі списку

    # Поля для пошуку
    search_fields = ('title', 'description')  # Поля, за якими можна шукати

    # Фільтри
    list_filter = ('release_date',)  # Фільтри для сортування за датою виходу

    # Кількість записів на сторінці
    list_per_page = 10  # Кількість записів, які відображаються на сторінці

    # Сортування за замовчуванням
    ordering = ('release_date',)  # Сортування за датою виходу

# Реєструємо модель і її конфігурацію в адмін-панелі
admin.site.register(Movie, MovieAdmin)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'id', 'image')  # Додаємо зображення в список
    fields = ('title', 'description', 'release_date', 'image')  # Поля для редагування
class MovieAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Основна інформація', {
            'fields': ('title', 'description')
        }),
        ('Додаткова інформація', {
            'fields': ('release_date', 'image'),
            'classes': ('collapse',),  # Робить секцію прихованою
        }),
    )
