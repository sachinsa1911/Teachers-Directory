from django.contrib import admin
from .models import LoginTable, TeacherModel
# Register your models here.
admin.site.register(LoginTable)


@admin.register(TeacherModel)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['FirstName', 'LastName', 'PhoneNumber', 'RoomNumber', 'Subjectstaught',
                    'EmailAddress', 'Profilepicture']
