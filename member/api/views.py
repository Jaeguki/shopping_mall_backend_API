from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view

from member.models import Member


@api_view(['POST'])
def login(request):
    results = Member.objects.filter(id=request.POST['id']).filter(password=request.POST['password'])
    if len(results) == 0:
        return JsonResponse({'result': 'fail'})
    else:
        return JsonResponse({'data': model_to_dict(results[0]), 'result': 'success'})


@api_view(['POST'])
def check_id(request):
    try:
        member = Member.objects.get(email=request.GET['id'])
    except Exception as e:
        member = None

    result = {
        'result': 'success',
        'data': 'not exist' if member is None else 'exist'
    }

    return JsonResponse(result)
