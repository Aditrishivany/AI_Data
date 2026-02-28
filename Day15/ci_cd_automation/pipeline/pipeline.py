import subprocess
import os
import shutil
import logging

# logging setup
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

PROJECT_ROOT = os.getcwd()

def install_dependencies():
    logging.info("Installing dependencies")
    subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)

def run_pytest():
    logging.info("Running pytest")
    subprocess.run(["pytest", "tests"], check=True)

def run_unittest():
    logging.info("Running unittest")
    subprocess.run(["python", "-m", "unittest", "discover", "tests"], check=True)

def build_project():
    logging.info("Building project")

    build_dir = os.path.join(PROJECT_ROOT, "build")
    dist_dir = os.path.join(PROJECT_ROOT, "dist")

    os.makedirs(build_dir, exist_ok=True)
    os.makedirs(dist_dir, exist_ok=True)

    shutil.copy("app/calculator.py", build_dir)
    shutil.make_archive("dist/app", "zip", build_dir)

def deploy_project():
    logging.info("Deploying project")
    shutil.copy("dist/app.zip", "deploy.zip")

def main():
    logging.info("Pipeline started")

    install_dependencies()
    run_pytest()
    run_unittest()
    build_project()
    deploy_project()

    logging.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()
