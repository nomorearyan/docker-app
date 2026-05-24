from flask import Flask, render_template
import platform
import os
import psutil
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    info = {
        "hostname":   platform.node(),
        "os":         platform.system() + " " + platform.release(),
        "python":     platform.python_version(),
        "cpu":        f"{psutil.cpu_percent(interval=1)}%",
        "memory":     f"{psutil.virtual_memory().percent}%",
        "time":       datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "container":  os.environ.get("CONTAINER_NAME", "docker-app"),
        "port":       os.environ.get("PORT", "5000"),
    }
    return render_template("index.html", info=info)

@app.route("/health")
def health():
    return {"status": "healthy", "time": datetime.now().isoformat()}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
