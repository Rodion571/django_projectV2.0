import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_reservation_is_processed'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=50)),
                ('item_description', ckeditor.fields.RichTextField()),
                ('item_icon', models.CharField(max_length=50)),
                ('item_slug', models.SlugField(unique=True)),
                ('item_follow_name', models.CharField(max_length=50)),
                ('item_follow_link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]