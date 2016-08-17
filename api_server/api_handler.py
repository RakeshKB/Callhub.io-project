__author__ = 'rakesh.kb'

import json
import time
import tornado.web
from api_server import settings
def return_success_response(request_handler, reason):
    request_handler.set_header('content-type', 'application/json')
    request_handler.set_header('Access-Control-Allow-Origin', '*')
    msg = {'status': 'ok', 'data': reason}
    data = json.dumps(msg)
    request_handler.write(data)


def return_error_response(request_handler, reason):
    request_handler.set_header('content-type', 'application/json')
    request_handler.set_header('Access-Control-Allow-Origin', '*')
    msg = {'status': 'error', 'reason': reason}
    data = json.dumps(msg)
    request_handler.write(data)

class FibonacciHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.RESULT = {}
    
    def get(self):
        self.value = int(self.get_argument('number'))
        # series begins with 1 1 2 3 5 . . .
        num1 = 1
        num2 = 1
        minutes = self.value // 60
        if self.value == 1 or self.value == 2:
            start = time.time()
            exec_time = time.time()-start
            self.RESULT['value'] = str(num1)
            self.RESULT['time'] = exec_time
            self.RESULT['fibo'] = self.value
            return return_success_response(self, reason=self.RESULT)
        
        for i in range(2, self.value):
            start = time.time()
            fibo = num1 + num2
            num1 = num2
            num2 = fibo
            exec_time = time.time()-start
        # print exec_time
        self.RESULT['value'] = str(fibo)
        self.RESULT['time'] = exec_time
        self.RESULT['fibo'] = self.value
        return return_success_response(self, reason=self.RESULT)
        


        
        
