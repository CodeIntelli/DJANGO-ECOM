from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Product, Cart, OrderPlaced, ReturnOrders, CancledOrders, subCategory, Category
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "fname",
        "lname",
        "phone",
        "addone",
        "addtwo",
        "city",
        "zipcode",
        "state",
    ]


@admin.register(Product)
class ProductModelAdmin(SummernoteModelAdmin):
    list_display = [
        "id",
        "title",
        "selling_price",
        "discount_price",
        "description",
        "brand",
        "subcategory",
        "product_image",
    ]
    summernote_fields = ("description",)


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "quantity"]


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ["id", "productCategory"]


@admin.register(subCategory)
class subCategory(admin.ModelAdmin):
    list_display = ["id", "productSubCategory", "productCategory"]


@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "customer",
        "product",
        "quantity",
        "ordered_date",
        "status",
    ]


@admin.register(ReturnOrders)
class ReturnOrdersModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "orderplaced",
        "rreason",
        "return_date",
        "bank_name",
        "bank_acc",
        "bank_ifsc",
        "holder_name",
        "upi_id",
    ]


@admin.register(CancledOrders)
class CancledOrdersModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "orderplaced",
        "reason",
        "cancle_date",
        "bank_name",
        "bank_acc",
        "bank_ifsc",
        "holder_name",
        "upi_id",
    ]
