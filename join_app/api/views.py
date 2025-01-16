from restframework.decorators import api_view
from restframework.response import response

@api_view()
def first_view(request):
    return Response({"message":"Hallo World!"})