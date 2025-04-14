from flask import Flask, render_template

# Create an instance of the Flask class
# Template folder tells flask where to look for templates
app = Flask(__name__, template_folder="app/templates")

if __name__ == "__main__":
    # Use @app to render pages it is a decorator so a function must go below
    @app.route("/")
    def home():
        # This goes to homepage using the render_template function
        return render_template("Homepage.html")

    app.run()
