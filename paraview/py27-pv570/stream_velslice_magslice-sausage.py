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
renderView1.ViewSize = [1632, 1270]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [32.0, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [86.72154683043681, 266.49345781934176, 68.68909622298105]
renderView1.CameraFocalPoint = [19.58679016341153, 68.33486241044196, 60.76518161026226]
renderView1.CameraViewUp = [0.9471614205094203, -0.3207326217769974, -0.0039785457934621]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 96.0
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'Render View'
renderView2 = CreateView('RenderView')
renderView2.ViewSize = [1632, 602]
renderView2.AxesGrid = 'GridAxes3DActor'
renderView2.CenterOfRotation = [32.00000071525574, 64.00000143051147, 64.0]
renderView2.StereoType = 'Crystal Eyes'
renderView2.CameraPosition = [187.20329582227467, -354.8432884805973, 53.683014989204715]
renderView2.CameraFocalPoint = [32.00000071525574, 64.00000143051147, 63.99999999999999]
renderView2.CameraViewUp = [0.9376957535104634, 0.3474572932142629, 0.00032131084893849415]
renderView2.CameraFocalDisk = 1.0
renderView2.CameraParallelScale = 115.63860123703756
renderView2.Background = [0.32, 0.34, 0.43]
renderView2.BackEnd = 'OSPRay raycaster'
renderView2.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitVertical(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, renderView2)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'VisItPixieReader'
washmc_741000h5 = VisItPixieReader(FileName='/Users/mikegriffiths/proj/washmc-data/uni6/h5/washmc_1261000.h5')
washmc_741000h5.Meshes = ['mesh_128x128x128']
washmc_741000h5.CellArrays = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'grid_left_index', 'grid_level', 'grid_parent_id', 'grid_particle_count']

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=washmc_741000h5)
extractSubset1.VOI = [0, 64, 0, 128, 0, 128]

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=extractSubset1)
cellDatatoPointData1.CellDataArraytoprocess = ['avtGhostZones', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']

# create a new 'Contour'
contour1 = Contour(Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'data/grid_0000000000/velocity_z']
contour1.Isosurfaces = [-0.003048754829757382]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Bounding Ruler'
boundingRuler1 = BoundingRuler(Input=extractSubset1)

# create a new 'Calculator'
calc_etot = Calculator(Input=extractSubset1)
calc_etot.AttributeType = 'Cell Data'
calc_etot.ResultArrayName = 'etot'
calc_etot.Function = 'data/grid_0000000000/internal_energy_bg+data/grid_0000000000/internal_energy_pert'

# create a new 'Calculator'
calc_vel = Calculator(Input=extractSubset1)
calc_vel.AttributeType = 'Cell Data'
calc_vel.ResultArrayName = 'vel'
calc_vel.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'

# create a new 'Cell Data to Point Data'
cellDatatoPointData2 = CellDatatoPointData(Input=calc_vel)
cellDatatoPointData2.CellDataArraytoprocess = ['avtGhostZones', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']

# create a new 'Contour'
contour2 = Contour(Input=cellDatatoPointData2)
contour2.ContourBy = ['POINTS', 'data/grid_0000000000/velocity_z']
contour2.Isosurfaces = [0.002]
contour2.PointMergeMethod = 'Uniform Binning'

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calc_vel,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['CELLS', 'vel']
streamTracer1.MaximumStreamlineLength = 228.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [0.0, 32.0, 32.0]
streamTracer1.SeedType.Point2 = [0.0, 96.0, 96.0]
streamTracer1.SeedType.Resolution = 7

# create a new 'Tube'
tube1 = Tube(Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']

# create a new 'Slice'
slice3 = Slice(Input=calc_vel)
slice3.SliceType = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [1.0, 64.0, 64.0]

# create a new 'Calculator'
calc_mag_bg = Calculator(Input=extractSubset1)
calc_mag_bg.AttributeType = 'Cell Data'
calc_mag_bg.ResultArrayName = 'mag_bg'
calc_mag_bg.Function = 'iHat*data/grid_0000000000/mag_field_x_bg+jHat*data/grid_0000000000/mag_field_y_bg+kHat*data/grid_0000000000/mag_field_z_bg'

# create a new 'Calculator'
calc_mag_perturb = Calculator(Input=extractSubset1)
calc_mag_perturb.AttributeType = 'Cell Data'
calc_mag_perturb.ResultArrayName = 'mag_perturb'
calc_mag_perturb.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'

# create a new 'Calculator'
calc_btot = Calculator(Input=extractSubset1)
calc_btot.AttributeType = 'Cell Data'
calc_btot.ResultArrayName = 'bt'
calc_btot.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'

# create a new 'Slice'
slice1 = Slice(Input=calc_btot)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [32.0, 64.0, 64.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# create a new 'Slice'
slice2 = Slice(Input=calc_btot)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [32.0, 64.0, 64.0]
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'Calculator'
calc_rhotot = Calculator(Input=extractSubset1)
calc_rhotot.AttributeType = 'Cell Data'
calc_rhotot.ResultArrayName = 'rhotot'
calc_rhotot.Function = 'data/grid_0000000000/density_pert+data/grid_0000000000/density_bg'

# create a new 'Slice'
perturbdensslice = Slice(Input=extractSubset1)
perturbdensslice.SliceType = 'Plane'
perturbdensslice.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
perturbdensslice.SliceType.Origin = [1.5077042758428456, 64.0, 64.0]

# create a new 'Bounding Ruler'
boundingRuler3 = BoundingRuler(Input=extractSubset1)
boundingRuler3.Axis = 'Z Axis'

# create a new 'Bounding Ruler'
boundingRuler2 = BoundingRuler(Input=extractSubset1)
boundingRuler2.Axis = 'Y Axis'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from extractSubset1
extractSubset1Display = Show(extractSubset1, renderView1)

# trace defaults for the display properties.
extractSubset1Display.Representation = 'Outline'
extractSubset1Display.ColorArrayName = [None, '']
extractSubset1Display.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset1Display.SelectOrientationVectors = 'None'
extractSubset1Display.ScaleFactor = 12.8
extractSubset1Display.SelectScaleArray = 'None'
extractSubset1Display.GlyphType = 'Arrow'
extractSubset1Display.GlyphTableIndexArray = 'None'
extractSubset1Display.GaussianRadius = 0.64
extractSubset1Display.SetScaleArray = [None, '']
extractSubset1Display.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset1Display.OpacityArray = [None, '']
extractSubset1Display.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset1Display.DataAxesGrid = 'GridAxesRepresentation'
extractSubset1Display.PolarAxes = 'PolarAxesRepresentation'

# show data from calc_mag_bg
calc_mag_bgDisplay = Show(calc_mag_bg, renderView1)

# trace defaults for the display properties.
calc_mag_bgDisplay.Representation = 'Outline'
calc_mag_bgDisplay.ColorArrayName = [None, '']
calc_mag_bgDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calc_mag_bgDisplay.SelectOrientationVectors = 'Result'
calc_mag_bgDisplay.ScaleFactor = 12.8
calc_mag_bgDisplay.SelectScaleArray = 'None'
calc_mag_bgDisplay.GlyphType = 'Arrow'
calc_mag_bgDisplay.GlyphTableIndexArray = 'None'
calc_mag_bgDisplay.GaussianRadius = 0.64
calc_mag_bgDisplay.SetScaleArray = [None, '']
calc_mag_bgDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calc_mag_bgDisplay.OpacityArray = [None, '']
calc_mag_bgDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calc_mag_bgDisplay.DataAxesGrid = 'GridAxesRepresentation'
calc_mag_bgDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from calc_mag_perturb
calc_mag_perturbDisplay = Show(calc_mag_perturb, renderView1)

# trace defaults for the display properties.
calc_mag_perturbDisplay.Representation = 'Outline'
calc_mag_perturbDisplay.ColorArrayName = [None, '']
calc_mag_perturbDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calc_mag_perturbDisplay.SelectOrientationVectors = 'mag_perturb'
calc_mag_perturbDisplay.ScaleFactor = 12.8
calc_mag_perturbDisplay.SelectScaleArray = 'None'
calc_mag_perturbDisplay.GlyphType = 'Arrow'
calc_mag_perturbDisplay.GlyphTableIndexArray = 'None'
calc_mag_perturbDisplay.GaussianRadius = 0.64
calc_mag_perturbDisplay.SetScaleArray = [None, '']
calc_mag_perturbDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calc_mag_perturbDisplay.OpacityArray = [None, '']
calc_mag_perturbDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calc_mag_perturbDisplay.DataAxesGrid = 'GridAxesRepresentation'
calc_mag_perturbDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from calc_vel
calc_velDisplay = Show(calc_vel, renderView1)

# trace defaults for the display properties.
calc_velDisplay.Representation = 'Outline'
calc_velDisplay.ColorArrayName = [None, '']
calc_velDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calc_velDisplay.SelectOrientationVectors = 'vel'
calc_velDisplay.ScaleFactor = 12.8
calc_velDisplay.SelectScaleArray = 'None'
calc_velDisplay.GlyphType = 'Arrow'
calc_velDisplay.GlyphTableIndexArray = 'None'
calc_velDisplay.GaussianRadius = 0.64
calc_velDisplay.SetScaleArray = [None, '']
calc_velDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calc_velDisplay.OpacityArray = [None, '']
calc_velDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calc_velDisplay.DataAxesGrid = 'GridAxesRepresentation'
calc_velDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from cellDatatoPointData2
cellDatatoPointData2Display = Show(cellDatatoPointData2, renderView1)

# trace defaults for the display properties.
cellDatatoPointData2Display.Representation = 'Outline'
cellDatatoPointData2Display.ColorArrayName = [None, '']
cellDatatoPointData2Display.OSPRayScaleArray = 'avtGhostZones'
cellDatatoPointData2Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData2Display.SelectOrientationVectors = 'vel'
cellDatatoPointData2Display.ScaleFactor = 12.8
cellDatatoPointData2Display.SelectScaleArray = 'None'
cellDatatoPointData2Display.GlyphType = 'Arrow'
cellDatatoPointData2Display.GlyphTableIndexArray = 'None'
cellDatatoPointData2Display.GaussianRadius = 0.64
cellDatatoPointData2Display.SetScaleArray = ['POINTS', 'avtGhostZones']
cellDatatoPointData2Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData2Display.OpacityArray = ['POINTS', 'avtGhostZones']
cellDatatoPointData2Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData2Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from boundingRuler1
boundingRuler1Display = Show(boundingRuler1, renderView1)

# trace defaults for the display properties.
boundingRuler1Display.LabelFormat = '%6.3g Mm'
boundingRuler1Display.Scale = 0.046875
boundingRuler1Display.NumberOfTicks = 7
boundingRuler1Display.Graduation = 6.0

# show data from boundingRuler2
boundingRuler2Display = Show(boundingRuler2, renderView1)

# trace defaults for the display properties.
boundingRuler2Display.LabelFormat = '%6.3g Mm'
boundingRuler2Display.Scale = 0.03125
boundingRuler2Display.NumberOfTicks = 9

# show data from boundingRuler3
boundingRuler3Display = Show(boundingRuler3, renderView1)

# trace defaults for the display properties.
boundingRuler3Display.LabelFormat = '%6.3g Mm'
boundingRuler3Display.Scale = 0.03125
boundingRuler3Display.NumberOfTicks = 9

# show data from calc_btot
calc_btotDisplay = Show(calc_btot, renderView1)

# trace defaults for the display properties.
calc_btotDisplay.Representation = 'Outline'
calc_btotDisplay.ColorArrayName = [None, '']
calc_btotDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calc_btotDisplay.SelectOrientationVectors = 'bt'
calc_btotDisplay.ScaleFactor = 12.8
calc_btotDisplay.SelectScaleArray = 'None'
calc_btotDisplay.GlyphType = 'Arrow'
calc_btotDisplay.GlyphTableIndexArray = 'None'
calc_btotDisplay.GaussianRadius = 0.64
calc_btotDisplay.SetScaleArray = [None, '']
calc_btotDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calc_btotDisplay.OpacityArray = [None, '']
calc_btotDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calc_btotDisplay.DataAxesGrid = 'GridAxesRepresentation'
calc_btotDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from slice1
slice1Display = Show(slice1, renderView1)

# get color transfer function/color map for 'bt'
btLUT = GetColorTransferFunction('bt')
btLUT.RGBPoints = [1.05586e-70, 0.231373, 0.298039, 0.752941, 0.046257912266945055, 0.865003, 0.865003, 0.865003, 0.09251582453389011, 0.705882, 0.0156863, 0.14902]
btLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'bt']
slice1Display.LookupTable = btLUT
slice1Display.Opacity = 0.44
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'bt'
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

# show data from slice3
slice3Display = Show(slice3, renderView1)

# get color transfer function/color map for 'vel'
velLUT = GetColorTransferFunction('vel')
velLUT.RGBPoints = [2.3373102460979543e-14, 0.231373, 0.298039, 0.752941, 0.15804042692262296, 0.865003, 0.865003, 0.865003, 0.31608085384522255, 0.705882, 0.0156863, 0.14902]
velLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['CELLS', 'vel']
slice3Display.LookupTable = velLUT
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.SelectOrientationVectors = 'vel'
slice3Display.ScaleFactor = 12.8
slice3Display.SelectScaleArray = 'None'
slice3Display.GlyphType = 'Arrow'
slice3Display.GlyphTableIndexArray = 'None'
slice3Display.GaussianRadius = 0.64
slice3Display.SetScaleArray = [None, '']
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityArray = [None, '']
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.PolarAxes = 'PolarAxesRepresentation'

# setup the color legend parameters for each legend in this view

# get color legend/bar for velLUT in view renderView1
velLUTColorBar = GetScalarBar(velLUT, renderView1)
velLUTColorBar.WindowLocation = 'UpperLeftCorner'
velLUTColorBar.Title = 'vel'
velLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
velLUTColorBar.Visibility = 1

# get color legend/bar for btLUT in view renderView1
btLUTColorBar = GetScalarBar(btLUT, renderView1)
btLUTColorBar.WindowLocation = 'UpperRightCorner'
btLUTColorBar.Title = 'bt'
btLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
btLUTColorBar.Visibility = 1

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
slice3Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'renderView2'
# ----------------------------------------------------------------

# show data from extractSubset1
extractSubset1Display_1 = Show(extractSubset1, renderView2)

# trace defaults for the display properties.
extractSubset1Display_1.Representation = 'Outline'
extractSubset1Display_1.ColorArrayName = [None, '']
extractSubset1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
extractSubset1Display_1.SelectOrientationVectors = 'None'
extractSubset1Display_1.ScaleFactor = 12.8
extractSubset1Display_1.SelectScaleArray = 'None'
extractSubset1Display_1.GlyphType = 'Arrow'
extractSubset1Display_1.GlyphTableIndexArray = 'None'
extractSubset1Display_1.GaussianRadius = 0.64
extractSubset1Display_1.SetScaleArray = [None, '']
extractSubset1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
extractSubset1Display_1.OpacityArray = [None, '']
extractSubset1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
extractSubset1Display_1.DataAxesGrid = 'GridAxesRepresentation'
extractSubset1Display_1.PolarAxes = 'PolarAxesRepresentation'

# show data from calc_vel
calc_velDisplay_1 = Show(calc_vel, renderView2)

# trace defaults for the display properties.
calc_velDisplay_1.Representation = 'Outline'
calc_velDisplay_1.ColorArrayName = [None, '']
calc_velDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
calc_velDisplay_1.SelectOrientationVectors = 'vel'
calc_velDisplay_1.ScaleFactor = 12.8
calc_velDisplay_1.SelectScaleArray = 'None'
calc_velDisplay_1.GlyphType = 'Arrow'
calc_velDisplay_1.GlyphTableIndexArray = 'None'
calc_velDisplay_1.GaussianRadius = 0.64
calc_velDisplay_1.SetScaleArray = [None, '']
calc_velDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
calc_velDisplay_1.OpacityArray = [None, '']
calc_velDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
calc_velDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
calc_velDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# show data from boundingRuler1
boundingRuler1Display_1 = Show(boundingRuler1, renderView2)

# trace defaults for the display properties.
boundingRuler1Display_1.LabelFormat = '%6.3g Mm'
boundingRuler1Display_1.Scale = 0.046875
boundingRuler1Display_1.NumberOfTicks = 7

# show data from boundingRuler2
boundingRuler2Display_1 = Show(boundingRuler2, renderView2)

# trace defaults for the display properties.
boundingRuler2Display_1.LabelFormat = '%6.3g Mm'
boundingRuler2Display_1.Scale = 0.03125
boundingRuler2Display_1.NumberOfTicks = 9

# show data from boundingRuler3
boundingRuler3Display_1 = Show(boundingRuler3, renderView2)

# trace defaults for the display properties.
boundingRuler3Display_1.LabelFormat = '%6.3g Mm'
boundingRuler3Display_1.Scale = 0.03125
boundingRuler3Display_1.NumberOfTicks = 9

# show data from slice3
slice3Display_1 = Show(slice3, renderView2)

# trace defaults for the display properties.
slice3Display_1.Representation = 'Surface'
slice3Display_1.ColorArrayName = ['CELLS', 'vel']
slice3Display_1.LookupTable = velLUT
slice3Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display_1.SelectOrientationVectors = 'vel'
slice3Display_1.ScaleFactor = 12.8
slice3Display_1.SelectScaleArray = 'None'
slice3Display_1.GlyphType = 'Arrow'
slice3Display_1.GlyphTableIndexArray = 'None'
slice3Display_1.GaussianRadius = 0.64
slice3Display_1.SetScaleArray = [None, '']
slice3Display_1.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display_1.OpacityArray = [None, '']
slice3Display_1.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice3Display_1.PolarAxes = 'PolarAxesRepresentation'

# show data from calc_btot
calc_btotDisplay_1 = Show(calc_btot, renderView2)

# trace defaults for the display properties.
calc_btotDisplay_1.Representation = 'Outline'
calc_btotDisplay_1.ColorArrayName = [None, '']
calc_btotDisplay_1.OSPRayScaleFunction = 'PiecewiseFunction'
calc_btotDisplay_1.SelectOrientationVectors = 'bt'
calc_btotDisplay_1.ScaleFactor = 12.8
calc_btotDisplay_1.SelectScaleArray = 'None'
calc_btotDisplay_1.GlyphType = 'Arrow'
calc_btotDisplay_1.GlyphTableIndexArray = 'None'
calc_btotDisplay_1.GaussianRadius = 0.64
calc_btotDisplay_1.SetScaleArray = [None, '']
calc_btotDisplay_1.ScaleTransferFunction = 'PiecewiseFunction'
calc_btotDisplay_1.OpacityArray = [None, '']
calc_btotDisplay_1.OpacityTransferFunction = 'PiecewiseFunction'
calc_btotDisplay_1.DataAxesGrid = 'GridAxesRepresentation'
calc_btotDisplay_1.PolarAxes = 'PolarAxesRepresentation'

# show data from slice1
slice1Display_1 = Show(slice1, renderView2)

# trace defaults for the display properties.
slice1Display_1.Representation = 'Surface'
slice1Display_1.ColorArrayName = ['CELLS', 'bt']
slice1Display_1.LookupTable = btLUT
slice1Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display_1.SelectOrientationVectors = 'bt'
slice1Display_1.ScaleFactor = 12.8
slice1Display_1.SelectScaleArray = 'None'
slice1Display_1.GlyphType = 'Arrow'
slice1Display_1.GlyphTableIndexArray = 'None'
slice1Display_1.GaussianRadius = 0.64
slice1Display_1.SetScaleArray = [None, '']
slice1Display_1.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display_1.OpacityArray = [None, '']
slice1Display_1.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display_1.DataAxesGrid = 'GridAxesRepresentation'
slice1Display_1.PolarAxes = 'PolarAxesRepresentation'

# show data from slice2
slice2Display = Show(slice2, renderView2)

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.ColorArrayName = ['CELLS', 'bt']
slice2Display.LookupTable = btLUT
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.SelectOrientationVectors = 'bt'
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

# show data from cellDatatoPointData2
cellDatatoPointData2Display_1 = Show(cellDatatoPointData2, renderView2)

# trace defaults for the display properties.
cellDatatoPointData2Display_1.Representation = 'Outline'
cellDatatoPointData2Display_1.ColorArrayName = [None, '']
cellDatatoPointData2Display_1.OSPRayScaleArray = 'avtGhostZones'
cellDatatoPointData2Display_1.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData2Display_1.SelectOrientationVectors = 'vel'
cellDatatoPointData2Display_1.ScaleFactor = 12.8
cellDatatoPointData2Display_1.SelectScaleArray = 'None'
cellDatatoPointData2Display_1.GlyphType = 'Arrow'
cellDatatoPointData2Display_1.GlyphTableIndexArray = 'None'
cellDatatoPointData2Display_1.GaussianRadius = 0.64
cellDatatoPointData2Display_1.SetScaleArray = ['POINTS', 'avtGhostZones']
cellDatatoPointData2Display_1.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData2Display_1.OpacityArray = ['POINTS', 'avtGhostZones']
cellDatatoPointData2Display_1.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData2Display_1.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData2Display_1.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData2Display_1.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData2Display_1.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for velLUT in view renderView2
velLUTColorBar_1 = GetScalarBar(velLUT, renderView2)
velLUTColorBar_1.Title = 'vel'
velLUTColorBar_1.ComponentTitle = 'Magnitude'

# set color bar visibility
velLUTColorBar_1.Visibility = 1

# get color legend/bar for btLUT in view renderView2
btLUTColorBar_1 = GetScalarBar(btLUT, renderView2)
btLUTColorBar_1.WindowLocation = 'UpperRightCorner'
btLUTColorBar_1.Title = 'bt'
btLUTColorBar_1.ComponentTitle = 'Magnitude'

# set color bar visibility
btLUTColorBar_1.Visibility = 1

# show color legend
slice3Display_1.SetScalarBarVisibility(renderView2, True)

# show color legend
slice1Display_1.SetScalarBarVisibility(renderView2, True)

# show color legend
slice2Display.SetScalarBarVisibility(renderView2, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'bt'
btPWF = GetOpacityTransferFunction('bt')
btPWF.Points = [1.05586e-70, 0.0, 0.5, 0.0, 0.09251582453389011, 1.0, 0.5, 0.0]
btPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'vel'
velPWF = GetOpacityTransferFunction('vel')
velPWF.Points = [2.3373102460979543e-14, 0.0, 0.5, 0.0, 0.31608085384522255, 1.0, 0.5, 0.0]
velPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(washmc_741000h5)
# ----------------------------------------------------------------