# Generated by Django 2.0.4 on 2018-08-17 03:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, verbose_name='company name')),
                ('first_name', models.CharField(max_length=50, verbose_name='first name')),
                ('last_name', models.CharField(max_length=50, verbose_name='last_name')),
                ('company_photo', models.ImageField(upload_to='profile_image')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone_number', models.CharField(max_length=11, verbose_name='phone number')),
                ('street', models.CharField(max_length=100, verbose_name='street address')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('state', models.CharField(choices=[('AL', 'AL'), ('AK', 'AK'), ('AZ', 'AZ'), ('AR', 'AR'), ('CA', 'CA'), ('CO', 'CO'), ('CT', 'CT'), ('DE', 'DE'), ('FL', 'FL'), ('GA', 'GA'), ('HI', 'HI'), ('ID', 'ID'), ('IL', 'IL'), ('IN', 'IN'), ('IA', 'IA'), ('KS', 'KS'), ('KY', 'KY'), ('LA', 'LA'), ('ME', 'ME'), ('MD', 'MD'), ('MA', 'MA'), ('MI', 'MI'), ('MN', 'MN'), ('MS', 'MS'), ('MO', 'MO'), ('MT', 'MT'), ('NE', 'NE'), ('NV', 'NV'), ('NH', 'NH'), ('NJ', 'NJ'), ('NM', 'NM'), ('NY', 'NY'), ('NC', 'NC'), ('ND', 'ND'), ('OH', 'OH'), ('OK', 'OK'), ('OR', 'OR'), ('PA', 'PA'), ('RI', 'RI'), ('SC', 'SC'), ('SD', 'SD'), ('TN', 'TN'), ('TX', 'TX'), ('UT', 'UT'), ('VT', 'VT'), ('VA', 'VA'), ('WA', 'WA'), ('WV', 'WV'), ('WI', 'WI'), ('WY', 'WY')], default='AL', max_length=50, verbose_name='state')),
                ('zip_code', models.CharField(max_length=5, verbose_name='zip code')),
                ('mission_statement', models.TextField(verbose_name='mission statement')),
                ('business_description', models.TextField(verbose_name='description of business')),
                ('organization_type', models.CharField(choices=[('for profit', 'for profit'), ('non-profit', 'non-profit')], default='for profit', max_length=50, verbose_name='organization type')),
                ('employee_number', models.CharField(choices=[('0-25', '0-25'), ('26-50', '26-50'), ('51-100', '51-100'), ('101-200', '101-200'), ('200+', '200+')], default='0-25', max_length=10, verbose_name='number of employees')),
                ('years_in_business', models.CharField(choices=[('0-5', '0-5'), ('6-10', '6-10'), ('11-15', '11-15'), ('16-20', '16-20'), ('21-25', '21-25'), ('26-30', '26-30'), ('31 or more', '31 or more')], default='0-5', max_length=10, verbose_name='years in business')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='5', max_length=50, verbose_name='rating')),
                ('rating_description', models.TextField(verbose_name='rating description')),
                ('employer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_rating_employer', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employer_being_rated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
