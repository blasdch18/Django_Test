from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .models import Poll

def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:20]
    data = {"results": list(polls.values("pk", "name", "created_by", "created"))}
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll, pk=pk)
    data = {"results": {
        "name": poll.name,
        "created_by": poll.created_by.username,
        "created": poll.created,
        "updated": poll.updated
    }}
    return JsonResponse(data)