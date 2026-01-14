from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the landing page
@app.route('/')
def home():
    # This renders the HTML file located in the 'templates' folder
    return render_template('welcome.html')

if __name__ == '__main__':
    # Run the app in debug mode (auto-reloads when you make changes)
    app.run(debug=True, port=5000)