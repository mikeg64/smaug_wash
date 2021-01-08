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



def createimage(i,renderView1):
    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------
    
    #fname='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/washmc_310000.h5'
    #ifname='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/images/washmc_310000.jpg'
    
    fnameroot='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni3/washmc_'
    ifnameroot='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni3/images/washmc_'
    fname=fnameroot+str(i*1000)+'.h5'
    ifname=ifnameroot+str(i*1000)+'.jpg'



    
    # create a new 'VisItPixieReader'
    washmc_h5 = VisItPixieReader(FileName=fname)
    
    # create a new 'VisItPixieReader'
    washmc_h5 = VisItPixieReader(FileName='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni3/washmc_157000.h5')
    washmc_h5.Meshes = ['mesh_128x128x128']
    washmc_h5.CellArrays = ['data/grid_0000000000/density_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']
    
    # create a new 'Calculator'
    vfieldcalc = Calculator(Input=washmc_h5)
    vfieldcalc.AttributeType = 'Cell Data'
    vfieldcalc.ResultArrayName = 'vfield'
    vfieldcalc.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'
    
    # create a new 'Calculator'
    bfieldcalc = Calculator(Input=washmc_h5)
    bfieldcalc.AttributeType = 'Cell Data'
    bfieldcalc.ResultArrayName = 'bfield'
    bfieldcalc.Function = """iHat*(data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_pert)
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
    
    # create a new 'VisItPixieReader'
    washmc_h5_1 = VisItPixieReader(FileName='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni3/washmc_180000.h5')
    washmc_h5_1.Meshes = ['mesh_128x128x128']
    washmc_h5_1.CellArrays = ['data/grid_0000000000/density_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']
    
    # create a new 'Calculator'
    vfieldcalc_1 = Calculator(Input=washmc_h5_1)
    vfieldcalc_1.AttributeType = 'Cell Data'
    vfieldcalc_1.ResultArrayName = 'vfield'
    vfieldcalc_1.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'
    
    # create a new 'Slice'
    slice2 = Slice(Input=vfieldcalc_1)
    slice2.SliceType = 'Plane'
    slice2.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice2.SliceType.Origin = [10.066587040295033, 64.0, 64.0]
    
    # create a new 'Calculator'
    bfieldcalc_1 = Calculator(Input=washmc_h5_1)
    bfieldcalc_1.AttributeType = 'Cell Data'
    bfieldcalc_1.ResultArrayName = 'bfield'
    bfieldcalc_1.Function = """iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)
    """
    
    # create a new 'Slice'
    slice1_1 = Slice(Input=bfieldcalc_1)
    slice1_1.SliceType = 'Plane'
    slice1_1.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice1_1.SliceType.Origin = [117.35696503409325, 64.0, 64.0]
    
    # create a new 'Slice'
    slice3_1 = Slice(Input=washmc_h5_1)
    slice3_1.SliceType = 'Plane'
    slice3_1.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice3_1.SliceType.Origin = [2.718475025821763, 64.0, 64.0]
    
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
    
    # create a new 'Slice'
    slice2_1 = Slice(Input=vfieldcalc)
    slice2_1.SliceType = 'Plane'
    slice2_1.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice2_1.SliceType.Origin = [10.066587040295033, 64.0, 64.0]
    
    # create a new 'Stream Tracer'
    streamTracer1_1 = StreamTracer(Input=vfieldcalc_1,
        SeedType='Point Source')
    streamTracer1_1.Vectors = ['CELLS', 'vfield']
    streamTracer1_1.MaximumStreamlineLength = 128.0
    
    # init the 'Point Source' selected for 'SeedType'
    streamTracer1_1.SeedType.Center = [13.23683034246972, 67.62323822572358, 87.4221649047337]
    streamTracer1_1.SeedType.NumberOfPoints = 5
    streamTracer1_1.SeedType.Radius = 25.6
    
    # create a new 'Tube'
    tube1_1 = Tube(Input=streamTracer1_1)
    tube1_1.Scalars = ['POINTS', 'AngularVelocity']
    tube1_1.Vectors = ['POINTS', 'Normals']
    tube1_1.Radius = 0.5861913131713867
    
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
    # show data from washmc_h5_1
    washmc_h5_1Display = Show(washmc_h5_1, renderView1)
    
    # trace defaults for the display properties.
    washmc_h5_1Display.Representation = 'Outline'
    washmc_h5_1Display.ColorArrayName = [None, '']
    washmc_h5_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    washmc_h5_1Display.SelectOrientationVectors = 'None'
    washmc_h5_1Display.ScaleFactor = 12.8
    washmc_h5_1Display.SelectScaleArray = 'None'
    washmc_h5_1Display.GlyphType = 'Arrow'
    washmc_h5_1Display.GlyphTableIndexArray = 'None'
    washmc_h5_1Display.GaussianRadius = 0.64
    washmc_h5_1Display.SetScaleArray = [None, '']
    washmc_h5_1Display.ScaleTransferFunction = 'PiecewiseFunction'
    washmc_h5_1Display.OpacityArray = [None, '']
    washmc_h5_1Display.OpacityTransferFunction = 'PiecewiseFunction'
    washmc_h5_1Display.DataAxesGrid = 'GridAxesRepresentation'
    washmc_h5_1Display.PolarAxes = 'PolarAxesRepresentation'
    
    # show data from vfieldcalc_1
    vfieldcalc_1Display = Show(vfieldcalc_1, renderView1)
    
    # trace defaults for the display properties.
    vfieldcalc_1Display.Representation = 'Outline'
    vfieldcalc_1Display.ColorArrayName = [None, '']
    vfieldcalc_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    vfieldcalc_1Display.SelectOrientationVectors = 'None'
    vfieldcalc_1Display.ScaleFactor = 12.8
    vfieldcalc_1Display.SelectScaleArray = 'None'
    vfieldcalc_1Display.GlyphType = 'Arrow'
    vfieldcalc_1Display.GlyphTableIndexArray = 'None'
    vfieldcalc_1Display.GaussianRadius = 0.64
    vfieldcalc_1Display.SetScaleArray = [None, '']
    vfieldcalc_1Display.ScaleTransferFunction = 'PiecewiseFunction'
    vfieldcalc_1Display.OpacityArray = [None, '']
    vfieldcalc_1Display.OpacityTransferFunction = 'PiecewiseFunction'
    vfieldcalc_1Display.DataAxesGrid = 'GridAxesRepresentation'
    vfieldcalc_1Display.PolarAxes = 'PolarAxesRepresentation'
    
    # show data from bfieldcalc_1
    bfieldcalc_1Display = Show(bfieldcalc_1, renderView1)
    
    # get color transfer function/color map for 'bfield'
    bfieldLUT = GetColorTransferFunction('bfield')
    bfieldLUT.RGBPoints = [3.1267867275147915e-75, 0.231373, 0.298039, 0.752941, 0.04460480621424919, 0.865003, 0.865003, 0.865003, 0.08920961242849838, 0.705882, 0.0156863, 0.14902]
    bfieldLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    bfieldcalc_1Display.Representation = 'Outline'
    bfieldcalc_1Display.ColorArrayName = ['CELLS', 'bfield']
    bfieldcalc_1Display.LookupTable = bfieldLUT
    bfieldcalc_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    bfieldcalc_1Display.SelectOrientationVectors = 'bfield'
    bfieldcalc_1Display.ScaleFactor = 12.8
    bfieldcalc_1Display.SelectScaleArray = 'None'
    bfieldcalc_1Display.GlyphType = 'Arrow'
    bfieldcalc_1Display.GlyphTableIndexArray = 'None'
    bfieldcalc_1Display.GaussianRadius = 0.64
    bfieldcalc_1Display.SetScaleArray = [None, '']
    bfieldcalc_1Display.ScaleTransferFunction = 'PiecewiseFunction'
    bfieldcalc_1Display.OpacityArray = [None, '']
    bfieldcalc_1Display.OpacityTransferFunction = 'PiecewiseFunction'
    bfieldcalc_1Display.DataAxesGrid = 'GridAxesRepresentation'
    bfieldcalc_1Display.PolarAxes = 'PolarAxesRepresentation'
    
    # show data from tube1_1
    tube1_1Display = Show(tube1_1, renderView1)
    
    # get color transfer function/color map for 'vfield'
    vfieldLUT = GetColorTransferFunction('vfield')
    vfieldLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.0012270127573967861, 0.865003, 0.865003, 0.865003, 0.0024540255147935722, 0.705882, 0.0156863, 0.14902]
    vfieldLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    tube1_1Display.Representation = 'Surface'
    tube1_1Display.ColorArrayName = ['POINTS', 'vfield']
    tube1_1Display.LookupTable = vfieldLUT
    tube1_1Display.Opacity = 0.26
    tube1_1Display.OSPRayScaleArray = 'AngularVelocity'
    tube1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    tube1_1Display.SelectOrientationVectors = 'Normals'
    tube1_1Display.ScaleFactor = 6.033758544921875
    tube1_1Display.SelectScaleArray = 'AngularVelocity'
    tube1_1Display.GlyphType = 'Arrow'
    tube1_1Display.GlyphTableIndexArray = 'AngularVelocity'
    tube1_1Display.GaussianRadius = 0.3016879272460938
    tube1_1Display.SetScaleArray = ['POINTS', 'AngularVelocity']
    tube1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
    tube1_1Display.OpacityArray = ['POINTS', 'AngularVelocity']
    tube1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
    tube1_1Display.DataAxesGrid = 'GridAxesRepresentation'
    tube1_1Display.PolarAxes = 'PolarAxesRepresentation'
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    tube1_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    tube1_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    
    # show data from slice1_1
    slice1_1Display = Show(slice1_1, renderView1)
    
    # trace defaults for the display properties.
    slice1_1Display.Representation = 'Surface'
    slice1_1Display.ColorArrayName = ['CELLS', 'bfield']
    slice1_1Display.LookupTable = bfieldLUT
    slice1_1Display.Opacity = 0.39
    slice1_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice1_1Display.SelectOrientationVectors = 'bfield'
    slice1_1Display.ScaleFactor = 12.8
    slice1_1Display.SelectScaleArray = 'None'
    slice1_1Display.GlyphType = 'Arrow'
    slice1_1Display.GlyphTableIndexArray = 'None'
    slice1_1Display.GaussianRadius = 0.64
    slice1_1Display.SetScaleArray = [None, '']
    slice1_1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice1_1Display.OpacityArray = [None, '']
    slice1_1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice1_1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice1_1Display.PolarAxes = 'PolarAxesRepresentation'
    
    # show data from slice3_1
    slice3_1Display = Show(slice3_1, renderView1)
    
    # get color transfer function/color map for 'datagrid_0000000000density_pert'
    datagrid_0000000000density_pertLUT = GetColorTransferFunction('datagrid_0000000000density_pert')
    datagrid_0000000000density_pertLUT.RGBPoints = [-1.1492035220006449e-07, 0.231373, 0.298039, 0.752941, -7.037492876403123e-10, 0.865003, 0.865003, 0.865003, 1.1351285362478386e-07, 0.705882, 0.0156863, 0.14902]
    datagrid_0000000000density_pertLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    slice3_1Display.Representation = 'Surface'
    slice3_1Display.ColorArrayName = ['CELLS', 'data/grid_0000000000/density_pert']
    slice3_1Display.LookupTable = datagrid_0000000000density_pertLUT
    slice3_1Display.Opacity = 0.37
    slice3_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice3_1Display.SelectOrientationVectors = 'None'
    slice3_1Display.ScaleFactor = 12.8
    slice3_1Display.SelectScaleArray = 'None'
    slice3_1Display.GlyphType = 'Arrow'
    slice3_1Display.GlyphTableIndexArray = 'None'
    slice3_1Display.GaussianRadius = 0.64
    slice3_1Display.SetScaleArray = [None, '']
    slice3_1Display.ScaleTransferFunction = 'PiecewiseFunction'
    slice3_1Display.OpacityArray = [None, '']
    slice3_1Display.OpacityTransferFunction = 'PiecewiseFunction'
    slice3_1Display.DataAxesGrid = 'GridAxesRepresentation'
    slice3_1Display.PolarAxes = 'PolarAxesRepresentation'
    
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
    vfieldLUTColorBar.Position = [0.8501506024096386, 0.6535433070866141]
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
    bfieldcalc_1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    tube1_1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    slice1_1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    slice3_1Display.SetScalarBarVisibility(renderView1, True)
    
    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------
    
    # get opacity transfer function/opacity map for 'datagrid_0000000000density_pert'
    datagrid_0000000000density_pertPWF = GetOpacityTransferFunction('datagrid_0000000000density_pert')
    datagrid_0000000000density_pertPWF.Points = [-1.1492035220006449e-07, 0.0, 0.5, 0.0, 1.1351285362478386e-07, 1.0, 0.5, 0.0]
    datagrid_0000000000density_pertPWF.ScalarRangeInitialized = 1
    
    # get opacity transfer function/opacity map for 'bfield'
    bfieldPWF = GetOpacityTransferFunction('bfield')
    bfieldPWF.Points = [3.1267867275147915e-75, 0.0, 0.5, 0.0, 0.08920961242849838, 1.0, 0.5, 0.0]
    bfieldPWF.ScalarRangeInitialized = 1
    
    # get opacity transfer function/opacity map for 'vfield'
    vfieldPWF = GetOpacityTransferFunction('vfield')
    vfieldPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.0024540255147935722, 1.0, 0.5, 0.0]
    vfieldPWF.ScalarRangeInitialized = 1
    
    # ----------------------------------------------------------------
    # finally, restore active source
    SetActiveSource(None)
    # ----------------------------------------------------------------
    
    # ----------------------------------------------------------------
    # finally, restore active source
    #SetActiveSource(tube1)
    # ----------------------------------------------------------------
    
    render_view = paraview.simple.GetActiveView()
    paraview.simple.SaveScreenshot(ifname, render_view)    
    
    
    
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1494, 1270]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [64.0, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [346.76520955895, -406.10808679610926, -136.1849792492555]
renderView1.CameraFocalPoint = [63.99999999999973, 63.99999999999887, 64.0000000000005]
renderView1.CameraViewUp = [0.8729284164344386, 0.41781290878025446, 0.25184986209614285]
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

for i in range(201,301):
 createimage(i, renderView1)       