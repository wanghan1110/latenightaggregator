#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask_script import Manager
from application import app
manager = Manager(app)

if __name__ == "__main__":
    manager.run()

# PORT = 5000

# ------- PRODUCTION CONFIG -------
# http_server = HTTPServer(WSGIContainer(app))
# http_server.bind(PORT)
# http_server.start(0)
# ioloop = tornado.ioloop.IOLoop().instance()
# autoreload.start(ioloop)
# ioloop.start()


# ------- DEVELOPMENT CONFIG -------
# app.run(port=PORT, debug=True)
