from django.shortcuts import render
from .models import Video
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    videos_list=Video.objects.order_by('-date_posted')
    videos= Paginator(videos_list,3)

    grouped_videos=[]
    for page in videos.page_range:
        page_objects=videos.page(page).object_list
        grouped_videos.append(page_objects)

    context={'videos':videos,'grouped_videos':grouped_videos}

    return render(request,'video/index.html',context)




def video(request,video_id):
    the_video= Video.objects.get(pk=video_id)

    context={'the_video':the_video}
    return render(request,'video/video.html',context)    