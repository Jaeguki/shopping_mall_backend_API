from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from mall.models import Mall


@api_view(['GET'])
def get_mall(request, mall_link):
    results = Mall.objects.filter(link=mall_link)
    if len(results) == 0:
        return JsonResponse({'result': 'fail'})
    else:
        return JsonResponse({'data': model_to_dict(results[0]), 'result': 'success'})

