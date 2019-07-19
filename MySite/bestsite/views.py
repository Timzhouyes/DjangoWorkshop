from django.shortcuts import render,redirect
from .models import Restraut
from .models import Category
from .models import Comment
from .models import Reply
from django.urls import reverse
from django.http import HttpResponse

# Create your views here.
def index(request):
    res_list = Restraut.objects.all()
    cate = Category.objects.all()
    limit = 2
    count = 0
    parent_list = []
    child_list = []
    for r in res_list:
        child_list.append(r)
        count += 1
        if count % 2 == 0:
            parent_list.append(child_list)
            child_list = []
    ctxt = {
        "parent_list": parent_list,
        "cate": cate,
    }
    return render(request, template_name='bestsite/index.html', context=ctxt)


def single(request, pk):
    print(pk)
    re = Restraut.objects.get(rid=pk)
    comments = Comment.objects.all()
    replies = Reply.objects.all()
    comment_list = []
    for c in comments:
        if c.res_id == re.rid:
            comment_list.append(c)
            child_list = []
            for r in replies:
                if c.cid == r.comment_id:
                    child_list.append(r)
            comment_list.append(child_list)

    ctxt = {
        "restr": re,
        "comments": comment_list,
    }
    return render(request, template_name='bestsite/single.html', context=ctxt)


def submit_reply(request, pk):
    post = request.POST
    reply = Reply()
    reply.user_id = 1
    reply.reply_to_id = post.get("reply_to_id")
    reply.reply_type = post.get("reply_type")
    reply.content = post.get("content")
    reply.comment_id = pk
    reply.reply_to_uid = post.get("reply_to_uid")

    reply.save()

    return redirect(reverse('bestsite:single', kwargs={'pk': pk}))


def submit_like(request, pk):
    post = request.post
    c = Comment.objects.get(id=pk)
    c.add_like()
    c.save()
    return redirect(reverse('bestsite:single', kwargs={'pk': pk}))


def submit_comment(request, pk):
    # pk:rid
    post = request.POST
    comment = Comment()
    comment.user_id = 1
    comment.price = post.get("price")
    comment.man_num = post.get("man_num")
    comment.service_fee = post.get("service_fee")
    comment.is_anoym = 0
    comment.rate = post.get("rate")
    comment.content = post.get("content")
    comment.like_num = 0
    comment.dislike_num = 0
    comment.res_id = pk
    comment.save()

    res = Restraut.objects.get(rid=comment.res_id)
    res.comment_add()
    res.new_average(comment.rate)
    res.save()
    return redirect(reverse('bestsite:single', kwargs={'pk': pk}))
