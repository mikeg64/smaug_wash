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
renderView1.ViewSize = [1942, 1412]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [32.0, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [239.76251878719324, 0.640916434808301, 308.3771165833229]
renderView1.CameraFocalPoint = [4.065694001785766, 72.51882254031378, 31.142749358984677]
renderView1.CameraViewUp = [0.705407579263351, -0.24797493532912449, -0.6640094717444442]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 96.0
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
washmc_h5 = VisItPixieReader(FileName='/Users/mikegriffiths/proj/washmc-data/uni6/h5/washmc_681000.h5')
washmc_h5.Meshes = ['mesh_128x128x128']
washmc_h5.CellArrays = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'grid_left_index', 'grid_level', 'grid_parent_id', 'grid_particle_count']

# create a new 'Extract Subset'
extractSubset1 = ExtractSubset(Input=washmc_h5)
extractSubset1.VOI = [0, 64, 0, 128, 0, 128]

# create a new 'Calculator'
calculator2 = Calculator(Input=extractSubset1)
calculator2.AttributeType = 'Cell Data'
calculator2.ResultArrayName = 'etot'
calculator2.Function = 'data/grid_0000000000/internal_energy_bg + data/grid_0000000000/internal_energy_pert'

# create a new 'Cell Data to Point Data'
cellDatatoPointData4 = CellDatatoPointData(Input=calculator2)
cellDatatoPointData4.CellDataArraytoprocess = ['avtGhostZones', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'etot']

# create a new 'Bounding Ruler'
boundingRuler3 = BoundingRuler(Input=extractSubset1)
boundingRuler3.Axis = 'Z Axis'

# create a new 'Calculator'
calc_mag_bg = Calculator(Input=extractSubset1)
calc_mag_bg.AttributeType = 'Cell Data'
calc_mag_bg.ResultArrayName = 'mag_bg'
calc_mag_bg.Function = 'iHat*data/grid_0000000000/mag_field_x_bg+jHat*data/grid_0000000000/mag_field_y_bg+kHat*data/grid_0000000000/mag_field_z_bg'

# create a new 'Calculator'
calc_btot = Calculator(Input=extractSubset1)
calc_btot.AttributeType = 'Cell Data'
calc_btot.ResultArrayName = 'bt'
calc_btot.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'

# create a new 'Stream Tracer'
streamTracer2 = StreamTracer(Input=calc_btot,
    SeedType='High Resolution Line Source')
streamTracer2.Vectors = ['CELLS', 'bt']
streamTracer2.MaximumStreamlineLength = 128.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer2.SeedType.Point2 = [64.0, 128.0, 128.0]
streamTracer2.SeedType.Resolution = 13

# create a new 'Tube'
tube2 = Tube(Input=streamTracer2)
tube2.Scalars = ['POINTS', 'AngularVelocity']
tube2.Vectors = ['POINTS', 'Normals']
tube2.Radius = 0.6394941913709045

