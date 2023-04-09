from django.contrib import admin
from .models import Question, Choice, Category, Nominee, Vote

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class NomineeAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'description')
    list_filter = ('category',)

class VoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'nominee', 'timestamp')
    list_filter = ('nominee__category', 'timestamp')
    date_hierarchy = 'timestamp'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(Category, CategoryAdmin)
admin.site.register(Nominee, NomineeAdmin)
admin.site.register(Vote, VoteAdmin)

# admin.site.register(Question)
# admin.site.register(Choice)
