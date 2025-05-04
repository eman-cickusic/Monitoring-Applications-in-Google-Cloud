from flask import Flask
import googlecloudprofiler

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello, World!"

# Start the profiler
try:
    googlecloudprofiler.start(verbose=3)
except (ValueError, NotImplementedError) as exc:
    print(exc)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
