# Generated by Django 5.1.3 on 2025-06-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appmustafa', '0002_comentario_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='foto_perfil',
            field=models.ImageField(blank=True, default='usuarios/perfiles/default.jpg', null=True, upload_to='usuarios/perfiles/'),
        ),
    ]
