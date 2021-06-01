from flask import Flask, request, Response
import sys
import os
import socket
import logging
import xmltodict

# creating a Flask app 
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>App is up, hit POST with XML for CVV validation</h1>"

@app.route("/" , methods = ['POST'])
def validate_cvv_post():
    xml_request=xmltodict.parse(request.data)
    #app.logger.info(xml_request)
    cvv_val = xml_request["params"]["param"]["@value"]
    app.logger.info(cvv_val)

    xml = response(int(cvv_val))
    return Response(xml, mimetype='text/xml')

@app.route("/<int:cvv>" , methods = ['GET'])
def validate_cvv(cvv):
    xml = response(cvv)
    return Response(xml, mimetype='text/xml')


def eval_cc_number(cc_number):
    if cc_number == 444 :
        return False , "I just dont like tripple fours"
    elif cc_number % 2 != 0 :
        return True , "That number was good"
    else:
        return False , "That number was bad"

def response(cc_number):
    isValid,msg = eval_cc_number(cc_number)
    value =  'accepted' if isValid else 'declined'
    result = str("<?xml version=\"1.0\" encoding=\"UTF-8\"?><outcome value=\""+value+"\" details=\""+msg+"\"/>")
    app.logger.info(result)
    return result

PORT = int(os.getenv('PORT', 8000))

host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name)
        
# driver function 
if __name__ == '__main__': 
    app.run(debug = True , host=host_ip, port=PORT )
