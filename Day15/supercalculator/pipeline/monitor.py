import os

def monitor():
    if os.path.exists("deployment/app.zip"):
        print("Application deployed successfully.")
    else:
        print("Deployment not found.")

if __name__ == "__main__":
    monitor()
