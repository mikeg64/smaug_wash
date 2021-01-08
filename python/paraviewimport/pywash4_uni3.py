# state file generated using paraview version 5.7.0-RC2

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------



def createimage(i,renderView1):
    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------
    #fname='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/washmc_310000.h5'
    #ifname='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/images/washmc_310000.jpg'
    
    fnameroot='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni3/washmc_'
    ifnameroot='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni3/images/washmc_'
    fname=fnameroot+str(i*10000)+'.h5'
    ifname=ifnameroot+str(i*10000)+'.jpg'



    
    # create a new 'VisItPixieReader'
    washmc_h5 = VisItPixieReader(FileName=fname)
    washmc_h5.Meshes = ['mesh_128x128x128']
    washmc_h5.CellArrays = ['data/grid_0000000000/density_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']
    
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
    slice2.SliceType.Origin = [10.066587040295033, 64.0, 64.0]
    
    # create a new 'Stream Tracer'
    streamTracer1 = StreamTracer(Input=vfieldcalc,
        SeedType='Point Source')
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
    slice1.SliceType.Origin = [117.35696503409325, 64.0, 64.0]
    
    # create a new 'Slice'
    slice3 = Slice(Input=washmc_h5)
    slice3.SliceType = 'Plane'
    slice3.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice3.SliceType.Origin = [7.574145161647489, 64.0, 64.0]
    
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from washmc_h5
    washmc_h5Display = Show(washmc_h5, renderView1)
    
    # trace defaults for the display properties.
    washmc_h5Display.Representation = 'Outline'
    washmc_h5Display.ColorArrayName = [None, '']
    washmc_h5Display.OSPRayScaleFunction = 'PiecewiseFunction'
    washmc_h5Display.SelectOrientationVectors = 'None'
    washmc_h5Display.ScaleFactor = 12.8
    washmc_h5Display.SelectScaleArray = 'None'
    washmc_h5Display.GlyphType = 'Arrow'
    washmc_h5Display.GlyphTableIndexArray = 'None'
    washmc_h5Display.GaussianRadius = 0.64
    washmc_h5Display.SetScaleArray = [None, '']
    washmc_h5Display.ScaleTransferFunction = 'PiecewiseFunction'
    washmc_h5Display.OpacityArray = [None, '']
    washmc_h5Display.OpacityTransferFunction = 'PiecewiseFunction'
    washmc_h5Display.DataAxesGrid = 'GridAxesRepresentation'
    washmc_h5Display.PolarAxes = 'PolarAxesRepresentation'
    
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
    bfieldLUT.RGBPoints = [3.1267867275147915e-75, 0.231373, 0.298039, 0.752941, 0.04460480621424919, 0.865003, 0.865003, 0.865003, 0.08920961242849838, 0.705882, 0.0156863, 0.14902]
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
    
    # show data from streamTracer1
    streamTracer1Display = Show(streamTracer1, renderView1)
    
    # get color transfer function/color map for 'vfield'
    vfieldLUT = GetColorTransferFunction('vfield')
    vfieldLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.0012270127573967861, 0.865003, 0.865003, 0.865003, 0.0024540255147935722, 0.705882, 0.0156863, 0.14902]
    vfieldLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    streamTracer1Display.Representation = 'Surface'
    streamTracer1Display.ColorArrayName = ['POINTS', 'vfield']
    streamTracer1Display.LookupTable = vfieldLUT
    streamTracer1Display.OSPRayScaleArray = 'AngularVelocity'
    streamTracer1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    streamTracer1Display.SelectOrientationVectors = 'Normals'
    streamTracer1Display.ScaleFactor = 11.06375608444214
    streamTracer1Display.SelectScaleArray = 'AngularVelocity'
    streamTracer1Display.GlyphType = 'Arrow'
    streamTracer1Display.GlyphTableIndexArray = 'AngularVelocity'
    streamTracer1Display.GaussianRadius = 0.5531878042221069
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
    tube1Display.ColorArrayName = ['POINTS', 'vfield']
    tube1Display.LookupTable = vfieldLUT
    tube1Display.Opacity = 0.26
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
    slice1Display.Opacity = 0.39
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
    
    # show data from slice3
    slice3Display = Show(slice3, renderView1)
    
    # get color transfer function/color map for 'datagrid_0000000000density_pert'
    datagrid_0000000000density_pertLUT = GetColorTransferFunction('datagrid_0000000000density_pert')
    datagrid_0000000000density_pertLUT.RGBPoints = [-5.477533588194977e-08, 0.231373, 0.298039, 0.752941, 4.146393512803804e-10, 0.865003, 0.865003, 0.865003, 5.5604614584510534e-08, 0.705882, 0.0156863, 0.14902]
    datagrid_0000000000density_pertLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    slice3Display.Representation = 'Surface'
    slice3Display.ColorArrayName = ['CELLS', 'data/grid_0000000000/density_pert']
    slice3Display.LookupTable = datagrid_0000000000density_pertLUT
    slice3Display.Opacity = 0.37
    slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice3Display.SelectOrientationVectors = 'None'
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
    
    # get color legend/bar for datagrid_0000000000density_pertLUT in view renderView1
    datagrid_0000000000density_pertLUTColorBar = GetScalarBar(datagrid_0000000000density_pertLUT, renderView1)
    datagrid_0000000000density_pertLUTColorBar.WindowLocation = 'UpperLeftCorner'
    datagrid_0000000000density_pertLUTColorBar.Title = 'data/grid_0000000000/density_pert'
    datagrid_0000000000density_pertLUTColorBar.ComponentTitle = ''
    
    # set color bar visibility
    datagrid_0000000000density_pertLUTColorBar.Visibility = 1
    
    # show color legend
    bfieldcalcDisplay.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    streamTracer1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    tube1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    slice1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    slice3Display.SetScalarBarVisibility(renderView1, True)
    
    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------
    
    # get opacity transfer function/opacity map for 'datagrid_0000000000density_pert'
    datagrid_0000000000density_pertPWF = GetOpacityTransferFunction('datagrid_0000000000density_pert')
    datagrid_0000000000density_pertPWF.Points = [-5.477533588194977e-08, 0.0, 0.5, 0.0, 5.5604614584510534e-08, 1.0, 0.5, 0.0]
    datagrid_0000000000density_pertPWF.ScalarRangeInitialized = 1
    
    # get opacity transfer function/opacity map for 'vfield'
    vfieldPWF = GetOpacityTransferFunction('vfield')
    vfieldPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.0024540255147935722, 1.0, 0.5, 0.0]
    vfieldPWF.ScalarRangeInitialized = 1
    
    # get opacity transfer function/opacity map for 'bfield'
    bfieldPWF = GetOpacityTransferFunction('bfield')
    bfieldPWF.Points = [3.1267867275147915e-75, 0.0, 0.5, 0.0, 0.08920961242849838, 1.0, 0.5, 0.0]
    bfieldPWF.ScalarRangeInitialized = 1
    
    # ----------------------------------------------------------------
    # finally, restore active source
    SetActiveSource(tube1)
    # ----------------------------------------------------------------
    
    render_view = paraview.simple.GetActiveView()
    paraview.simple.SaveScreenshot(ifname, render_view)
    
    
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
renderView1.CameraPosition = [286.60348123922034, 192.29758386250566, -344.55443972673436]
renderView1.CameraFocalPoint = [64.00000000000021, 63.99999999999967, 63.99999999999864]
renderView1.CameraViewUp = [0.8863948313460335, -0.09545945804439104, 0.4529808989713673]
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



for i in range(1,31):
 createimage(i, renderView1)    
