from django.shortcuts import render
from django.contrib import messages
from .models import trainer
from .froms import trainFrom
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import re
# Create your views here.
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
rule = "^[0-9]{10}|[0-9]{12}$"

tt = trainer.objects.order_by("id")
ltE = []
ltM = []
for i in tt:
    ltE.append(i.Email)
    ltM.append(i.Mobile_number)


def index(request):
    print(ltE)
    print(ltM)
    if request.method == "POST":
        form = trainFrom(request.POST)
        email = request.POST['Email']
        phone = request.POST['Mobile_number']

        if not (re.search(regex, email)):
            return render(request, 'index.html', {'email_err': "please enter valid email"})
        if not (re.search(rule, phone)):
            return render(request, 'index.html', {'phone_err': "Invalid mobile number"})
        if phone in ltM and email in ltE:
            return render(request, 'index.html', {'phone_err': "this phone in alredy use", 'email_err': "this email in alredy in use"})
        if email in ltE:
            return render(request, 'index.html', {'email_err': "this email in alredy in use"})
        if phone in ltM:
            return render(request, 'index.html', {'phone_err': "this phone in alredy use"})

        if form.is_valid():
            form.save()
    return render(request, 'index.html', {})


def home(request):
    print("runing")
    item_list = trainer.objects.order_by("id")
    paginator = Paginator(item_list, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    if request.method == 'POST':
        search_query = request.POST['search']
        print("going")
        results = trainer.objects.filter(Q(Name__icontains=search_query) | Q(Country__icontains=search_query) | Q(Skills__icontains=search_query) | Q(
            Email__icontains=search_query) | Q(Mobile_number=search_query) | Q(Profession=search_query) | Q(Address__icontains=search_query))
        paginator = Paginator(results, 3)  # 3 posts in each page
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            post_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            post_list = paginator.page(paginator.num_pages)

        return render(request, 'home.html', {'page': page, 'post_list': post_list})
    return render(request, 'home.html', {'page': page, 'post_list': post_list})
