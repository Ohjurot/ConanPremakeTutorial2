import subprocess

def RunConan(build_type):
    subprocess.run((
        'conan', 'install', '.', 
        '--build', 'missing', 
        '--output-folder=./dependencies', 
        f'--settings=build_type={build_type}'
    ))

def RunPremake(action):
    subprocess.run((
        'premake5', action
    ))

if __name__ == "__main__":
    RunConan("Debug")
    RunConan("Release")
    RunPremake("vs2022")
