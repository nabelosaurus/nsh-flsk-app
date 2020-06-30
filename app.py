from flask import Flask
from flask import request
from datetime import datetime
import os
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
@app.route('/')
def hello_world():
    visitors_address = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    
    now = datetime.now()
    dt_string = now.strftime("%d.%m.%Y %H:%M:%S")
    
    return 'Current date and time is: '+ dt_string +'\nYour IP address is: ' + visitors_address
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=port)
