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
	remove_from_scene(objects["Cube"])

plywoodThickness = .435
shelfWidth       = 23.75
shelfLength      = 47.75
numShelves       = 4

def verticals() :
	o = [obox.copy()]
	o[0].scale = (3.5, 1.5, 6 * 12)
	o[0].location = (1.5, 0, 0)
	o.append(o[0].copy())
	o[1].location[1] += shelfLength + 1.5
	o.append(o[0].copy())
	o[2].location[0] += shelfWidth - 3 - 3.5
	o.append(o[1].copy())
	o[3].location[0] += shelfWidth - 3 - 3.5
	for i in range(4) :
		view_layer_objects.link(o[i])

def shelfFrame() :
	o = [obox.copy()]
	o[0].scale = (1.5, shelfLength + 3, 3.5)
	o[0].location = (0, 0, 6 * 12 / numShelves - 3.5 - plywoodThickness)
	o.append(o[0].copy())
	o[1].location[0] += shelfWidth - 1.5
	o.append(obox.copy())
	o[2].scale = (shelfWidth - 3, 1.5, 3.5)
	o[2].location = (1.5, 1.5, 6 * 12 / numShelves - 3.5 - plywoodThickness)
	o.append(o[2].copy())
	o[3].location[1] += shelfLength - 1.5
	o.append(o[2].copy())
	o[4].location[1] += (shelfLength - 1.5) / 2 
	for i in range(numShelves) :
		view_layer_objects.link(o[i])
	for j in range(1, numShelves) :
		for i in range(numShelves) :
			o[i] = o[i].copy()
			o[i].location[2] += 6 * 12 / numShelves
			view_layer_objects.link(o[i])

verticals()
shelfFrame()

view_layer.update()


