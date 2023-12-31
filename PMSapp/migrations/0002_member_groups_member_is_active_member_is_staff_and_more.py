# Generated by Django 4.2.7 on 2023-12-01 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('PMSapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='pmsapp_member_user_groups', to='auth.group'),
        ),
        migrations.AddField(
            model_name='member',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='member',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='member',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='member',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='member',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='pmsapp_member_user_permissions', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='member',
            name='username',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
