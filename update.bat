@echo off
git fetch origin
git reset --hard main
git pull
rm config.json
rmdir -r -fo config.json
"libs/pythonlib/python.exe" -m pip install --force-reinstall -r requirements.txt
