with open('requirements.txt', 'r') as f:
    packages = f.readlines()

for package in packages:
    package_name = package.split('==')[0].strip()
    if package_name:
        import subprocess
        subprocess.call(['pip', 'uninstall', '-y', package_name])
