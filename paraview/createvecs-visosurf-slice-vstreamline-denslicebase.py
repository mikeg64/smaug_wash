# state file generated using paraview version 5.9.0-RC3

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [590, 484]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [63.99183115363121, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [177.91042148082522, -266.6480991676383, -183.28073256520912]
renderView1.CameraFocalPoint = [63.99183115363144, 64.00000000000094, 63.999999999999744]
renderView1.CameraViewUp = [0.9639728057605139, 0.21552908667584256, 0.15589625573078977]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 110.85596817070905
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(590, 484)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'VisItPixieReader'
washmc_ = VisItPixieReader(registrationName='washmc_*', FileName='C:\\Users\\Mike\\data\\washmc-data\\uni6\\h5\\washmc_1241000.h5')
washmc_.Meshes = ['mesh_128x128x128']
washmc_.CellArrays = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'grid_left_index', 'grid_level', 'grid_parent_id', 'grid_particle_count']

# create a new 'Calculator'
calc_mag_bg = Calculator(registrationName='calc_mag_bg', Input=washmc_)
calc_mag_bg.AttributeType = 'Cell Data'
calc_mag_bg.ResultArrayName = 'mag_bg'
calc_mag_bg.Function = 'iHat*data/grid_0000000000/mag_field_x_bg+jHat*data/grid_0000000000/mag_field_y_bg+kHat*data/grid_0000000000/mag_field_z_bg'

# create a new 'Calculator'
calc_mag = Calculator(registrationName='calc_mag', Input=washmc_)
calc_mag.AttributeType = 'Cell Data'
calc_mag.ResultArrayName = 'magtot'
calc_mag.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'

# create a new 'Cell Data to Point Data'
celtopointperturbdensslice = CellDatatoPointData(registrationName='celtopoint-perturbdensslice', Input=washmc_)
celtopointperturbdensslice.CellDataArraytoprocess = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'vtkGhostType']
celtopointperturbdensslice.PassCellData = 1

# create a new 'Slice'
sliceperturbdens = Slice(registrationName='Slice-perturb-dens', Input=celtopointperturbdensslice)
sliceperturbdens.SliceType = 'Plane'
sliceperturbdens.HyperTreeGridSlicer = 'Plane'
sliceperturbdens.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
sliceperturbdens.SliceType.Origin = [0.5550021981894281, 64.0, 64.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
sliceperturbdens.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]

# create a new 'Calculator'
calc_vel = Calculator(registrationName='calc_vel', Input=washmc_)
calc_vel.AttributeType = 'Cell Data'
calc_vel.ResultArrayName = 'vel'
calc_vel.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName='CellDatatoPointData1', Input=calc_vel)
cellDatatoPointData1.CellDataArraytoprocess = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'vel', 'vtkGhostType']
cellDatatoPointData1.PassCellData = 1

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'data/grid_0000000000/velocity_z']
contour1.Isosurfaces = [-0.0002725235781010477]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Slice'
slice_vz_x = Slice(registrationName='Slice_vz_x', Input=calc_vel)
slice_vz_x.SliceType = 'Plane'
slice_vz_x.HyperTreeGridSlicer = 'Plane'
slice_vz_x.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice_vz_x.SliceType.Origin = [3.7320650932642336, 64.0, 64.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice_vz_x.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(registrationName='StreamTracer2', Input=calc_vel,
    SeedType='Point Cloud')
streamTracer2.Vectors = ['CELLS', 'vel']
streamTracer2.MaximumStreamlineLength = 128.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer2.SeedType.Center = [-6.576192800848423, 64.0, 64.0]
streamTracer2.SeedType.NumberOfPoints = 30
streamTracer2.SeedType.Radius = 45.0

# create a new 'Tube'
tube2 = Tube(registrationName='Tube2', Input=streamTracer2)
tube2.Scalars = ['POINTS', 'AngularVelocity']
tube2.Vectors = ['POINTS', 'Normals']
tube2.Radius = 0.7109235191345215
tube2.RadiusFactor = 20.0

# create a new 'Slice'
slice_v_y = Slice(registrationName='Slice_v_y', Input=calc_vel)
slice_v_y.SliceType = 'Plane'
slice_v_y.HyperTreeGridSlicer = 'Plane'
slice_v_y.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice_v_y.SliceType.Origin = [40.834093376905784, 64.0, 64.0]
slice_v_y.SliceType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice_v_y.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]

