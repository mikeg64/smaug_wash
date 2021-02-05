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
    #id=1000+i*20000
    id=1000+i*1000
    #id=621000+i*1000
    #fnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/h5/washmc_'
    #ifnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/images/washmc_'
    
    
    fnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/h5/washmc_'
    ifnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/images-kink-y/washmc_'
    
    fname=fnameroot+str(id)+'.h5'
    ifname=ifnameroot+str(id)+'.jpg'
    
    
    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------
    
    # create a new 'VisItPixieReader'
    washmc_741000h5 = VisItPixieReader(FileName=fname)
    washmc_741000h5.Meshes = ['mesh_128x128x128']
    washmc_741000h5.CellArrays = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'grid_left_index', 'grid_level', 'grid_parent_id', 'grid_particle_count']


    #newhere
    
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
    
    # create a new 'Slice'
    slice3 = Slice(Input=calc_vel)
    slice3.SliceType = 'Plane'
    slice3.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice3.SliceType.Origin = [1.0, 64.0, 64.0]
    
    # create a new 'Stream Tracer'
    streamTracer1 = StreamTracer(Input=calc_vel,
        SeedType='High Resolution Line Source')
    streamTracer1.Vectors = ['CELLS', 'vel']
    streamTracer1.MaximumStreamlineLength = 228.0
    
    # init the 'High Resolution Line Source' selected for 'SeedType'
    streamTracer1.SeedType.Point1 = [0.0, 32.0, 32.0]
    streamTracer1.SeedType.Point2 = [0.0, 96.0, 96.0]
    streamTracer1.SeedType.Resolution = 7
    
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
    
    # create a new 'Tube'
    tube1 = Tube(Input=streamTracer1)
    tube1.Scalars = ['POINTS', 'AngularVelocity']
    tube1.Vectors = ['POINTS', 'Normals']
    
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
    
    # show data from slice2
    slice2Display = Show(slice2, renderView1)
    
    # get color transfer function/color map for 'bt'
    btLUT = GetColorTransferFunction('bt')
    btLUT.RGBPoints = [1.05586e-70, 0.231373, 0.298039, 0.752941, 0.046257912266945055, 0.865003, 0.865003, 0.865003, 0.09251582453389011, 0.705882, 0.0156863, 0.14902]
    btLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    slice2Display.Representation = 'Surface'
    slice2Display.ColorArrayName = ['CELLS', 'bt']
    slice2Display.LookupTable = btLUT
    slice2Display.Opacity = 0.47
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
    slice2Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    slice3Display.SetScalarBarVisibility(renderView1, True)
    
    
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
    render_view=renderView1
    paraview.simple.SaveScreenshot(ifname, render_view) 




def ResetSession():
    pxm = servermanager.ProxyManager()
    pxm.UnRegisterProxies()
    del pxm
    Disconnect()
    Connect() 


#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()



i=0

#id=1000+i*20000
#id=1000+i*1000
#fnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/h5/washmc_'
#ifnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/images/washmc_'


fnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/h5/washmc_'
ifnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/images/washmc_'

fname=fnameroot+str(id)+'.h5'
ifname=ifnameroot+str(id)+'.jpg'






# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1632, 1270]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [31.51106783747673, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [57.70479146948316, 217.75252354016362, 204.2166958427241]
renderView1.CameraFocalPoint = [31.511067837477412, 64.00000000000057, 63.99999999999995]
renderView1.CameraViewUp = [0.9807340677925325, 0.010796897347395973, -0.1950490073770752]
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

for i in range(0,1271): 
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()
    
    # get the material library
    materialLibrary1 = GetMaterialLibrary()
    
    
    
    #I=37
    
    #id=1000+i*20000
    #fnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/h5/washmc_'
    #ifnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/images/washmc_'
    
    
    #fnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/h5/washmc_'
    #ifnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/images/washmc_'
    
    #fname=fnameroot+str(id)+'.h5'
    #ifname=ifnameroot+str(id)+'.jpg'
    



    # Create a new 'Render View'
    renderView1 = CreateView('RenderView')
    renderView1.ViewSize = [1632, 1270]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.CenterOfRotation = [32.0, 64.0, 64.0]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [85.37615508747277, 48.0910114119654, -138.60656881674353]
    renderView1.CameraFocalPoint = [20.191144261936756, 51.27394938533013, 60.33431732657975]
    renderView1.CameraViewUp = [0.9502901940124107, 0.00043527115949859845, 0.31136531229870934]
    renderView1.CameraFocalDisk = 1.0
    renderView1.CameraParallelScale = 96.0
    renderView1.BackEnd = 'OSPRay raycaster'
    renderView1.OSPRayMaterialLibrary = materialLibrary1
    
    #SetActiveView(None)
    
    # ----------------------------------------------------------------
    # setup view layouts
    # ----------------------------------------------------------------
    
    # create new layout object 'Layout #1'
    layout1 = CreateLayout(name='Layout #1')
    layout1.AssignView(0, renderView1)
    
    # ----------------------------------------------------------------
    # restore active view
    #SetActiveView(renderView1)
    # ----------------------------------------------------------------
    
    createimage(i, renderView1) 
    for j in range(0, 10):
        ResetSession()
        servermanager.LoadState("/home/cs1mkg/data/smaug_wash/paraview/sample.pvsm")
        renderView=SetActiveView(GetRenderView())
        Render()  




