





def createimage(i,renderView1):
	# ----------------------------------------------------------------
	# setup the data processing pipelines
	# ----------------------------------------------------------------
	#fname='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/washmc_310000.h5'
	#ifname='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/images/washmc_310000.jpg'

	fnameroot='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/washmc_'
	ifnameroot='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/images/washmc_'

	fname=fnameroot+str(i*10000)+'.h5'
	ifname=ifnameroot+str(i*10000)+'.jpg'

	# create a new 'VisItPixieReader'
	washmc_h5 = VisItPixieReader(FileName=fname)
	washmc_h5.Meshes = ['mesh_128x128x128']
	washmc_h5.CellArrays = ['data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']

	# create a new 'Calculator'
	bfieldcalc = Calculator(Input=washmc_h5)
	bfieldcalc.AttributeType = 'Cell Data'
	bfieldcalc.ResultArrayName = 'bfield'
	bfieldcalc.Function = """iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)
"""

	# create a new 'Slice'
	slice1 = Slice(Input=bfieldcalc)
	slice1.SliceType = 'Plane'
	slice1.SliceOffsetValues = [0.0]

	# init the 'Plane' selected for 'SliceType'
	slice1.SliceType.Origin = [109.2836351789272, 64.0, 64.0]

	# create a new 'Calculator'
	vfieldcalc = Calculator(Input=washmc_h5)
	vfieldcalc.AttributeType = 'Cell Data'
	vfieldcalc.ResultArrayName = 'vfield'
	vfieldcalc.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'

	# create a new 'Slice'
	slice2 = Slice(Input=vfieldcalc)
	slice2.SliceType = 'Plane'
	slice2.SliceOffsetValues = [0.0]

	# init the 'Plane' selected for 'SliceType'
	slice2.SliceType.Origin = [0.02317771427184967, 64.0, 64.0]

	# create a new 'Stream Tracer'
	streamTracer1 = StreamTracer(Input=vfieldcalc, SeedType='Point Source')
	streamTracer1.Vectors = ['CELLS', 'vfield']
	streamTracer1.MaximumStreamlineLength = 128.0

	# init the 'Point Source' selected for 'SeedType'
	streamTracer1.SeedType.Center = [13.23683034246972, 67.62323822572358, 87.4221649047337]
	streamTracer1.SeedType.Radius = 12.8

	# create a new 'Tube'
	tube1 = Tube(Input=streamTracer1)
	tube1.Scalars = ['POINTS', 'AngularVelocity']
	tube1.Vectors = ['POINTS', 'Normals']
	tube1.Radius = 0.5933405303955078

	# ----------------------------------------------------------------
	# setup the visualization in view 'renderView1'
	# ----------------------------------------------------------------

	# show data from vfieldcalc
	vfieldcalcDisplay = Show(vfieldcalc, renderView1)

	# trace defaults for the display properties.
	vfieldcalcDisplay.Representation = 'Outline'
	vfieldcalcDisplay.ColorArrayName = [None, '']
	vfieldcalcDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
	vfieldcalcDisplay.SelectOrientationVectors = 'None'
	vfieldcalcDisplay.ScaleFactor = 12.8
	vfieldcalcDisplay.SelectScaleArray = 'None'
	vfieldcalcDisplay.GlyphType = 'Arrow'
	vfieldcalcDisplay.GlyphTableIndexArray = 'None'
	vfieldcalcDisplay.GaussianRadius = 0.64
	vfieldcalcDisplay.SetScaleArray = [None, '']
	vfieldcalcDisplay.ScaleTransferFunction = 'PiecewiseFunction'
	vfieldcalcDisplay.OpacityArray = [None, '']
	vfieldcalcDisplay.OpacityTransferFunction = 'PiecewiseFunction'
	vfieldcalcDisplay.DataAxesGrid = 'GridAxesRepresentation'
	vfieldcalcDisplay.PolarAxes = 'PolarAxesRepresentation'

	# show data from bfieldcalc
	bfieldcalcDisplay = Show(bfieldcalc, renderView1)

	# get color transfer function/color map for 'bfield'
	bfieldLUT = GetColorTransferFunction('bfield')
	bfieldLUT.RGBPoints = [3.19828e-75, 0.231373, 0.298039, 0.752941, 0.04460321654312536, 0.865003, 0.865003, 0.865003, 0.08920643308625072, 0.705882, 0.0156863, 0.14902]
	bfieldLUT.ScalarRangeInitialized = 1.0

	# trace defaults for the display properties.
	bfieldcalcDisplay.Representation = 'Outline'
	bfieldcalcDisplay.ColorArrayName = ['CELLS', 'bfield']
	bfieldcalcDisplay.LookupTable = bfieldLUT
	bfieldcalcDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
	bfieldcalcDisplay.SelectOrientationVectors = 'bfield'
	bfieldcalcDisplay.ScaleFactor = 12.8
	bfieldcalcDisplay.SelectScaleArray = 'None'
	bfieldcalcDisplay.GlyphType = 'Arrow'
	bfieldcalcDisplay.GlyphTableIndexArray = 'None'
	bfieldcalcDisplay.GaussianRadius = 0.64
	bfieldcalcDisplay.SetScaleArray = [None, '']
	bfieldcalcDisplay.ScaleTransferFunction = 'PiecewiseFunction'
	bfieldcalcDisplay.OpacityArray = [None, '']
	bfieldcalcDisplay.OpacityTransferFunction = 'PiecewiseFunction'
	bfieldcalcDisplay.DataAxesGrid = 'GridAxesRepresentation'
	bfieldcalcDisplay.PolarAxes = 'PolarAxesRepresentation'

	# show data from tube1
	tube1Display = Show(tube1, renderView1)

	# get color transfer function/color map for 'vfield'
	vfieldLUT = GetColorTransferFunction('vfield')
	vfieldLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.00015467511149859538, 0.865003, 0.865003, 0.865003, 0.00030935022299719077, 0.705882, 0.0156863, 0.14902]
	vfieldLUT.ScalarRangeInitialized = 1.0

	# trace defaults for the display properties.
	tube1Display.Representation = 'Surface'
	tube1Display.ColorArrayName = ['POINTS', 'vfield']
	tube1Display.LookupTable = vfieldLUT
	tube1Display.OSPRayScaleArray = 'AngularVelocity'
	tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
	tube1Display.SelectOrientationVectors = 'Normals'
	tube1Display.ScaleFactor = 6.033758544921875
	tube1Display.SelectScaleArray = 'AngularVelocity'
	tube1Display.GlyphType = 'Arrow'
	tube1Display.GlyphTableIndexArray = 'AngularVelocity'
	tube1Display.GaussianRadius = 0.3016879272460938
	tube1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
	tube1Display.ScaleTransferFunction = 'PiecewiseFunction'
	tube1Display.OpacityArray = ['POINTS', 'AngularVelocity']
	tube1Display.OpacityTransferFunction = 'PiecewiseFunction'
	tube1Display.DataAxesGrid = 'GridAxesRepresentation'
	tube1Display.PolarAxes = 'PolarAxesRepresentation'

	# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
	tube1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

	# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
	tube1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

	# show data from slice1
	slice1Display = Show(slice1, renderView1)

	# trace defaults for the display properties.
	slice1Display.Representation = 'Surface'
	slice1Display.ColorArrayName = ['CELLS', 'bfield']
	slice1Display.LookupTable = bfieldLUT
	slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
	slice1Display.SelectOrientationVectors = 'bfield'
	slice1Display.ScaleFactor = 12.8
	slice1Display.SelectScaleArray = 'None'
	slice1Display.GlyphType = 'Arrow'
	slice1Display.GlyphTableIndexArray = 'None'
	slice1Display.GaussianRadius = 0.64
	slice1Display.SetScaleArray = [None, '']
	slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
	slice1Display.OpacityArray = [None, '']
	slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
	slice1Display.DataAxesGrid = 'GridAxesRepresentation'
	slice1Display.PolarAxes = 'PolarAxesRepresentation'

	# show data from slice2
	slice2Display = Show(slice2, renderView1)

	# trace defaults for the display properties.
	slice2Display.Representation = 'Surface'
	slice2Display.ColorArrayName = ['CELLS', 'vfield']
	slice2Display.LookupTable = vfieldLUT
	slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
	slice2Display.SelectOrientationVectors = 'vfield'
	slice2Display.ScaleFactor = 12.8
	slice2Display.SelectScaleArray = 'None'
	slice2Display.GlyphType = 'Arrow'
	slice2Display.GlyphTableIndexArray = 'None'
	slice2Display.GaussianRadius = 0.64
	slice2Display.SetScaleArray = [None, '']
	slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
	slice2Display.OpacityArray = [None, '']
	slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
	slice2Display.DataAxesGrid = 'GridAxesRepresentation'
	slice2Display.PolarAxes = 'PolarAxesRepresentation'

	# setup the color legend parameters for each legend in this view

	# get color legend/bar for bfieldLUT in view renderView1
	bfieldLUTColorBar = GetScalarBar(bfieldLUT, renderView1)
	bfieldLUTColorBar.Title = 'bfield'
	bfieldLUTColorBar.ComponentTitle = 'Magnitude'

	# set color bar visibility
	bfieldLUTColorBar.Visibility = 1

	# get color legend/bar for vfieldLUT in view renderView1
	vfieldLUTColorBar = GetScalarBar(vfieldLUT, renderView1)
	vfieldLUTColorBar.WindowLocation = 'UpperRightCorner'
	vfieldLUTColorBar.Title = 'vfield'
	vfieldLUTColorBar.ComponentTitle = 'Magnitude'

	# set color bar visibility
	vfieldLUTColorBar.Visibility = 1

	# show color legend
	bfieldcalcDisplay.SetScalarBarVisibility(renderView1, True)

	# show color legend
	tube1Display.SetScalarBarVisibility(renderView1, True)

	# show color legend
	slice1Display.SetScalarBarVisibility(renderView1, True)

	# show color legend
	slice2Display.SetScalarBarVisibility(renderView1, True)

	# ----------------------------------------------------------------
	# setup color maps and opacity mapes used in the visualization
	# note: the Get..() functions create a new object, if needed
	# ----------------------------------------------------------------

	# get opacity transfer function/opacity map for 'bfield'
	bfieldPWF = GetOpacityTransferFunction('bfield')
	bfieldPWF.Points = [3.19828e-75, 0.0, 0.5, 0.0, 0.08920643308625072, 1.0, 0.5, 0.0]
	bfieldPWF.ScalarRangeInitialized = 1

	# get opacity transfer function/opacity map for 'vfield'
	vfieldPWF = GetOpacityTransferFunction('vfield')
	vfieldPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.00030935022299719077, 1.0, 0.5, 0.0]
	vfieldPWF.ScalarRangeInitialized = 1

	# ----------------------------------------------------------------
	# finally, restore active source
	SetActiveSource(None)
	# ----------------------------------------------------------------

	render_view = paraview.simple.GetActiveView()
	paraview.simple.SaveScreenshot(ifname, render_view)









# state file generated using paraview version 5.7.0-RC2

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.7.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2116, 1270]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [64.0, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [232.41509340431676, 283.56467422001595, -331.42005545174095]
renderView1.CameraFocalPoint = [64.0000000000007, 63.999999999999844, 63.99999999999893]
renderView1.CameraViewUp = [0.9317862015966341, -0.2617476005746883, 0.25152071109057866]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 125.8623586833384
renderView1.Background = [0.32, 0.34, 0.43]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------





for i in range(1,30):
 createimage(i, renderView1)