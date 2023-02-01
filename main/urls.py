from django.urls import path

from main.views import (
    AddDefinitionView,
    DefineView,
    DeleteDefinitionView,
    GetDefinitionView,
    HealthCheckView,
    ListDefinitionsView,
)

define_urls = (
    [
        path("add", view=AddDefinitionView.as_view(), name="add"),
        path("get", view=GetDefinitionView.as_view(), name="get"),
        path("define", view=DefineView.as_view(), name="define"),
        path("list", view=ListDefinitionsView.as_view(), name="list"),
        path("delete", view=DeleteDefinitionView.as_view(), name="delete"),
        path("health_check", view=HealthCheckView.as_view(), name="health_check"),
    ],
    "define",
)
