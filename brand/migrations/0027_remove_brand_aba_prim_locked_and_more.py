# Generated by Django 4.1.4 on 2023-03-09 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("brand", "0026_brandupdate")]

    operations = [
        migrations.RemoveField(model_name="brand", name="aba_prim_locked"),
        migrations.RemoveField(model_name="brand", name="cusip_locked"),
        migrations.RemoveField(model_name="brand", name="ein_locked"),
        migrations.RemoveField(model_name="brand", name="fdic_cert_locked"),
        migrations.RemoveField(model_name="brand", name="googleid_locked"),
        migrations.RemoveField(model_name="brand", name="isin_locked"),
        migrations.RemoveField(model_name="brand", name="lei_locked"),
        migrations.RemoveField(model_name="brand", name="ncua_locked"),
        migrations.RemoveField(model_name="brand", name="occ_locked"),
        migrations.RemoveField(model_name="brand", name="permid_locked"),
        migrations.RemoveField(model_name="brand", name="rssd_hd_locked"),
        migrations.RemoveField(model_name="brand", name="rssd_locked"),
        migrations.RemoveField(model_name="brand", name="thrift_hc_locked"),
        migrations.RemoveField(model_name="brand", name="thrift_locked"),
        migrations.RemoveField(model_name="brand", name="viafid_locked"),
        migrations.AlterField(
            model_name="brand", name="aba_prim", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="cusip", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="ein", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="fdic_cert", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="googleid", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="isin", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="lei", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="ncua", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="occ", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="permid", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="rssd", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="rssd_hd", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="thrift", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="thrift_hc", field=models.TextField(blank=True, default="")
        ),
        migrations.AlterField(
            model_name="brand", name="viafid", field=models.TextField(blank=True, default="")
        ),
    ]