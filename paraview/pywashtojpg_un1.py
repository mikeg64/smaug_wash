# state file generated using paraview version 5.9.0-RC3

#### import the simple module from the paraview
from paraview.simple import *

def createimage(i,renderView1):
# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

    #fname='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/washmc_310000.h5'
    #ifname='/Volumes/Shared/sp2rc2/Shared/simulations/washmc/washmc_2p5_2p5_12p5_mach180_uni1/images/washmc_310000.jpg'
    # fname='C:\\Users\\Mike\\data\\washmc-data\\uni1\\h5\\washmc_1000.h5'
    id=1000+i*20000
    fnameroot='C:\\Users\\Mike\\data\\washmc-data\\uni1\\h5\\washmc_'
    ifnameroot='C:\\Users\\Mike\\data\\washmc-data\\uni1\\images\\washmc_'
    fname=fnameroot+str(id)+'.h5'
    ifname=ifnameroot+str(id)+'.jpg'





    # create a new 'VisItPixieReader'
    washmc_ = VisItPixieReader(registrationName='washmc_*', FileName='C:\\Users\\Mike\\data\\washmc-data\\uni1\\h5\\washmc_1000.h5')
    washmc_.Meshes = ['mesh_128x128x128']
    washmc_.CellArrays = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'grid_left_index', 'grid_level', 'grid_parent_id', 'grid_particle_count']

    # create a new 'Calculator'
    calc_vel = Calculator(registrationName='calc_vel', Input=washmc_)
    calc_vel.AttributeType = 'Cell Data'
    calc_vel.ResultArrayName = 'vel'
    calc_vel.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'

    # create a new 'Calculator'
    calc_mag_pert = Calculator(registrationName='calc_mag_pert', Input=washmc_)
    calc_mag_pert.AttributeType = 'Cell Data'
    calc_mag_pert.ResultArrayName = 'mag_pert'
    calc_mag_pert.Function = 'iHat*data/grid_0000000000/mag_field_x_pert+jHat*data/grid_0000000000/mag_field_y_pert+kHat*data/grid_0000000000/mag_field_z_pert'

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

    # show data from calc_vel
    calc_velDisplay = Show(calc_vel, renderView1, 'UniformGridRepresentation')

    # get color transfer function/color map for 'vel'
    velLUT = GetColorTransferFunction('vel')
    velLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.00047400981480303543, 0.865003, 0.865003, 0.865003, 0.0009480196296060709, 0.705882, 0.0156863, 0.14902]
    velLUT.ScalarRangeInitialized = 1.0

    # get opacity transfer function/opacity map for 'vel'
    velPWF = GetOpacityTransferFunction('vel')
    velPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.0009480196296060709, 1.0, 0.5, 0.0]
    velPWF.ScalarRangeInitialized = 1

    # trace defaults for the display properties.
    calc_velDisplay.Representation = 'Outline'
    calc_velDisplay.ColorArrayName = ['CELLS', 'vel']
    calc_velDisplay.LookupTable = velLUT
    calc_velDisplay.SelectTCoordArray = 'None'
    calc_velDisplay.SelectNormalArray = 'None'
    calc_velDisplay.SelectTangentArray = 'None'
    calc_velDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    calc_velDisplay.SelectOrientationVectors = 'None'
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
    calc_velDisplay.ScalarOpacityUnitDistance = 1.7320508075688772
    calc_velDisplay.ScalarOpacityFunction = velPWF
    calc_velDisplay.OpacityArrayName = ['CELLS', 'data/grid_0000000000/density_bg']
    calc_velDisplay.SliceFunction = 'Plane'
    calc_velDisplay.Slice = 64

    # init the 'Plane' selected for 'SliceFunction'
    calc_velDisplay.SliceFunction.Origin = [64.0, 64.0, 64.0]

    # show data from calc_mag_bg
    calc_mag_bgDisplay = Show(calc_mag_bg, renderView1, 'UniformGridRepresentation')

    # trace defaults for the display properties.
    calc_mag_bgDisplay.Representation = 'Outline'
    calc_mag_bgDisplay.ColorArrayName = [None, '']
    calc_mag_bgDisplay.SelectTCoordArray = 'None'
    calc_mag_bgDisplay.SelectNormalArray = 'None'
    calc_mag_bgDisplay.SelectTangentArray = 'None'
    calc_mag_bgDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    calc_mag_bgDisplay.SelectOrientationVectors = 'None'
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
    calc_mag_bgDisplay.ScalarOpacityUnitDistance = 1.7320508075688772
    calc_mag_bgDisplay.OpacityArrayName = ['CELLS', 'data/grid_0000000000/density_bg']
    calc_mag_bgDisplay.SliceFunction = 'Plane'
    calc_mag_bgDisplay.Slice = 64

    # init the 'Plane' selected for 'SliceFunction'
    calc_mag_bgDisplay.SliceFunction.Origin = [64.0, 64.0, 64.0]

    # show data from calc_mag_pert
    calc_mag_pertDisplay = Show(calc_mag_pert, renderView1, 'UniformGridRepresentation')

    # trace defaults for the display properties.
    calc_mag_pertDisplay.Representation = 'Outline'
    calc_mag_pertDisplay.ColorArrayName = [None, '']
    calc_mag_pertDisplay.SelectTCoordArray = 'None'
    calc_mag_pertDisplay.SelectNormalArray = 'None'
    calc_mag_pertDisplay.SelectTangentArray = 'None'
    calc_mag_pertDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    calc_mag_pertDisplay.SelectOrientationVectors = 'calc_mag_pert'
    calc_mag_pertDisplay.ScaleFactor = 12.8
    calc_mag_pertDisplay.SelectScaleArray = 'None'
    calc_mag_pertDisplay.GlyphType = 'Arrow'
    calc_mag_pertDisplay.GlyphTableIndexArray = 'None'
    calc_mag_pertDisplay.GaussianRadius = 0.64
    calc_mag_pertDisplay.SetScaleArray = [None, '']
    calc_mag_pertDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    calc_mag_pertDisplay.OpacityArray = [None, '']
    calc_mag_pertDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    calc_mag_pertDisplay.DataAxesGrid = 'GridAxesRepresentation'
    calc_mag_pertDisplay.PolarAxes = 'PolarAxesRepresentation'
    calc_mag_pertDisplay.ScalarOpacityUnitDistance = 1.7320508075688772
    calc_mag_pertDisplay.OpacityArrayName = ['CELLS', 'calc_mag_pert']
    calc_mag_pertDisplay.SliceFunction = 'Plane'
    calc_mag_pertDisplay.Slice = 64

    # init the 'Plane' selected for 'SliceFunction'
    calc_mag_pertDisplay.SliceFunction.Origin = [64.0, 64.0, 64.0]

    # show data from calc_mag
    calc_magDisplay = Show(calc_mag, renderView1, 'UniformGridRepresentation')

    # trace defaults for the display properties.
    calc_magDisplay.Representation = 'Outline'
    calc_magDisplay.ColorArrayName = [None, '']
    calc_magDisplay.SelectTCoordArray = 'None'
    calc_magDisplay.SelectNormalArray = 'None'
    calc_magDisplay.SelectTangentArray = 'None'
    calc_magDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
    calc_magDisplay.SelectOrientationVectors = 'None'
    calc_magDisplay.ScaleFactor = 12.8
    calc_magDisplay.SelectScaleArray = 'None'
    calc_magDisplay.GlyphType = 'Arrow'
    calc_magDisplay.GlyphTableIndexArray = 'None'
    calc_magDisplay.GaussianRadius = 0.64
    calc_magDisplay.SetScaleArray = [None, '']
    calc_magDisplay.ScaleTransferFunction = 'PiecewiseFunction'
    calc_magDisplay.OpacityArray = [None, '']
    calc_magDisplay.OpacityTransferFunction = 'PiecewiseFunction'
    calc_magDisplay.DataAxesGrid = 'GridAxesRepresentation'
    calc_magDisplay.PolarAxes = 'PolarAxesRepresentation'
    calc_magDisplay.ScalarOpacityUnitDistance = 1.7320508075688772
    calc_magDisplay.OpacityArrayName = ['CELLS', 'data/grid_0000000000/density_bg']
    calc_magDisplay.SliceFunction = 'Plane'
    calc_magDisplay.Slice = 64

    # init the 'Plane' selected for 'SliceFunction'
    calc_magDisplay.SliceFunction.Origin = [64.0, 64.0, 64.0]


    # create a new 'Slice'
    slice2 = Slice(registrationName='Slice2', Input=calc_vel)
    slice2.SliceType = 'Plane'
    slice2.HyperTreeGridSlicer = 'Plane'
    slice2.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice2.SliceType.Origin = [3.7320650932642336, 64.0, 64.0]

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice2.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]


    # show data from slice2
    slice2Display = Show(slice2, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    slice2Display.Representation = 'Surface'
    slice2Display.ColorArrayName = ['CELLS', 'vel']
    slice2Display.LookupTable = velLUT
    slice2Display.SelectTCoordArray = 'None'
    slice2Display.SelectNormalArray = 'None'
    slice2Display.SelectTangentArray = 'None'
    slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
    slice2Display.SelectOrientationVectors = 'vel'
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

    # create a new 'Slice'
    slice3 = Slice(registrationName='Slice3', Input=calc_vel)
    slice3.SliceType = 'Plane'
    slice3.HyperTreeGridSlicer = 'Plane'
    slice3.SliceOffsetValues = [0.0]

    # init the 'Plane' selected for 'SliceType'
    slice3.SliceType.Origin = [58.74124112428019, 64.0, 64.0]

    # init the 'Plane' selected for 'HyperTreeGridSlicer'
    slice3.HyperTreeGridSlicer.Origin = [64.0, 64.0, 64.0]




    # show data from slice3
    slice3Display = Show(slice3, renderView1, 'GeometryRepresentation')

    # trace defaults for the display properties.
    slice3Display.Representation = 'Surface'
    slice3Display.ColorArrayName = ['CELLS', 'vel']
    slice3Display.LookupTable = velLUT
    slice3Display.SelectTCoordArray = 'None'
    slice3Display.SelectNormalArray = 'None'
    slice3Display.SelectTangentArray = 'None'
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



    # create a new 'Stream Tracer'
    streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=calc_mag,
        SeedType='Point Cloud')
    streamTracer1.Vectors = ['CELLS', 'magtot']
    streamTracer1.MaximumStreamlineLength = 128.0

    # init the 'Point Cloud' selected for 'SeedType'
    streamTracer1.SeedType.Center = [16.293325440438153, 61.02467013937933, 63.958468490532425]
    streamTracer1.SeedType.NumberOfPoints = 33
    streamTracer1.SeedType.Radius = 32.0   
        
    # create a new 'Tube'
    tube1 = Tube(registrationName='Tube1', Input=streamTracer1)
    tube1.Scalars = ['POINTS', 'AngularVelocity']
    tube1.Vectors = ['POINTS', 'Normals']
    tube1.Radius = 1.2798048502672463
    

    # show data from tube1
    tube1Display = Show(tube1, renderView1, 'GeometryRepresentation')

    # get color transfer function/color map for 'magtot'
    magtotLUT = GetColorTransferFunction('magtot')
    magtotLUT.RGBPoints = [1.2442459703157378e-75, 0.231373, 0.298039, 0.752941, 0.0446031, 0.865003, 0.865003, 0.865003, 0.0892062, 0.705882, 0.0156863, 0.14902]
    magtotLUT.ScalarRangeInitialized = 1.0

    # trace defaults for the display properties.
    tube1Display.Representation = 'Surface'
    tube1Display.ColorArrayName = ['POINTS', 'magtot']
    tube1Display.LookupTable = magtotLUT
    tube1Display.SelectTCoordArray = 'None'
    tube1Display.SelectNormalArray = 'TubeNormals'
    tube1Display.SelectTangentArray = 'None'
    tube1Display.OSPRayScaleArray = 'AngularVelocity'
    tube1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    tube1Display.SelectOrientationVectors = 'Normals'
    tube1Display.ScaleFactor = 12.798049630131572
    tube1Display.SelectScaleArray = 'AngularVelocity'
    tube1Display.GlyphType = 'Arrow'
    tube1Display.GlyphTableIndexArray = 'AngularVelocity'
    tube1Display.GaussianRadius = 0.6399024815065787
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

    # setup the color legend parameters for each legend in this view

    # get color legend/bar for magtotLUT in view renderView1
    magtotLUTColorBar = GetScalarBar(magtotLUT, renderView1)
    magtotLUTColorBar.Title = 'magtot'
    magtotLUTColorBar.ComponentTitle = 'Magnitude'

    # set color bar visibility
    magtotLUTColorBar.Visibility = 1

    # get color legend/bar for velLUT in view renderView1
    velLUTColorBar = GetScalarBar(velLUT, renderView1)
    velLUTColorBar.WindowLocation = 'UpperRightCorner'
    velLUTColorBar.Title = 'vel'
    velLUTColorBar.ComponentTitle = 'Magnitude'

    # set color bar visibility
    velLUTColorBar.Visibility = 1

    # show color legend
    calc_velDisplay.SetScalarBarVisibility(renderView1, True)

    # show color legend
    slice2Display.SetScalarBarVisibility(renderView1, True)

    # show color legend
    slice3Display.SetScalarBarVisibility(renderView1, True)

    # show color legend
    tube1Display.SetScalarBarVisibility(renderView1, True)

    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------

    # get opacity transfer function/opacity map for 'magtot'
    magtotPWF = GetOpacityTransferFunction('magtot')
    magtotPWF.Points = [1.2442459703157378e-75, 0.0, 0.5, 0.0, 0.0892062, 1.0, 0.5, 0.0]
    magtotPWF.ScalarRangeInitialized = 1


    # ----------------------------------------------------------------
    # finally, restore active source
    #SetActiveSource(tube1)
    # ----------------------------------------------------------------
    
    render_view = paraview.simple.GetActiveView()
    paraview.simple.SaveScreenshot(ifname, render_view) 



    # ----------------------------------------------------------------
    # setup extractors
    # ----------------------------------------------------------------

    # create extractor
    ##jPG1 = CreateExtractor('JPG', renderView1, registrationName='JPG1')
    # trace defaults for the extractor.
    # init the 'JPG' selected for 'Writer'
    ##jPG1.Writer.FileName = 'RenderView1_%.6ts%cm.jpg'
    ##jPG1.Writer.ImageResolution = [590, 240]
    ##jPG1.Writer.Format = 'JPEG'

