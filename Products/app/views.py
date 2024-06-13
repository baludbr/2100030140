from django.http import JsonResponse
import requests

BEARER_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE4MjY1NTU1LCJpYXQiOjE3MTgyNjUyNTUsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6IjdlODM5YzIwLTJjZmItNDNiZS05Nzg3LTg0NDZjNzdiYjFjZSIsInN1YiI6ImR3YXJhbXB1ZGliYWxhamlyZWRkeUBnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJLTCBVTklWRVJTSVRZIiwiY2xpZW50SUQiOiI3ZTgzOWMyMC0yY2ZiLTQzYmUtOTc4Ny04NDQ2Yzc3YmIxY2UiLCJjbGllbnRTZWNyZXQiOiJJWEdxZlVpd2Rpa2FsbU5wIiwib3duZXJOYW1lIjoiRFdBUkFNUFVESSBCQUxBSkkgUkVERFkiLCJvd25lckVtYWlsIjoiZHdhcmFtcHVkaWJhbGFqaXJlZGR5QGdtYWlsLmNvbSIsInJvbGxObyI6IjIxMDAwMzAxNDAifQ.pQty5LQjNLBGfHsMY58qeC2V8Qm-zD6S2VkrroAskDI"


def top_products(request, cn, can):
    minp=request.GET.get('minPrice', 0)
    n=int(request.GET.get('n', 10))
    pg=int(request.GET.get('pg', 1))
    maxp=request.GET.get('maxPrice', 1000000)
    sort_by=request.GET.get('sortBy', 'price')
    order=request.GET.get('order', 'asc')

    url = f'http://20.244.56.144/test/companies/{cn}/categories/{can}/products'
    pd = {
        'top': n,
        'minPrice': minp,
        'maxPrice': maxp
    }

    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
    }

    res = requests.get(url,headers=headers,params=pd)

    if res.status_code ==200:
        products = res.json()

        for i in products:
            i['category'] = can
            i['company'] = cn
           

        rorder = order == 'desc'
        products = sorted(products, key=lambda x: x.get(sort_by, 0), reverse=rorder)

        stind = (pg - 1) * n
        endind = stind + n
        p_prod = products[stind:endind]

        res_data = {
            'total_products': len(products),
            'total_pgs': (len(products) + n - 1) // n,
            'current_pg': pg,
            'products': p_prod
        }

        return JsonResponse(res_data)
    else:
        return JsonResponse({'error': 'Failed to fetch products'}, status=res.status_code)
