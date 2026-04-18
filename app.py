from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# صفحة الـ HTML اللي رح تظهر للمستخدم
HTML_PAGE = """
<!doctype html>
<html>
  <head><title>Addition App</title></head>
  <body style="font-family: Arial; margin: 40px;">
    <h1>Simple Addition Web App</h1>
    <form method="post">
      <label>First number:</label>
      <input type="number" name="a" required><br><br>
      <label>Second number:</label>
      <input type="number" name="b" required><br><br>
      <input type="submit" value="Add">
    </form>
    {% if result is not none %}
      <hr>
      <h2>Result: {{ result }}</h2>
    {% endif %}
    <p style="margin-top: 20px; color: gray;">Status: OK - Hello from gp1-demo!</p>
  </body>
</html>
"""

def add_numbers(a, b):
    return a + b

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            a = float(request.form["a"])
            b = float(request.form["b"])
            result = add_numbers(a, b)
        except Exception as e:
            result = "Error in calculation"
    
    return render_template_string(HTML_PAGE, result=result)

@app.route("/status")
def status():
    return jsonify({"status": "ok", "message": "Hello from gp1-demo!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)