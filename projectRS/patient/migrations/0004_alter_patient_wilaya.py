# Generated by Django 4.0.3 on 2022-06-10 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0003_wilaya_remove_patient_user_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='Wilaya',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.wilaya'),
        ),
    ]