import os

def deploy():
    print("Deploying application...")

    os.makedirs("deploy", exist_ok=True)

    with open("deploy/status.txt", "w") as f:
        f.write("Deployment successful")

if __name__ == "__main__":
    deploy()
