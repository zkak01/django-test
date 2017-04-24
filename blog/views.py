# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h2>This is the blog</h2>")
