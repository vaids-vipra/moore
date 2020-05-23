# Generated by Django 2.2.10 on 2020-04-04 13:06

from django.db import migrations
from itertools import chain
from utils.data_migrations import stream_field_filter_map

def imagedesc_to_columns(block):
    image = {
        'type': 'image',
        'value':{
            'image': block['value']['image'],
            'height': 400
        }
    }

    text = {
        'type': 'paragraph',
        'value': {
            'alignment': "Left",
            'text': block['value']['description']
        }
    }
    
    if block['value']['image_alignment'] == "left":
        return {
            'type': 'columns',
            'value': {
                'columns':[
                    {
                        'width': 6,
                        'content': [
                            image
                        ]
                    },
                    {
                        'width': 6,
                        'content': [
                            text
                        ]
                    }
                ]
            }
        }
    else:
        return {
            'type': 'columns',
            'value': {
                'columns':[
                    {
                        'width': 6,
                        'content': [
                            text
                        ]
                    },
                    {
                        'width': 6,
                        'content': [
                            image
                        ]
                    }
                ]
            }
        }
        
def apply_to_all_pages(apps, mapper):
    HomePage = apps.get_model('home', 'HomePage')
    WebPage = apps.get_model('home', 'WebPage')
    hps = HomePage.objects.all()
    wps = WebPage.objects.all();
    for obj in chain(hps, wps):
        # There is a long-standing mistake that image-icons and image-description have swapped tags in the database. I will make another migration to change that later.
        obj.body_en = stream_field_filter_map(obj.body_en, "image_icons", mapper)
        obj.body_sv = stream_field_filter_map(obj.body_sv, "image_icons", mapper)
        obj.save();

def forwards(apps, schema_editor):
    apply_to_all_pages(apps, imagedesc_to_columns)
    

class Migration(migrations.Migration):

    dependencies = [
        ('home', '0037_auto_20200404_1504'),
    ]

    operations = [
        #This cannot be ran backwards without accidentally destroying all other column blocks
        migrations.RunPython(forwards)
    ]