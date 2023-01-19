from django.urls import path

from main.views import AddDefinitionView, DefineView, GetDefinitionView

define_urls = (
    [
        path("add", view=AddDefinitionView.as_view(), name="add"),
        path("get", view=GetDefinitionView.as_view(), name="get"),
        path("define", view=DefineView.as_view(), name="define"),
    ],
    "define",
)
