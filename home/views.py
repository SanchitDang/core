import json
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from apis.models import Users, Bids, Assessment
from .models import PanelUser,Assessments
from .forms import DynamicAssessmentForm, LoginForm,UserForm,AssessmentForm,ItemsSubCategoriesForm,ItemsCategoryForm,MyprofleForm,DomainsForm,UserTypeForm
from apis.models import  ItemsSubCategories,ItemsCategory,Scraps,Services,Products,Referral,Domains,UserType




def panel_login(request):
    
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user_type = form.cleaned_data['user_type']
            user = PanelUser.objects.filter(email=email, password=password).first()
            if user is not None:
                login(request, user,backend='home.models.PanelUserAuthBackend')
                return redirect('dashboard')
            else:
                print("User not found")
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
        else:
            return render(request, 'login.html', {'form': form, 'error': 'Invalid form data'})
        
    return render(request, 'login.html', {'form': form})



def panel_logout(request):

    return redirect('panel_login')


@login_required(login_url='panel_login')
def dashboard(request):
    print("user login",request.user.is_authenticated)
    # Get the count of all users
    user_count = Users.objects.count()

    # Get the count of users based on user_type
    supplier_count = Users.objects.filter(user_type='supplier').count()
    manufacturer_count = Users.objects.filter(user_type='manufacturer').count()
    referral_count = Users.objects.filter(user_type='referral').count()

    bid_count = Bids.objects.count()

    on_going_bid_count= Bids.objects.filter(bid_status='on_going').count()
    bid_finished_count = Bids.objects.filter(bid_status='finished').count()
    bid_cancelled_count = Bids.objects.filter(bid_status='cancelled').count()


    context = {
        "manufacturer": "manufacturer",
        "supplier": "supplier",
        'user_count': user_count,
        'bid_count': bid_count,
        'supplier_count': supplier_count,
        'manufacturer_count': manufacturer_count,
        'referral_count': referral_count,
        "bid_cancelled_count": bid_cancelled_count,
        "on_going_bid_count": on_going_bid_count,
        "bid_finished_count": bid_finished_count
    }

   

    return render(request, 'dashboard.html', context)





def my_profile(request):
    user_id = request.user.id

    user = PanelUser.objects.filter(id=user_id).first()

    print("Profile user",user)
    if user is None:
        print("User not found")
        messages.success(request, 'User not found')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    form = MyprofleForm(instance=user)
    if request.method == 'POST':
        form = MyprofleForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            print("User saved")
            messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print(form.errors)

    return render(request, 'my-profile.html', {'form': form, 'user_id': user_id})



