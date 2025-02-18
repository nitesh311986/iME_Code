import os
import subprocess
import sys


def run_command(command):
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, check=True)
    return result


def install_dependencies():
    print("Installing dependencies...")
    run_command(f"pip install --upgrade pip")
    run_command(f"pip install -r requirements.txt")


def pre_build_steps():
    print("Running pre-build steps...")
    # run_command("webdriver-manager update")


def build_steps():
    print("Running tests...")
    env_stage = os.getenv("ENV_STAGE")  # Capture the environment variable

    if env_stage:
        print(f"Running tests in environment: {env_stage}")
        # Pass the environment variable to pytest
        run_command(f"pytest --alluredir=../allure-results --junitxml=reports/result.xml --env={env_stage}")
    else:
        run_command("pytest --alluredir=../allure-results --junitxml=reports/result.xml")


def post_build_steps():
    print("Generating Allure report...")
    run_command("allure generate --clean -o allure-report allure-results")


def main():
    print("Starting build script...")

    args = sys.argv[1:]

    if "install" in args:
        install_dependencies()

    if "pre_build" in args:
        pre_build_steps()

    if "build" in args:
        build_steps()

    if "post_build" in args:
        post_build_steps()

    if not args:
        install_dependencies()
        pre_build_steps()
        build_steps()
        post_build_steps()

    print("Build script completed.")

if __name__ == "__main__":
    main()

# import os
# import subprocess
# import sys
#
#
# def run_command(command):
#     print(f"Running command: {command}")
#     result = subprocess.run(command, shell=True, check=True)
#     return result
#
#
# def install_dependencies():
#     print("Installing dependencies...")
#     run_command(f"pip install --upgrade pip")
#     run_command(f"pip install -r requirements.txt")
#     run_command(f"pip install coverage")  # Install coverage.py
#
#
# def pre_build_steps():
#     print("Running pre-build steps...")
#     # run_command("webdriver-manager update")
#
#
# def build_steps():
#     env_stage = os.getenv("ENV_STAGE")  # Capture the environment variable
#     if env_stage:
#         print(f"Running tests in environment: {env_stage}")
#         # Run tests with coverage and store the result in separate folders
#         run_command(
#             f"coverage run -m pytest --alluredir=../allure-results --junitxml=reports/result.xml --env={env_stage}")
#     else:
#         run_command("coverage run -m pytest --alluredir=../allure-results --junitxml=reports/result.xml")
#
#         # Save coverage report as .coverage file (binary format used for merging later)
#     run_command(f"coverage save .coverage")
#
#
# def post_build_steps():
#     print("Generating Allure report...")
#     run_command("allure generate --clean -o allure-report allure-results")
#     # Generate coverage report in HTML format
#     run_command(f"coverage html -d ../htmlcov")
#
#
# def main():
#     print("Starting build script...")
#     args = sys.argv[1:]
#
#     if "install" in args:
#         install_dependencies()
#
#     if "pre_build" in args:
#         pre_build_steps()
#
#     if "build" in args:
#         build_steps()
#
#     if "post_build" in args:
#         post_build_steps()
#
#     if not args:
#         install_dependencies()
#         pre_build_steps()
#         build_steps()
#         post_build_steps()
#
#     print("Build script completed.")
#
# if __name__ == "__main__":
#     main()