from django.contrib import admin

# Register your models here.
from posts.models import Post

# create class to customize admin
class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_link = ["updated"]
    list_filter = ["updated", "timestamp"]
    list_editable = ["title"]
    search_fields = ["title", "content"]

    class Meta:
        model = Post



# Registering the Post Model into admin site
# and connects Post Model witth PostModelAdmin
admin.site.register(Post, PostModelAdmin)
