from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced, ReturnOrders, CancledOrders, subCategory, Category
from .forms import (
    CustomerRegistrationForm,
    CustomerProfileForm,
    CancledOrdersForm,
    ReturnOrdersForm,
)
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
# from google_currency import convert
import json
import random
import datetime
from currency_converter import CurrencyConverter
c = CurrencyConverter()


""" 
todo: for class based view you need to put this command for login authentication required system
* @method_decorator(login_required, name='dispatch')

todo: for function based approch we need to put this command for login authentication
* @login_required

"""


class home(View):
    def get(self, request):
        product = Category.objects.all()
        subproducts = subCategory.objects.all()
        latestproduct = Product.objects.all()[:12]
        deal_product = Product.objects.all()[12:]

        print(deal_product)
        Mobiles = Product.objects.filter(subcategory="4")
        Laptops = Product.objects.filter(subcategory="5")
        Accessories = Product.objects.filter(subcategory="6")
        Audio = Product.objects.filter(subcategory="7")
        Smart_Warable = Product.objects.filter(subcategory="8")
        Cameras = Product.objects.filter(subcategory="9")
        sportshoes = Product.objects.filter(subcategory="10")
        Mens_Top_Wear = Product.objects.filter(subcategory="11")
        womentop = Product.objects.filter(subcategory="12")
        menbottom = Product.objects.filter(subcategory="13")
        womenbottom = Product.objects.filter(subcategory="14")
        Watches = Product.objects.filter(subcategory="15")
        Bag = Product.objects.filter(subcategory="16")
        HomeAppliances = Product.objects.filter(subcategory="17")
        KitchenAppliances = Product.objects.filter(subcategory="18")
        Refregeator = Product.objects.filter(subcategory="19")
        AirConditioners = Product.objects.filter(subcategory="20")
        WashingMachine = Product.objects.filter(subcategory="21")

        return render(
            request,
            "home.html",
            {
                "deal_product": deal_product,
                "product": product, "subproducts": subproducts,
                "Mobiles": Mobiles,
                "latestproduct": latestproduct,
                "Laptops": Laptops,
                "WashingMachine": WashingMachine,
                "AirConditioners": AirConditioners,
                "Refregeator": Refregeator,
                "KitchenAppliances": KitchenAppliances,
                "HomeAppliances": HomeAppliances,
                "Accessories": Accessories,
                "Audio": Audio,
                "Smart_Warable": Smart_Warable,
                "Cameras": Cameras,
                "sportshoes": sportshoes,
                "Mens_Top_Wear": Mens_Top_Wear,
                "womentop": womentop,
                "menbottom": menbottom,
                "womenbottom": womenbottom,
                "Watches": Watches,
                "Bag": Bag,
            },
        )


class product_detail(View):
    def get(self, request, id):
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        product = Product.objects.get(id=id)
        item_already_in_cart = False
        if request.user.is_authenticated:
            item_already_in_cart = Cart.objects.filter(
                Q(product=product.id) & Q(user=request.user)
            ).exists()
        return render(
            request,
            "productdetail.html",
            {"products": product, "item_already_in_cart": item_already_in_cart,
                "product": headerproduct, "subproducts": subproducts},
        )


def Categories(request, id):
    headerproduct = Category.objects.all()
    subproducts = subCategory.objects.all()
    mobilesdata = Product.objects.filter(subcategory=id)
    for md in mobilesdata:
        print(md)

    return render(request, 'mobile.html', {"md": md, 'mobilesdata': mobilesdata, "product": headerproduct, "subproducts": subproducts})


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    def get(self, request):
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        form = CustomerProfileForm()
        return render(request, "profile.html", {"form": form, "active": "btn-primary", "product": headerproduct, "subproducts": subproducts})

    def post(self, request):
        # form = CustomerProfileForm(request.POST or None)

        form = CustomerProfileForm(request.POST)
        if request.method == "POST" and form.is_valid():
            user = request.user
            fname = form.cleaned_data["fname"]
            lname = form.cleaned_data["lname"]
            phone = form.cleaned_data["phone"]
            addone = form.cleaned_data["addone"]
            addtwo = form.cleaned_data["addtwo"]
            city = form.cleaned_data["city"]
            state = form.cleaned_data["state"]
            zipcode = form.cleaned_data["zipcode"]
            reg = Customer(
                user=user,
                fname=fname,
                lname=lname,
                phone=phone,
                addone=addone,
                addtwo=addtwo,
                city=city,
                state=state,
                zipcode=zipcode,
            )

            reg.save()
            messages.success(
                request, "Congratulation! Address Addedd Successfully")
            return redirect("/profile", {"form": form, "active": "btn-primary"})


