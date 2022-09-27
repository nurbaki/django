from django.utils import timezone
from django.contrib import admin
from .models import Product, Review, Category
# Register your models here.
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from import_export.admin import ImportExportModelAdmin
from products.resources import ReviewResource






admin.site.site_title = "Clarusway Title"
admin.site.site_header = "Clarusway Admin Portal"  
admin.site.index_title = "Welcome to Clarusway Admin Portal"


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1
    classes = ('collapse',)

class EntityAdmin(admin.ModelAdmin):
    ...
    list_filter = (
        # for ordinary fields
        ('a_charfield', DropdownFilter),
        # for choice fields
        ('a_choicefield', ChoiceDropdownFilter),
        # for related fields
        ('a_foreignkey_field', RelatedDropdownFilter),
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "create_date", "is_in_stock", "update_date", "added_days_ago", "how_many_reviews")
    list_editable = ( "is_in_stock",)
    list_display_links = ("name", )
    list_filter = ("is_in_stock", "create_date")
    ordering = ("name", )
    search_fields = ("name",)
    prepopulated_fields = {'slug' : ('name',)}
    list_per_page = 25
    date_hierarchy = "update_date"
    # fields = ( "description",("name", "slug"), "is_in_stock")
    inlines = (ReviewInline,)
    fieldsets = (
        ("Main Menü", {
            "fields": (
                ('name', 'slug'), "is_in_stock"# to display multiple fields on the same line, wrap those fields in their own tuple
            ),
            # 'classes': ('wide', 'extrapretty'), wide or collapse
        }),
        ('Optionals Settings', {
            "classes" : ("collapse", ),
            "fields" : ("description", "categories"),
            'description' : "You can use this section for optionals settings"
        })
    )
    filter_vertical = ("categories", )
    
    actions = ("is_in_stock", )
    def is_in_stock(self, request, queryset):
        count = queryset.update(is_in_stock=True)
        self.message_user(request, f"{count} çeşit ürün stoğa eklendi")
        
    is_in_stock.short_description = 'İşaretlenen ürünleri stoğa ekle'
    
    
    
    def added_days_ago(self, product):
        diff = timezone.now() - product.create_date
        return diff.days
    
    def how_many_reviews(self, product):
        count = product.reviews.count()
        return count


class ReviewAdmin(ImportExportModelAdmin):
    list_display = ('__str__', 'created_date', 'is_released')
    list_per_page = 50
    raw_id_fields = ('product',)
    list_filter = (
        ('product', RelatedDropdownFilter),
    )
    resource_class = ReviewResource


admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)