# Generated by Django 2.0 on 2018-04-14 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_star_rating', models.CharField(blank=True, max_length=10)),
                ('two_star_rating', models.CharField(blank=True, max_length=10)),
                ('three_star_rating', models.CharField(blank=True, max_length=10)),
                ('four_star_rating', models.CharField(blank=True, max_length=10)),
                ('five_star_rating', models.CharField(blank=True, max_length=10)),
                ('accessible_rooms', models.CharField(blank=True, max_length=1)),
                ('air_conditioning', models.CharField(blank=True, max_length=1)),
                ('airport_transportation', models.CharField(blank=True, max_length=1)),
                ('bar_lounge', models.CharField(blank=True, max_length=1)),
                ('breakfast_available', models.CharField(blank=True, max_length=1)),
                ('breakfast_buffet', models.CharField(blank=True, max_length=1)),
                ('breakfast_included', models.CharField(blank=True, max_length=1)),
                ('business_center', models.CharField(blank=True, max_length=1)),
                ('concierge', models.CharField(blank=True, max_length=1)),
                ('dry_cleaning', models.CharField(blank=True, max_length=1)),
                ('facilities_for_disabled_guests', models.CharField(blank=True, max_length=1)),
                ('family_rooms', models.CharField(blank=True, max_length=1)),
                ('fitness_center', models.CharField(blank=True, max_length=1)),
                ('free_airport_transportation', models.CharField(blank=True, max_length=1)),
                ('free_internet', models.CharField(blank=True, max_length=1)),
                ('free_parking', models.CharField(blank=True, max_length=1)),
                ('free_wifi', models.CharField(blank=True, max_length=1)),
                ('heated_pool', models.CharField(blank=True, max_length=1)),
                ('hot_tub', models.CharField(blank=True, max_length=1)),
                ('housekeeping', models.CharField(blank=True, max_length=1)),
                ('indoor_pool', models.CharField(blank=True, max_length=1)),
                ('internet', models.CharField(blank=True, max_length=1)),
                ('kitchenette', models.CharField(blank=True, max_length=1)),
                ('laundry_service', models.CharField(blank=True, max_length=1)),
                ('meeting_rooms', models.CharField(blank=True, max_length=1)),
                ('multilingual_staff', models.CharField(blank=True, max_length=1)),
                ('nonSmoking_hotel', models.CharField(blank=True, max_length=1)),
                ('nonSmoking_rooms', models.CharField(blank=True, max_length=1)),
                ('parking', models.CharField(blank=True, max_length=1)),
                ('pets_allowed', models.CharField(blank=True, max_length=1)),
                ('room_service', models.CharField(blank=True, max_length=1)),
                ('self_serve_laundry', models.CharField(blank=True, max_length=1)),
                ('shuttle_bus_service', models.CharField(blank=True, max_length=1)),
                ('spa', models.CharField(blank=True, max_length=1)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('locality', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('rating', models.CharField(blank=True, max_length=10)),
                ('review_num', models.CharField(blank=True, max_length=10)),
                ('star', models.CharField(blank=True, max_length=10)),
                ('street_address', models.CharField(blank=True, max_length=255)),
                ('web', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