def mobile(request, data=None):
    headerproduct = Category.objects.all()
    subproducts = subCategory.objects.all()
    if data == None:
        mobilesdata = Product.objects.filter(subcategory="4")
    elif data == "IPHONE" or data == "SAMSUNG":
        mobilesdata = Product.objects.filter(
            subcategory="4").filter(brand=data)
    elif data == "below":
        mobilesdata = Product.objects.filter(subcategory="4").filter(
            discount_price__lt=50000
        )
    elif data == "above":
        mobilesdata = Product.objects.filter(subcategory="4").filter(
            discount_price__gt=50000
        )
    return render(request, "mobile.html", {"mobilesdata": mobilesdata, "product": headerproduct, "subproducts": subproducts})


class CustomerRegistration(View):
    def get(self, request):
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        form = CustomerRegistrationForm()
        return render(request, "customerregistration.html", {"form": form, "product": headerproduct, "subproducts": subproducts})

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Configuration! Registraion Successfully Completed"
            )
        return render(request, "customerregistration.html", {"form": form})


@method_decorator(login_required, name="dispatch")
class AddressView(View):
    def get(self, request):
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        if request.user.is_authenticated:
            data = Customer.objects.filter(user=request.user)
            return render(
                request, "address.html", {
                    "data": data, "active": "btn-primary", "product": headerproduct, "subproducts": subproducts}
            )
        else:
            return redirect("/accounts/login")


@login_required
def add_to_cart(request):
    user = request.user
    product_id = request.GET.get("prod_id")
    product_title = Product.objects.get(id=product_id)
    Cart(user=user, product=product_title).save()
    print(product_id)
    return redirect("/showcart")


@login_required
def showcart(request):
    if request.user.is_authenticated:
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        user = request.user
        cart = Cart.objects.filter(user=user)
        print(cart)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user == user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * p.product.discount_price
                amount += tempamount
                total_amount = amount + shipping_amount
            return render(
                request,
                "addtocart.html",
                {
                    "cart": cart,
                    "total_amount": total_amount,
                    "amount": amount,
                    "shipping_amount": shipping_amount,
                    "product": headerproduct, "subproducts": subproducts
                },
            )
        else:
            return render(request, "empty.html", {"product": headerproduct, "subproducts": subproducts})
    else:
        return redirect("/accounts/login")


# def plusCart(request):
#     pass
@login_required
def plusCart(request):
    if request.method == "GET":
        # 2nd field will be ajax id
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity += 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * p.product.discount_price
                amount += tempamount

            data = {
                "quantity": c.quantity,
                "amount": amount,
                "totalamount": amount + shipping_amount,
            }

            return JsonResponse(data)


@login_required
def minusCart(request):
    if request.method == "GET":
        # 2nd field will be ajax id
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity -= 1
        c.save()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        print(cart_product)
        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * p.product.discount_price
                amount += tempamount

            data = {
                "quantity": c.quantity,
                "amount": amount,
                "totalamount": amount + shipping_amount,
            }

            return JsonResponse(data)


@login_required
def removeCart(request):
    if request.method == "GET":
        # 2nd field will be ajax id
        prod_id = request.GET["prod_id"]
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        print(cart_product)
        for p in cart_product:
            tempamount = p.quantity * p.product.discount_price
            amount += tempamount

        data = {
            "amount": amount,
            "totalamount": amount + shipping_amount,
        }
        return JsonResponse(data)


