import subprocess
import shutil
import os
import logging
from datetime import datetime

# Setup logging
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_command(command):
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        logging.error(f"Command failed: {command}")
        exit(1)

def install_dependencies():
    logging.info("Installing dependencies")
    run_command("pip install -r requirements.txt")

def run_tests():
    logging.info("Running pytest")
    run_command("pytest")

def build_artifact():
    logging.info("Building artifact")
    
    os.makedirs("build", exist_ok=True)
    os.makedirs("dist", exist_ok=True)
    
    shutil.copytree("app", "build/app", dirs_exist_ok=True)
    shutil.make_archive("dist/app", "zip", "build")

def main():
    logging.info("Pipeline started")

    install_dependencies()
    run_tests()
    build_artifact()

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()
