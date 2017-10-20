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
    # logging.basicConfig(level=logging.DEBUG, format="﻿%(name)s ﻿%(asctime)s ﻿%（message)s", \
    #                     filename="walry.log")
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("request:{}".format(request.COOKIES))
    response = HttpResponse(content_type='application/json')
    name = response.set_cookie("age","23")
    # response.content = json.dumps({"say":"hello"})
    response["Access-Control-Allow-Origin"] = "*"
    # return HttpResponse("nihao")
    return response

@csrf_exempt
def test1(request):
    logging.debug("request_test1:{}".format(request.COOKIES))
    response = HttpResponse(content_type='application/json')
    # name = response.set_cookie("name","mhl")
    # response.content = json.dumps(status)
    response["Access-Control-Allow-Origin"] = "*"
    return response