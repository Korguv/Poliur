# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agent(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    nicname = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    tnum = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'agent'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = True
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Balance(models.Model):
    plan_sm = models.IntegerField()
    id_nomenclature = models.ForeignKey('Nomenclature', models.DO_NOTHING, db_column='id_nomenclature')
    date = models.DateField()
    quantity = models.IntegerField()
    sum = models.IntegerField()
    id_source = models.ForeignKey('Source', models.DO_NOTHING, db_column='id_source')
    id_hardness = models.ForeignKey('Hardness', models.DO_NOTHING, db_column='id_hardness', blank=True, null=True)
    id_order = models.ForeignKey('OrderSm', models.DO_NOTHING, db_column='id_order', blank=True, null=True)
    id_plane = models.PositiveIntegerField(blank=True, null=True)
    text = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'balance'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'django_session'


class GroupSm(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=30)

    class Meta:
        managed = True
        db_table = 'group_sm'


class Hardness(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=10)

    class Meta:
        managed = True
        db_table = 'hardness'


class Hollyday(models.Model):
    id_date = models.DateField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'hollyday'


class Nomenclature(models.Model):
    name = models.CharField(max_length=50)
    nicname = models.CharField(max_length=50, blank=True, null=True)
    id_subgroup = models.ForeignKey('Subgroup', models.DO_NOTHING, db_column='id_subgroup')
    text = models.CharField(max_length=150, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    volume = models.DecimalField(max_digits=8, decimal_places=3, blank=True, null=True)
    id_form = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'nomenclature'


class OrderSm(models.Model):
    date_in = models.DateField()
    date_out = models.DateField()
    id_agent = models.ForeignKey(Agent, models.DO_NOTHING, db_column='id_agent')
    priority = models.SmallIntegerField()
    text = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'order_sm'


class Shipment(models.Model):
    payment = models.IntegerField()
    date_in = models.DateField()
    date_out = models.DateField()
    sum = models.IntegerField()
    ship_num = models.TextField()
    id_stat = models.ForeignKey('StatShip', models.DO_NOTHING, db_column='id_stat', blank=True, null=True)
    id_ship_agent = models.ForeignKey(Agent, models.DO_NOTHING, db_column='id_ship_agent', blank=True, null=True)
    text = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'shipment'


class Source(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        managed = True
        db_table = 'source'


class StatShip(models.Model):
    stat = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'stat_ship'


class StudentsStudent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=240)
    email = models.CharField(max_length=254)
    document = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    registrationdate = models.DateField(db_column='registrationDate')  # Field name made lowercase.
    photo = models.CharField(max_length=512)

    class Meta:
        managed = True
        db_table = 'students_student'


class Subgroup(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    id_group = models.ForeignKey(GroupSm, models.DO_NOTHING, db_column='id_group')

    class Meta:
        managed = True
        db_table = 'subgroup'


class SumShip(models.Model):
    id_bal = models.ForeignKey(Balance, models.DO_NOTHING, db_column='id_bal', blank=True, null=True)
    id_ship = models.ForeignKey(Shipment, models.DO_NOTHING, db_column='id_ship', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sum_ship'


class Teg(models.Model):
    name = models.TextField()

    class Meta:
        managed = True
        db_table = 'teg'


class TegsNom(models.Model):
    id_nom = models.ForeignKey(Balance, models.DO_NOTHING, db_column='id_nom')
    id_teg = models.ForeignKey(Teg, models.DO_NOTHING, db_column='id_teg')

    class Meta:
        managed = True
        db_table = 'tegs_nom'


class Test1(models.Model):
    txt = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'test1'


class WorkHours(models.Model):
    date_work = models.ForeignKey(Hollyday, models.DO_NOTHING, db_column='date_work')
    hours = models.IntegerField()
    id_workers = models.ForeignKey('Workers', models.DO_NOTHING, db_column='id_workers', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'work_hours'


class Workers(models.Model):
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    status = models.CharField(max_length=100, blank=True, null=True)
    path = models.CharField(max_length=100, blank=True, null=True)
    doc_name = models.CharField(max_length=20, blank=True, null=True)
    foto_name = models.CharField(max_length=20, blank=True, null=True)
    tnum = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    text = models.CharField(max_length=200, blank=True, null=True)
    salary = models.IntegerField()
    bonus = models.SmallIntegerField()
    date_in = models.DateField(blank=True, null=True)
    data_out = models.DateField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'workers'
