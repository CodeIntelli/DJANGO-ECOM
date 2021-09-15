# Generated by Django 3.2.6 on 2021-09-13 16:03

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
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=200)),
                ('lname', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('addone', models.CharField(max_length=200)),
                ('addtwo', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh ', 'Arunachal Pradesh '), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir ', 'Jammu and Kashmir '), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Customer',
            },
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancled', 'Cancled'), ('Return', 'Return')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermart.customer')),
            ],
            options={
                'db_table': 'OrderPlaced',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptops'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('BG', 'Bag'), ('HP', 'HeadPhone'), ('W', 'Watches'), ('S', 'Shoes')], max_length=2)),
                ('product_image', models.ImageField(upload_to='productImg')),
            ],
            options={
                'db_table': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ReturnOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rreason', models.CharField(choices=[('BAD_QUALITY', 'ORDER_CREATED_BY_MISTAKE'), ('PRODUCT_DAMAGE', 'ITEM NOT ARRIVED ON TIME'), ('MISSING_PART', 'SHIPPING COST TOO HIGH'), ('PRODUCT_AND_BOX_DAMAGE', 'ITEM COST TOO HIGH'), ('WRONG_ITEM_SEND', 'FOUND CHEAPER SOMEWHERE ELSE'), ('ITEM_DEFECTIVE', 'NEED TO CHANGE SHIPPING ADDRESS'), ('OTHER', 'OTHER')], max_length=150)),
                ('return_date', models.DateTimeField(auto_now_add=True)),
                ('bank_name', models.CharField(choices=[('State Bank of India (SBI)', 'State Bank of India (SBI)'), ('Punjab National Bank', 'Punjab National Bank'), ('Bank of Baroda', 'Bank of Baroda'), ('Canara Bank', 'Canara Bank'), ('Union Bank of India', 'Union Bank of India'), ('Bank of India', 'Bank of India'), ('Indian Bank', 'Indian Bank'), ('Central Bank of India', 'Central Bank of India'), ('Indian Overseas Bank', 'Indian Overseas Bank'), ('UCO Bank', 'UCO Bank'), ('Bank of Maharashtra', 'Bank of Maharashtra'), ('Punjab & Sindh Bank', 'Punjab & Sindh Bank'), ('Axis', 'Axis'), ('Bandhan', 'Bandhan'), ('HDFC', 'HDFC'), ('ICICI', 'ICICI'), ('IDBI', 'IDBI'), ('Kotak Mahindra', 'Kotak Mahindra'), ('South Indian Bank', 'South Indian Bank'), ('Yes Bank', 'Yes Bank'), ('IndusInd Bank', 'IndusInd Bank')], max_length=50)),
                ('bank_acc', models.CharField(max_length=50)),
                ('bank_ifsc', models.CharField(blank=True, max_length=20, null=True)),
                ('holder_name', models.CharField(blank=True, max_length=150, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=50, null=True)),
                ('orderplaced', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermart.orderplaced')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Order_Return',
            },
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermart.product'),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermart.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='CancledOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(choices=[('ORDER_MISTAKE', 'ORDER_CREATED_BY_MISTAKE'), ('NOT_ARRIVED_TIME', 'ITEM NOT ARRIVED ON TIME'), ('S_HIGH_COST', 'SHIPPING COST TOO HIGH'), ('I_HIGH_COST', 'ITEM COST TOO HIGH'), ('FOUND_CHEAPER', 'FOUND CHEAPER SOMEWHERE ELSE'), ('CHANGE_S_ADDRESS', 'NEED TO CHANGE SHIPPING ADDRESS'), ('CHANGE_S_SPEED', 'NEED TO CHANGE SHIPPING SPEED'), ('CHANGE_BILLING_ADDRESS', 'NEED TO CHANGE BILLING ADDRESS'), ('CHANGE_PAYMETHOD', 'NEED TO CHANGE PAYMENT METHOD'), ('OTHER', 'OTHER')], max_length=50)),
                ('cancle_date', models.DateTimeField(auto_now_add=True)),
                ('bank_name', models.CharField(choices=[('State Bank of India (SBI)', 'State Bank of India (SBI)'), ('Punjab National Bank', 'Punjab National Bank'), ('Bank of Baroda', 'Bank of Baroda'), ('Canara Bank', 'Canara Bank'), ('Union Bank of India', 'Union Bank of India'), ('Bank of India', 'Bank of India'), ('Indian Bank', 'Indian Bank'), ('Central Bank of India', 'Central Bank of India'), ('Indian Overseas Bank', 'Indian Overseas Bank'), ('UCO Bank', 'UCO Bank'), ('Bank of Maharashtra', 'Bank of Maharashtra'), ('Punjab & Sindh Bank', 'Punjab & Sindh Bank'), ('Axis', 'Axis'), ('Bandhan', 'Bandhan'), ('HDFC', 'HDFC'), ('ICICI', 'ICICI'), ('IDBI', 'IDBI'), ('Kotak Mahindra', 'Kotak Mahindra'), ('South Indian Bank', 'South Indian Bank'), ('Yes Bank', 'Yes Bank'), ('IndusInd Bank', 'IndusInd Bank')], max_length=50)),
                ('bank_acc', models.CharField(max_length=50)),
                ('bank_ifsc', models.CharField(blank=True, max_length=20, null=True)),
                ('holder_name', models.CharField(blank=True, max_length=150, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=50, null=True)),
                ('orderplaced', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supermart.orderplaced')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Order_Cancled',
            },
        ),
    ]
