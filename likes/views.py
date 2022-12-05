from django.shortcuts import render

from likes.models import Like


def marta_view(request):
    if request.method == 'GET':
        if not Like.objects.all().count():
            like = Like()
            like.save()
            context = {'likes': like.count}
            return render(request, 'likes/marta.html', context=context)
        else:
            like = Like.objects.first()
            context = {'likes': like.count}
            return render(request, 'likes/marta.html', context=context)
    if request.method == 'POST':
        like = Like.objects.first()
        like.count += 1
        like.save()
        context = {'likes': like.count}
        return render(request, 'likes/marta.html', context=context)
