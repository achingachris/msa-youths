from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Question, Choice, NominationCategory, Nominee
from .resources import NominationCategoryResource, NomineeResource


admin.site.register(Question)
admin.site.register(Choice)

@admin.register(NominationCategory)
class NominationCategoryAdmin(ImportExportModelAdmin):
    resource_class = NominationCategoryResource
    
@admin.register(Nominee)
class NomineeAdmin(ImportExportModelAdmin):
    resource_class = NomineeResource
