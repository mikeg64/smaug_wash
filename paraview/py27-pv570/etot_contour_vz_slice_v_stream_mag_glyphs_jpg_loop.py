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
    #id=620000+i*1000
    #fnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/h5/washmc_'
    #ifnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/images/washmc_'
    
    
    fnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/h5/washmc_'
    ifnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/images-econt-vstream-bglyph/washmc_'
    
    fname=fnameroot+str(id)+'.h5'
    ifname=ifnameroot+str(id)+'.jpg'



    # ----------------------------------------------------------------
    # setup the data processing pipelines
    # ----------------------------------------------------------------
    
    # create a new 'VisItPixieReader'
    washmc_741000h5 = VisItPixieReader(FileName=fname)
    washmc_741000h5.Meshes = ['mesh_128x128x128']
    washmc_741000h5.CellArrays = ['data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'grid_left_index', 'grid_level', 'grid_parent_id', 'grid_particle_count']
    
    # create a new 'Extract Subset'
    extractSubset1 = ExtractSubset(Input=washmc_741000h5)
    extractSubset1.VOI = [0, 64, 0, 128, 0, 128]
    
    # create a new 'Calculator'
    calculator2 = Calculator(Input=extractSubset1)
    calculator2.AttributeType = 'Cell Data'
    calculator2.ResultArrayName = 'etot'
    calculator2.Function = 'data/grid_0000000000/internal_energy_bg + data/grid_0000000000/internal_energy_pert'
    
    # create a new 'Cell Data to Point Data'
    cellDatatoPointData4 = CellDatatoPointData(Input=calculator2)
    cellDatatoPointData4.CellDataArraytoprocess = ['avtGhostZones', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z', 'etot']
    
    # create a new 'Calculator'
    calc_mag_perturb = Calculator(Input=extractSubset1)
    calc_mag_perturb.AttributeType = 'Cell Data'
    calc_mag_perturb.ResultArrayName = 'mag_perturb'
    calc_mag_perturb.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'
    
    # create a new 'Bounding Ruler'
    boundingRuler3 = BoundingRuler(Input=extractSubset1)
    boundingRuler3.Axis = 'Z Axis'
    
    # create a new 'Calculator'
    calc_btot = Calculator(Input=extractSubset1)
    calc_btot.AttributeType = 'Cell Data'
    calc_btot.ResultArrayName = 'bt'
    calc_btot.Function = 'iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)'
    
    # create a new 'Cell Data to Point Data'
    cellDatatoPointData3 = CellDatatoPointData(Input=calc_btot)
    cellDatatoPointData3.CellDataArraytoprocess = ['avtGhostZones', 'bt', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']
    
    # create a new 'Calculator'
    calculator1 = Calculator(Input=cellDatatoPointData3)
    calculator1.ResultArrayName = 'vel'
    calculator1.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'
    
    # create a new 'Slice'
    slice1 = Slice(Input=calc_btot)
    slice1.SliceType = 'Plane'
    slice1.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice1.SliceType.Origin = [32.0, 64.0, 64.0]
    slice1.SliceType.Normal = [0.0, 1.0, 0.0]
    
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
    
    # create a new 'Cell Data to Point Data'
    cellDatatoPointData1 = CellDatatoPointData(Input=extractSubset1)
    cellDatatoPointData1.CellDataArraytoprocess = ['avtGhostZones', 'data/grid_0000000000/density_bg', 'data/grid_0000000000/density_pert', 'data/grid_0000000000/internal_energy_bg', 'data/grid_0000000000/internal_energy_pert', 'data/grid_0000000000/mag_field_x_bg', 'data/grid_0000000000/mag_field_x_pert', 'data/grid_0000000000/mag_field_y_bg', 'data/grid_0000000000/mag_field_y_pert', 'data/grid_0000000000/mag_field_z_bg', 'data/grid_0000000000/mag_field_z_pert', 'data/grid_0000000000/velocity_x', 'data/grid_0000000000/velocity_y', 'data/grid_0000000000/velocity_z']
    
    # create a new 'Slice'
    slice2 = Slice(Input=calc_btot)
    slice2.SliceType = 'Plane'
    slice2.SliceOffsetValues = [0.0]
    
    # init the 'Plane' selected for 'SliceType'
    slice2.SliceType.Origin = [32.0, 64.0, 64.0]
    slice2.SliceType.Normal = [0.0, 0.0, 1.0]
    
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
    
    # create a new 'Contour'
    contour4 = Contour(Input=cellDatatoPointData4)
    contour4.ContourBy = ['POINTS', 'data/grid_0000000000/internal_energy_pert']
    contour4.Isosurfaces = [132.8602507251465]
    contour4.PointMergeMethod = 'Uniform Binning'
    
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
    calc_rhotot = Calculator(Input=extractSubset1)
    calc_rhotot.AttributeType = 'Cell Data'
    calc_rhotot.ResultArrayName = 'rhotot'
    calc_rhotot.Function = 'data/grid_0000000000/density_pert+data/grid_0000000000/density_bg'
    
    # create a new 'Bounding Ruler'
    boundingRuler2 = BoundingRuler(Input=extractSubset1)
    boundingRuler2.Axis = 'Y Axis'
    
    # create a new 'Bounding Ruler'
    boundingRuler1 = BoundingRuler(Input=extractSubset1)
    
    # create a new 'Calculator'
    calc_mag_bg = Calculator(Input=extractSubset1)
    calc_mag_bg.AttributeType = 'Cell Data'
    calc_mag_bg.ResultArrayName = 'mag_bg'
    calc_mag_bg.Function = 'iHat*data/grid_0000000000/mag_field_x_bg+jHat*data/grid_0000000000/mag_field_y_bg+kHat*data/grid_0000000000/mag_field_z_bg'
    
    # create a new 'Contour'
    contour3 = Contour(Input=calculator1)
    contour3.ContourBy = ['POINTS', 'data/grid_0000000000/internal_energy_pert']
    contour3.Isosurfaces = [-122.54900373848508, 132.8602507251465, 388.2695051887781]
    contour3.PointMergeMethod = 'Uniform Binning'
    
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
    
    # ----------------------------------------------------------------
    # setup the visualization in view 'renderView1'
    # ----------------------------------------------------------------
    
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
    
    # show data from tube1
    tube1Display = Show(tube1, renderView1)
    
    # get color transfer function/color map for 'vel'
    velLUT = GetColorTransferFunction('vel')
    velLUT.RGBPoints = [-0.009208698359313743, 0.231373, 0.298039, 0.752941, 0.0007407006874036864, 0.865003, 0.865003, 0.865003, 0.010690099734121123, 0.705882, 0.0156863, 0.14902]
    velLUT.ScalarRangeInitialized = 1.0
    velLUT.VectorComponent = 2
    velLUT.VectorMode = 'Component'
    
    # trace defaults for the display properties.
    tube1Display.Representation = 'Surface'
    tube1Display.ColorArrayName = ['POINTS', 'vel']
    tube1Display.LookupTable = velLUT
    tube1Display.Opacity = 0.77
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
    
    # show data from slice3
    slice3Display = Show(slice3, renderView1)
    
    # get color transfer function/color map for 'datagrid_0000000000velocity_z'
    datagrid_0000000000velocity_zLUT = GetColorTransferFunction('datagrid_0000000000velocity_z')
    datagrid_0000000000velocity_zLUT.RGBPoints = [-0.0060071741648935, 0.231373, 0.298039, 0.752941, -0.0006513410490052137, 0.865003, 0.865003, 0.865003, 0.004704492066883072, 0.705882, 0.0156863, 0.14902]
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
    
    # show data from calculator1
    calculator1Display = Show(calculator1, renderView1)
    
    # trace defaults for the display properties.
    calculator1Display.Representation = 'Outline'
    calculator1Display.ColorArrayName = [None, '']
    calculator1Display.OSPRayScaleArray = 'avtGhostZones'
    calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    calculator1Display.SelectOrientationVectors = 'vel'
    calculator1Display.ScaleFactor = 12.8
    calculator1Display.SelectScaleArray = 'None'
    calculator1Display.GlyphType = 'Arrow'
    calculator1Display.GlyphTableIndexArray = 'None'
    calculator1Display.GaussianRadius = 0.64
    calculator1Display.SetScaleArray = ['POINTS', 'avtGhostZones']
    calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
    calculator1Display.OpacityArray = ['POINTS', 'avtGhostZones']
    calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
    calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
    calculator1Display.PolarAxes = 'PolarAxesRepresentation'
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    
    # show data from glyph1
    glyph1Display = Show(glyph1, renderView1)
    
    # get color transfer function/color map for 'datagrid_0000000000mag_field_z_pert'
    datagrid_0000000000mag_field_z_pertLUT = GetColorTransferFunction('datagrid_0000000000mag_field_z_pert')
    datagrid_0000000000mag_field_z_pertLUT.RGBPoints = [-0.00019333443705566364, 0.231373, 0.298039, 0.752941, -8.286714441748907e-07, 0.865003, 0.865003, 0.865003, 0.00019167709416731385, 0.705882, 0.0156863, 0.14902]
    datagrid_0000000000mag_field_z_pertLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    glyph1Display.Representation = 'Surface'
    glyph1Display.ColorArrayName = ['POINTS', 'data/grid_0000000000/mag_field_z_pert']
    glyph1Display.LookupTable = datagrid_0000000000mag_field_z_pertLUT
    glyph1Display.OSPRayScaleArray = 'avtGhostZones'
    glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
    glyph1Display.SelectOrientationVectors = 'None'
    glyph1Display.ScaleFactor = 14.362644004821778
    glyph1Display.SelectScaleArray = 'None'
    glyph1Display.GlyphType = 'Arrow'
    glyph1Display.GlyphTableIndexArray = 'None'
    glyph1Display.GaussianRadius = 0.7181322002410889
    glyph1Display.SetScaleArray = ['POINTS', 'avtGhostZones']
    glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
    glyph1Display.OpacityArray = ['POINTS', 'avtGhostZones']
    glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
    glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
    glyph1Display.PolarAxes = 'PolarAxesRepresentation'
    
    # init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
    glyph1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    
    # init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
    glyph1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.1757813367477812e-38, 1.0, 0.5, 0.0]
    
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
    
    # get color transfer function/color map for 'etot'
    etotLUT = GetColorTransferFunction('etot')
    etotLUT.RGBPoints = [1519182.8602507247, 0.231373, 0.298039, 0.752941, 1519310.8676253622, 0.865003, 0.865003, 0.865003, 1519438.875, 0.705882, 0.0156863, 0.14902]
    etotLUT.ScalarRangeInitialized = 1.0
    
    # trace defaults for the display properties.
    contour4Display.Representation = 'Surface'
    contour4Display.ColorArrayName = ['POINTS', 'etot']
    contour4Display.LookupTable = etotLUT
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
    
    # setup the color legend parameters for each legend in this view
    
    # get color legend/bar for datagrid_0000000000velocity_zLUT in view renderView1
    datagrid_0000000000velocity_zLUTColorBar = GetScalarBar(datagrid_0000000000velocity_zLUT, renderView1)
    datagrid_0000000000velocity_zLUTColorBar.WindowLocation = 'LowerLeftCorner'
    datagrid_0000000000velocity_zLUTColorBar.Position = [0.8481425702811245, 0.03976377952755906]
    datagrid_0000000000velocity_zLUTColorBar.Title = 'z-Component of Velocity'
    datagrid_0000000000velocity_zLUTColorBar.ComponentTitle = ''
    
    # set color bar visibility
    datagrid_0000000000velocity_zLUTColorBar.Visibility = 1
    
    # get color legend/bar for velLUT in view renderView1
    velLUTColorBar = GetScalarBar(velLUT, renderView1)
    velLUTColorBar.WindowLocation = 'UpperLeftCorner'
    velLUTColorBar.Position = [0.0021436227224008574, 0.6558073654390935]
    velLUTColorBar.Title = 'vel'
    velLUTColorBar.ComponentTitle = 'Z'
    
    # set color bar visibility
    velLUTColorBar.Visibility = 1
    
    # get color legend/bar for datagrid_0000000000mag_field_z_pertLUT in view renderView1
    datagrid_0000000000mag_field_z_pertLUTColorBar = GetScalarBar(datagrid_0000000000mag_field_z_pertLUT, renderView1)
    datagrid_0000000000mag_field_z_pertLUTColorBar.Title = 'z component perturbed B'
    datagrid_0000000000mag_field_z_pertLUTColorBar.ComponentTitle = ''
    
    # set color bar visibility
    datagrid_0000000000mag_field_z_pertLUTColorBar.Visibility = 1
    
    # get color legend/bar for etotLUT in view renderView1
    etotLUTColorBar = GetScalarBar(etotLUT, renderView1)
    etotLUTColorBar.WindowLocation = 'UpperRightCorner'
    etotLUTColorBar.Title = 'etot'
    etotLUTColorBar.ComponentTitle = ''
    
    # set color bar visibility
    etotLUTColorBar.Visibility = 1
    
    # show color legend
    tube1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    slice3Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    glyph1Display.SetScalarBarVisibility(renderView1, True)
    
    # show color legend
    contour4Display.SetScalarBarVisibility(renderView1, True)
    
    # ----------------------------------------------------------------
    # setup color maps and opacity mapes used in the visualization
    # note: the Get..() functions create a new object, if needed
    # ----------------------------------------------------------------
    
    # get opacity transfer function/opacity map for 'datagrid_0000000000mag_field_z_pert'
    datagrid_0000000000mag_field_z_pertPWF = GetOpacityTransferFunction('datagrid_0000000000mag_field_z_pert')
    datagrid_0000000000mag_field_z_pertPWF.Points = [-0.00019333443705566364, 0.0, 0.5, 0.0, 0.00019167709416731385, 1.0, 0.5, 0.0]
    datagrid_0000000000mag_field_z_pertPWF.ScalarRangeInitialized = 1
    
    # get opacity transfer function/opacity map for 'datagrid_0000000000velocity_z'
    datagrid_0000000000velocity_zPWF = GetOpacityTransferFunction('datagrid_0000000000velocity_z')
    datagrid_0000000000velocity_zPWF.Points = [-0.0060071741648935, 0.0, 0.5, 0.0, 0.004704492066883072, 1.0, 0.5, 0.0]
    datagrid_0000000000velocity_zPWF.ScalarRangeInitialized = 1
    
    # get opacity transfer function/opacity map for 'etot'
    etotPWF = GetOpacityTransferFunction('etot')
    etotPWF.Points = [1519182.8602507247, 0.0, 0.5, 0.0, 1519438.875, 1.0, 0.5, 0.0]
    etotPWF.ScalarRangeInitialized = 1
    
    # get opacity transfer function/opacity map for 'vel'
    velPWF = GetOpacityTransferFunction('vel')
    velPWF.Points = [-0.009208698359313743, 0.0, 0.5, 0.0, 0.010690099734121123, 1.0, 0.5, 0.0]
    velPWF.ScalarRangeInitialized = 1
    
    # ----------------------------------------------------------------
    # finally, restore active source
    SetActiveSource(washmc_741000h5)
    # ----------------------------------------------------------------


    # ----------------------------------------------------------------
    render_view=renderView1
    paraview.simple.SaveScreenshot(ifname, render_view) 




















#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2348, 1412]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [32.0, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [254.95366954580783, -71.57150480114426, 224.8722247973803]
renderView1.CameraFocalPoint = [32.00000000000057, 63.99999999999976, 64.00000000000047]
renderView1.CameraViewUp = [0.6039450201427604, 0.04925431385434736, -0.7955026242643694]
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



i=0

#id=1000+i*20000
#id=1000+i*1000
#fnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/h5/washmc_'
#ifnameroot='/Users/mikegriffiths/proj/washmc-data/uni6/images/washmc_'


fnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/h5/washmc_'
ifnameroot='/home/cs1mkg/fastdata/smaug_wash/washmc_2p5_2p5_12p5_mach180_uni6/images-econt-vstream-bglyph/washmc_'

fname=fnameroot+str(id)+'.h5'
ifname=ifnameroot+str(id)+'.jpg'


# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [2348, 1412]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [32.0, 64.0, 64.0]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [254.95366954580783, -71.57150480114426, 224.8722247973803]
renderView1.CameraFocalPoint = [32.00000000000057, 63.99999999999976, 64.00000000000047]
renderView1.CameraViewUp = [0.6039450201427604, 0.04925431385434736, -0.7955026242643694]
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

for i in range(620,1271): 
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
    renderView1.ViewSize = [2348, 1412]
    renderView1.AxesGrid = 'GridAxes3DActor'
    renderView1.CenterOfRotation = [32.0, 64.0, 64.0]
    renderView1.StereoType = 'Crystal Eyes'
    renderView1.CameraPosition = [254.95366954580783, -71.57150480114426, 224.8722247973803]
    renderView1.CameraFocalPoint = [32.00000000000057, 63.99999999999976, 64.00000000000047]
    renderView1.CameraViewUp = [0.6039450201427604, 0.04925431385434736, -0.7955026242643694]
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


