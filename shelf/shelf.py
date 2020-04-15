import bpy
import bmesh
from math import radians

view_layer         = bpy.context.view_layer
view_layer_objects = view_layer.active_layer_collection.collection.objects
scene              = bpy.context.scene
objects            = bpy.data.objects
meshes             = bpy.data.meshes

ov2x4 = objects["Cube"].copy()
ov2x4.name = "v2x4"
ov2x4.data = ov2x4.data.copy()
ov2x4.data.name = "v2x4"
ov2x4.data.vertices[0].co = ( 1.5, 3.5, 1.0 )
ov2x4.data.vertices[1].co = ( 1.5, 3.5, 0.0 )
ov2x4.data.vertices[2].co = ( 1.5, 0.0, 1.0 )
ov2x4.data.vertices[3].co = ( 1.5, 0.0, 0.0 )
ov2x4.data.vertices[4].co = ( 0.0, 3.5, 1.0 )
ov2x4.data.vertices[5].co = ( 0.0, 3.5, 0.0 )
ov2x4.data.vertices[6].co = ( 0.0, 0.0, 1.0 )
ov2x4.data.vertices[7].co = ( 0.0, 0.0, 0.0 )

oh2x4 = objects["Cube"].copy()
oh2x4.data = oh2x4.data.copy()
oh2x4.name = "h2x4"
oh2x4.data.name = "h2x4"
oh2x4.data.vertices[0].co = ( 3.5, 1.0, 1.5 )
oh2x4.data.vertices[1].co = ( 3.5, 0.0, 1.5 )
oh2x4.data.vertices[2].co = ( 3.5, 1.0, 0.0 )
oh2x4.data.vertices[3].co = ( 3.5, 0.0, 0.0 )
oh2x4.data.vertices[4].co = ( 0.0, 1.0, 1.5 )
oh2x4.data.vertices[5].co = ( 0.0, 0.0, 1.5 )
oh2x4.data.vertices[6].co = ( 0.0, 1.0, 0.0 )
oh2x4.data.vertices[7].co = ( 0.0, 0.0, 0.0 )

assert not ov2x4.data is oh2x4.data

if ("Cube" in view_layer_objects):
	view_layer_objects.unlink(objects["Cube"])
	#objects.remove(objects["Cube"])

def v2x4(length = 8 * 12, rotation = (0, 0, 0), location = (0, 0, 0)):
	t = ov2x4.copy()
	t.rotation_euler = (radians(rotation[0]), radians(rotation[1]), radians(rotation[2]))
	t.scale = (1, 1, length)
	t.location = location
	view_layer_objects.link(t)
	return t

def h2x4(length = 8 * 12, rotation = (0, 0, 0), location = (0, 0, 0)):
	t = oh2x4.copy()
	t.rotation_euler = (radians(rotation[0]), radians(rotation[1]), radians(rotation[2]))
	t.scale = (1, length, 1)
	t.location = location
	view_layer_objects.link(t)
	return t

shelfHeight     = 8 * 12 / 5
shelfWidth      = 2 * 12
shelfThickness  = 15 / 32

def makeTallVerticals() :
	l = 8 * 12
	a = (0, 0, 0)
	ySpacing = (12 * 12 - 3.5) / 3
	v2x4(l, a, (               0, 0 * ySpacing, 0))
	v2x4(l, a, (               0, 1 * ySpacing, 0))
	v2x4(l, a, (               0, 2 * ySpacing, 0))
	v2x4(l, a, (               0, 3 * ySpacing, 0))
	v2x4(l, a, (shelfWidth + 1.5, 0 * ySpacing, 0))
	v2x4(l, a, (shelfWidth + 1.5, 1 * ySpacing, 0))
	v2x4(l, a, (shelfWidth + 1.5, 2 * ySpacing, 0))
	v2x4(l, a, (shelfWidth + 1.5, 3 * ySpacing, 0))

def makeLongHorizontals() :
	l = 12 * 12
	a = (0, 90, 0)
	w = shelfWidth
	h2x4(l, a, (1.5, 0, 1 * shelfHeight - shelfThickness))
	h2x4(l, a, (1.5, 0, 2 * shelfHeight - shelfThickness))
	h2x4(l, a, (1.5, 0, 3 * shelfHeight - shelfThickness))
	h2x4(l, a, (1.5, 0, 4 * shelfHeight - shelfThickness))
	h2x4(l, a, (1.5, 0, 5 * shelfHeight - shelfThickness))
	h2x4(l, a, (w  , 0, 1 * shelfHeight - shelfThickness))
	h2x4(l, a, (w  , 0, 2 * shelfHeight - shelfThickness))
	h2x4(l, a, (w  , 0, 3 * shelfHeight - shelfThickness))
	h2x4(l, a, (w  , 0, 4 * shelfHeight - shelfThickness))
	h2x4(l, a, (w  , 0, 5 * shelfHeight - shelfThickness))

def makeShortVerticals() :
	l = shelfHeight - 3.5 - shelfThickness
	a = (0, 0, 0)
	w = shelfWidth
	spacing = (12 * 12 - 3.5) / 3
	for i in range(5) :
		v2x4(l, a, (1.5 , 0 * spacing, i / 5 * 8 * 12))
		v2x4(l, a, (w   , 0 * spacing, i / 5 * 8 * 12))
		v2x4(l, a, (1.5 , 1 * spacing, i / 5 * 8 * 12))
		v2x4(l, a, (w   , 1 * spacing, i / 5 * 8 * 12))
		v2x4(l, a, (1.5 , 2 * spacing, i / 5 * 8 * 12))
		v2x4(l, a, (w   , 2 * spacing, i / 5 * 8 * 12))
		v2x4(l, a, (1.5 , 3 * spacing, i / 5 * 8 * 12))
		v2x4(l, a, (w   , 3 * spacing, i / 5 * 8 * 12))

def makeShortHorizontals() :
	l = shelfWidth - 2 * 1.5
	a = (0, 90, -90)
	spacing = (12 * 12 - 1.5) / 6
	for j in range(7) :
		for i in range(1, 6) :
			h2x4(l, a, (3.0, 1.5 + j * spacing, i * shelfHeight - shelfThickness))

#def makeShelves() :
#	

makeTallVerticals()
makeLongHorizontals()
makeShortVerticals()
makeShortHorizontals()
#makeShelves()

view_layer.update()

# To enter into interactive mode; press Ctl-D to terminate.
# __import__('code').interact(local=dict(globals(), **locals()))

#scene.render.filepath = '//./'

# Make the animation 3 seconds.
#scene = bpy.context.scene
#scene.render.fps = 30
#scene.frame_start = 1
#scene.frame_end   = 1

# Create first key frame.
#cube.keyframe_insert(data_path="location", frame=1)

#bpy.ops.render.render(animation=True)

