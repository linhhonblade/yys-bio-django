from django.contrib import admin

from .models import Role, Lane, Shiki


class ShikiAdmin(admin.ModelAdmin):
    fieldsets = [
        ("General Information", {"fields": ["name", "avatar_image", "gender", "role_ids", "lane_ids"]})
    ]
    list_display = ["name", "get_roles"]
    search_fields = ["name", "role_ids", "lane_ids"]
    readonly_fields = ['avatar_image']
    filter_horizontal = ('role_ids', 'lane_ids')


class RoleAdmin(admin.ModelAdmin):
    fields = ["name", "icon_image"]
    list_display = ["name", "icon_image"]
    readonly_fields = ['icon_image']


class LaneAdmin(admin.ModelAdmin):
    fields = ["name", "icon"]
    list_display = ["name", "icon"]


admin.site.register(Shiki, ShikiAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(Lane, LaneAdmin)
