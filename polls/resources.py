from import_export import resources
from .models import NominationCategory, Nominee

class NominationCategoryResource(resources.ModelResource):
    class Meta:
        model = NominationCategory

class NomineeResource(resources.ModelResource):
    class Meta:
        model = Nominee