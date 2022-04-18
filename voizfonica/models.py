from django.db import models

class Admin(models.Model):
    adminname=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

class Customer(models.Model):
    Cname=models.CharField(max_length=50)
    Cadhar=models.CharField(max_length=50)
    Cemail=models.CharField(max_length=50)
    Caddress=models.CharField(max_length=50)
    Calternatemobilenumber=models.CharField(max_length=50)
    Typeofcustomer=models.CharField(max_length=50)
    Newnumber=models.CharField(max_length=50)
    password=models.CharField(max_length=50,default='admin')
    profilephoto=models.ImageField(upload_to='images/',default=None)
    aadharphoto=models.ImageField(upload_to='images/',default=None)

# Create your models here.
class Prepaidplans(models.Model):
    price=models.CharField(max_length=100)
    calls=models.CharField(max_length=100)
    validity=models.CharField(max_length=100)
    data=models.CharField(max_length=100)
    messages=models.CharField(max_length=100)
    offers=models.CharField(max_length=100)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)

class Postpaidplans(models.Model):
    price=models.CharField(max_length=100)
    calls=models.CharField(max_length=100)
    data=models.CharField(max_length=100)
    messages=models.CharField(max_length=100)
    offers=models.CharField(max_length=100)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)

class Query(models.Model):
    
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=50)
    message=models.CharField(max_length=500)
    replymessage=models.CharField(max_length=500,blank=True)
   


class DonglePrepaidplans(models.Model):
    price=models.CharField(max_length=100)
    data=models.CharField(max_length=100)
    validity=models.CharField(max_length=100)
    offers=models.CharField(max_length=100)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)

class DonglePostpaidplans(models.Model):
    price=models.CharField(max_length=100)
    data=models.CharField(max_length=100)
    offers=models.CharField(max_length=100)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)

class Prepaidplansusage(models.Model):
    mobilenumber=models.CharField(max_length=10)
    plan=models.CharField(max_length=100)


class PrepaidRechargeHistory(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    mobile=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    calls=models.CharField(max_length=100)
    validity=models.CharField(max_length=100)
    data=models.CharField(max_length=100)
    messages=models.CharField(max_length=100)
    offers=models.CharField(max_length=100)
    date=models.CharField(max_length=50)


class PrepaidRechargeDongle(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)
    number=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    data=models.CharField(max_length=100)
    offers=models.CharField(max_length=100)
    date=models.CharField(max_length=50)    

class Postpaidbroughtplan(models.Model):
    date=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    calls=models.CharField(max_length=100)
    data=models.CharField(max_length=100)
    edata=models.CharField(max_length=100,blank=True)
    messages=models.CharField(max_length=100)
    emessages=models.CharField(max_length=100,blank=True) 
    eprice=models.CharField(max_length=100,blank=True)
    tprice=models.CharField(max_length=100,blank=True)
    offers=models.CharField(max_length=100)
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)

class DonglePostpaidbroughtplans(models.Model):
    date=models.CharField(max_length=100)
    mobilenumber=models.CharField(max_length=100)
    price=models.CharField(max_length=100)    
    data=models.CharField(max_length=100)
    edata=models.CharField(max_length=100,blank=True)
    eprice=models.CharField(max_length=100,blank=True)
    tprice=models.CharField(max_length=100,blank=True)    
    offers=models.CharField(max_length=100)    
    id=models.AutoField(auto_created=True,primary_key=True,serialize=False)


    


