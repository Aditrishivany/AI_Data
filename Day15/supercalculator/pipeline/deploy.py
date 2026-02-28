import shutil
import os
import logging

def deploy():
    logging.info("Deploying application")

    os.makedirs("deployment", exist_ok=True)
    shutil.copy("dist/app.zip", "deployment/app.zip")

    logging.info("Deployment successful")

if __name__ == "__main__":
    deploy()
