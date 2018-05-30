# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from art.models import Tag, Art

__author__ = "wuyou"
__date__ = "2018/5/29 15:00"
from django.shortcuts import render, HttpResponse


def index_handler(request):
    # url = request.path
    tags = Tag.objects.all()
    # 文章列表
    t = int(request.GET.get('t', 0))
    # page = self.get_argument("page", 1)
    page = int(request.GET.get("page", 1))
    if t == 0:
        # sql = "select count(*) from art"
        total = len(Art.objects.all())
    else:
        total = len(Art.objects.filter(a_tag_id=t))
    context = dict(
        pagenum=0,
        total=0,
        prev=1,
        next=1,
        pagerange=range(1, 2),
        data=[],
        url=request.path,
        tags=tags,
        page=page,
        t=t
    )
    if total > 0:
        shownum = 8
        import math
        pagenum = int(math.ceil(total / shownum))
        if page < 1:
            # self.redirect(request.path + "?page=%d&t=%d" % (1, t))
            url = request.path + "?page=%d&t=%d" % (1, t)
            return HttpResponseRedirect(url)
        if page > pagenum:
            # self.redirect(self.request.path + "?page=%d&t=%d" % (pagenum, t))
            url = request.path + "?page=%d&t=%d" % (pagenum, t)
            return HttpResponseRedirect(url)
        offset = (page - 1) * int(shownum)

        if t == 0:
            # sql = "select id,title,info,img from art limit :offset,:limit"
            # data = self.db.execute(sql, dict(offset=offset, limit=int(shownum))).fetchall()
            data = Art.objects.all()[offset:shownum + offset]
        else:
            data = Art.objects.filter(a_tag_id=t)[offset:shownum + offset]
        btnnum = 5
        if btnnum > pagenum:
            firstpage = 1
            lastpage = pagenum
        else:
            if page == 1:
                firstpage = 1
                lastpage = btnnum
            else:
                firstpage = page - 2
                lastpage = page + btnnum - 3
                if firstpage < 1:
                    firstpage = 1
                if lastpage > pagenum:
                    lastpage = pagenum
        prev = page - 1
        next = page + 1
        if prev < 1:
            prev = 1
        if next > pagenum:
            next = pagenum
        context = dict(
            pagenum=pagenum,
            total=total,
            prev=prev,
            next=next,
            pagerange=range(firstpage, lastpage + 1),
            data=data,
            url=request.path,
            tags=tags,
            page=page,
            t=t
        )
    return render(request, "home/index.html", context=context)
