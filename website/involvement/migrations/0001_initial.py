# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 10:42
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.contrib.wagtailroutablepage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0018_remove_rendition_filter'),
        ('wagtailcore', '0032_add_bulk_delete_page_permission'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('draft', models.BooleanField(default=False, help_text='Save application as a draft', verbose_name='Draft')),
                ('cover_letter', models.TextField(blank=True, help_text='Present yourself and state why you are what we are looking for', verbose_name='Cover Letter')),
                ('qualifications', models.TextField(blank=True, help_text='Give a summary of relevant qualifications', verbose_name='Qualifications')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Applications',
            },
        ),
        migrations.CreateModel(
            name='Function',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archived', models.BooleanField(default=False, help_text='Hide the position from menus', verbose_name='Archived')),
                ('name_en', models.CharField(help_text='Enter the name of the function', max_length=255, verbose_name='English function name')),
                ('name_sv', models.CharField(help_text='Enter the name of the function', max_length=255, verbose_name='Swedish function name')),
                ('description_en', models.TextField(blank=True, help_text='Enter a description of the function', verbose_name='English function description')),
                ('description_sv', models.TextField(blank=True, help_text='Enter a description of the function', verbose_name='Swedish function description')),
            ],
            options={
                'verbose_name_plural': 'Functions',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commencement', models.DateField(default=datetime.date.today, verbose_name='Commencement of recruitment')),
                ('deadline', models.DateField(verbose_name='Recruitment deadline')),
                ('appointments', models.IntegerField(default=1, help_text='Enter the number of concurrent appointments to the position', verbose_name='Number of appointments')),
                ('term_from', models.DateField(verbose_name='Date of appointment')),
                ('term_to', models.DateField(verbose_name='End date of appointment')),
                ('comment_en', models.TextField(blank=True, help_text='Enter extra comments specific to the position this year.', verbose_name='English extra comments')),
                ('comment_sv', models.TextField(blank=True, help_text='Enter extra comments specific to the position this year.', verbose_name='Swedish extra comments')),
                ('function', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='positions', to='involvement.Function')),
            ],
            options={
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='RecruitmentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_sv', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.contrib.wagtailroutablepage.models.RoutablePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(help_text='Enter the name of your reference', max_length=255, verbose_name='Name')),
                ('position', models.CharField(help_text='Enter the position in which your reference relates to you', max_length=255, verbose_name='Position')),
                ('email', models.EmailField(blank=True, help_text='Enter an e-mail address on which your reference in reachable', max_length=254, verbose_name='E-mail address')),
                ('phone_number', models.CharField(blank=True, help_text='Enter a valid phone number', max_length=20, validators=[django.core.validators.RegexValidator(message='Enter a phone number on which your reference is reachable', regex='^\\+?\\d+$')], verbose_name='Phone number')),
                ('comment', models.CharField(blank=True, help_text='Enter any additional comments regarding your reference', max_length=500, verbose_name='Comment')),
                ('application', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='involvement.Application')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(help_text='Enter the name of the team', max_length=255, verbose_name='English team name')),
                ('name_sv', models.CharField(help_text='Enter the name of the team', max_length=255, verbose_name='Swedish team name')),
                ('description_en', models.TextField(blank=True, help_text='Enter a description of the team', verbose_name='English team description')),
                ('description_sv', models.TextField(blank=True, help_text='Enter a description of the team', verbose_name='Swedish team description')),
                ('leader_en', models.CharField(blank=True, help_text='Enter the name of position of the team leader', max_length=255, verbose_name='English team leader position name')),
                ('leader_sv', models.CharField(blank=True, help_text='Enter the name of position of the team leader', max_length=255, verbose_name='Swedish team leader position name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Contact e-mail address')),
                ('logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.AddField(
            model_name='recruitmentpage',
            name='excluded_teams',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='Select teams to exclude from the page', related_name='exclude_on_page', to='involvement.Team', verbose_name='Excluded teams'),
        ),
        migrations.AddField(
            model_name='recruitmentpage',
            name='included_teams',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, help_text='Select teams to include on the page', related_name='include_on_page', to='involvement.Team', verbose_name='Included teams'),
        ),
        migrations.AddField(
            model_name='function',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='functions', to='involvement.Team'),
        ),
        migrations.AddField(
            model_name='application',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='applications', to='involvement.Position'),
        ),
        migrations.AlterUniqueTogether(
            name='application',
            unique_together=set([('position', 'applicant')]),
        ),
    ]
