from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse
import yt_dlp as youtube_dl
import os
from urllib.parse import quote

def index(request):
    # Get success message from the request
    success_message = request.GET.get('success')
    return render(request, 'youtube.html', {'success_message': success_message})

def download(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        ydl_opts = {
            'format': 'best',  # Download the best available format
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,  # Download single video
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = f"{info_dict['title']}.mp4"

            # Check if the file exists and return it
            if os.path.isfile(filename):
                response = FileResponse(open(filename, 'rb'), content_type='video/mp4')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'
                # After sending the file, delete it
                os.remove(filename)
                
                # URL encode the success message
                success_message = quote(f"Video '{info_dict['title']}' successfully downloaded.")
                return redirect(f'/?success={success_message}')
    return HttpResponse("Successfully Downloaded.")
