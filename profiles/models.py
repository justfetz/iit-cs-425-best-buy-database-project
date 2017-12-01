from django.db import models

# Create your models here.
class profile(models.Model):
	name = models.CharField(max_length=120, blank=True, null=True)
	description = models.TextField(default='description default text')
	location = models.CharField(max_length=120, default='my location default', blank=True, null=True)
	job = models.CharField(max_length=120, null=True)

	def __unicode__(self):
		return self.name 

class customer(models.Model):
	name = models.CharField(max_length=120, blank=True, null=True)
	customerID = models.IntegerField(primary_key=True)
	firstName = models.TextField(max_length=120, default='John', blank=True, null=True)
	lastName = models.TextField(max_length=120, default='Doe', null=True)
	streetNumber = models.CharField(max_length=12, blank=True, null=True)
	streetName = models.CharField(default='default', max_length=120)
	city = models.CharField(max_length=120, default='my location default', blank=True, null=True)
	state = models.CharField(max_length=120, null=True)
	zipcode = models.CharField(max_length=12, null = True)

	def __unicode__(self):
		return self.name 

class order(models.Model):
	orderID = models.IntegerField(primary_key=True)
	description = models.TextField(max_length=120, blank=True, null=True)
	timeStamp = models.DateTimeField(auto_now=False)

	def __unicode__(self):
		return self.name 

class frequentshopper(models.Model):
	customerID = models.CharField(max_length=120, default='defaultID', primary_key=True)
	barcode = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name 

class commerce(models.Model):
	storeID = models.CharField(max_length=120, primary_key=True)
	location = models.CharField(max_length=120, null=True)


	def __unicode__(self):
		return self.name 

class onlineStore(models.Model):
	storeID = models.CharField(max_length=120, primary_key=True)
	isOnline = models.NullBooleanField(max_length=5)


	def __unicode__(self):
		return self.name 

class brickMortar(models.Model):
	storeID = models.CharField(max_length=120, primary_key=True)
	isOnline = models.NullBooleanField(max_length=5)
	streetNumber = models.CharField(max_length=12, blank=True, null=True)
	streetName = models.CharField(max_length=120, default='default')
	city = models.CharField(max_length=120, default='my location default', blank=True, null=True)
	state = models.CharField(max_length=120, null=True)
	zipcode = models.CharField(max_length=12, null = True)

	def __unicode__(self):
		return self.name 

class products(models.Model):
	productID = models.CharField(primary_key=True, max_length=120)
	UPC = models.BigIntegerField(null=True)
	productName = models.CharField(max_length=120, blank=True, null=True)
	description = models.TextField(default='description default text')


	def __unicode__(self):
		return self.name 

class productType(models.Model):
	typeCodeID =  models.CharField(max_length=120, primary_key=True)
	prodTypename = models.CharField(max_length=120, blank=True, null=True)
	description = models.TextField(default='description default text')

	def __unicode__(self):
		return self.name 

class manufacturer(models.Model):
	manufacturerID = models.CharField(max_length=120, primary_key=True)
	name = models.CharField(max_length=120, null=True)
	location = models.CharField(max_length=120, default='my location default', blank=True, null=True)
	
	def __unicode__(self):
		return self.name 

class storeServices(models.Model):
	serviceID = models.CharField(max_length=120, primary_key=True)
	serviceName = models.TextField(max_length=120)

	def __unicode__(self):
		return self.name 

class category(models.Model):
	categoryID = models.CharField(primary_key=True, max_length=120)
	categoryName = models.CharField(max_length=120)

	def __unicode__(self):
		return self.name 

class transactions(models.Model):
	transactionID = models.CharField(primary_key=True, max_length=120)
	productID = models.CharField(null=True, max_length=120)
	quantity = models.IntegerField(null=True)

	def __unicode__(self):
		return self.name 

