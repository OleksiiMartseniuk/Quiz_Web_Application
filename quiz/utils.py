class PermissionsViewMixin:

    def permissions_view(self, request):
        perms = False
        if request.user.has_perms(['xlsx.view_xlsx', 'xlsx.add_xlsx']):
            perms = True
        context = {
            'perms': perms,
        }
        return context


