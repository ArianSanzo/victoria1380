from .models import PrimaryCategory, SecondaryCategory

def primary_to_secondary_context(request=None):
    primary_to_secondary = {}
    primary_categories = PrimaryCategory.objects.all()
    for primary in primary_categories:
        secondary_categories = SecondaryCategory.objects.filter(products__primary_category=primary).distinct()
        primary_to_secondary[primary] = secondary_categories
    return {'primary_to_secondary': primary_to_secondary}
