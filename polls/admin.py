from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import NominationCategory, Nominee
from .resources import NominationCategoryResource, NomineeResource


@admin.register(NominationCategory)
class NominationCategoryAdmin(ImportExportModelAdmin):
    resource_class = NominationCategoryResource
    list_display = ('category_name', 'description', 'nominee_count')

    def nominee_count(self, obj):
        return obj.nominee_set.count()
    nominee_count.short_description = 'Number of Nominees'
    
@admin.register(Nominee)
class NomineeAdmin(ImportExportModelAdmin):
    resource_class = NomineeResource
    list_display = ('nominee_name', 'category', 'description', 'votes')
    search_fields = ('nominee_name', 'category__category_name')
    list_filter = ('category',)

    def votes(self, obj):
        # Assuming you have added a 'votes' field to the Nominee model
        return obj.votes
    votes.short_description = 'Number of Votes'
