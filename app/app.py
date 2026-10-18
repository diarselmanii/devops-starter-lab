from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
	<head>
	   <title>IT Infrastructure Dashboard</title>
	</head>
	<body>
	    <h1>Welcome to my first DevOps project!</h1>
	    <p>Application status: Online</p>
	    <a href="/health">Check application health</a>
	</body>
    </html>
    """

@app.route("/health")
def health():
	return jsonify(status="ok")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=False)

