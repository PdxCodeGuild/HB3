from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet, TypeViewSet, NoteViewSet

router = DefaultRouter()
# after creating a router end point register views to a path
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('types', TypeViewSet, basename='types')
router.register('notes', NoteViewSet, basename='notes')

urlpatterns = router.urls + [

]