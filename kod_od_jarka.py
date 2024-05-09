import argparse
import subprocess
import sys
import time
import threading

class Color:
    def __init__(self):
        pass

    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'

animate = False
def progress_animation():
    global animate
    chars = ['\\', '|', '/', '-']
    while animate:
        for char in chars:
            if animate:
                sys.stdout.write('\r' + char)
            sys.stdout.flush()
            time.sleep(0.1)

def progress_loading():
    global animate
    animate = True
    progress_animation()

def progress_clear():
    global animate
    animate = False

def assemble_app(environment, version, verboseMode, gradlew_args = ""):
    gradle_command = "gradlew assembleApi{}{}".format(environment.capitalize(), version.capitalize())
    if gradlew_args:
        gradle_command += gradlew_args
    print(f"Execute gradle command {Color.YELLOW + gradle_command + Color.END}")

    try:
        loading_thread = threading.Thread(target=progress_loading)
        loading_thread.start()

        result = subprocess.run(gradle_command.split(), capture_output=True, shell=True, text=True, check=True)

        sys.stdout.write('')
        sys.stdout.flush()
        progress_clear()
        print(Color.GREEN + "\rSUCCESS" + Color.END)
        print(Color.GREEN + "Check app/build/outputs/apk" + Color.END)
        if verboseMode:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        sys.stdout.write('')
        sys.stdout.flush()
        progress_clear()
        print(Color.RED + "\rFAILURE" + Color.END)
        print(e.stderr)

if __name__ == "__main__":
    environment_options = {"1": "test", "2": "prod"}
    version_options = {"1": "debug", "2": "release"}

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="display gradle wrapper output")
    args = parser.parse_args()

    print(Color.CYAN + "*** IPTAB BUILD SCRIPT ***\n" + Color.END)

    # Environment
    print(Color.BLUE + "Choose environment" + Color.END)
    for key, value in environment_options.items():
        print(f"{key}: {value}")
    while True:
        environment_choice = input("Option: ").strip()
        if environment_choice in environment_options:
            environment = environment_options[environment_choice]
            break
        else:
            print("Wrong option, choose again.")

    # Version
    print(Color.BLUE + "Choose version" + Color.END)
    for key, value in version_options.items():
        print(f"{key}: {value}")
    while True:
        version_choice = input("Option: ").strip()
        if version_choice in version_options:
            version = version_options[version_choice]
            break
        else:
            print("Wrong option, choose again.")

    # Additional config
    additional_config = False
    print(Color.BLUE + "Additional config" + Color.END)
    while True:
        additional_options = input("(Y/N): ").strip().lower()
        if additional_options == "y":
            additional_config = True
            break
        elif additional_options == "n":
            additional_config = False
            break
        else:
            print("Wrong option, choose again.")

    if not additional_config:
        assemble_app(environment, version, args.verbose)
    else:
        gradlew_args = ""

        # Testing Functions
        print(Color.BLUE + "Testing Functions" + Color.END)
        while True:
            testing_functions = input("(Y/N): ").strip().lower()
            if testing_functions == "y":
                gradlew_args += " -PtestingFunctions=true"
                break
            elif testing_functions == "n":
                gradlew_args += " -PtestingFunctions=false"
                break
            else:
                print("Wrong option, choose again.")

        # Debug menu
        print(Color.BLUE + "Debug menu" + Color.END)
        while True:
            debug_menu = input("(Y/N): ").strip().lower()
            if debug_menu == "y":
                gradlew_args += " -PdebugMenu=true"
                break
            elif debug_menu == "n":
                gradlew_args += " -PdebugMenu=false"
                break
            else:
                print("Wrong option, choose again.")

        # Dummy mode
        print(Color.BLUE + "Dummy mode" + Color.END)
        while True:
            dummy_mode = input("(Y/N): ").strip().lower()
            if dummy_mode == "y":
                gradlew_args += " -PdummyMode=true"
                break
            elif dummy_mode == "n":
                gradlew_args += " -PdummyMode=false"
                break
            else:
                print("Wrong option, choose again.")

        # Posnet features
        print(Color.BLUE + "Posnet features" + Color.END)
        while True:
            posnet_features = input("(Y/N): ").strip().lower()
            if posnet_features == "y":
                gradlew_args += " -PposnetFeatures=true"
                break
            elif posnet_features == "n":
                gradlew_args += " -PposnetFeatures=false"
                break
            else:
                print("Wrong option, choose again.")

        assemble_app(environment, version, args.verbose, gradlew_args)