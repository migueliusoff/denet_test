import json

from django.conf import settings
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from core.services import PolygonInfoService


def get_balance_view(request: HttpRequest) -> JsonResponse:
    if request.method != "GET":
        return JsonResponse({"status": 405, "message": "Method Not Allowed"}, status=405)

    address = request.GET.get("address")
    if not address:
        return JsonResponse({"status": 400, "message": "Provide address GET parameter"}, status=400)

    service = PolygonInfoService(settings.CONTRACT_ADDRESS)
    balance = service.get_balance(address)
    return JsonResponse({"balance": balance})


@csrf_exempt
def get_balance_batch_view(request: HttpRequest) -> JsonResponse:
    if request.method != "POST":
        return JsonResponse({"status": 405, "message": "Method Not Allowed"}, status=405)

    addresses = json.loads(request.body).get("addresses")
    if not addresses:
        return JsonResponse({"status": 400, "message": "Provide addresses list"}, status=400)

    service = PolygonInfoService(settings.CONTRACT_ADDRESS)
    balances = service.get_balance_batch(addresses)
    return JsonResponse({"balances": balances})


def get_top_view(request: HttpRequest) -> JsonResponse:
    if request.method != "GET":
        return JsonResponse({"status": 405, "message": "Method Not Allowed"}, status=405)

    n = request.GET.get("n")
    if not n:
        return JsonResponse({"status": 400, "message": "Provide n GET parameter"}, status=400)

    try:
        int(n)
    except ValueError:
        return JsonResponse({"status": 400, "message": "n parameter must be an integer"}, status=400)

    service = PolygonInfoService(settings.CONTRACT_ADDRESS)
    top = service.get_top(int(n))
    return JsonResponse({"top": top})


def get_token_info_view(request: HttpRequest) -> JsonResponse:
    if request.method != "GET":
        return JsonResponse({"status": 405, "message": "Method Not Allowed"}, status=405)

    token_address = request.GET.get("token_address")
    if not token_address:
        return JsonResponse({"status": 400, "message": "Provide n GET parameter"}, status=400)

    service = PolygonInfoService(settings.CONTRACT_ADDRESS)
    info = service.get_token_info(token_address)
    return JsonResponse({"token_info": info})
