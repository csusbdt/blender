export PYTHONPATH=.

/C/Program\ Files/Blender\ Foundation/Blender\ 2.93/blender.exe \
-b --python-exit-code 1 -P anim1.py

if [ $? -eq "0" ]; then
    start anim.mp4
fi

rm -rf __pycache__
rm -rf temp

