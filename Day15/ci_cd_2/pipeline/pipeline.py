import subprocess
import os
import shutil
import logging
import sys

# Ensure project root is in PYTHONPATH
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

logging.basicConfig(
    filename=os.path.join(PROJECT_ROOT, "logs/pipeline.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def install_dependencies():
    logging.info("Installing dependencies")
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
        check=True,
        cwd=PROJECT_ROOT
    )

def run_pytest():
    logging.info("Running pytest")
    subprocess.run(
        [sys.executable, "-m", "pytest", "tests"],
        check=True,
        cwd=PROJECT_ROOT
    )

def run_unittest():
    logging.info("Running unittest")
    subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "tests"],
        check=True,
        cwd=PROJECT_ROOT
    )

def build_project():
    logging.info("Building project")

    build_dir = os.path.join(PROJECT_ROOT, "build")
    dist_dir = os.path.join(PROJECT_ROOT, "dist")

    os.makedirs(build_dir, exist_ok=True)
    os.makedirs(dist_dir, exist_ok=True)

    shutil.copy(
        os.path.join(PROJECT_ROOT, "app/calculator.py"),
        build_dir
    )

    shutil.make_archive(
        os.path.join(dist_dir, "app"),
        "zip",
        build_dir
    )

def deploy_project():
    logging.info("Deploying project")

    shutil.copy(
        os.path.join(PROJECT_ROOT, "dist/app.zip"),
        os.path.join(PROJECT_ROOT, "deploy.zip")
    )

def main():
    logging.info("Pipeline started")

    install_dependencies()
    run_pytest()
    run_unittest()
    build_project()
    deploy_project()

    logging.info("Pipeline completed successfully")
    print("✅ Pipeline completed successfully")

if __name__ == "__main__":
    main()
