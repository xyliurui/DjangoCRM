# Generated by Django 2.1.3 on 2018-11-09 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20181109_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='role',
            field=models.ManyToManyField(related_name='userprofile', to='crm.Role', verbose_name='角色列表'),
        ),
    ]