#### disable automatic camera reset on 'Show'
#paraview.simple._DisableFirstRenderCameraReset()

def ResetSession():
    pxm = servermanager.ProxyManager()
    pxm.UnRegisterProxies()
    del pxm
    Disconnect()
    Connect()










#for i in range(1,64):
for i in range(0,64):
    # ----------------------------------------------------------------
    # setup views used in the visualization
    # ----------------------------------------------------------------

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [590, 240]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.CenterOfRotation = [65.36662292480469, 64.0, 64.0]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [295.54135931262795, -219.38643721913917, -165.75795257942997]
    renderView1.CameraFocalPoint = [65.36662292480476, 63.99999999999978, 63.99999999999984]
    renderView1.CameraViewUp = [0.8454995752878751, 0.3993345879722615, 0.3544888644753838]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 111.64584807592982
    renderView1.BackEnd = 'OSPRay raycaster'
    renderView1.OSPRayMaterialLibrary = materialLibrary1

    SetActiveView(None)

    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------

    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView1)
    layout1.SetSize(590, 240)

    # ----------------------------------------------------------------
    # restore active view
    SetActiveView(renderView1)
    # ----------------------------------------------------------------
    createimage(i, renderView1) 
    for j in range(0, 10):
        ResetSession()
        servermanager.LoadState("C:\\Users\\Mike\\temp\\sample.pvsm")
        renderView=SetActiveView(GetRenderView())
        Render()   




# ----------------------------------------------------------------
# restore active source
#SetActiveSource(jPG1)
# ----------------------------------------------------------------