def edit_user_profile(request, id):
    user = Users.objects.get(id=id)

    user.user_types = user.user_types[0]

    print("User type",user.user_types)

    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            print("User saved")
            messages.success(request, 'Profile updated successfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print(form.errors)
        

    return render(request, 'user-profile.html', {'form': form,'userid': id,"user":user})



def edit_user_assessment(request, id):
    print("Assessment id",id)
    assessment = Assessments.objects.filter(created_by=id).first()
    if assessment is None:
        print("Assessment not found")
        messages.success(request, 'Assessment not found')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        print("Assessment found")
    form = AssessmentForm(instance=assessment)
    if request.method == 'POST':
        form = AssessmentForm(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
            print("Assessment saved")
            messages.success(request, 'Assessment updated successfully')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            print(form.errors)

    return render(request, 'user-assement.html', {'form': form})



def manufacturers_list(request):
    users = Users.objects.filter(user_type='manufacturer')

    context = {
        'users': users
    }

    return render(request, 'user-type-list.html', context)




def suppliers_list(request):
    users = Users.objects.filter(user_type='supplier')

    context = {
        'users': users
    }

    return render(request, 'user-type-list.html', context)






def bids_by_type_view(request):
    bid_type = request.GET.get('bid_type', '')  # Assuming bid_type is a field in your Bids model
    bids = Bids.objects.filter(bid_type=bid_type)

    return render(request, 'bids.html', {'bids': bids, 'bid_type': bid_type,})



def bids_view(request):
    bids = Bids.objects.all()

    return render(request, 'bid-list.html', {'bids': bids,})


def bids_edit_view(request,bid_id):    

    bid = Bids.objects.filter(id=bid_id)

    if request.method == "POST":
            bid_id = request.POST.get('id')
            bid = get_object_or_404(Bids, id=bid_id)

            bid.item = request.POST.get('item')
            bid.description = request.POST.get('description')
            bid.price = request.POST.get('price') 
            bid.bid_type = request.POST.get('bid_type')
            bid.bid_category = request.POST.get('bid_category')
            bid.bid_sub_category = request.POST.get('bid_sub_category')
            bid.bid_opening_time = request.POST.get('bid_opening_time')
            bid.bid_closing_time = request.POST.get('bid_closing_time')

            bid.save()  

            bid_id = request.GET.get('id', '')       
            bid = Bids.objects.filter(id=bid_id)
            return render(request, 'edit-bid.html', {'bid_data': bid, 'bid_id': bid_id,})

    return render(request, 'edit-bid.html', {'bid_data': bid, 'bid_id': bid_id,})



def toggle_approval(request, bid_id):
    try:
        print("bid_id found ", bid_id)
        bid = Bids.objects.get(id=bid_id)
        bid.is_approved = 'no' if bid.is_approved == 'yes' else 'yes'
        bid.save()
        return JsonResponse({'status': 'success', 'is_approved': bid.is_approved})
    except Bids.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Bid not found'}, status=404)

def create_assessment(request):
    if request.method == 'POST':
        # Process dynamic data and convert it to JSON
        dynamic_data = {}
        for key, value in request.POST.items():
            if key.startswith('data_key_') and value:
                field_number = key.split('_')[-1]
                data_key = value
                data_value = request.POST.get(f'data_value_{field_number}')
                dynamic_data[data_key] = data_value

        Assessment.objects.create(data=dynamic_data)
        return redirect('/')  # Redirect to the assessment list vie

    return render(request, 'create_assessment.html',)





def edit_assessment(request, assessment_id):
    assessment = Assessment.objects.get(pk=assessment_id)
    form_data = {}
    for i, (key, value) in enumerate(assessment.data.items()):
        form_data['data_key_{}'.format(i)] = key
        form_data['data_value_{}'.format(i)] = value

    form = DynamicAssessmentForm(initial=form_data)

    if request.method == 'POST':
        dynamic_data = {}
        for key, value in request.POST.items():
            if key.startswith('data_key_') and value:
                field_number = key.split('_')[-1]
                data_key = value
                data_value = request.POST.get(f'data_value_{field_number}')
                dynamic_data[data_key] = data_value

        assessment.data = dynamic_data
        assessment.save()
        return redirect('/')  # Redirect to the assessment list view

    return render(request, 'edit_assessment.html', {'data': form_data, 'form': form,})




def category_list(request):
    categories = ItemsCategory.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'category-list.html', context)




def add_category(request):
    form = ItemsCategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    
    return render(request, 'add-update-category.html', {'form': form,})



def update_category(request, category_id):
    category = ItemsCategory.objects.get(id=category_id)
    form = ItemsCategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    
    return render(request, 'add-update-category.html', {'form': form, 'category_id': category_id,})




def delete_category(request, category_id):
    category = ItemsCategory.objects.get(id=category_id)
    subcategory=ItemsSubCategories.objects.filter(category_id=category_id) 
    if subcategory:
        for sub in subcategory:
            sub.delete()
    category.delete()
    return redirect('category_list')



def sub_category_list(request):
    sub_categories = ItemsSubCategories.objects.all()
    # get category list from ItemsSubCategories.ItemsCategory


    # for category in sub_categories:
        # print(category.category_id)
        # category_name = ItemsCategory.objects.get(id=category.category_id)
        # print(category_name.category)
        # category.category_id = category_name.category
    
    context = {
        'sub_categories': sub_categories

    }

    return render(request, 'sub-category-list.html', context)



def add_sub_category(request,):
    form = ItemsSubCategoriesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('sub_category_list')
    
    return render(request, 'add-update-sub-category.html', {'form': form})



def update_sub_category(request, sub_category_id):
    sub_category = ItemsSubCategories.objects.get(id=sub_category_id)
    form = ItemsSubCategoriesForm(request.POST or None, instance=sub_category)
    if form.is_valid(): 
        form.save()
        return redirect('sub_category_list')
    

    return render(request, 'add-update-sub-category.html', {'form': form, 'sub_category_id': sub_category_id,})


def view_product(request,user_id):
    product = Products.objects.filter(user_id=user_id)
    type = "product"
    return render(request, 'view-product-scrvices-scrap.html' , {"datas":product, "type":type})


def view_scrvices(request,user_id):
    services = Services.objects.filter(user_id=user_id)
    type = "services"
    return render(request, 'view-product-scrvices-scrap.html',{"datas":services, "type":type})


def view_scrap(request,user_id):
    scrap = Scraps.objects.filter(user_id=user_id)
    type = "scrap"
    return render(request, 'view-product-scrvices-scrap.html',{"datas":scrap, "type":type})



def referral_list(request):
    referral = Referral.objects.all()
    return render(request, 'referral-list.html',{"referrals":referral})

def delete_referral(request,referral_id):
    referral = Referral.objects.get(id=referral_id)
    referral.delete()
    return redirect('referral_list')



def manufacturer_bids_list(request,user_id):
    bids = Bids.objects.filter(party1_id=user_id)
    return render(request, 'bid-list.html',{"bids":bids})




def supplier_bids_list(request,user_id):
    bids = Bids.objects.all()

    bid_list =[]

    for b in bids:

        if b.other_parties :
            data_list = json.loads(b.other_parties)

            for data in list(data_list):
                if data['party_id'] == user_id:
                    bid_list.append(b)

    return render(request, 'supplier-bid-list.html',{"bids":bid_list,"user_id":user_id})


def supplier_view_bid_details(request,user_id,bid_id):
    bid = Bids.objects.get(id=bid_id)
    for b in json.loads(bid.other_parties):
        if b['party_id'] == user_id:
            bid.other_parties = b
            break
    return render(request, 'view-bid-details.html',{"bid":bid})




def domains_list(request):
    domanis = Domains.objects.all()

    return render(request, 'user-domanis-list.html',{"datas":domanis})


def add_domains(request):
    form = DomainsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('domains_list')
    
    return render(request, 'add-update-domanis-user-type.html', {'form': form})


def user_type_list(request):
    user_type = UserType.objects.all()

    return render(request, 'user-domanis-list.html',{"datas":user_type})


def add_user_type(request):
    form = UserTypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_type_list')
    
    return render(request, 'add-update-domanis-user-type.html', {'form': form})

