from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_footeritem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footeritem',
            name='item_follow_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='footeritem',
            name='item_follow_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='footeritem',
            name='item_icon',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]