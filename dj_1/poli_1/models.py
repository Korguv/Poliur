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