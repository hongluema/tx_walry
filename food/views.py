# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import logging, json

# Create your views here.
logger = logging.getLogger("mahl")

@csrf_exempt
def test(request):
    logging.basicConfig(level=logging.DEBUG, format="﻿%(name)s ﻿%(asctime)s ﻿%（message)s", \
                        filename="/home/mhl/projects/django/walry/walry.log")
    # logging.basicConfig(level=logging.DEBUG)
    # logger.debug("request:{}".format(request.COOKIES)
    logger.debug("request:bedug")
    # response = HttpResponse(content_type='application/json')
    # name = response.set_cookie("sex","1")
    # response.content = json.dumps({"say":"hello"})
    # response["Access-Control-Allow-Origin"] = "*"
    request.session["sex"] = 1
    return HttpResponse("nihao")
    # return response

@csrf_exempt
def test1(request):
    logging.debug("request_test1:{}".format(request.COOKIES))
    response = HttpResponse(content_type='application/json')
    # name = response.set_cookie("name","mhl")
    # response.content = json.dumps(status)
    response["Access-Control-Allow-Origin"] = "*"
    return response