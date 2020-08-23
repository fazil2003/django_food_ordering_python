from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Products,Users,Orders,Total

# Create your views here.
def home(request,methods=['GET']):
    products=Products.objects.all()
    kart=''
    total=0
    username=request.session['username']
    phone = request.session['phone']
    return render(request,"home.html",{'products':products,'kart':kart,'total':total,'username':username,'phone':phone})

def home1(request,methods=['GET']):
    products=Products.objects.all()
    kart=request.GET['kart']
    total=len(kart)

    username = request.session['username']
    phone = request.session['phone']
    last='last del yes'
    return render(request, "home.html",{'last':last,'products': products, 'kart': kart, 'total': total, 'username': username, 'phone': phone})


def profile(request,methods=['GET']):
    phone1=int(request.session['phone'])
    name1 = request.session['username']
    t1=Users.objects.filter(phone=phone1).first()
    name=str(t1.name)
    phone=int(t1.phone)
    password=str(t1.password)
    address=str(t1.address)
    return render(request, "profile.html",{'name':name,'phone':phone,'password':password,'address':address})

def update_profile(request,methods=['POST']):
    phone1 = int(request.session['phone'])

    new_phone = int(request.POST['phone'])
    new_password = str(request.POST['password'])
    new_username = str(request.POST['name'])
    new_address = str(request.POST['address'])

    Users.objects.filter(phone=phone1).update(phone=new_phone)
    Users.objects.filter(phone=new_phone).update(name=new_username)
    Users.objects.filter(phone=new_phone).update(address=new_address)
    Users.objects.filter(phone=new_phone).update(password=new_password)

    request.session['username']=new_username
    request.session['phone']=new_phone

    return redirect("/home")

def login(request,methods=['GET']):
    return render(request,"login.html")

def logout(request):
    del request.session['phone']
    del request.session['username']
    return redirect("/")

def register(request,methods=['POST']):
    new_phone = int(request.POST['phone'])
    new_password = str(request.POST['password'])
    new_username = str(request.POST['name'])
    new_address = str(request.POST['address'])
    t4=Users(name=new_username,phone=new_phone,address=new_address,password=new_password)
    t4.save()

    request.session['username'] = new_username
    request.session['phone'] = new_phone

    return redirect("/home")

def validate(request,methods=['POST']):
    phone = int(request.POST['phone'])
    password=str(request.POST['password'])

    t=Users.objects.filter(phone=phone).first()
    if(t.password==password):
        request.session['username']=t.name
        request.session['phone'] = t.phone
        return redirect("/home")
    else:
        return redirect("/")


def other(request,methods=['POST']):
    choice=request.GET['choice']
    if(choice=='help'):
        choice='Help - foodSpace'
        text='This is an help page'
    else:
        choice='Terms & Conditions - foodSpace'
        text='This is the terms & conditions page'
    return render(request,"other.html",{'choice':choice,'text':text})

def add_to_kart(request,methods=['GET']):
    id = request.GET['id']
    kart=str(request.GET['kart'])
    kart=kart+id

    return render(request, "add_to_kart.html", {'id': id,'kart':kart})

def mykart(request,methods=['GET']):
    kart = str(request.GET['kart'])
    sum=0
    mydict=dict()
    pricedict=dict()
    for item in kart:
        t=Products.objects.filter(id=item).first()
        sum=sum+int(t.price)
        name=str(t.name)
        price_rate=int(t.price)
        if(name in mydict):
            mydict[name]=mydict[name]+1
            pricedict[name]=pricedict[name]+price_rate
        else:
            mydict[name]=1
            pricedict[name] = price_rate
    bill_amount=[]
    counter=1
    for key,value in mydict.items():
        values=str(counter)+". "+key+" ✕ "+str(value)+" = ₹"+str(pricedict[key])+" "
        bill_amount.append(values)
        counter=counter+1
    total = str(request.GET['total'])
    return render(request,"mykart.html",{'kart':kart,'total':total,'sum':sum,'mydict':mydict,'bill_amount':bill_amount})

def checkout(request,methods=['GET']):
    phone1 = int(request.session['phone'])
    name1 = request.session['username']
    orders1 = request.GET['orders']
    sum=request.GET['sum']
    t5 = Orders(name=name1, phone=phone1, orders=orders1,sum=sum)
    t5.save()

    return redirect("/home")

def admin(request):
    #q=Orders.objects.all()
    q = Orders.objects.order_by('-id').all() #id desc so -id if not desc then id
    t = Total.objects.filter(id=1).first()
    if(t):
        sum = int(t.earn)
    else:
        sum=0

    return render(request, "admin.html", {'q': q,'total':sum})

def complete_order(request,method=['GET']):
    id=int(request.GET['id'])
    sum=int(request.GET['sum'])
    t=Total.objects.filter(id=1).first()
    if (t):
        value = sum + int(t.earn)
    else:
        value = sum

    Total.objects.filter(id=1).update(earn=value)
    Orders.objects.filter(id=id).delete()
    return redirect("/admin")




