from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='is_processed',
            field=models.BooleanField(default=False),
        ),
    ]