from django.urls import path

from core.views import get_balance_batch_view, get_balance_view, get_token_info_view, get_top_view

urlpatterns = [
    path("get_balance", get_balance_view, name="get-balance"),
    path("get_balance_batch", get_balance_batch_view, name="get-balance-batch"),
    path("top", get_top_view, name="top"),
    path("get_token_info", get_token_info_view, name="get-token-info"),
]
