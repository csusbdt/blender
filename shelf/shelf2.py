import bpy
import bmesh
from math import radians

view_layer         = bpy.context.view_layer
view_layer_objects = view_layer.active_layer_collection.collection.objects
scene              = bpy.context.scene
objects            = bpy.data.objects
meshes             = bpy.data.meshes

obox = objects["Cube"].copy()
obox.data = obox.data.copy()
obox.name = "obox"
obox.data.name = "obox"
obox.data.vertices[0].co = ( 1.0, 1.0, 1.0 )
obox.data.vertices[1].co = ( 1.0, 0.0, 1.0 )
obox.data.vertices[2].co = ( 1.0, 1.0, 0.0 )
obox.data.vertices[3].co = ( 1.0, 0.0, 0.0 )
obox.data.vertices[4].co = ( 0.0, 1.0, 1.0 )
obox.data.vertices[5].co = ( 0.0, 0.0, 1.0 )
obox.data.vertices[6].co = ( 0.0, 1.0, 0.0 )
obox.data.vertices[7].co = ( 0.0, 0.0, 0.0 )

def remove_from_scene(o) :
	bpy.context.view_layer.active_layer_collection.collection.objects.unlink(o)

if ("Cube" in view_layer_objects):
	#view_layer_objects.unlink(objects["Cube"]) DOESN'T WORK
	remove_from_scene(objects["Cube"])

shelfHeight      = 8 * 12 / 5
shelfWidth       = 23.75
shelfThickness   = 0.435
shelfLength      = 47.75
plywoodY         = 4 * 12 - 1.5
plywoodThickness = .438
plywoodZ         = 8 * 12

def makeTallVerticals() :
	o = [obox.copy()]
	o[0].scale = (1.5, 3.5, 8 * 12)
	view_layer_objects.link(o[0])
	for i in range(1, 4) :
		o.append(o[0].copy())
		view_layer_objects.link(o[i])
	o[0].location[1] = 0
	o[1].location[1] = plywoodY - 3.5
	o[2].location[1] = shelfLength * 3 - plywoodY 
	o[3].location[1] = shelfLength * 3 - 3.5
	for i in range(4) :
		o[i] = o[i].copy()
		o[i].location[0] = shelfWidth + 1.5
		view_layer_objects.link(o[i])

def makeShortVerticals() :
	o = [obox.copy()]
	o[0].scale = (1.5, 3.5, shelfHeight - 3.5 - shelfThickness)
	o[0].location[0] = 1.5
	view_layer_objects.link(o[0])
	for i in range(1, 4) :
		o.append(o[0].copy())
		view_layer_objects.link(o[i])
	o[0].location[1] = 0
	o[1].location[1] = plywoodY - 3.5
	o[2].location[1] = shelfLength * 3 - plywoodY 
	o[3].location[1] = shelfLength * 3 - 3.5
	t = []
	for i in range(4) :
		t.append(o[i].copy())
		t[i].location[0] += shelfWidth - 1.5
		view_layer_objects.link(t[i])
	for j in range(1,5) :
		for i in range(4) :
			o[i] = o[i].copy()
			t[i] = t[i].copy()
			o[i].location[2] += shelfHeight
			t[i].location[2] += shelfHeight
			view_layer_objects.link(o[i])
			view_layer_objects.link(t[i])

def makeShelves() :
	o = []
	o.append(obox.copy())
	o[0].scale = (shelfWidth, shelfLength, shelfThickness)
	o[0].location = (1.5, 0, shelfHeight - shelfThickness)
	view_layer_objects.link(o[0])
	o.append(o[0].copy())
	o[1].location[1] += shelfLength
	view_layer_objects.link(o[1])
	o.append(o[1].copy())
	o[2].location[1] += shelfLength
	view_layer_objects.link(o[2])
	for j in range(1,6) :
		for i in range(3) :
			t = o[i].copy()
			t.location[2] = j * shelfHeight - shelfThickness
			view_layer_objects.link(t)

def makeLongHorizontals() :
	for j in range(1, 6) :
		o       = obox.copy()
		o.scale = (1.5, 3 * shelfLength, 3.5)
		o.location[0] = 1.5
		o.location[2] = j * shelfHeight - shelfThickness - 3.5
		view_layer_objects.link(o)
		o = o.copy()
		o.location[0] = shelfWidth 
		view_layer_objects.link(o)

def makeShortHorizontals() :
	for j in range(1, 6) :
		for i in range(3) :
			s = shelfWidth
			
			o1      = obox.copy()
			o1.scale = (shelfWidth - 2 * 1.5, 1.5, 3.5)
			o1.location[0] = 2 * 1.5
			o1.location[1] = i * shelfLength
			o1.location[2] = j * shelfHeight - shelfThickness - 3.5
			view_layer_objects.link(o1)
			o2 = o1.copy()
			o2.location[1] = (i + .5) * shelfLength - 1.5 / 2
			view_layer_objects.link(o2)
			o3 = o2.copy()
			o3.location[1] = (i + 1) * shelfLength - 1.5 
			view_layer_objects.link(o3)

def makeBackingBoards() :
	o  = obox.copy()
	o.scale = (plywoodThickness, plywoodY, plywoodZ)
	o.location = (-plywoodThickness, 0, 0)
	view_layer_objects.link(o)
	t = o.copy()
	t.location[1] = 3 * shelfLength - plywoodY
	view_layer_objects.link(t)


makeTallVerticals()
makeLongHorizontals()
makeShortVerticals()
makeShortHorizontals()
makeShelves()
makeBackingBoards()

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

