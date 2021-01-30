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
renderView1.ViewSize = [1490, 1270]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [31.51106783747673, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [81.91128493255674, 280.4506472714317, -58.60686653960058]
renderView1.CameraFocalPoint = [32.18203324897445, 61.640167365921, 59.92524334712296]
renderView1.CameraViewUp = [0.9804420646125451, -0.16340480797763693, 0.10969150681835672]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 96.16408223999768
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

# create a new 'Calculator'
calc_mag_perturb = Calculator(Input=extractSubset1)
calc_mag_perturb.AttributeType = 'Cell Data'
calc_mag_perturb.ResultArrayName = 'mag_perturb'
calc_mag_perturb.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'

# create a new 'Bounding Ruler'
boundingRuler2 = BoundingRuler(Input=extractSubset1)
boundingRuler2.Axis = 'Y Axis'

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
streamTracer1.MaximumStreamlineLength = 128.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [0.0, 32.0, 32.0]
streamTracer1.SeedType.Point2 = [0.0, 96.0, 96.0]
streamTracer1.SeedType.Resolution = 25

# create a new 'Tube'
tube1 = Tube(Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.8

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=extractSubset1)
cellDatatoPointData1.CellDataArraytoprocess = ['avtGhostZones', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']

# create a new 'Slice'
slice1 = Slice(Input=extractSubset1)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [1.5077042758428456, 64.0, 64.0]

# create a new 'Calculator'
calc_mag_bg = Calculator(Input=extractSubset1)
calc_mag_bg.AttributeType = 'Cell Data'
calc_mag_bg.ResultArrayName = 'mag_bg'
calc_mag_bg.Function = 'iHat*data/grid_0000000000/mag_field_x_bg+jHat*data/grid_0000000000/mag_field_y_bg+kHat*data/grid_0000000000/mag_field_z_bg'

# create a new 'Bounding Ruler'
boundingRuler1 = BoundingRuler(Input=extractSubset1)

# create a new 'Bounding Ruler'
boundingRuler3 = BoundingRuler(Input=extractSubset1)
boundingRuler3.Axis = 'Z Axis'

# create a new 'Contour'
contour1 = Contour(Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'data/grid_0000000000/velocity_z']
contour1.Isosurfaces = [-0.003048754829757382]
contour1.PointMergeMethod = 'Uniform Binning'

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

# show data from cellDatatoPointData1
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1)

# get color transfer function/color map for 'datagrid_0000000000velocity_z'
datagrid_0000000000velocity_zLUT = GetColorTransferFunction('datagrid_0000000000velocity_z')
datagrid_0000000000velocity_zLUT.RGBPoints = [-0.009707228867535144, 0.231373, 0.298039, 0.752941, 0.000818661173138847, 0.865003, 0.865003, 0.865003, 0.011344551213812839, 0.705882, 0.0156863, 0.14902]
datagrid_0000000000velocity_zLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
cellDatatoPointData1Display.Representation = 'Outline'
cellDatatoPointData1Display.ColorArrayName = ['POINTS', 'data/grid_0000000000/velocity_z']
cellDatatoPointData1Display.LookupTable = datagrid_0000000000velocity_zLUT
cellDatatoPointData1Display.OSPRayScaleArray = 'avtGhostZones'
cellDatatoPointData1Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.SelectOrientationVectors = 'None'
cellDatatoPointData1Display.ScaleFactor = 12.8
cellDatatoPointData1Display.SelectScaleArray = 'None'
cellDatatoPointData1Display.GlyphType = 'Arrow'
cellDatatoPointData1Display.GlyphTableIndexArray = 'None'
cellDatatoPointData1Display.GaussianRadius = 0.64
cellDatatoPointData1Display.SetScaleArray = ['POINTS', 'avtGhostZones']
cellDatatoPointData1Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.OpacityArray = ['POINTS', 'avtGhostZones']
cellDatatoPointData1Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData1Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

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

# show data from contour2
contour2Display = Show(contour2, renderView1)

# get color transfer function/color map for 'vel'
velLUT = GetColorTransferFunction('vel')
velLUT.RGBPoints = [2.0681455509733683e-10, 0.231373, 0.298039, 0.752941, 0.15533753433233272, 0.865003, 0.865003, 0.865003, 0.31067506845785087, 0.705882, 0.0156863, 0.14902]
velLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour2Display.Representation = 'Surface'
contour2Display.ColorArrayName = ['POINTS', 'vel']
contour2Display.LookupTable = velLUT
contour2Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour2Display.SelectOrientationVectors = 'None'
contour2Display.ScaleFactor = -2.0000000000000002e+298
contour2Display.SelectScaleArray = 'None'
contour2Display.GlyphType = 'Arrow'
contour2Display.GlyphTableIndexArray = 'None'
contour2Display.GaussianRadius = -1e+297
contour2Display.SetScaleArray = [None, '']
contour2Display.ScaleTransferFunction = 'PiecewiseFunction'
contour2Display.OpacityArray = [None, '']
contour2Display.OpacityTransferFunction = 'PiecewiseFunction'
contour2Display.DataAxesGrid = 'GridAxesRepresentation'
contour2Display.PolarAxes = 'PolarAxesRepresentation'

# show data from streamTracer1
streamTracer1Display = Show(streamTracer1, renderView1)

# trace defaults for the display properties.
streamTracer1Display.Representation = 'Surface'
streamTracer1Display.ColorArrayName = [None, '']
streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
streamTracer1Display.SelectOrientationVectors = 'Normals'
streamTracer1Display.ScaleFactor = 5.904342683346477
streamTracer1Display.SelectScaleArray = 'AngularVelocity'
streamTracer1Display.GlyphType = 'Arrow'
streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
streamTracer1Display.GaussianRadius = 0.2952171341673238
streamTracer1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.ScaleTransferFunction = 'PiecewiseFunction'
streamTracer1Display.OpacityArray = ['POINTS', 'AngularVelocity']
streamTracer1Display.OpacityTransferFunction = 'PiecewiseFunction'
streamTracer1Display.DataAxesGrid = 'GridAxesRepresentation'
streamTracer1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
streamTracer1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
streamTracer1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from tube1
tube1Display = Show(tube1, renderView1)

# trace defaults for the display properties.
tube1Display.Representation = 'Surface'
tube1Display.ColorArrayName = ['POINTS', 'vel']
tube1Display.LookupTable = velLUT
tube1Display.OSPRayScaleArray = 'AngularVelocity'
tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube1Display.SelectOrientationVectors = 'Normals'
tube1Display.ScaleFactor = 4.36705718934536
tube1Display.SelectScaleArray = 'AngularVelocity'
tube1Display.GlyphType = 'Arrow'
tube1Display.GlyphTableIndexArray = 'AngularVelocity'
tube1Display.GaussianRadius = 0.21835285946726798
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

# get color transfer function/color map for 'datagrid_0000000000density_pert'
datagrid_0000000000density_pertLUT = GetColorTransferFunction('datagrid_0000000000density_pert')
datagrid_0000000000density_pertLUT.RGBPoints = [-2.1316989633253864e-06, 0.231373, 0.298039, 0.752941, -1.0109652463988963e-08, 0.865003, 0.865003, 0.865003, 2.1114796583974085e-06, 0.705882, 0.0156863, 0.14902]
datagrid_0000000000density_pertLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.ColorArrayName = ['CELLS', 'data/grid_0000000000/density_pert']
slice1Display.LookupTable = datagrid_0000000000density_pertLUT
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.SelectOrientationVectors = 'None'
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

# setup the color legend parameters for each legend in this view

# get color legend/bar for datagrid_0000000000velocity_zLUT in view renderView1
datagrid_0000000000velocity_zLUTColorBar = GetScalarBar(datagrid_0000000000velocity_zLUT, renderView1)
datagrid_0000000000velocity_zLUTColorBar.Position = [0.8481425702811245, 0.03976377952755906]
datagrid_0000000000velocity_zLUTColorBar.Title = 'z-Component of Velocity'
datagrid_0000000000velocity_zLUTColorBar.ComponentTitle = ''

# set color bar visibility
datagrid_0000000000velocity_zLUTColorBar.Visibility = 1

# get color legend/bar for velLUT in view renderView1
velLUTColorBar = GetScalarBar(velLUT, renderView1)
velLUTColorBar.WindowLocation = 'UpperRightCorner'
velLUTColorBar.Title = 'vel'
velLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
velLUTColorBar.Visibility = 1

# get color legend/bar for datagrid_0000000000density_pertLUT in view renderView1
datagrid_0000000000density_pertLUTColorBar = GetScalarBar(datagrid_0000000000density_pertLUT, renderView1)
datagrid_0000000000density_pertLUTColorBar.WindowLocation = 'UpperLeftCorner'
datagrid_0000000000density_pertLUTColorBar.Title = 'Perturbed Density'
datagrid_0000000000density_pertLUTColorBar.ComponentTitle = ''

# set color bar visibility
datagrid_0000000000density_pertLUTColorBar.Visibility = 1

# show color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
contour2Display.SetScalarBarVisibility(renderView1, True)

# show color legend
tube1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'datagrid_0000000000velocity_z'
datagrid_0000000000velocity_zPWF = GetOpacityTransferFunction('datagrid_0000000000velocity_z')
datagrid_0000000000velocity_zPWF.Points = [-0.009707228867535144, 0.0, 0.5, 0.0, 0.011344551213812839, 1.0, 0.5, 0.0]
datagrid_0000000000velocity_zPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'vel'
velPWF = GetOpacityTransferFunction('vel')
velPWF.Points = [2.0681455509733683e-10, 0.0, 0.5, 0.0, 0.31067506845785087, 1.0, 0.5, 0.0]
velPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'datagrid_0000000000density_pert'
datagrid_0000000000density_pertPWF = GetOpacityTransferFunction('datagrid_0000000000density_pert')
datagrid_0000000000density_pertPWF.Points = [-2.1316989633253864e-06, 0.0, 0.5, 0.0, 2.1114796583974085e-06, 1.0, 0.5, 0.0]
datagrid_0000000000density_pertPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(streamTracer1)
# ----------------------------------------------------------------