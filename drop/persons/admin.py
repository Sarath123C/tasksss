
from django.contrib import admin

# Register your models here.
from persons.models import Department, Person, Course

admin.site.register(Course)
admin.site.register(Department)
admin.site.register(Person)