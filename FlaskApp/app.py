import os
from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Flask vefsíðan mín</h1>
    <p>Veldur hlekk til þess að fara á aðra síðu</p>
    <p><a href="/sida2" title="Síða 2">Síða 2 </a> | <a href="/sida3" title="Síða 3">Síða 3 </a></p>
    <p>Hérna er mynd</p>
    <img src="https://picsum.photos/400" />
    """ .format(time=the_time)

@app.route('/sida2')
def page2():
    return """
    <h1>Síða 2</h1>
    <p><a href="/" title="Forsíða">Forsíða </a> | <a href="/sida3" title="Síða 3">Síða 3 </a></p>
    <p>Önnur mynd</p>
    <img src="https://picsum.photos/400" />
    """ 
@app.route('/sida3')
def page3():
    return """
    <h1>Síða 3</h1>
    <p><a href="/" title="Forsíða">Forsíða </a> | <a href="/sida2" title="Síða 2">Síða 2 </a></p>
    <p>Enn önnur mynd</p>
    <img src="https://picsum.photos/400" />
    """ 

if __name__ == '__main__':
    app.run()
    #app.run(debug=True, use_reloader=True)