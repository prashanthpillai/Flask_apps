from flask import Flask, request, render_template

app = Flask(__name__)

# ROUTING

# @app.route('/')
# def index():
#     return "This is Prashanth's homepage"
#
# @app.route('/tuna')
# def tuna():
#     return "<h1> Tuna is good <h1>"
#
# @app.route('/profile/<username>')
# def profile(username):
#     return 'Hello %s !' % username
#
# @app.route('/post/<int:post_id>')
# def post(post_id):
#     return '<h2> Post ID is %s <h2>' % post_id
#------------------------------------------------------------

# HTTP METHODS
#
# @app.route('/')
# def index():
#     return "Method used : %s" % request.method
#
# @app.route('/bacon', methods=['GET', 'POST'])
# def bacon():
#     if request.method == 'POST':
#         return "You are using POST"
#     else:
#         return "You are probably using GET"
#------------------------------------------------------------

# HTML TEMPLATES

# @app.route('/')
# def index():
#     return 'Home Page'
#\\\
# @app.route("/profile/<name>")
# def profile(name):
#     return render_template("profile.html", name=name)
#

#------------------------------------------------------------

# Mapping multiple URLs

# @app.route('/')
# @app.route('/<user>')
# def index(user=None):
#     return render_template('user.html', user=user)

#------------------------------------------------------------

# Passing objects

@app.route('/shopping')
def index(user=None):
    food = ['beef', 'cheese', 'fish', 'orange']
    return render_template('shopping.html', food = food)

if __name__ == "__main__":
    app.run(debug=True)