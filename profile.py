#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    profile
    ~~~~~~~

    Implements the profile performance for cobra

    :author:    Feei <feei@feei.cn>
    :author:    Lightless <root@lightless.me>
    :homepage:  https://github.com/wufeifei/cobra
    :license:   MIT, see LICENSE for more details.
    :copyright: Copyright (c) 2017 Feei. All rights reserved
"""
from werkzeug.contrib.profiler import ProfilerMiddleware
from app import web

web.config['PROFILE'] = True
web.wsgi_app = ProfilerMiddleware(web.wsgi_app, restrictions=[30])
web.run(debug=True)
