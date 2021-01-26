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
renderView1.ViewSize = [501, 484]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [63.99183115363121, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [77.88676410956191, 124.99840528932752, 191.83660261077503]
renderView1.CameraFocalPoint = [26.572397277662603, 70.29390925310257, 77.8213970198278]
renderView1.CameraViewUp = [0.9233321210137231, -0.237952503704325, -0.3013907767088148]
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
layout1.SetSize(501, 484)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'VisItPixieReader'
washmc_ = VisItPixieReader(registrationName='washmc_*', FileName='C:\\Users\\Mike\\data\\washmc-data\\uni6\\h5\\washmc_1221000.h5')
washmc_.Meshes = ['mesh_128x128x128']
washmc_.CellArrays = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'grid_left_index', 'grid_level', 'grid_parent_id', 'grid_particle_count']

# create a new 'Calculator'
calc_mag_pert = Calculator(registrationName='calc_mag_pert', Input=washmc_)
calc_mag_pert.AttributeType = 'Cell Data'
calc_mag_pert.ResultArrayName = 'mag_pert'
calc_mag_pert.Function = 'iHat*data/grid_0000000000/mag_field_x_pert+jHat*data/grid_0000000000/mag_field_y_pert+kHat*data/grid_0000000000/mag_field_z_pert'

# create a new 'Cell Data to Point Data'
celtopointperturbdensslice = CellDatatoPointData(registrationName='celtopoint-perturbdensslice', Input=washmc_)
celtopointperturbdensslice.CellDataArraytoprocess = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'vtkGhostType']
celtopointperturbdensslice.PassCellData = 1

# create a new 'Calculator'
calc_mag = Calculator(registrationName='calc_mag', Input=washmc_)
calc_mag.AttributeType = 'Cell Data'
calc_mag.ResultArrayName = 'magtot'
calc_mag.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'

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

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(registrationName='ExtractSubset1', Input=washmc_)
extractSubset1.VOI = [0, 64, 0, 128, 0, 128]

# create a new 'Cell Data to Point Data'
cellpointtopertubdensesub = CellDatatoPointData(registrationName='cellpointtopertubdense-sub', Input=extractSubset1)
cellpointtopertubdensesub.CellDataArraytoprocess = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'vtkGhostType']

# create a new 'Calculator'
calcvel = Calculator(registrationName='calcvel', Input=extractSubset1)
calcvel.AttributeType = 'Cell Data'
calcvel.ResultArrayName = 'velsub'
calcvel.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'

# create a new 'Cell Data to Point Data'
cellpointodatavelsub = CellDatatoPointData(registrationName='cellpointodatavel-sub', Input=calcvel)
cellpointodatavelsub.CellDataArraytoprocess = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'velsub', 'vtkGhostType']

# create a new 'Calculator'
vmag = Calculator(registrationName='vmag', Input=cellpointodatavelsub)
vmag.ResultArrayName = 'vmag-subset'
vmag.Function = 'sqrt(velsub_X*velsub_X+velsub_Y*velsub_Y+velsub_Z*velsub_Z)'

# create a new 'Contour'
contour_vmag_subset = Contour(registrationName='Contour_vmag_subset', Input=vmag)
contour_vmag_subset.ContourBy = ['POINTS', 'vmag-subset']
contour_vmag_subset.Isosurfaces = [0.0076239977679756574, 0.015247994857272016, 0.022871991946568374]
contour_vmag_subset.PointMergeMethod = 'Uniform Binning'

# create a new 'Stream Tracer'
streamTracer3 = StreamTracer(registrationName='StreamTracer3', Input=calcvel,
    SeedType='Point Cloud')
streamTracer3.Vectors = ['CELLS', 'velsub']
streamTracer3.MaximumStreamlineLength = 128.0

# init the 'Point Cloud' selected for 'SeedType'
streamTracer3.SeedType.Center = [0.0, 64.0, 64.0]
streamTracer3.SeedType.NumberOfPoints = 20
streamTracer3.SeedType.Radius = 12.8

# create a new 'Tube'
vsubtube = Tube(registrationName='v-sub-tube', Input=streamTracer3)
vsubtube.Scalars = ['POINTS', 'AngularVelocity']
vsubtube.Vectors = ['POINTS', 'Normals']
vsubtube.Radius = 0.2255741901397705

