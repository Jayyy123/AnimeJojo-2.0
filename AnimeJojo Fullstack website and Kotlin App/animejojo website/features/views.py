from django.shortcuts import render




def features(request):
    return render(request, 'features/features.html')

def wallpapers(request):
    return render(request, 'features/wallpapers.html')

def animeQuiz(request):
    return render(request, 'features/animequiz.html')

def randomAnime(request):
    return render(request, 'features/page.html')

def characterize(request):
    return render(request, 'features/characterize.html')

