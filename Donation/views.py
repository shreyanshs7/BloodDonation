from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from Helpers.tokens import token_required, get_user
from Helpers.utils import assert_found
from Helpers.methods import respond
from Donation.models import DonationRequest, Donor
from Helpers.serializers import get_model_json

# Create your views here.
@token_required
@require_http_methods(['POST'])
def donation_request(request):
    token = request.META.get('HTTP_AUTHORIZATION')
    user = get_user(token)
    assert_found(user, "No user found")
    blood_type = request.POST.get('blood_type')
    units_of_blood = request.POST.get('units_of_blood')
    is_urgent = request.POST.get('is_urgent')
    donation_request_obj = DonationRequest.objects.create(donation_request_by = user, blood_type = blood_type, units_of_blood = units_of_blood, is_urgent = is_urgent)
    donation_request_obj.save()

    response = {}
    response['success'] = True
    response['message'] = "Donation request successfully made"
    return respond(respond)
    

@require_http_methods(['GET'])
def donor_list(request):
    donors = Donor.objects.all()
    donors_list []
    for obj in donors:
        temp = get_model_json(obj)
        donor_list.append(temp)
    response = {}
    respond['success'] = True
    response['data'] = donors_list
    return respond(reponse)