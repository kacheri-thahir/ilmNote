from django.contrib.admin import AdminSite
from django.http import Http404

# Custom admin panel where superuser only can login for others 404 page 
# Go and code in dashboard/admin.py where need to add custom adminpage and then in ilmnote/urls.py change custom admin site.


class SuperuserOnlyAdminSite(AdminSite):
    site_header = "Secure Admin"
    site_title = "Secure Admin"
    index_title = "Admin Panel"

    def has_permission(self, request):
        # Only allow active superusers
        if request.user.is_active and request.user.is_superuser:
            return True
        # For anyone else, raise 404
        raise Http404("Page not found")
# Create an instance
secure_admin_site = SuperuserOnlyAdminSite(name='secure_admin')
