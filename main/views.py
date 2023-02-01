import re
from typing import Dict
from urllib.parse import unquote

from django.http import HttpResponse
from rest_framework import views

from main.manager import create_definition, get_definitions
from main.serializers import CreateDefintionSerializer


# convert x-www-form-urlencoded to json
def convert_x_www_form_data_to_dict(data: str) -> Dict[str, str]:
    return {k: unquote(v) for k, v in [x.split("=") for x in data.split("&")]}


# format incoming slack message
# slack send text with plus signs for spaces
def format_incoming_slack_message(text: str) -> str:
    spaced_def = re.sub(r"(?<!\\)\+", " ", text)
    return spaced_def.replace("\\+", "+").replace("\+", "+")


# slack route
class DefineView(views.APIView):
    def post(self, request):
        return self._handle_request(request)

    def get(self, request):
        return self._handle_request(request)

    def _handle_request(self, request):
        request_data = convert_x_www_form_data_to_dict(request.body.decode("utf-8"))
        if "text" not in request_data:
            return HttpResponse("")

        argument = request_data["text"]
        args = argument.split("=", maxsplit=1)
        response_text = ""

        if len(args) == 1:
            term = args[0]
            response_text = f"Definition(s) for {term}:\n"
            definitions = get_definitions(term)
            if not definitions:
                response_text = (
                    f"No definition found for {term} create one with /define {term}=[definition]"
                )
            if len(definitions) == 1:
                response_text += definitions[0].definition
            else:
                response_text += "\n".join(
                    f"{idx+1}. {d.definition}" for idx, d in enumerate(definitions)
                )

        elif len(args) == 2:
            term, new_def = args
            formated_def = format_incoming_slack_message(new_def)
            new_def = create_definition(term, formated_def)
            response_text = f"Added definition for {term}: {new_def.definition}"

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