# create a new 'Slice'
vz_sub_slice_y = Slice(registrationName='vz_sub_slice_y', Input=extractSubset1)
vz_sub_slice_y.SliceType = 'Plane'
vz_sub_slice_y.HyperTreeGridSlicer = 'Plane'
vz_sub_slice_y.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
vz_sub_slice_y.SliceType.Origin = [32.0, 64.00961949903078, 64.0]
vz_sub_slice_y.SliceType.Normal = [0.0, 1.0, 0.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
vz_sub_slice_y.HyperTreeGridSlicer.Origin = [32.0, 64.0, 64.0]

# create a new 'Slice'
vz_sub_slice_z = Slice(registrationName='vz_sub_slice_z', Input=extractSubset1)
vz_sub_slice_z.SliceType = 'Plane'
vz_sub_slice_z.HyperTreeGridSlicer = 'Plane'
vz_sub_slice_z.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
vz_sub_slice_z.SliceType.Origin = [32.0, 64.0, 64.0]
vz_sub_slice_z.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
vz_sub_slice_z.HyperTreeGridSlicer.Origin = [32.0, 64.0, 64.0]

# create a new 'Calculator'
calc_mag_bg = Calculator(registrationName='calc_mag_bg', Input=washmc_)
calc_mag_bg.AttributeType = 'Cell Data'
calc_mag_bg.ResultArrayName = 'mag_bg'
calc_mag_bg.Function = 'iHat*data/grid_0000000000/mag_field_x_bg+jHat*data/grid_0000000000/mag_field_y_bg+kHat*data/grid_0000000000/mag_field_z_bg'

# create a new 'Tube'
tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
tube1.Scalars = ['POINTS', 'AngularVelocity']
tube1.Vectors = ['POINTS', 'Normals']
tube1.Radius = 0.9194942289652303
tube1.RadiusFactor = 2.0

# create a new 'Slice'
denspertsubsetslice = Slice(registrationName='dens-pert-subset-slice', Input=cellpointtopertubdensesub)
denspertsubsetslice.SliceType = 'Plane'
denspertsubsetslice.HyperTreeGridSlicer = 'Plane'
denspertsubsetslice.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
denspertsubsetslice.SliceType.Origin = [2.1659297139752565, 64.0, 64.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
denspertsubsetslice.HyperTreeGridSlicer.Origin = [32.0, 64.0, 64.0]

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
slice_vz_z = Slice(registrationName='slice_vz_z', Input=calc_vel)
slice_vz_z.SliceType = 'Plane'
slice_vz_z.HyperTreeGridSlicer = 'Plane'
slice_vz_z.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice_vz_z.SliceType.Origin = [64.0, 64.0, 58.682287379454756]
slice_vz_z.SliceType.Normal = [0.0, 0.0, 1.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice_vz_z.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]

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
calcmag = Calculator(registrationName='calcmag', Input=extractSubset1)
calcmag.AttributeType = 'Cell Data'
calcmag.ResultArrayName = 'magtotsub'
calcmag.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'

# create a new 'Slice'
sliceperturbdens = Slice(registrationName='Slice-perturb-dens', Input=celtopointperturbdensslice)
sliceperturbdens.SliceType = 'Plane'
sliceperturbdens.HyperTreeGridSlicer = 'Plane'
sliceperturbdens.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
sliceperturbdens.SliceType.Origin = [0.5550021981894281, 64.0, 64.0]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
sliceperturbdens.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from washmc_
washmc_Display = Show(washmc_, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
washmc_Display.Representation = 'Outline'
washmc_Display.ColorArrayName = [None, '']
washmc_Display.SelectTCoordArray = 'None'
washmc_Display.SelectNormalArray = 'None'
washmc_Display.SelectTangentArray = 'None'
washmc_Display.OSPRayScaleFunction = 'PiecewiseFunction'
washmc_Display.SelectOrientationVectors = 'None'
washmc_Display.ScaleFactor = 12.8
washmc_Display.SelectScaleArray = 'None'
washmc_Display.GlyphType = 'Arrow'
washmc_Display.GlyphTableIndexArray = 'None'
washmc_Display.GaussianRadius = 0.64
washmc_Display.SetScaleArray = [None, '']
washmc_Display.ScaleTransferFunction = 'PiecewiseFunction'
washmc_Display.OpacityArray = [None, '']
washmc_Display.OpacityTransferFunction = 'PiecewiseFunction'
washmc_Display.DataAxesGrid = 'GridAxesRepresentation'
washmc_Display.PolarAxes = 'PolarAxesRepresentation'
washmc_Display.ScalarOpacityUnitDistance = 1.7320508075688772
washmc_Display.OpacityArrayName = ['CELLS', 'vtkGhostType']
washmc_Display.SliceFunction = 'Plane'
washmc_Display.Slice = 64

# init the 'Plane' selected for 'SliceFunction'
washmc_Display.SliceFunction.Origin = [64.0, 64.0, 64.0]

# show data from calcmag
calcmagDisplay = Show(calcmag, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
calcmagDisplay.Representation = 'Outline'
calcmagDisplay.ColorArrayName = [None, '']
calcmagDisplay.SelectTCoordArray = 'None'
calcmagDisplay.SelectNormalArray = 'None'
calcmagDisplay.SelectTangentArray = 'None'
calcmagDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
calcmagDisplay.SelectOrientationVectors = 'magtotsub'
calcmagDisplay.ScaleFactor = 12.8
calcmagDisplay.SelectScaleArray = 'None'
calcmagDisplay.GlyphType = 'Arrow'
calcmagDisplay.GlyphTableIndexArray = 'None'
calcmagDisplay.GaussianRadius = 0.64
calcmagDisplay.SetScaleArray = [None, '']
calcmagDisplay.ScaleTransferFunction = 'PiecewiseFunction'
calcmagDisplay.OpacityArray = [None, '']
calcmagDisplay.OpacityTransferFunction = 'PiecewiseFunction'
calcmagDisplay.DataAxesGrid = 'GridAxesRepresentation'
calcmagDisplay.PolarAxes = 'PolarAxesRepresentation'
calcmagDisplay.ScalarOpacityUnitDistance = 1.88988157484231
calcmagDisplay.OpacityArrayName = ['CELLS', 'data/grid_0000000000/density_bg']
calcmagDisplay.SliceFunction = 'Plane'
calcmagDisplay.Slice = 64

# init the 'Plane' selected for 'SliceFunction'
calcmagDisplay.SliceFunction.Origin = [32.0, 64.0, 64.0]

# show data from cellpointodatavelsub
cellpointodatavelsubDisplay = Show(cellpointodatavelsub, renderView1, 'UniformGridRepresentation')

# trace defaults for the display properties.
cellpointodatavelsubDisplay.Representation = 'Outline'
cellpointodatavelsubDisplay.ColorArrayName = [None, '']
cellpointodatavelsubDisplay.SelectTCoordArray = 'None'
cellpointodatavelsubDisplay.SelectNormalArray = 'None'
cellpointodatavelsubDisplay.SelectTangentArray = 'None'
cellpointodatavelsubDisplay.OSPRayScaleArray = 'data/grid_0000000000/density_bg'
cellpointodatavelsubDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
cellpointodatavelsubDisplay.SelectOrientationVectors = 'velsub'
cellpointodatavelsubDisplay.ScaleFactor = 12.8
cellpointodatavelsubDisplay.SelectScaleArray = 'None'
cellpointodatavelsubDisplay.GlyphType = 'Arrow'
cellpointodatavelsubDisplay.GlyphTableIndexArray = 'None'
cellpointodatavelsubDisplay.GaussianRadius = 0.64
cellpointodatavelsubDisplay.SetScaleArray = ['POINTS', 'data/grid_0000000000/density_bg']
cellpointodatavelsubDisplay.ScaleTransferFunction = 'PiecewiseFunction'
cellpointodatavelsubDisplay.OpacityArray = ['POINTS', 'data/grid_0000000000/density_bg']
cellpointodatavelsubDisplay.OpacityTransferFunction = 'PiecewiseFunction'
cellpointodatavelsubDisplay.DataAxesGrid = 'GridAxesRepresentation'
cellpointodatavelsubDisplay.PolarAxes = 'PolarAxesRepresentation'
cellpointodatavelsubDisplay.ScalarOpacityUnitDistance = 1.88988157484231
cellpointodatavelsubDisplay.OpacityArrayName = ['POINTS', 'data/grid_0000000000/density_bg']
cellpointodatavelsubDisplay.SliceFunction = 'Plane'
cellpointodatavelsubDisplay.Slice = 64

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellpointodatavelsubDisplay.ScaleTransferFunction.Points = [0.0001, 0.0, 0.5, 0.0, 0.00019797125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellpointodatavelsubDisplay.OpacityTransferFunction.Points = [0.0001, 0.0, 0.5, 0.0, 0.00019797125, 1.0, 0.5, 0.0]

# init the 'Plane' selected for 'SliceFunction'
cellpointodatavelsubDisplay.SliceFunction.Origin = [32.0, 64.0, 64.0]

# show data from vsubtube
vsubtubeDisplay = Show(vsubtube, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'velsub'
velsubLUT = GetColorTransferFunction('velsub')
velsubLUT.RGBPoints = [0.00014150865986141701, 0.231373, 0.298039, 0.752941, 0.14738280301229045, 0.865003, 0.865003, 0.865003, 0.29462409736471945, 0.705882, 0.0156863, 0.14902]
velsubLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
vsubtubeDisplay.Representation = 'Surface'
vsubtubeDisplay.ColorArrayName = ['POINTS', 'velsub']
vsubtubeDisplay.LookupTable = velsubLUT
vsubtubeDisplay.SelectTCoordArray = 'None'
vsubtubeDisplay.SelectNormalArray = 'TubeNormals'
vsubtubeDisplay.SelectTangentArray = 'None'
vsubtubeDisplay.OSPRayScaleArray = 'AngularVelocity'
vsubtubeDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
vsubtubeDisplay.SelectOrientationVectors = 'Normals'
vsubtubeDisplay.ScaleFactor = 12.999537837505342
vsubtubeDisplay.SelectScaleArray = 'AngularVelocity'
vsubtubeDisplay.GlyphType = 'Arrow'
vsubtubeDisplay.GlyphTableIndexArray = 'AngularVelocity'
vsubtubeDisplay.GaussianRadius = 0.6499768918752671
vsubtubeDisplay.SetScaleArray = ['POINTS', 'AngularVelocity']
vsubtubeDisplay.ScaleTransferFunction = 'PiecewiseFunction'
vsubtubeDisplay.OpacityArray = ['POINTS', 'AngularVelocity']
vsubtubeDisplay.OpacityTransferFunction = 'PiecewiseFunction'
vsubtubeDisplay.DataAxesGrid = 'GridAxesRepresentation'
vsubtubeDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
vsubtubeDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
vsubtubeDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from denspertsubsetslice
denspertsubsetsliceDisplay = Show(denspertsubsetslice, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'datagrid_0000000000density_pert'
datagrid_0000000000density_pertLUT = GetColorTransferFunction('datagrid_0000000000density_pert')
datagrid_0000000000density_pertLUT.RGBPoints = [-2.5424809000484024e-06, 0.231373, 0.298039, 0.752941, -1.0790307728032502e-07, 0.865003, 0.865003, 0.865003, 2.3266747454877524e-06, 0.705882, 0.0156863, 0.14902]
datagrid_0000000000density_pertLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
denspertsubsetsliceDisplay.Representation = 'Surface'
denspertsubsetsliceDisplay.ColorArrayName = ['POINTS', 'data/grid_0000000000/density_pert']
denspertsubsetsliceDisplay.LookupTable = datagrid_0000000000density_pertLUT
denspertsubsetsliceDisplay.SelectTCoordArray = 'None'
denspertsubsetsliceDisplay.SelectNormalArray = 'None'
denspertsubsetsliceDisplay.SelectTangentArray = 'None'
denspertsubsetsliceDisplay.OSPRayScaleArray = 'data/grid_0000000000/density_bg'
denspertsubsetsliceDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
denspertsubsetsliceDisplay.SelectOrientationVectors = 'None'
denspertsubsetsliceDisplay.ScaleFactor = 12.8
denspertsubsetsliceDisplay.SelectScaleArray = 'None'
denspertsubsetsliceDisplay.GlyphType = 'Arrow'
denspertsubsetsliceDisplay.GlyphTableIndexArray = 'None'
denspertsubsetsliceDisplay.GaussianRadius = 0.64
denspertsubsetsliceDisplay.SetScaleArray = ['POINTS', 'data/grid_0000000000/density_bg']
denspertsubsetsliceDisplay.ScaleTransferFunction = 'PiecewiseFunction'
denspertsubsetsliceDisplay.OpacityArray = ['POINTS', 'data/grid_0000000000/density_bg']
denspertsubsetsliceDisplay.OpacityTransferFunction = 'PiecewiseFunction'
denspertsubsetsliceDisplay.DataAxesGrid = 'GridAxesRepresentation'
denspertsubsetsliceDisplay.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
denspertsubsetsliceDisplay.ScaleTransferFunction.Points = [0.0001, 0.0, 0.5, 0.0, 0.00019797125, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
denspertsubsetsliceDisplay.OpacityTransferFunction.Points = [0.0001, 0.0, 0.5, 0.0, 0.00019797125, 1.0, 0.5, 0.0]

# show data from contour_vmag_subset
contour_vmag_subsetDisplay = Show(contour_vmag_subset, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'datagrid_0000000000velocity_z'
datagrid_0000000000velocity_zLUT = GetColorTransferFunction('datagrid_0000000000velocity_z')
datagrid_0000000000velocity_zLUT.RGBPoints = [-0.006706429541863223, 0.231373, 0.298039, 0.752941, 0.0005818509768697562, 0.865003, 0.865003, 0.865003, 0.007870131495602735, 0.705882, 0.0156863, 0.14902]
datagrid_0000000000velocity_zLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour_vmag_subsetDisplay.Representation = 'Surface'
contour_vmag_subsetDisplay.ColorArrayName = ['POINTS', 'data/grid_0000000000/velocity_z']
contour_vmag_subsetDisplay.LookupTable = datagrid_0000000000velocity_zLUT
contour_vmag_subsetDisplay.Opacity = 0.49
contour_vmag_subsetDisplay.SelectTCoordArray = 'None'
contour_vmag_subsetDisplay.SelectNormalArray = 'None'
contour_vmag_subsetDisplay.SelectTangentArray = 'None'
contour_vmag_subsetDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
contour_vmag_subsetDisplay.SelectOrientationVectors = 'None'
contour_vmag_subsetDisplay.ScaleFactor = -2.0000000000000002e+298
contour_vmag_subsetDisplay.SelectScaleArray = 'None'
contour_vmag_subsetDisplay.GlyphType = 'Arrow'
contour_vmag_subsetDisplay.GlyphTableIndexArray = 'None'
contour_vmag_subsetDisplay.GaussianRadius = -1e+297
contour_vmag_subsetDisplay.SetScaleArray = [None, '']
contour_vmag_subsetDisplay.ScaleTransferFunction = 'PiecewiseFunction'
contour_vmag_subsetDisplay.OpacityArray = [None, '']
contour_vmag_subsetDisplay.OpacityTransferFunction = 'PiecewiseFunction'
contour_vmag_subsetDisplay.DataAxesGrid = 'GridAxesRepresentation'
contour_vmag_subsetDisplay.PolarAxes = 'PolarAxesRepresentation'

# setup the color legend parameters for each legend in this view

# get color legend/bar for datagrid_0000000000velocity_zLUT in view renderView1
datagrid_0000000000velocity_zLUTColorBar = GetScalarBar(datagrid_0000000000velocity_zLUT, renderView1)
datagrid_0000000000velocity_zLUTColorBar.WindowLocation = 'LowerLeftCorner'
datagrid_0000000000velocity_zLUTColorBar.Position = [0.006779661016949152, 0.10640495867768596]
datagrid_0000000000velocity_zLUTColorBar.Title = 'Vz'
datagrid_0000000000velocity_zLUTColorBar.ComponentTitle = ''

# set color bar visibility
datagrid_0000000000velocity_zLUTColorBar.Visibility = 1

# get color legend/bar for datagrid_0000000000density_pertLUT in view renderView1
datagrid_0000000000density_pertLUTColorBar = GetScalarBar(datagrid_0000000000density_pertLUT, renderView1)
datagrid_0000000000density_pertLUTColorBar.WindowLocation = 'UpperLeftCorner'
datagrid_0000000000density_pertLUTColorBar.Title = 'dens_perturb'
datagrid_0000000000density_pertLUTColorBar.ComponentTitle = ''

# set color bar visibility
datagrid_0000000000density_pertLUTColorBar.Visibility = 1

# get color legend/bar for velsubLUT in view renderView1
velsubLUTColorBar = GetScalarBar(velsubLUT, renderView1)
velsubLUTColorBar.WindowLocation = 'UpperRightCorner'
velsubLUTColorBar.Position = [0.7672955974842768, 0.6460348162475822]
velsubLUTColorBar.Title = 'v'
velsubLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
velsubLUTColorBar.Visibility = 1

# show color legend
vsubtubeDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
denspertsubsetsliceDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
contour_vmag_subsetDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'datagrid_0000000000velocity_z'
datagrid_0000000000velocity_zPWF = GetOpacityTransferFunction('datagrid_0000000000velocity_z')
datagrid_0000000000velocity_zPWF.Points = [-0.006706429541863223, 0.0, 0.5, 0.0, 0.007870131495602735, 1.0, 0.5, 0.0]
datagrid_0000000000velocity_zPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'datagrid_0000000000density_pert'
datagrid_0000000000density_pertPWF = GetOpacityTransferFunction('datagrid_0000000000density_pert')
datagrid_0000000000density_pertPWF.Points = [-2.5424809000484024e-06, 0.0, 0.5, 0.0, 2.3266747454877524e-06, 1.0, 0.5, 0.0]
datagrid_0000000000density_pertPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'velsub'
velsubPWF = GetOpacityTransferFunction('velsub')
velsubPWF.Points = [0.00014150865986141701, 0.0, 0.5, 0.0, 0.29462409736471945, 1.0, 0.5, 0.0]
velsubPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(contour_vmag_subset)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')