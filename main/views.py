from typing import Dict, List
from urllib.parse import quote, unquote

from django.http import HttpResponse
from rest_framework import views

from main.manager import create_definition, get_definitions
from main.models import Definition
from main.serializers import CreateDefintionSerializer


# convert x-www-form-urlencoded to json
def convert_x_www_form_data_to_dict(data: str) -> Dict[str, str]:
    return {k: unquote(v) for k, v in [x.split("=") for x in data.split("&")]}


# slack route
class DefineView(views.APIView):
    def get(self, request):
        request_data = convert_x_www_form_data_to_dict(request.body.decode("utf-8"))
        if "text" not in request_data:
            return HttpResponse("")

        definitions: List[Definition] = []

        argument = request_data["text"]
        args = argument.split("=", maxsplit=1)
        if len(args) == 1:
            term = args[0]
            definitions = get_definitions(term)

        elif len(args) == 2:
            term, new_def = args
            definitions = [create_definition(term, new_def)]

        response_text = "\n".join(quote(d.definition) for d in definitions)

        return HttpResponse(response_text)


# Convinience/testing routes
class AddDefinitionView(views.APIView):
    def post(self, request):
        serializer = CreateDefintionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_definition(**serializer.validated_data)

        return HttpResponse()


class GetDefinitionView(views.APIView):
    def get(self, request):
        term = request.query_params.get("term")

        defins = get_definitions(term)

        response_text = "\n".join(d.definition for d in defins)

        return HttpResponse(response_text)
