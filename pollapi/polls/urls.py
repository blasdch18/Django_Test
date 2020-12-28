# polls/urls.py
from django.urls import path

#from .views import QuestionViewSet
#from .views import ChoiceViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import routers

from django.urls import path
from .views import polls_list, polls_detail
from .apiviews import ChoiceList, CreateChoice
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path("questions", ChoiceList.as_view(), name="choice_list"),
    path("choices/", CreateChoice.as_view(), name="create_choice"),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title='Polls API')),
]


"""
router = routers.DefaultRouter()
router.register('', QuestionViewSet, basename='questions')
router.register(r'choices', ChoiceViewSet, basename='choices')
urlpatterns = router.urls
"""