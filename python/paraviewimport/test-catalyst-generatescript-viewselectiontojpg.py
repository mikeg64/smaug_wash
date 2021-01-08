
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
      renderView1.ViewSize = [1494, 1270]
      renderView1.AxesGrid = 'GridAxes3DActor'
      renderView1.CenterOfRotation = [64.0, 64.0, 64.0]
      renderView1.StereoType = 'Crystal Eyes'
      renderView1.CameraPosition = [472.59200283322616, 266.6337124135096, -182.09628222354104]
      renderView1.CameraFocalPoint = [64.00000000000004, 63.99999999999998, 63.99999999999992]
      renderView1.CameraViewUp = [0.6082835807515485, -0.6104480780336138, 0.5072910697155447]
      renderView1.CameraFocalDisk = 1.0
      renderView1.CameraParallelScale = 110.85125168440814
      renderView1.Background = [0.32, 0.34, 0.43]
      renderView1.BackEnd = 'OSPRay raycaster'
      renderView1.OSPRayMaterialLibrary = materialLibrary1

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='image_%t.jpg', freq=1, fittoscreen=0, magnification=1, width=747, height=635, cinema={}, compression=-1)
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
      washmc_ = coprocessor.CreateProducer(datadescription, 'washmc_*')

      # create a new 'Slice'
      slice1 = Slice(Input=washmc_)
      slice1.SliceType = 'Plane'
      slice1.SliceOffsetValues = [0.0]

      # init the 'Plane' selected for 'SliceType'
      slice1.SliceType.Origin = [5.554498796690172, 64.0, 64.0]

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from washmc_
      washmc_Display = Show(washmc_, renderView1)

      # get color transfer function/color map for 'datagrid_0000000000density_pert'
      datagrid_0000000000density_pertLUT = GetColorTransferFunction('datagrid_0000000000density_pert')
      datagrid_0000000000density_pertLUT.RGBPoints = [-3.3922270702123095e-11, 0.231373, 0.298039, 0.752941, -1.1164603498491806e-12, 0.865003, 0.865003, 0.865003, 3.1689350002424733e-11, 0.705882, 0.0156863, 0.14902]
      datagrid_0000000000density_pertLUT.ScalarRangeInitialized = 1.0

      # trace defaults for the display properties.
      washmc_Display.Representation = 'Outline'
      washmc_Display.ColorArrayName = ['CELLS', 'data/grid_0000000000/density_pert']
      washmc_Display.LookupTable = datagrid_0000000000density_pertLUT
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

      # show data from slice1
      slice1Display = Show(slice1, renderView1)

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

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for datagrid_0000000000density_pertLUT in view renderView1
      datagrid_0000000000density_pertLUTColorBar = GetScalarBar(datagrid_0000000000density_pertLUT, renderView1)
      datagrid_0000000000density_pertLUTColorBar.Position = [0.8481425702811245, 0.0547244094488189]
      datagrid_0000000000density_pertLUTColorBar.Title = 'data/grid_0000000000/density_pert'
      datagrid_0000000000density_pertLUTColorBar.ComponentTitle = ''

      # set color bar visibility
      datagrid_0000000000density_pertLUTColorBar.Visibility = 1

      # show color legend
      washmc_Display.SetScalarBarVisibility(renderView1, True)

      # show color legend
      slice1Display.SetScalarBarVisibility(renderView1, True)

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get opacity transfer function/opacity map for 'datagrid_0000000000density_pert'
      datagrid_0000000000density_pertPWF = GetOpacityTransferFunction('datagrid_0000000000density_pert')
      datagrid_0000000000density_pertPWF.Points = [-3.3922270702123095e-11, 0.0, 0.5, 0.0, 3.1689350002424733e-11, 1.0, 0.5, 0.0]
      datagrid_0000000000density_pertPWF.ScalarRangeInitialized = 1

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
  freqs = {'washmc_*': [1, 1]}
  coprocessor.SetUpdateFrequencies(freqs)
  if requestSpecificArrays:
    arrays = [['avtGhostZones', 1], ['data/grid_0000000000/density_pert', 1]]
    coprocessor.SetRequestedArrays('washmc_*', arrays)
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
coprocessor.EnableLiveVisualization(False, 1)

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
