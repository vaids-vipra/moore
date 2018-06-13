# Generated by Django 2.0.5 on 2018-06-11 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('involvement', '0012_auto_20180608_1442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'default_permissions': (), 'permissions': (('admin', 'Admin'), ('fum', 'FUM'), ('board', 'Board'), ('bureau', 'Bureau'), ('group_leader', 'Group Leader')), 'verbose_name': 'Role', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'default_permissions': (), 'verbose_name': 'Team', 'verbose_name_plural': 'Teams'},
        ),
        migrations.RemoveField(
            model_name='role',
            name='official',
        ),
        migrations.RemoveField(
            model_name='team',
            name='group',
        ),
        migrations.AddField(
            model_name='role',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='roles', to='auth.Group'),
        ),
    ]
