from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Welcome to My Site',
        'content': 'This is the homepage of My Site.',
    }
    return render(request, 'download.html', context)

from django.http import HttpResponse
from pytube import YouTube
from urllib.parse import unquote

from django.http import HttpResponse
from pytube import YouTube
from urllib.parse import unquote
import requests

def download(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        if url:
            try:
                yt = YouTube(unquote(url))
                stream = yt.streams.get_highest_resolution()
                if stream:
                    video_content = requests.get(stream.url).content
                    filename = stream.default_filename
                    response = HttpResponse(video_content, content_type='video/mp4')
                    response['Content-Disposition'] = f'attachment; filename="{filename}"'
                    return response
                else:
                    return HttpResponse("No stream available for this video.", status=400)
            except Exception as e:
                return HttpResponse(f"An error occurred: {str(e)}", status=400)
        else:
            return HttpResponse("No URL provided", status=400)
    else:
        return HttpResponse("Method not allowed", status=405)
