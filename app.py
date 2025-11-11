from flask import Flask, jsonify
import os
import platform
import psutil

app = Flask(__name__)

integrantes = ["Sophia Ploposki"]

@app.route("/")
def home():
    process = psutil.Process(os.getpid())  # processo atual
    mem_info = process.memory_info().rss / (1024 * 1024)  # memória em MB
    cpu_percent = psutil.cpu_percent(interval=0.5)  #CPU em %

    info = f"""
    <h2>Informações do Sistema</h2>
    <p><b>Integrantes:</b> {', '.join(integrantes)}</p>
    <p><b>PID:</b> {process.pid}</p>
    <p><b>Memória utilizada:</b> {mem_info:.2f} MB</p>
    <p><b>Uso de CPU:</b> {cpu_percent:.2f}%</p>
    <p><b>Sistema Operacional:</b> {platform.system()} ({platform.release()})</p>
    """
    return info

@app.route("/info")
def info():
    return f"<p>Integrantes da equipe: {', '.join(integrantes)}</p>"

@app.route("/metrics")
def metrics():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info().rss / (1024 * 1024)
    cpu_percent = psutil.cpu_percent(interval=0.5)
    sistema = f"{platform.system()} ({platform.release()})"

    return jsonify({
        "integrantes": integrantes,
        "PID": process.pid,
        "memoria_MB": round(mem_info, 2),
        "cpu_percent": round(cpu_percent, 2),
        "sistema_operacional": sistema
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
