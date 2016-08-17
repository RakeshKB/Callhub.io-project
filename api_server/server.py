#!/usr/bin/python
import sys
import json
import logging
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import api_server.api_handler
from api_server import settings
from tornado.log import enable_pretty_logging

def run():
    # Bootstrap singletons
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, settings.LOG_LEVEL))
    enable_pretty_logging(logger=logger)

    application = tornado.web.Application(
        [
            (r"/api/fibonacci/", api_server.api_handler.FibonacciHandler)
        ], **settings.APP_SETTINGS)
    logger.info('Starting server at port:%s' % settings.APPLICATION_PORT)

    application.listen(settings.APPLICATION_PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()