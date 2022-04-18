# Generated by Django 3.2.6 on 2021-11-23 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adminname', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=50)),
                ('Cadhar', models.CharField(max_length=50)),
                ('Cemail', models.CharField(max_length=50)),
                ('Caddress', models.CharField(max_length=50)),
                ('Calternatemobilenumber', models.CharField(max_length=50)),
                ('Typeofcustomer', models.CharField(max_length=50)),
                ('Newnumber', models.CharField(max_length=50)),
                ('password', models.CharField(default='admin', max_length=50)),
                ('profilephoto', models.ImageField(default=None, upload_to='images/')),
                ('aadharphoto', models.ImageField(default=None, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='DonglePostpaidbroughtplans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('edata', models.CharField(blank=True, max_length=100)),
                ('eprice', models.CharField(blank=True, max_length=100)),
                ('tprice', models.CharField(blank=True, max_length=100)),
                ('offers', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DonglePostpaidplans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('offers', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DonglePrepaidplans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('offers', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Postpaidbroughtplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('date', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('calls', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('edata', models.CharField(blank=True, max_length=100)),
                ('messages', models.CharField(max_length=100)),
                ('emessages', models.CharField(blank=True, max_length=100)),
                ('eprice', models.CharField(blank=True, max_length=100)),
                ('tprice', models.CharField(blank=True, max_length=100)),
                ('offers', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Postpaidplans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=100)),
                ('calls', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('messages', models.CharField(max_length=100)),
                ('offers', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prepaidplans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('price', models.CharField(max_length=100)),
                ('calls', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('messages', models.CharField(max_length=100)),
                ('offers', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Prepaidplansusage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobilenumber', models.CharField(max_length=10)),
                ('plan', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PrepaidRechargeDongle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('offers', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PrepaidRechargeHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('calls', models.CharField(max_length=100)),
                ('validity', models.CharField(max_length=100)),
                ('data', models.CharField(max_length=100)),
                ('messages', models.CharField(max_length=100)),
                ('offers', models.CharField(max_length=100)),
                ('date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('replymessage', models.CharField(blank=True, max_length=500)),
            ],
        ),
    ]
