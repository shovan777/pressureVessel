from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@require_http_methods(['POST', 'GET'])
@csrf_exempt
def data(request):
    """Calculate nozzle detail and weild sizing.

    Parameters
    ----------
    request : type
        Description of parameter `request`.

    Returns
    -------
    t_c: float
        minimum fillet weild throat dimension
    r_1: float
        minimum inside corner radius

    """
    if request.method == 'POST':
        # GET THE VALUES FROM swain
        cylinder_t = 0.625
        nozzle_d = 10
        nozzle_t = 0.5
        C_A = 0.125

        t_c = calculate_t_c(cylinder_t, nozzle_t, C_A)