# create a new 'Cell Data to Point Data'
cellDatatoPointData3 = CellDatatoPointData(Input=calc_btot)
cellDatatoPointData3.CellDataArraytoprocess = ['avtGhostZones', 'bt', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']

# create a new 'Calculator'
calculator1 = Calculator(Input=cellDatatoPointData3)
calculator1.ResultArrayName = 'vel'
calculator1.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'

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

# create a new 'Slice'
slice5 = Slice(Input=calc_vel)
slice5.SliceType = 'Plane'
slice5.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice5.SliceType.Origin = [32.0, 64.0, 64.0]

# create a new 'Stream Tracer'
streamTracer1 = StreamTracer(Input=calc_vel,
    SeedType='High Resolution Line Source')
streamTracer1.Vectors = ['CELLS', 'vel']
streamTracer1.MaximumStreamlineLength = 103.68

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer1.SeedType.Point1 = [0.0, 32.0, 32.0]
streamTracer1.SeedType.Point2 = [0.0, 96.0, 96.0]
streamTracer1.SeedType.Resolution = 14

# create a new 'Tube'
tube1 = Tube(Input=streamTracer1)
tube1.Scalars = ['POINTS', 'Rotation']
tube1.Vectors = ['POINTS', 'vel']
tube1.RadiusFactor = 20.0

# create a new 'Slice'
slice3 = Slice(Input=calc_vel)
slice3.SliceType = 'Plane'
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [1.0, 64.0, 64.0]

# create a new 'Slice'
perturbdensslice = Slice(Input=extractSubset1)
perturbdensslice.SliceType = 'Plane'
perturbdensslice.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
perturbdensslice.SliceType.Origin = [1.5077042758428456, 64.0, 64.0]

# create a new 'Calculator'
calc_mag_perturb = Calculator(Input=extractSubset1)
calc_mag_perturb.AttributeType = 'Cell Data'
calc_mag_perturb.ResultArrayName = 'mag_perturb'
calc_mag_perturb.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'

# create a new 'Calculator'
calc_rhotot = Calculator(Input=extractSubset1)
calc_rhotot.AttributeType = 'Cell Data'
calc_rhotot.ResultArrayName = 'rhotot'
calc_rhotot.Function = 'data/grid_0000000000/density_pert+data/grid_0000000000/density_bg'

# create a new 'Contour'
contour4 = Contour(Input=cellDatatoPointData4)
contour4.ContourBy = ['POINTS', 'data/grid_0000000000/internal_energy_pert']
contour4.Isosurfaces = [50.0]
contour4.PointMergeMethod = 'Uniform Binning'

# create a new 'Bounding Ruler'
boundingRuler2 = BoundingRuler(Input=extractSubset1)
boundingRuler2.Axis = 'Y Axis'

# create a new 'Bounding Ruler'
boundingRuler1 = BoundingRuler(Input=extractSubset1)

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(Input=extractSubset1)
cellDatatoPointData1.CellDataArraytoprocess = ['avtGhostZones', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']

# create a new 'Contour'
contour1 = Contour(Input=cellDatatoPointData1)
contour1.ContourBy = ['POINTS', 'data/grid_0000000000/velocity_z']
contour1.Isosurfaces = [-0.003048754829757382]
contour1.PointMergeMethod = 'Uniform Binning'

# create a new 'Slice'
slice4 = Slice(Input=calc_btot)
slice4.SliceType = 'Plane'
slice4.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice4.SliceType.Origin = [32.0, 64.0, 64.0]

# create a new 'Glyph'
glyph1 = Glyph(Input=slice4,
    GlyphType='Arrow')
glyph1.OrientationArray = ['CELLS', 'bt']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 8.32
glyph1.GlyphTransform = 'Transform2'
glyph1.MaximumNumberOfSamplePoints = 500

# create a new 'Slice'
slice1 = Slice(Input=calc_btot)
slice1.SliceType = 'Plane'
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [32.0, 64.0, 64.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# create a new 'Stream Tracer'
streamTracer3 = StreamTracer(Input=calc_btot,
    SeedType='High Resolution Line Source')
streamTracer3.Vectors = ['CELLS', 'bt']
streamTracer3.MaximumStreamlineLength = 128.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer3.SeedType.Point1 = [0.0, 128.0, 0.0]
streamTracer3.SeedType.Point2 = [64.0, 0.0, 128.0]
streamTracer3.SeedType.Resolution = 13

# create a new 'Tube'
tube3 = Tube(Input=streamTracer3)
tube3.Scalars = ['POINTS', 'AngularVelocity']
tube3.Vectors = ['POINTS', 'Normals']
tube3.Radius = 0.7072479057312012

# create a new 'Stream Tracer'
streamTracer4 = StreamTracer(Input=calc_btot,
    SeedType='High Resolution Line Source')
streamTracer4.Vectors = ['CELLS', 'bt']
streamTracer4.MaximumStreamlineLength = 128.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer4.SeedType.Point1 = [0.0, 64.0, 0.0]
streamTracer4.SeedType.Point2 = [64.0, 64.0, 128.0]
streamTracer4.SeedType.Resolution = 13

# create a new 'Tube'
tube4 = Tube(Input=streamTracer4)
tube4.Scalars = ['POINTS', 'AngularVelocity']
tube4.Vectors = ['POINTS', 'Normals']
tube4.Radius = 0.9589157962799072

# create a new 'Slice'
slice2 = Slice(Input=calc_btot)
slice2.SliceType = 'Plane'
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [32.0, 64.0, 64.0]
slice2.SliceType.Normal = [0.0, 0.0, 1.0]

# create a new 'Glyph'
glyph2 = Glyph(Input=slice5,
    GlyphType='Arrow')
glyph2.OrientationArray = ['CELLS', 'vel']
glyph2.ScaleArray = ['POINTS', 'No scale array']
glyph2.VectorScaleMode = 'Scale by Components'
glyph2.ScaleFactor = 6.4
glyph2.GlyphTransform = 'Transform2'
glyph2.MaximumNumberOfSamplePoints = 500

# create a new 'Contour'
contour3 = Contour(Input=calculator1)
contour3.ContourBy = ['POINTS', 'data/grid_0000000000/internal_energy_pert']
contour3.Isosurfaces = [-122.54900373848508, 132.8602507251465, 388.2695051887781]
contour3.PointMergeMethod = 'Uniform Binning'

# create a new 'Stream Tracer'
streamTracer5 = StreamTracer(Input=calc_btot,
    SeedType='High Resolution Line Source')
streamTracer5.Vectors = ['CELLS', 'bt']
streamTracer5.MaximumStreamlineLength = 128.0

# init the 'High Resolution Line Source' selected for 'SeedType'
streamTracer5.SeedType.Point1 = [0.0, 0.0, 64.0]
streamTracer5.SeedType.Point2 = [64.0, 128.0, 64.0]
streamTracer5.SeedType.Resolution = 13

# create a new 'Tube'
tube5 = Tube(Input=streamTracer5)
tube5.Scalars = ['POINTS', 'AngularVelocity']
tube5.Vectors = ['POINTS', 'Normals']
tube5.Radius = 0.9882419586181641

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

# get color transfer function/color map for 'bt'
btLUT = GetColorTransferFunction('bt')
btLUT.RGBPoints = [1.05586e-70, 0.231373, 0.298039, 0.752941, 0.046257912266945055, 0.865003, 0.865003, 0.865003, 0.09251582453389011, 0.705882, 0.0156863, 0.14902]
btLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
calc_btotDisplay.Representation = 'Outline'
calc_btotDisplay.ColorArrayName = ['CELLS', 'bt']
calc_btotDisplay.LookupTable = btLUT
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

# show data from slice3
slice3Display = Show(slice3, renderView1)

# get color transfer function/color map for 'datagrid_0000000000velocity_z'
datagrid_0000000000velocity_zLUT = GetColorTransferFunction('datagrid_0000000000velocity_z')
datagrid_0000000000velocity_zLUT.RGBPoints = [-0.0060071741648935, 0.231373, 0.298039, 0.752941, 0.00031098199224094403, 0.865003, 0.865003, 0.865003, 0.006629138149375388, 0.705882, 0.0156863, 0.14902]
datagrid_0000000000velocity_zLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.ColorArrayName = ['CELLS', 'data/grid_0000000000/velocity_z']
slice3Display.LookupTable = datagrid_0000000000velocity_zLUT
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

# show data from cellDatatoPointData4
cellDatatoPointData4Display = Show(cellDatatoPointData4, renderView1)

# trace defaults for the display properties.
cellDatatoPointData4Display.Representation = 'Outline'
cellDatatoPointData4Display.ColorArrayName = ['POINTS', '']
cellDatatoPointData4Display.OSPRayScaleArray = 'etot'
cellDatatoPointData4Display.OSPRayScaleFunction = 'PiecewiseFunction'
cellDatatoPointData4Display.SelectOrientationVectors = 'None'
cellDatatoPointData4Display.ScaleFactor = 12.8
cellDatatoPointData4Display.SelectScaleArray = 'etot'
cellDatatoPointData4Display.GlyphType = 'Arrow'
cellDatatoPointData4Display.GlyphTableIndexArray = 'etot'
cellDatatoPointData4Display.GaussianRadius = 0.64
cellDatatoPointData4Display.SetScaleArray = ['POINTS', 'etot']
cellDatatoPointData4Display.ScaleTransferFunction = 'PiecewiseFunction'
cellDatatoPointData4Display.OpacityArray = ['POINTS', 'etot']
cellDatatoPointData4Display.OpacityTransferFunction = 'PiecewiseFunction'
cellDatatoPointData4Display.DataAxesGrid = 'GridAxesRepresentation'
cellDatatoPointData4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
cellDatatoPointData4Display.ScaleTransferFunction.Points = [1518927.4509962613, 0.0, 0.5, 0.0, 1519438.2695051888, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
cellDatatoPointData4Display.OpacityTransferFunction.Points = [1518927.4509962613, 0.0, 0.5, 0.0, 1519438.2695051888, 1.0, 0.5, 0.0]

# show data from contour4
contour4Display = Show(contour4, renderView1)

# get separate color transfer function/color map for 'etot'
separate_contour4Display_etotLUT = GetColorTransferFunction('etot', contour4Display, separate=True)
separate_contour4Display_etotLUT.AutomaticRescaleRangeMode = 'Never'
separate_contour4Display_etotLUT.RGBPoints = [40.0, 0.231373, 0.298039, 0.752941, 65.0, 0.865003, 0.865003, 0.865003, 90.0, 0.705882, 0.0156863, 0.14902]
separate_contour4Display_etotLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
contour4Display.Representation = 'Surface'
contour4Display.ColorArrayName = ['POINTS', 'etot']
contour4Display.LookupTable = separate_contour4Display_etotLUT
contour4Display.Opacity = 0.18
contour4Display.OSPRayScaleArray = 'etot'
contour4Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour4Display.SelectOrientationVectors = 'None'
contour4Display.ScaleFactor = 2.745428848266602
contour4Display.SelectScaleArray = 'etot'
contour4Display.GlyphType = 'Arrow'
contour4Display.GlyphTableIndexArray = 'etot'
contour4Display.GaussianRadius = 0.13727144241333009
contour4Display.SetScaleArray = ['POINTS', 'etot']
contour4Display.ScaleTransferFunction = 'PiecewiseFunction'
contour4Display.OpacityArray = ['POINTS', 'etot']
contour4Display.OpacityTransferFunction = 'PiecewiseFunction'
contour4Display.DataAxesGrid = 'GridAxesRepresentation'
contour4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour4Display.ScaleTransferFunction.Points = [1519182.875, 0.0, 0.5, 0.0, 1519438.875, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour4Display.OpacityTransferFunction.Points = [1519182.875, 0.0, 0.5, 0.0, 1519438.875, 1.0, 0.5, 0.0]

# set separate color map
contour4Display.UseSeparateColorMap = True

# show data from glyph2
glyph2Display = Show(glyph2, renderView1)

# get color transfer function/color map for 'datagrid_0000000000internal_energy_pert'
datagrid_0000000000internal_energy_pertLUT = GetColorTransferFunction('datagrid_0000000000internal_energy_pert')
datagrid_0000000000internal_energy_pertLUT.RGBPoints = [-84.069647640578, 0.231373, 0.298039, 0.752941, 152.09992654592196, 0.865003, 0.865003, 0.865003, 388.2695007324219, 0.705882, 0.0156863, 0.14902]
datagrid_0000000000internal_energy_pertLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph2Display.Representation = 'Surface'
glyph2Display.ColorArrayName = ['POINTS', 'data/grid_0000000000/internal_energy_pert']
glyph2Display.LookupTable = datagrid_0000000000internal_energy_pertLUT
glyph2Display.OSPRayScaleArray = 'avtGhostZones'
glyph2Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph2Display.SelectOrientationVectors = 'None'
glyph2Display.ScaleFactor = 14.649712657928468
glyph2Display.SelectScaleArray = 'None'
glyph2Display.GlyphType = 'Arrow'
glyph2Display.GlyphTableIndexArray = 'None'
glyph2Display.GaussianRadius = 0.7324856328964233
glyph2Display.SetScaleArray = ['POINTS', 'avtGhostZones']
glyph2Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph2Display.OpacityArray = ['POINTS', 'avtGhostZones']
glyph2Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph2Display.DataAxesGrid = 'GridAxesRepresentation'
glyph2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
glyph2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
glyph2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from tube2
tube2Display = Show(tube2, renderView1)

# get color transfer function/color map for 'bt'
btLUT_1 = GetColorTransferFunction('bt')
btLUT_1.RGBPoints = [1.05586e-70, 0.231373, 0.298039, 0.752941, 0.046257912266945055, 0.865003, 0.865003, 0.865003, 0.09251582453389011, 0.705882, 0.0156863, 0.14902]
btLUT_1.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
tube2Display.Representation = 'Surface'
tube2Display.ColorArrayName = ['POINTS', 'bt']
tube2Display.LookupTable = btLUT_1
tube2Display.OSPRayScaleArray = 'AngularVelocity'
tube2Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube2Display.SelectOrientationVectors = 'Normals'
tube2Display.ScaleFactor = 6.3952078850939875
tube2Display.SelectScaleArray = 'AngularVelocity'
tube2Display.GlyphType = 'Arrow'
tube2Display.GlyphTableIndexArray = 'AngularVelocity'
tube2Display.GaussianRadius = 0.3197603942546994
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

# show data from tube3
tube3Display = Show(tube3, renderView1)

# trace defaults for the display properties.
tube3Display.Representation = 'Surface'
tube3Display.ColorArrayName = ['POINTS', 'bt']
tube3Display.LookupTable = btLUT
tube3Display.OSPRayScaleArray = 'AngularVelocity'
tube3Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube3Display.SelectOrientationVectors = 'Normals'
tube3Display.ScaleFactor = 7.212529945373536
tube3Display.SelectScaleArray = 'AngularVelocity'
tube3Display.GlyphType = 'Arrow'
tube3Display.GlyphTableIndexArray = 'AngularVelocity'
tube3Display.GaussianRadius = 0.36062649726867674
tube3Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube3Display.ScaleTransferFunction = 'PiecewiseFunction'
tube3Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube3Display.OpacityTransferFunction = 'PiecewiseFunction'
tube3Display.DataAxesGrid = 'GridAxesRepresentation'
tube3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from tube4
tube4Display = Show(tube4, renderView1)

# trace defaults for the display properties.
tube4Display.Representation = 'Surface'
tube4Display.ColorArrayName = ['POINTS', 'bt']
tube4Display.LookupTable = btLUT
tube4Display.OSPRayScaleArray = 'AngularVelocity'
tube4Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube4Display.SelectOrientationVectors = 'Normals'
tube4Display.ScaleFactor = 9.502665233612062
tube4Display.SelectScaleArray = 'AngularVelocity'
tube4Display.GlyphType = 'Arrow'
tube4Display.GlyphTableIndexArray = 'AngularVelocity'
tube4Display.GaussianRadius = 0.47513326168060305
tube4Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube4Display.ScaleTransferFunction = 'PiecewiseFunction'
tube4Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube4Display.OpacityTransferFunction = 'PiecewiseFunction'
tube4Display.DataAxesGrid = 'GridAxesRepresentation'
tube4Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube4Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube4Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# show data from tube5
tube5Display = Show(tube5, renderView1)

# trace defaults for the display properties.
tube5Display.Representation = 'Surface'
tube5Display.ColorArrayName = ['POINTS', 'bt']
tube5Display.LookupTable = btLUT
tube5Display.OSPRayScaleArray = 'AngularVelocity'
tube5Display.OSPRayScaleFunction = 'PiecewiseFunction'
tube5Display.SelectOrientationVectors = 'Normals'
tube5Display.ScaleFactor = 10.064117527008058
tube5Display.SelectScaleArray = 'AngularVelocity'
tube5Display.GlyphType = 'Arrow'
tube5Display.GlyphTableIndexArray = 'AngularVelocity'
tube5Display.GaussianRadius = 0.5032058763504028
tube5Display.SetScaleArray = ['POINTS', 'AngularVelocity']
tube5Display.ScaleTransferFunction = 'PiecewiseFunction'
tube5Display.OpacityArray = ['POINTS', 'AngularVelocity']
tube5Display.OpacityTransferFunction = 'PiecewiseFunction'
tube5Display.DataAxesGrid = 'GridAxesRepresentation'
tube5Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
tube5Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
tube5Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for datagrid_0000000000velocity_zLUT in view renderView1
datagrid_0000000000velocity_zLUTColorBar = GetScalarBar(datagrid_0000000000velocity_zLUT, renderView1)
datagrid_0000000000velocity_zLUTColorBar.WindowLocation = 'LowerLeftCorner'
datagrid_0000000000velocity_zLUTColorBar.Position = [0.8481425702811245, 0.03976377952755906]
datagrid_0000000000velocity_zLUTColorBar.Title = 'Vz - mag slice'
datagrid_0000000000velocity_zLUTColorBar.ComponentTitle = ''

# set color bar visibility
datagrid_0000000000velocity_zLUTColorBar.Visibility = 1

# get color legend/bar for btLUT in view renderView1
btLUTColorBar = GetScalarBar(btLUT, renderView1)
btLUTColorBar.WindowLocation = 'UpperLeftCorner'
btLUTColorBar.Title = 'bt'
btLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
btLUTColorBar.Visibility = 1

# get color legend/bar for separate_contour4Display_etotLUT in view renderView1
separate_contour4Display_etotLUTColorBar = GetScalarBar(separate_contour4Display_etotLUT, renderView1)
separate_contour4Display_etotLUTColorBar.WindowLocation = 'UpperRightCorner'
separate_contour4Display_etotLUTColorBar.Title = 'etot - isosurface'
separate_contour4Display_etotLUTColorBar.ComponentTitle = ''

# set color bar visibility
separate_contour4Display_etotLUTColorBar.Visibility = 1

# get color legend/bar for btLUT_1 in view renderView1
btLUT_1ColorBar = GetScalarBar(btLUT_1, renderView1)
btLUT_1ColorBar.WindowLocation = 'UpperLeftCorner'
btLUT_1ColorBar.Title = 'bt'
btLUT_1ColorBar.ComponentTitle = 'mag - tube'

# set color bar visibility
btLUT_1ColorBar.Visibility = 1

# get color legend/bar for datagrid_0000000000internal_energy_pertLUT in view renderView1
datagrid_0000000000internal_energy_pertLUTColorBar = GetScalarBar(datagrid_0000000000internal_energy_pertLUT, renderView1)
datagrid_0000000000internal_energy_pertLUTColorBar.Title = 'Perturb Energy- Arrow'
datagrid_0000000000internal_energy_pertLUTColorBar.ComponentTitle = ''

# set color bar visibility
datagrid_0000000000internal_energy_pertLUTColorBar.Visibility = 1

# show color legend
calc_btotDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
slice3Display.SetScalarBarVisibility(renderView1, True)

# show color legend
contour4Display.SetScalarBarVisibility(renderView1, True)

# show color legend
glyph2Display.SetScalarBarVisibility(renderView1, True)

# show color legend
tube2Display.SetScalarBarVisibility(renderView1, True)

# show color legend
tube3Display.SetScalarBarVisibility(renderView1, True)

# show color legend
tube4Display.SetScalarBarVisibility(renderView1, True)

# show color legend
tube5Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'bt'
btPWF = GetOpacityTransferFunction('bt')
btPWF.Points = [1.05586e-70, 0.0, 0.5, 0.0, 0.09251582453389011, 1.0, 0.5, 0.0]
btPWF.ScalarRangeInitialized = 1

# get separate opacity transfer function/opacity map for 'etot'
separate_contour4Display_etotPWF = GetOpacityTransferFunction('etot', contour4Display, separate=True)
separate_contour4Display_etotPWF.Points = [40.0, 0.0, 0.5, 0.0, 90.0, 1.0, 0.5, 0.0]
separate_contour4Display_etotPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'bt'
btPWF_1 = GetOpacityTransferFunction('bt')
btPWF_1.Points = [1.05586e-70, 0.0, 0.5, 0.0, 0.09251582453389011, 1.0, 0.5, 0.0]
btPWF_1.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'datagrid_0000000000internal_energy_pert'
datagrid_0000000000internal_energy_pertPWF = GetOpacityTransferFunction('datagrid_0000000000internal_energy_pert')
datagrid_0000000000internal_energy_pertPWF.Points = [-84.069647640578, 0.0, 0.5, 0.0, 388.2695007324219, 1.0, 0.5, 0.0]
datagrid_0000000000internal_energy_pertPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'datagrid_0000000000velocity_z'
datagrid_0000000000velocity_zPWF = GetOpacityTransferFunction('datagrid_0000000000velocity_z')
datagrid_0000000000velocity_zPWF.Points = [-0.0060071741648935, 0.0, 0.5, 0.0, 0.006629138149375388, 1.0, 0.5, 0.0]
datagrid_0000000000velocity_zPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(extractSubset1)
# ----------------------------------------------------------------