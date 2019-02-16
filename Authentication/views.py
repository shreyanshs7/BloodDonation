from django.shortcuts import render
from Helpers.methods import respond
from django.contrib.auth.models
from Helpers.methods import get_or_none
from Helpers.tokens import token_required, generate_token
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from Helpers.utils import assert_found, assert_true
from Authentication.models import Hospital, UserDetail
from Helpers.serializers import get_model_json

# Create your views here.
@require_http_methods(['POST'])
def user_hospital_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = get_or_none(User, username = username)
    assert_found(user, "Account with username not found")
    response = {}
    if user.check_password(password):
        response['success'] = True
        response['token'] = generate_token(user)
        return respond(reponse)
    response['success'] = False
    response['message'] = "Invalid Credentials"
    return respond(response)

@require_http_methods(['POST'])
def hospital_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    name = request.POST.get('name')
    state = request.POST.get('state')
    city = request.POST.get('city')
    address = request.POST.get('address')
    contact = request.POST.get('contact')
    latitude = request.POST.get('latitude')
    longitude = request.POST.get('longitude')

    hospital = get_or_none(User, username = username)
    assert_true(hospital != None, "Account with this username already exists")
    hospital_user_obj = User.objects.create_user(username = username, password = password)
    hospital_user_obj.save()
    hospital_obj = Hospital.objects.create(username = hospital_user_obj, name = name, state = state, city = city, address = address, contact = contact)
    hospital_obj.save()

    response = {}
    response['success'] = False
    reponse['data'] = get_model_json(hospital_obj)
    return respond(reponse)

@require_http_methods(['POST'])
def user_register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    state = request.POST.get('state')
    city = request.POST.get('city')
    address = request.POST.get('address')
    contact = request.POST.get('contact')
    weight = request.POST.get('weight')
    gender = request.POST.get('gender')

    user = get_or_none(User, username = username)
    assert_true(user != None, "Account with this username already exists")
    user_obj = User.objects.create_user(username = username, password = password)
    user_obj.save()
    user_detail_obj = UserDetail.objects.create(username = user_obj, first_name = first_name, last_name = last_name, state = state, city = city, address = address, contact = contact, weight = weight, gender = gender)
    user_detail_obj.save()

    response = {}
    response['success'] = False
    reponse['data'] = get_model_json(user_detail_obj)
    return respond(reponse)