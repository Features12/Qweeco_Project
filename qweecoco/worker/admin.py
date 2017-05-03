# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from worker.models import Worker


# Форма для создания новых пользователей
class UserCreationForm(forms.ModelForm):
    """" Форма для создания новых пользователей. Включение всех требуемых полей,
    а также поле повторно ввода пароля. """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Worker
        fields = ('email',)

    def clean_password2(self):
        # Проверка на совпадение двух введённых паролей
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Сохранение пароля в хешированном формате
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# Форма для обновления пользователей
class UserChangeForm(forms.ModelForm):
    """" Форма для обновление пользователей. Включает все поля для пользователей,
    но заменяет поле формата пароля пользователя в админке, на хеш-формат. Эта манипуляция
     делается для безопасности. """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Worker
        fields = ('email', 'password', 'is_active', 'is_admin',)

    def clean_password(self):
        # Независимо от того, что пользователь предоставляет, вернуть первоначальное значение.
        # Это делается здесь, а не на поле, потому что
        # поля не имеют доступа к начальному значению
        return self.initial["password"]


# Форма для добавления и изменения экземпляров пользователей
class WorkerAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    #Поля, которые должны использоваться при отображении модели пользователя.
    # Эти переопределение определений на базе UserAdmin,
    # что ссылается на конкретные поля на авт.Пользователей.
    list_filter = ('is_admin', 'role')
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        ('Personal info', {'fields': ('middle_name', 'first_name', 'last_name', 'role', 'date_of_birth', )}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )
    list_display = ('email', 'first_name', 'last_name', 'role', 'is_active', 'date_of_birth', )
    # add_fieldsets не стандартный атрибут ModelAdmin. UserAdmin
    # переопределяет get_fieldsets использовать этот атрибут при создании пользователя.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Регистрация новой модели UserAdmin...
admin.site.register(Worker, WorkerAdmin)
admin.site.unregister(Group)