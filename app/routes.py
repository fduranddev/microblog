from app import app


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Frédéric"}
    return (
        """
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Bonjour, """
        + user["username"]
        + """!</h1>
    </body>
</html>"""
    )
