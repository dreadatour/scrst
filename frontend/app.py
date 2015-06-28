# coding: utf-8
import httplib
import urllib

from flask import Flask, abort, render_template


app = Flask(__name__)
app.config.from_object('config')


@app.errorhandler(404)
def error_not_found(e):
    """
    View '404 Page not found' error.
    """
    return render_template('error.html', code=404), 404


@app.errorhandler(500)
def error_server(e):
    """
    View '500 Server error' error.
    """
    return render_template('error.html', code=500), 500


@app.route('/<filename>', methods=['GET'])
def screenshot(filename):
    """
    Get screenshot.
    """
    if not filename.endswith('.png'):
        filename += '.png'

    img_domain = app.config['AWS_S3_DOMAIN']
    img_path = '{0}{1}'.format(app.config['AWS_S3_PATH'], filename)
    img_url = 'http://{0}{1}'.format(img_domain, img_path)

    connect = httplib.HTTPConnection(img_domain)
    connect.request('HEAD', img_path)

    response = connect.getresponse()
    if response.status != 200:
        abort(404)

    headers = dict(response.getheaders())
    img_width = headers.get('x-amz-meta-width')
    img_height = headers.get('x-amz-meta-height')
    img_title = headers.get('x-amz-meta-title', filename)
    img_title = urllib.unquote(img_title).decode('utf-8')

    return render_template(
        'screenshot.html',
        filename=filename,
        url=img_url,
        width=img_width,
        height=img_height,
        title=img_title
    )


@app.route('/', methods=['GET'])
def index():
    """
    Get index page.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
