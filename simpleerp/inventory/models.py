from django.db import models

# Create your models here.
class Inventory(models.Model):
	sku = models.CharField(max_length=500)
	quantity = models.IntegerField()

class Sales(models.Model):
	sales_type = models.CharField(max_length=500)
	operator = models.CharField(max_length=500)
	job_date = models.DateTimeField()
	sku = models.CharField(max_length=500)
	qty = models.IntegerField()
	color_type = models.CharField(max_length=500)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	page_type = models.CharField(max_length=100)
	dtp_page_count = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)
	dtp_cost = models.DecimalField(max_digits=10, decimal_places=2, default=None, blank=True, null=True)

class InventoryChangeLog(models.Model):
	sku = models.CharField(max_length=500)
	quantity = models.IntegerField()
	change_type = models.CharField(max_length=500)
	change_by = models.CharField(max_length=500)
	change_date = models.DateTimeField()
	comment = models.CharField(max_length=500, default=None, blank=True, null=True)




