from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'speciality', 'experience_years', 'hospital', 'email')
    search_fields = ('name', 'speciality', 'hospital', 'email')
    list_filter = ('speciality', 'hospital')
    ordering = ('-experience_years', 'name')
    fields = ('name', 'speciality', 'experience_years', 'hospital', 'email', 'phone', 'bio')
    readonly_fields = ('email',)

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()

