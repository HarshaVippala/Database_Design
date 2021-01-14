from django.contrib import admin
from .models import*

admin.site.register(ShClass)
admin.site.register(ShCorp)
#admin.site.register(ShCorpDisc)
admin.site.register(ShCustomer)
admin.site.register(ShDiscCoupons)
#admin.site.register(ShIndvDisc)
admin.site.register(ShInvoice)
admin.site.register(ShIndv)
admin.site.register(ShOffLoc)
admin.site.register(ShPayment)
admin.site.register(ShReservation)
admin.site.register(ShVehicle)
'''
from django.contrib.admin import AdminSite

class WowAdminSite(AdminSite):

    site_header = "Wowcarz Admin"
    site_title = "Wowcarz Events Admin Portal"
    index_title = "Wowcarz to WDS Events Portal"

wow_admin_site = WowAdminSite(name='Wowadmin')'''
'''
from django.contrib.auth.models import User, Group
class cAdmin(admin.ModelAdmin):
    list_display = ('ssn_number','first_name', 'last_name', 'email_id')
    search_fields = ('first_name', 'last_name')
    list_filter=('state','zip_code','policy_type')
    ordering=('ssn_number',)

class dAdmin(admin.ModelAdmin):
    list_display = ('liscense_num','first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter=('vpk',)

class HPAdmin(admin.ModelAdmin):
    list_display = ('premium_id','afn','hss', 'swimming_pool', 'premium_amount')
    search_fields = ('premium_id', 'premium_amount')
    #list_filter=('',)
class HAdmin(admin.ModelAdmin):
    list_display = ('house_id','purchase_date','area', 'purchase_value')
    search_fields = ('area', 'house_id')
    list_filter=('premium','house_type')
class IAdmin(admin.ModelAdmin):
    list_display = ('invoice_id','due_date','amount')
    search_fields = ('ssn_number', 'invoice_id')
    list_filter=('cpk','due_date')
class PAdmin(admin.ModelAdmin):
    list_display = ('reciept_id','method', 'installment_amount')
    search_fields = ('installment_amount', 'reciept_id')
    list_filter=('invoice','method')
class policyAdmin(admin.ModelAdmin):
    list_display = ('policy_id','start_date','end_date')
    search_fields = ('start_date', 'policy_id')
    list_filter=('end_date','insurance_status')
class vAdmin(admin.ModelAdmin):
    list_display = ('vin','vehicle_make','vehicle_model')
    search_fields = ('vehicle_model', 'vehicle_make')
    list_filter=('vpk_id','vehicle_year','vehicle_status')




wow_admin_site.register(User)
wow_admin_site.register(Group)
wow_admin_site.register(Customer,cAdmin)
wow_admin_site.register(Driver,dAdmin)
wow_admin_site.register(HousePremium,HPAdmin)
wow_admin_site.register(Houses,HAdmin)
wow_admin_site.register(Invoice,IAdmin)
wow_admin_site.register(Payment,PAdmin)
wow_admin_site.register(Policy,policyAdmin)
wow_admin_site.register(Vehicle,vAdmin)
'''