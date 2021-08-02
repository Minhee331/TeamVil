from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import render
from .models import *
from account.models import *
from django.contrib.auth.models import User
import json

# Create your views here.
#커뮤니티 리스트 함수
def community_list_back(request):
    community = Com.objects.all().order_by('-id')
    return render(request,'community copy.html', {'community':community})

def community_detail_back(request, community_id):
    community = Com.objects.get(id = community_id)
    comments = Comment.objects.filter(com_id = community, parent = 0)
    #대댓글
    replydict = {} #dict 형식
    for comment in comments:
        replylist = []
        replies = Comment.objects.filter(parent = comment.id) #replies변수에 parent랑 comment.id랑 같은 값들 모두 넣어줌 
        for reply in replies: #가져 온 값들을 for문으로 하나하나 돌리기
            replylist.append(reply) #하나하나 나온 reply를 replylist에 넣어줌
        replydict[str(comment.id)] = replylist  #딕셔너리 형태로, str(comment.id)가 key이고 replylist가 value;
    # replys = Comment.objects.filter(com_id = community, parent = comment_id) 
    return render(request, 'community copy.html', {'community':community, "comments":comments, "replydict":replydict.items()})

def community_new_back(request):
    user = request.user
    return render(request, 'community_new_back.html',{'user':user})

def community_new_db_back(request):
    obj = json.loads(request.body)
    com = Com()
    com.user_id = request.user
    com.content = obj['content']
    com.save()
    return render(request, 'community_list_back.html')

def comment(request):
    obj = json.loads(request.body)
    comment = Comment()
    comment.user_id = request.user
    profile = Profile.objects.get(user_id = request.user) 
    comment.content = obj['comment_content']
    com_id = Com.objects.get(id = obj['com_id']) #'{{community.id}}'
    comment.com_id = com_id
    comment.parent = obj['parent']
    comment.save() # 댓글 = 0 / 대댓글 = 해당 댓글의 id를 갖는다고 했잖아
    essence = {
        'user':profile.name,
        'comment':comment.content,
        'comment_id': comment.id
    }
    return JsonResponse(essence)

def reply(request):
    obj = json.loads(request.body)
    comment = Comment()
    # reply = Comment.objects.get(id=comment_id) #? 뭔가 말로 표현할 수 없지만 이렇게 해야될 것 같은 기분
    comment.user_id = request.user
    profile = Profile.objects.get(user_id = request.user)
    comment.content = obj['reply_content']
    com_id = Com.objects.get(id = obj['com_id'])
    comment.com_id = com_id
    comment.parent = obj['parent']
    comment.save() 
    essences = {
        'user':profile.name,
        'comment':comment.content
    }
    return JsonResponse(essences)

def register_info(request):
    return render(request, 'register_info.html')

def info(request):
    return render(request, 'info.html')

def info_detail(request):
    return render(request, 'info_detail.html')



# kay
def community(request):
    return render(request, 'community copy.html')