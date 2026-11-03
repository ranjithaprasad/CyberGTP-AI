@app.route("/")
def home():
    return jsonify({
        "name": "CyberGTP AI",
        "status": "Running",
        "message": "Welcome to your AI assistant!"
    })

       
      
