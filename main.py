# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# +
# https://github.com/Davepar/docker-webapp2/blob/master/Dockerfile

import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Esta es una prueba de actualizacion 1.6 - Hola a todos esta es la version uno.seis!')

class AdminPage(webapp2.RequestHandler):
    def get(self):
	self.response.headers['Content-Type'] = 'application/json'   
	obj = {
	  'success': 'true',
	  'mensaje': 'Ahora estas en modo administrador - preparate'
	}
	self.response.write(json.dumps(obj))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/admin', AdminPage)
], debug=True)

def main():
    import os
    from werkzeug.serving import run_simple
    from werkzeug.wsgi import SharedDataMiddleware
    # Add handler for static filesss
    app_with_static = SharedDataMiddleware(app, {
        '/static': os.path.join(os.path.dirname(__file__), 'static')
    })
    # Bind to all addresses (i.e. 0.0.0.0), otherwise the world outside this
    # Docker container won't be able to see the server
    run_simple('0.0.0.0', 8080, app_with_static, use_reloader=True)

if __name__ == '__main__':
    main()
