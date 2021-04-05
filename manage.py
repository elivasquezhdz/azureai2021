from flask import Flask, render_template,request,redirect,send_from_directory,url_for
from forms import TextForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '0251527bx0b22zy0c602dgde210wa328'

@app.route('/about')
def index():
    return render_template('about.html')



@app.route('/videos')
def video():
    videos = []
    return render_template('videos.html',posts=videos)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/summarize', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def summarize():
    form = TextForm()
    text = form.text.data
    if form.validate_on_submit():
        text = form.text.data
        #flash(f'Account created for {form.username.data}!', 'success')
        return render_template('results.html', name="asa")
    return render_template('summarize.html', form=form)


@app.route('/nosummarize', methods=['GET', 'POST'])
def nosummarize():
    form = TextForm()
    text = form.text.data
    if form.validate_on_submit():
        text = form.text.data
        #flash(f'Account created for {form.username.data}!', 'success')
        return render_template('results.html', name="asa")
    return render_template('nosummarize.html', form=form)


if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)