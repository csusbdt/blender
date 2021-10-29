import bpy
import subprocess

scene = bpy.context.scene

def render():
    scene.render.filepath = '//temp/'
    bpy.ops.render.render(animation=True)
    gitbash = "C:\Program Files\Git\git-bash.exe"
    cmd = """
        ffmpeg  -f image2           \
                -framerate 30       \
                -i 'temp/%04d.png'  \
                -s 720x480          \
                -y                  \
                -pix_fmt yuv420p    \
                anim.mp4
    """
    subprocess.run([gitbash, "-c", cmd])

