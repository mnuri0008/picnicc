from flask import Flask, render_template, send_from_directory
app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/room/<code>')
def room(code):
    return render_template('room.html', code=code)

@app.route('/manifest.json')
def manifest_file():
    return send_from_directory('static', 'manifest.json', mimetype='application/manifest+json')

@app.route('/service-worker.js')
def sw_file():
    return send_from_directory('static', 'service-worker.js', mimetype='text/javascript')

@app.route('/static/icons/icon-192.png')
def icon192_alias():
    return send_from_directory('static/icons', 'icon-192.png', mimetype='image/png')

@app.route('/static/icons/icon-512.png')
def icon512_alias():
    return send_from_directory('static/icons', 'icon-512.png', mimetype='image/png')

@app.route('/.well-known/assetlinks.json')
def assetlinks():
    return send_from_directory('static/.well-known', 'assetlinks.json', mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
