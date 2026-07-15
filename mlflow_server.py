import subprocess
from pyngrok import ngrok
from dotenv import load_dotenv
import os
import sys
import time


def main():
    print(sys.path)
    bin_dir = os.path.dirname(sys.executable) #provides the path of the python executable
    env = os.environ.copy()
    #mlflow will be searched from env PATH variable (sys.path unless passed otherwise). We append the path of the new env we create via 'python -m venv'
    env["PATH"] = bin_dir + os.pathsep + env.get("PATH", "") 
  
    load_dotenv()
    grok_auth = os.getenv("NGROK_AUTH")
    print(f"Using auth: {grok_auth}")

    try:

        mlflow_process = subprocess.Popen(
          ["mlflow", "server", "--host", "127.0.0.1", "--port", "8000", "--allowed-hosts", "*"],
          env=env,
          stdout=subprocess.DEVNULL,  # Routes logs away from the main thread
          stderr=subprocess.DEVNULL
          )

        # Wait 3 seconds to let MLflow bind to port 5000
        time.sleep(3)

        ngrok.kill()
        ngrok.set_auth_token(grok_auth)
        tunnel = ngrok.connect(addr="127.0.0.1:8000", proto="http")
        print(f"Public URL: {tunnel.public_url}")

        while True: #keep main thread running as ngrok agent should be kept alive
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopping tunnel and MLflow...")
        ngrok.disconnect(public_url.public_url)
        mlflow_process.terminate()

if __name__ == "__main__":
    main()
