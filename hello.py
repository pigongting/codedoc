#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

from doc import insertType

def application(environ, start_response):
  start_response('200 OK', [('Content-Type', 'application/json')])
  if (environ['PATH_INFO'][1:] == 'pi'):
    aa = json.dumps(insertType(environ))
    print("DATA:", aa)
    # body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    # return [body.encode('utf-8')]
    print(aa.encode('utf-8'))
    return [aa.encode('utf-8')]
  else:
    return ['[]'.encode('utf-8')]