@login_required
def checkout(request):

    if request.user.is_authenticated:
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        user = request.user
        add = Customer.objects.filter(user=user)
        cart_items = Cart.objects.filter(user=user)
        amount = 0.0
        shipping_amount = 70.0
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user ==
                        request.user]
        if not add:
            return redirect("/profile")

        if cart_product:
            for p in cart_product:
                tempamount = p.quantity * p.product.discount_price
                amount += tempamount
                total_amount = amount + shipping_amount
                print(total_amount)
            a = c.convert(total_amount, "INR", "USD")
            main_amount = round(a, 2)
            print(main_amount)
            final_amount = main_amount
        return render(
            request,
            "checkout.html",
            {
                "add": add,
                "total_amount": total_amount,
                "cart_items": cart_items,
                "final_amount": final_amount,
                "amount": amount,
                "shipping_amount": shipping_amount,
                "product": headerproduct, "subproducts": subproducts
            },
        )
    else:
        return redirect("/accounts/login")


@login_required
def payment_done(request):
    user = request.user
    custid = request.GET.get("custid")
    print("custid", custid)
    customer = Customer.objects.get(id=custid)
    print("customer", customer)
    cart = Cart.objects.filter(user=user)
    print("cart", cart)
    for c in cart:
        OrderPlaced(
            user=user, customer=customer, product=c.product, quantity=c.quantity
        ).save()
        c.delete()
    return redirect("orders")


def buy_now(request):
    return render(request, "buynow.html")


@login_required
def orders(request):
    if request.user.is_authenticated:
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        user = request.user
        order_data = OrderPlaced.objects.filter(user=user)
        order_data1 = OrderPlaced.objects.all()
        if order_data:
            return render(request, "orders.html", {"order_data": order_data, "product": headerproduct, "subproducts": subproducts})
        else:
            return render(request, "orderEmpty.html")
    else:
        return redirect("/accounts/login")


class returnorder(View):
    def get(self, request, id):
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        order = OrderPlaced.objects.get(id=id)
        form = ReturnOrdersForm()
        print("order id", order)
        return render(request, "returnorder.html", {"order": order, "form": form, "product": headerproduct, "subproducts": subproducts})


class returnorderdata(View):
    def post(self, request, id):
        form = ReturnOrdersForm(request.POST)
        if form.is_valid():
            user = request.user
            order = OrderPlaced.objects.get(id=id)
            print("orderplaced id:-===========", order)
            rreason = form.cleaned_data["rreason"]
            bank_name = form.cleaned_data["bank_name"]
            bank_acc = form.cleaned_data["bank_acc"]
            bank_ifsc = form.cleaned_data["bank_ifsc"]
            holder_name = form.cleaned_data["holder_name"]
            upi_id = form.cleaned_data["upi_id"]
            reg = ReturnOrders(
                user=user,
                orderplaced=order,
                rreason=rreason,
                bank_name=bank_name,
                bank_acc=bank_acc,
                bank_ifsc=bank_ifsc,
                holder_name=holder_name,
                upi_id=upi_id,
            )
            reg.save()

            order.status = "Return"
            order.save()
            return redirect("/orders")


class cancleorderdata(View):
    def post(self, request, id):
        form = CancledOrdersForm(request.POST)
        if form.is_valid():
            user = request.user
            order = OrderPlaced.objects.get(id=id)
            reason = form.cleaned_data["reason"]
            bank_name = form.cleaned_data["bank_name"]
            bank_acc = form.cleaned_data["bank_acc"]
            bank_ifsc = form.cleaned_data["bank_ifsc"]
            holder_name = form.cleaned_data["holder_name"]
            upi_id = form.cleaned_data["upi_id"]
            reg = CancledOrders(
                user=user,
                orderplaced=order,
                reason=reason,
                bank_name=bank_name,
                bank_acc=bank_acc,
                bank_ifsc=bank_ifsc,
                holder_name=holder_name,
                upi_id=upi_id,
            )
            reg.save()
            order.status = "Cancled"

            order.save()
            return redirect("/orders")


class cancleorder(View):
    def get(self, request, id):
        headerproduct = Category.objects.all()
        subproducts = subCategory.objects.all()
        order = OrderPlaced.objects.get(id=id)
        form = CancledOrdersForm()
        print("order id", order)
        return render(request, "cancleorder.html", {"order": order, "form": form, "product": headerproduct, "subproducts": subproducts})


def PageNotFound(request):
    return render(request, "404.html")