# create a new 'Calculator'
calc_mag_pert = Calculator(registrationName='calc_mag_pert', Input=washmc_)
calc_mag_pert.AttributeType = 'Cell Data'
calc_mag_pert.ResultArrayName = 'mag_pert'
calc_mag_pert.Function = 'iHat*data/grid_0000000000/mag_field_x_pert+jHat*data/grid_0000000000/mag_field_y_pert+kHat*data/grid_0000000000/mag_field_z_pert'

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=calc_mag)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [98.15436160461222, 64.0, 64.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calc_mag,
    SeedType='Point Cloud')
streamTracer1.Vectors = ['CELLS', 'magtot']
streamTracer1.MaximumStreamlineLength = 128.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer1.SeedType.Center = [14.469582522288794, 61.11670202434248, 63.3654621027544]
streamTracer1.SeedType.NumberOfPoints = 16
streamTracer1.SeedType.Radius = 35.0

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.9194942289652303
tube1.RadiusFactor = 2.0

# create a new 'Slice'
slice_vz_z = Slice(registrationName='slice_vz_z', Input=calc_vel)
slice_vz_z.SliceType = 'Plane'
slice_vz_z.HyperTreeGridSlicer = 'Plane'
slice_vz_z.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice_vz_z.SliceType.Origin = [64.0, 64.0, 58.682287379454756]
slice_vz_z.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice_vz_z.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from slice_v_y
slice_v_yDisplay = Show(slice_v_y, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'datagrid_0000000000velocity_z'
datagrid_0000000000velocity_zLUT = GetColorTransferFunction('datagrid_0000000000velocity_z')
datagrid_0000000000velocity_zLUT.RGBPoints = [-0.00907199054104386, 0.231373, 0.298039, 0.752941, 0.0004458843044053782, 0.865003, 0.865003, 0.865003, 0.009963759149854616, 0.705882, 0.0156863, 0.14902]
datagrid_0000000000velocity_zLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice_v_yDisplay.Representation = 'Surface'
slice_v_yDisplay.ColorArrayName = ['CELLS', 'data/grid_0000000000/velocity_z']
slice_v_yDisplay.LookupTable = datagrid_0000000000velocity_zLUT
slice_v_yDisplay.Opacity = 0.52
slice_v_yDisplay.SelectTCoordArray = 'None'
slice_v_yDisplay.SelectNormalArray = 'None'
slice_v_yDisplay.SelectTangentArray = 'None'
slice_v_yDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
slice_v_yDisplay.SelectOrientationVectors = 'vel'
slice_v_yDisplay.ScaleFactor = 12.8
slice_v_yDisplay.SelectScaleArray = 'None'
slice_v_yDisplay.GlyphType = 'Arrow'
slice_v_yDisplay.GlyphTableIndexArray = 'None'
slice_v_yDisplay.GaussianRadius = 0.64
slice_v_yDisplay.SetScaleArray = [None, '']
slice_v_yDisplay.ScaleTransferFunction = 'PiecewiseFunction'
slice_v_yDisplay.OpacityArray = [None, '']
slice_v_yDisplay.OpacityTransferFunction = 'PiecewiseFunction'
slice_v_yDisplay.DataAxesGrid = 'GridAxesRepresentation'
slice_v_yDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from contour1
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'vel'
velLUT = GetColorTransferFunction('vel')
velLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.15322434123028017, 0.865003, 0.865003, 0.865003, 0.30644868246056034, 0.705882, 0.0156863, 0.14902]
velLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.ColorArrayName = ['POINTS', 'vel']
contour1Display.LookupTable = velLUT
contour1Display.Opacity = 0.24
contour1Display.SelectTCoordArray = 'None'
contour1Display.SelectNormalArray = 'None'
contour1Display.SelectTangentArray = 'None'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.ScaleFactor = -2.0000000000000002e+298
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.GaussianRadius = -1e+297
contour1Display.SetScaleArray = [None, '']
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityArray = [None, '']
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# show data from slice_vz_z
slice_vz_zDisplay = Show(slice_vz_z, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
slice_vz_zDisplay.Representation = 'Surface'
slice_vz_zDisplay.ColorArrayName = ['CELLS', 'data/grid_0000000000/velocity_z']
slice_vz_zDisplay.LookupTable = datagrid_0000000000velocity_zLUT
slice_vz_zDisplay.SelectTCoordArray = 'None'
slice_vz_zDisplay.SelectNormalArray = 'None'
slice_vz_zDisplay.SelectTangentArray = 'None'
slice_vz_zDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
slice_vz_zDisplay.SelectOrientationVectors = 'vel'
slice_vz_zDisplay.ScaleFactor = 12.8
slice_vz_zDisplay.SelectScaleArray = 'None'
slice_vz_zDisplay.GlyphType = 'Arrow'
slice_vz_zDisplay.GlyphTableIndexArray = 'None'
slice_vz_zDisplay.GaussianRadius = 0.64
slice_vz_zDisplay.SetScaleArray = [None, '']
slice_vz_zDisplay.ScaleTransferFunction = 'PiecewiseFunction'
slice_vz_zDisplay.OpacityArray = [None, '']
slice_vz_zDisplay.OpacityTransferFunction = 'PiecewiseFunction'
slice_vz_zDisplay.DataAxesGrid = 'GridAxesRepresentation'
slice_vz_zDisplay.PolarAxes = 'PolarAxesRepresentation'

# show data from tube2
tube2Display = Show(tube2, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'vel'
velLUT_1 = GetColorTransferFunction('vel')
velLUT_1.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.15322434123028017, 0.865003, 0.865003, 0.865003, 0.30644868246056034, 0.705882, 0.0156863, 0.14902]
velLUT_1.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = ['POINTS', 'vel']
tube2Display.LookupTable = velLUT_1
tube2Display.SelectTCoordArray = 'None'
tube2Display.SelectNormalArray = 'TubeNormals'
tube2Display.SelectTangentArray = 'None'
tube2Display.OSPRayScaleArray = 'AngularVelocity'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'Normals'
tube2Display.ScaleFactor = 13.023181009292603
tube2Display.SelectScaleArray = 'AngularVelocity'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'AngularVelocity'
tube2Display.GaussianRadius = 0.6511590504646302
tube2Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube2Display.ScaleTransferFunction = 'PiecewiseFunction'
tube2Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube2Display.OpacityTransferFunction = 'PiecewiseFunction'
tube2Display.DataAxesGrid = 'GridAxesRepresentation'
tube2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from sliceperturbdens
sliceperturbdensDisplay = Show(sliceperturbdens, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'datagrid_0000000000density_pert'
datagrid_0000000000density_pertLUT = GetColorTransferFunction('datagrid_0000000000density_pert')
datagrid_0000000000density_pertLUT.RGBPoints = [-1.7647579290310452e-06, 0.231373, 0.298039, 0.752941, -1.3842840699524163e-07, 0.865003, 0.865003, 0.865003, 1.487901115040562e-06, 0.705882, 0.0156863, 0.14902]
datagrid_0000000000density_pertLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
sliceperturbdensDisplay.Representation = 'Surface'
sliceperturbdensDisplay.ColorArrayName = ['POINTS', 'data/grid_0000000000/density_pert']
sliceperturbdensDisplay.LookupTable = datagrid_0000000000density_pertLUT
sliceperturbdensDisplay.SelectTCoordArray = 'None'
sliceperturbdensDisplay.SelectNormalArray = 'None'
sliceperturbdensDisplay.SelectTangentArray = 'None'
sliceperturbdensDisplay.OSPRayScaleArray = 'data/grid_0000000000/density_bg'
sliceperturbdensDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
sliceperturbdensDisplay.SelectOrientationVectors = 'None'
sliceperturbdensDisplay.ScaleFactor = 12.8
sliceperturbdensDisplay.SelectScaleArray = 'None'
sliceperturbdensDisplay.GlyphType = 'Arrow'
sliceperturbdensDisplay.GlyphTableIndexArray = 'None'
sliceperturbdensDisplay.GaussianRadius = 0.64
sliceperturbdensDisplay.SetScaleArray = ['POINTS', 'data/grid_0000000000/density_bg']
sliceperturbdensDisplay.ScaleTransferFunction = 'PiecewiseFunction'
sliceperturbdensDisplay.OpacityArray = ['POINTS', 'data/grid_0000000000/density_bg']
sliceperturbdensDisplay.OpacityTransferFunction = 'PiecewiseFunction'
sliceperturbdensDisplay.DataAxesGrid = 'GridAxesRepresentation'
sliceperturbdensDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
sliceperturbdensDisplay.ScaleTransferFunction.Points = [0.0001, 0.0, 0.5, 0.0, 0.00019797125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
sliceperturbdensDisplay.OpacityTransferFunction.Points = [0.0001, 0.0, 0.5, 0.0, 0.00019797125, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for velLUT in view renderView1
velLUTColorBar = GetScalarBar(velLUT, renderView1)
velLUTColorBar.WindowLocation = 'UpperRightCorner'
velLUTColorBar.Title = 'vel'
velLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
velLUTColorBar.Visibility = 1

# get color legend/bar for velLUT_1 in view renderView1
velLUT_1ColorBar = GetScalarBar(velLUT_1, renderView1)
velLUT_1ColorBar.WindowLocation = 'UpperLeftCorner'
velLUT_1ColorBar.Title = 'vel'
velLUT_1ColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
velLUT_1ColorBar.Visibility = 1

# get color legend/bar for datagrid_0000000000velocity_zLUT in view renderView1
datagrid_0000000000velocity_zLUTColorBar = GetScalarBar(datagrid_0000000000velocity_zLUT, renderView1)
datagrid_0000000000velocity_zLUTColorBar.WindowLocation = 'LowerLeftCorner'
datagrid_0000000000velocity_zLUTColorBar.Position = [0.006779661016949152, 0.10640495867768596]
datagrid_0000000000velocity_zLUTColorBar.Title = 'data/grid_0000000000/velocity_z'
datagrid_0000000000velocity_zLUTColorBar.ComponentTitle = ''

# set color bar visibility
datagrid_0000000000velocity_zLUTColorBar.Visibility = 1

# get color legend/bar for datagrid_0000000000density_pertLUT in view renderView1
datagrid_0000000000density_pertLUTColorBar = GetScalarBar(datagrid_0000000000density_pertLUT, renderView1)
datagrid_0000000000density_pertLUTColorBar.Title = 'data/grid_0000000000/density_pert'
datagrid_0000000000density_pertLUTColorBar.ComponentTitle = ''

# set color bar visibility
datagrid_0000000000density_pertLUTColorBar.Visibility = 1

# show color legend
slice_v_yDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
slice_vz_zDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
tube2Display.SetScalarBarVisibility(renderView1, True)

# show color legend
sliceperturbdensDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'vel'
velPWF = GetOpacityTransferFunction('vel')
velPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.30644868246056034, 1.0, 0.5, 0.0]
velPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'datagrid_0000000000velocity_z'
datagrid_0000000000velocity_zPWF = GetOpacityTransferFunction('datagrid_0000000000velocity_z')
datagrid_0000000000velocity_zPWF.Points = [-0.00907199054104386, 0.0, 0.5, 0.0, 0.009963759149854616, 1.0, 0.5, 0.0]
datagrid_0000000000velocity_zPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'datagrid_0000000000density_pert'
datagrid_0000000000density_pertPWF = GetOpacityTransferFunction('datagrid_0000000000density_pert')
datagrid_0000000000density_pertPWF.Points = [-1.7647579290310452e-06, 0.0, 0.5, 0.0, 1.487901115040562e-06, 1.0, 0.5, 0.0]
datagrid_0000000000density_pertPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'vel'
velPWF_1 = GetOpacityTransferFunction('vel')
velPWF_1.Points = [0.0, 0.0, 0.5, 0.0, 0.30644868246056034, 1.0, 0.5, 0.0]
velPWF_1.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(slice1)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')