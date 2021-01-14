from django.db import models

class ShClass(models.Model):
    type_id = models.BigIntegerField(primary_key=True)
    type = models.CharField(max_length=10)
    rate = models.BigIntegerField()
    fees_om = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'sh_class'


class ShCorp(models.Model):
    cust = models.OneToOneField('ShCustomer', models.DO_NOTHING, primary_key=True)
    corp_id = models.SmallIntegerField(unique=True)
    corp_name = models.CharField(max_length=30)
    reg_comp = models.CharField(max_length=30)
    emp_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sh_corp'


class ShCorpDisc(models.Model):
    coup = models.OneToOneField('ShDiscCoupons', models.DO_NOTHING, primary_key=True)
    sh_corp_cust_id = models.FloatField()
    sh_corp_corp = models.ForeignKey(ShCorp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sh_corp_disc'


class ShCustomer(models.Model):
    cust_id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=30)
    phn_num = models.BigIntegerField()
    street_add = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=10)
    zipcode = models.BigIntegerField()
    cust_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'sh_customer'


class ShDiscCoupons(models.Model):
    coup_id = models.BigIntegerField(primary_key=True)
    perc_disc = models.BigIntegerField()
    coup_type = models.CharField(max_length=12)
    sh_reservation_res = models.OneToOneField('ShReservation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sh_disc_coupons'


class ShIndv(models.Model):
    cust = models.OneToOneField(ShCustomer, models.DO_NOTHING, primary_key=True)
    lic_num = models.SmallIntegerField(unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    ins_comp = models.CharField(max_length=30)
    ins_num = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sh_indv'


class ShIndvDisc(models.Model):
    coup = models.OneToOneField(ShDiscCoupons, models.DO_NOTHING, primary_key=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    sh_indv_lic_num = models.ForeignKey(ShIndv, models.DO_NOTHING, db_column='sh_indv_lic_num')
    sh_indv_cust_id = models.FloatField()

    class Meta:
        managed = False
        db_table = 'sh_indv_disc'


class ShInvoice(models.Model):
    inv_id = models.BigIntegerField(primary_key=True)
    inv_date = models.DateTimeField()
    inv_amount = models.FloatField()
    sh_reservation_res = models.OneToOneField('ShReservation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sh_invoice'


class ShOffLoc(models.Model):
    fid = models.BigIntegerField(primary_key=True)
    street_addr = models.CharField(max_length=30)
    off_city = models.CharField(max_length=10)
    off_state = models.CharField(max_length=10)
    off_zip = models.BigIntegerField()
    off_phnum = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sh_off_loc'


class ShPayment(models.Model):
    pay_id = models.BigIntegerField(primary_key=True)
    pay_date = models.DateTimeField()
    pay_type = models.CharField(max_length=30)
    sh_invoice_inv = models.ForeignKey(ShInvoice, models.DO_NOTHING)
    card_num = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sh_payment'


class ShReservation(models.Model):
    res_id = models.BigIntegerField(primary_key=True)
    pickup = models.DateTimeField()
    dropoff = models.DateTimeField()
    start_odo = models.BigIntegerField()
    end_odo = models.BigIntegerField()
    odo_limit = models.BigIntegerField(blank=True, null=True)
    veh = models.ForeignKey('ShVehicle', models.DO_NOTHING)
    sh_customer_cust = models.ForeignKey(ShCustomer, models.DO_NOTHING)
    veh_id2 = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'sh_reservation'


class ShVehicle(models.Model):
    veh_id = models.CharField(primary_key=True, max_length=10)
    make = models.CharField(max_length=30)
    model = models.CharField(max_length=10)
    year = models.SmallIntegerField()
    vin = models.IntegerField()
    license = models.IntegerField()
    sh_class_type = models.ForeignKey(ShClass, models.DO_NOTHING)
    sh_off_loc_fid = models.ForeignKey(ShOffLoc, models.DO_NOTHING, db_column='sh_off_loc_fid')

    class Meta:
        managed = False
        db_table = 'sh_vehicle'
