
#--------------------------------------------------------------

# Global timestep output options
timeStepToStartOutputAt=0
forceOutputAtFirstCall=False

# Global screenshot output options
imageFileNamePadding=0
rescale_lookuptable=False

# Whether or not to request specific arrays from the adaptor.
requestSpecificArrays=False

# a root directory under which all Catalyst output goes
rootDirectory=''

# makes a cinema D index table
make_cinema_table=False

#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# paraview version 5.7.0-RC2
#--------------------------------------------------------------

from paraview.simple import *
from paraview import coprocessing

# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 5.7.0-RC2

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      # trace generated using paraview version 5.7.0-RC2
      #
      # To ensure correct image size when batch processing, please search 
      # for and uncomment the line `# renderView*.ViewSize = [*,*]`

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # get the material library
      materialLibrary1 = GetMaterialLibrary()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [2016, 1666]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [64.0, 64.0, 64.0]
      renderView1.StereoType = 'Crystal Eyes'
      renderView1.CameraPosition = [150.75812126127408, 127.4424285729388, -406.50759479222404]
      renderView1.CameraFocalPoint = [64.00000000000048, 63.99999999999953, 63.99999999999896]
      renderView1.CameraViewUp = [0.9836976602805247, -0.02900873146368332, 0.1774750874277552]
      renderView1.CameraFocalDisk = 1.0
      renderView1.CameraParallelScale = 125.8623586833384
      renderView1.Background = [0.32, 0.34, 0.43]
      renderView1.BackEnd = 'OSPRay raycaster'
      renderView1.OSPRayMaterialLibrary = materialLibrary1

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='image_%t.png', freq=1, fittoscreen=1, magnification=1, width=1008, height=833, cinema={}, compression=-1)
      renderView1.ViewTime = datadescription.GetTime()

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
      # create a producer from a simulation input
      washmc_h5 = coprocessor.CreateProducer(datadescription, 'washmc_..h5')

      # create a new 'Calculator'
      vfieldcalc = Calculator(Input=washmc_h5)
      vfieldcalc.AttributeType = 'Cell Data'
      vfieldcalc.ResultArrayName = 'vfield'
      vfieldcalc.Function = 'iHat*data/grid_0000000000/velocity_x+jHat*data/grid_0000000000/velocity_y+kHat*data/grid_0000000000/velocity_z'

      # create a new 'Calculator'
      bfieldcalc = Calculator(Input=washmc_h5)
      bfieldcalc.AttributeType = 'Cell Data'
      bfieldcalc.ResultArrayName = 'bfield'
      bfieldcalc.Function = """iHat*(data/grid_0000000000/mag_field_x_bg+data/grid_0000000000/mag_field_x_pert)+jHat*(data/grid_0000000000/mag_field_y_bg+data/grid_0000000000/mag_field_y_pert)+kHat*(data/grid_0000000000/mag_field_z_bg+data/grid_0000000000/mag_field_z_pert)
      """

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
      slice2 = Slice(Input=vfieldcalc)
      slice2.SliceType = 'Plane'
      slice2.SliceOffsetValues = [0.0]

      # init the 'Plane' selected for 'SliceType'
      slice2.SliceType.Origin = [0.02317771427184967, 64.0, 64.0]

      # create a new 'Slice'
      slice1 = Slice(Input=bfieldcalc)
      slice1.SliceType = 'Plane'
      slice1.SliceOffsetValues = [0.0]

      # init the 'Plane' selected for 'SliceType'
      slice1.SliceType.Origin = [109.2836351789272, 64.0, 64.0]

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

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
      bfieldLUT.RGBPoints = [3.19828e-75, 0.231373, 0.298039, 0.752941, 0.04460321654312536, 0.865003, 0.865003, 0.865003, 0.08920643308625072, 0.705882, 0.0156863, 0.14902]
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

      # show data from tube1
      tube1Display = Show(tube1, renderView1)

      # get color transfer function/color map for 'vfield'
      vfieldLUT = GetColorTransferFunction('vfield')
      vfieldLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.00015467511149859538, 0.865003, 0.865003, 0.865003, 0.00030935022299719077, 0.705882, 0.0156863, 0.14902]
      vfieldLUT.ScalarRangeInitialized = 1.0

      # trace defaults for the display properties.
      tube1Display.Representation = 'Surface'
      tube1Display.ColorArrayName = ['POINTS', 'vfield']
      tube1Display.LookupTable = vfieldLUT
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

      # show data from slice2
      slice2Display = Show(slice2, renderView1)

      # trace defaults for the display properties.
      slice2Display.Representation = 'Surface'
      slice2Display.ColorArrayName = ['CELLS', 'vfield']
      slice2Display.LookupTable = vfieldLUT
      slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
      slice2Display.SelectOrientationVectors = 'vfield'
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

      # show color legend
      bfieldcalcDisplay.SetScalarBarVisibility(renderView1, True)

      # show color legend
      tube1Display.SetScalarBarVisibility(renderView1, True)

      # show color legend
      slice1Display.SetScalarBarVisibility(renderView1, True)

      # show color legend
      slice2Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get opacity transfer function/opacity map for 'vfield'
      vfieldPWF = GetOpacityTransferFunction('vfield')
      vfieldPWF.Points = [0.0, 0.0, 0.5, 0.0, 0.00030935022299719077, 1.0, 0.5, 0.0]
      vfieldPWF.ScalarRangeInitialized = 1

      # get opacity transfer function/opacity map for 'bfield'
      bfieldPWF = GetOpacityTransferFunction('bfield')
      bfieldPWF.Points = [3.19828e-75, 0.0, 0.5, 0.0, 0.08920643308625072, 1.0, 0.5, 0.0]
      bfieldPWF.ScalarRangeInitialized = 1

      # ----------------------------------------------------------------
      # finally, restore active source
      SetActiveSource(slice1)
      # ----------------------------------------------------------------
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'washmc_..h5': [1, 1, 1, 1, 1, 1, 1, 1]}
  coprocessor.SetUpdateFrequencies(freqs)
  if requestSpecificArrays:
    arrays = [['avtGhostZones', 1], ['data/grid_0000000000/mag_field_x_bg', 1], ['data/grid_0000000000/mag_field_x_pert', 1], ['data/grid_0000000000/mag_field_y_bg', 1], ['data/grid_0000000000/mag_field_y_pert', 1], ['data/grid_0000000000/mag_field_z_bg', 1], ['data/grid_0000000000/mag_field_z_pert', 1], ['data/grid_0000000000/velocity_x', 1], ['data/grid_0000000000/velocity_y', 1], ['data/grid_0000000000/velocity_z', 1]]
    coprocessor.SetRequestedArrays('washmc_..h5', arrays)
  coprocessor.SetInitialOutputOptions(timeStepToStartOutputAt,forceOutputAtFirstCall)

  if rootDirectory:
      coprocessor.SetRootDirectory(rootDirectory)

  if make_cinema_table:
      coprocessor.EnableCinemaDTable()

  return coprocessor


#--------------------------------------------------------------
# Global variable that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView and the update frequency
coprocessor.EnableLiveVisualization(True, 1)

# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor

    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=rescale_lookuptable,
        image_quality=0, padding_amount=imageFileNamePadding)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
