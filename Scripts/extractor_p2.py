# trace generated using paraview version 5.12.1
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 12

#### import the simple module from the paraview
from paraview.simple import *

rd = $rdd

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Open FOAM Reader'
v1foam = OpenFOAMReader(
    registrationName="$jj.foam",
    FileName="$ddir/Case_$ii/Case_$ii_$jj/$jj.foam",
)

# Properties modified on v1foam
v1foam.SkipZeroTime = 0
v1foam.CaseType = "Decomposed Case"

# get active view
renderView1 = GetActiveViewOrCreate("RenderView")

# show data in view
v1foamDisplay = Show(v1foam, renderView1, "UnstructuredGridRepresentation")

# trace defaults for the display properties.
v1foamDisplay.Representation = "Surface"

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
v1foamDisplay.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction("p")

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction("p")

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D("p")

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

animationScene1.GoToLast()

# create a new 'Plot Over Line'
plotOverLine1 = PlotOverLine(registrationName="PlotOverLine1", Input=v1foam)

# Properties modified on v1foam
v1foam.MeshRegions = ["internalMesh"]
v1foam.CellArrays = [
    "U",
    "div(phi)",
    "magR",
    "momentError",
    "nuTilda",
    "nut",
    "p",
    "turbulenceProperties:I",
    "turbulenceProperties:L",
    "turbulenceProperties:R",
    "turbulenceProperties:devReff",
    "turbulenceProperties:epsilon",
    "turbulenceProperties:k",
    "turbulenceProperties:nuEff",
    "turbulenceProperties:nut",
]

# Properties modified on plotOverLine1
plotOverLine1.Point1 = [0.0, rd, 15 * 2 * rd]
plotOverLine1.Point2 = [0.0, -rd, 15 * 2 * rd]

# show data in view
plotOverLine1Display = Show(plotOverLine1, renderView1, "GeometryRepresentation")

# trace defaults for the display properties.
plotOverLine1Display.Representation = "Surface"

# Create a new 'Line Chart View'
lineChartView1 = CreateView("XYChartView")

# show data in view
plotOverLine1Display_1 = Show(plotOverLine1, lineChartView1, "XYChartRepresentation")

# get layout
layout1 = GetLayoutByName("Layout #1")

# add view to a layout so it's visible in UI
AssignViewToLayout(view=lineChartView1, layout=layout1, hint=0)

# Properties modified on plotOverLine1Display_1
plotOverLine1Display_1.SeriesOpacity = [
    "arc_length",
    "1",
    "div(phi)",
    "1",
    "magR",
    "1",
    "momentError_X",
    "1",
    "momentError_Y",
    "1",
    "momentError_Z",
    "1",
    "momentError_Magnitude",
    "1",
    "nut",
    "1",
    "nuTilda",
    "1",
    "p",
    "1",
    "turbulenceProperties:devReff_XX",
    "1",
    "turbulenceProperties:devReff_YY",
    "1",
    "turbulenceProperties:devReff_ZZ",
    "1",
    "turbulenceProperties:devReff_XY",
    "1",
    "turbulenceProperties:devReff_YZ",
    "1",
    "turbulenceProperties:devReff_XZ",
    "1",
    "turbulenceProperties:devReff_Magnitude",
    "1",
    "turbulenceProperties:epsilon",
    "1",
    "turbulenceProperties:I",
    "1",
    "turbulenceProperties:k",
    "1",
    "turbulenceProperties:L",
    "1",
    "turbulenceProperties:nuEff",
    "1",
    "turbulenceProperties:nut",
    "1",
    "turbulenceProperties:R_XX",
    "1",
    "turbulenceProperties:R_YY",
    "1",
    "turbulenceProperties:R_ZZ",
    "1",
    "turbulenceProperties:R_XY",
    "1",
    "turbulenceProperties:R_YZ",
    "1",
    "turbulenceProperties:R_XZ",
    "1",
    "turbulenceProperties:R_Magnitude",
    "1",
    "U_X",
    "1",
    "U_Y",
    "1",
    "U_Z",
    "1",
    "U_Magnitude",
    "1",
    "vtkValidPointMask",
    "1",
    "Points_X",
    "1",
    "Points_Y",
    "1",
    "Points_Z",
    "1",
    "Points_Magnitude",
    "1",
]
plotOverLine1Display_1.SeriesPlotCorner = [
    "Points_Magnitude",
    "0",
    "Points_X",
    "0",
    "Points_Y",
    "0",
    "Points_Z",
    "0",
    "U_Magnitude",
    "0",
    "U_X",
    "0",
    "U_Y",
    "0",
    "U_Z",
    "0",
    "arc_length",
    "0",
    "div(phi)",
    "0",
    "magR",
    "0",
    "momentError_Magnitude",
    "0",
    "momentError_X",
    "0",
    "momentError_Y",
    "0",
    "momentError_Z",
    "0",
    "nuTilda",
    "0",
    "nut",
    "0",
    "p",
    "0",
    "turbulenceProperties:I",
    "0",
    "turbulenceProperties:L",
    "0",
    "turbulenceProperties:R_Magnitude",
    "0",
    "turbulenceProperties:R_XX",
    "0",
    "turbulenceProperties:R_XY",
    "0",
    "turbulenceProperties:R_XZ",
    "0",
    "turbulenceProperties:R_YY",
    "0",
    "turbulenceProperties:R_YZ",
    "0",
    "turbulenceProperties:R_ZZ",
    "0",
    "turbulenceProperties:devReff_Magnitude",
    "0",
    "turbulenceProperties:devReff_XX",
    "0",
    "turbulenceProperties:devReff_XY",
    "0",
    "turbulenceProperties:devReff_XZ",
    "0",
    "turbulenceProperties:devReff_YY",
    "0",
    "turbulenceProperties:devReff_YZ",
    "0",
    "turbulenceProperties:devReff_ZZ",
    "0",
    "turbulenceProperties:epsilon",
    "0",
    "turbulenceProperties:k",
    "0",
    "turbulenceProperties:nuEff",
    "0",
    "turbulenceProperties:nut",
    "0",
    "vtkValidPointMask",
    "0",
]
plotOverLine1Display_1.SeriesLineStyle = [
    "Points_Magnitude",
    "1",
    "Points_X",
    "1",
    "Points_Y",
    "1",
    "Points_Z",
    "1",
    "U_Magnitude",
    "1",
    "U_X",
    "1",
    "U_Y",
    "1",
    "U_Z",
    "1",
    "arc_length",
    "1",
    "div(phi)",
    "1",
    "magR",
    "1",
    "momentError_Magnitude",
    "1",
    "momentError_X",
    "1",
    "momentError_Y",
    "1",
    "momentError_Z",
    "1",
    "nuTilda",
    "1",
    "nut",
    "1",
    "p",
    "1",
    "turbulenceProperties:I",
    "1",
    "turbulenceProperties:L",
    "1",
    "turbulenceProperties:R_Magnitude",
    "1",
    "turbulenceProperties:R_XX",
    "1",
    "turbulenceProperties:R_XY",
    "1",
    "turbulenceProperties:R_XZ",
    "1",
    "turbulenceProperties:R_YY",
    "1",
    "turbulenceProperties:R_YZ",
    "1",
    "turbulenceProperties:R_ZZ",
    "1",
    "turbulenceProperties:devReff_Magnitude",
    "1",
    "turbulenceProperties:devReff_XX",
    "1",
    "turbulenceProperties:devReff_XY",
    "1",
    "turbulenceProperties:devReff_XZ",
    "1",
    "turbulenceProperties:devReff_YY",
    "1",
    "turbulenceProperties:devReff_YZ",
    "1",
    "turbulenceProperties:devReff_ZZ",
    "1",
    "turbulenceProperties:epsilon",
    "1",
    "turbulenceProperties:k",
    "1",
    "turbulenceProperties:nuEff",
    "1",
    "turbulenceProperties:nut",
    "1",
    "vtkValidPointMask",
    "1",
]
plotOverLine1Display_1.SeriesLineThickness = [
    "Points_Magnitude",
    "2",
    "Points_X",
    "2",
    "Points_Y",
    "2",
    "Points_Z",
    "2",
    "U_Magnitude",
    "2",
    "U_X",
    "2",
    "U_Y",
    "2",
    "U_Z",
    "2",
    "arc_length",
    "2",
    "div(phi)",
    "2",
    "magR",
    "2",
    "momentError_Magnitude",
    "2",
    "momentError_X",
    "2",
    "momentError_Y",
    "2",
    "momentError_Z",
    "2",
    "nuTilda",
    "2",
    "nut",
    "2",
    "p",
    "2",
    "turbulenceProperties:I",
    "2",
    "turbulenceProperties:L",
    "2",
    "turbulenceProperties:R_Magnitude",
    "2",
    "turbulenceProperties:R_XX",
    "2",
    "turbulenceProperties:R_XY",
    "2",
    "turbulenceProperties:R_XZ",
    "2",
    "turbulenceProperties:R_YY",
    "2",
    "turbulenceProperties:R_YZ",
    "2",
    "turbulenceProperties:R_ZZ",
    "2",
    "turbulenceProperties:devReff_Magnitude",
    "2",
    "turbulenceProperties:devReff_XX",
    "2",
    "turbulenceProperties:devReff_XY",
    "2",
    "turbulenceProperties:devReff_XZ",
    "2",
    "turbulenceProperties:devReff_YY",
    "2",
    "turbulenceProperties:devReff_YZ",
    "2",
    "turbulenceProperties:devReff_ZZ",
    "2",
    "turbulenceProperties:epsilon",
    "2",
    "turbulenceProperties:k",
    "2",
    "turbulenceProperties:nuEff",
    "2",
    "turbulenceProperties:nut",
    "2",
    "vtkValidPointMask",
    "2",
]
plotOverLine1Display_1.SeriesMarkerStyle = [
    "Points_Magnitude",
    "0",
    "Points_X",
    "0",
    "Points_Y",
    "0",
    "Points_Z",
    "0",
    "U_Magnitude",
    "0",
    "U_X",
    "0",
    "U_Y",
    "0",
    "U_Z",
    "0",
    "arc_length",
    "0",
    "div(phi)",
    "0",
    "magR",
    "0",
    "momentError_Magnitude",
    "0",
    "momentError_X",
    "0",
    "momentError_Y",
    "0",
    "momentError_Z",
    "0",
    "nuTilda",
    "0",
    "nut",
    "0",
    "p",
    "0",
    "turbulenceProperties:I",
    "0",
    "turbulenceProperties:L",
    "0",
    "turbulenceProperties:R_Magnitude",
    "0",
    "turbulenceProperties:R_XX",
    "0",
    "turbulenceProperties:R_XY",
    "0",
    "turbulenceProperties:R_XZ",
    "0",
    "turbulenceProperties:R_YY",
    "0",
    "turbulenceProperties:R_YZ",
    "0",
    "turbulenceProperties:R_ZZ",
    "0",
    "turbulenceProperties:devReff_Magnitude",
    "0",
    "turbulenceProperties:devReff_XX",
    "0",
    "turbulenceProperties:devReff_XY",
    "0",
    "turbulenceProperties:devReff_XZ",
    "0",
    "turbulenceProperties:devReff_YY",
    "0",
    "turbulenceProperties:devReff_YZ",
    "0",
    "turbulenceProperties:devReff_ZZ",
    "0",
    "turbulenceProperties:epsilon",
    "0",
    "turbulenceProperties:k",
    "0",
    "turbulenceProperties:nuEff",
    "0",
    "turbulenceProperties:nut",
    "0",
    "vtkValidPointMask",
    "0",
]
plotOverLine1Display_1.SeriesMarkerSize = [
    "Points_Magnitude",
    "4",
    "Points_X",
    "4",
    "Points_Y",
    "4",
    "Points_Z",
    "4",
    "U_Magnitude",
    "4",
    "U_X",
    "4",
    "U_Y",
    "4",
    "U_Z",
    "4",
    "arc_length",
    "4",
    "div(phi)",
    "4",
    "magR",
    "4",
    "momentError_Magnitude",
    "4",
    "momentError_X",
    "4",
    "momentError_Y",
    "4",
    "momentError_Z",
    "4",
    "nuTilda",
    "4",
    "nut",
    "4",
    "p",
    "4",
    "turbulenceProperties:I",
    "4",
    "turbulenceProperties:L",
    "4",
    "turbulenceProperties:R_Magnitude",
    "4",
    "turbulenceProperties:R_XX",
    "4",
    "turbulenceProperties:R_XY",
    "4",
    "turbulenceProperties:R_XZ",
    "4",
    "turbulenceProperties:R_YY",
    "4",
    "turbulenceProperties:R_YZ",
    "4",
    "turbulenceProperties:R_ZZ",
    "4",
    "turbulenceProperties:devReff_Magnitude",
    "4",
    "turbulenceProperties:devReff_XX",
    "4",
    "turbulenceProperties:devReff_XY",
    "4",
    "turbulenceProperties:devReff_XZ",
    "4",
    "turbulenceProperties:devReff_YY",
    "4",
    "turbulenceProperties:devReff_YZ",
    "4",
    "turbulenceProperties:devReff_ZZ",
    "4",
    "turbulenceProperties:epsilon",
    "4",
    "turbulenceProperties:k",
    "4",
    "turbulenceProperties:nuEff",
    "4",
    "turbulenceProperties:nut",
    "4",
    "vtkValidPointMask",
    "4",
]

# Rescale transfer function
pLUT.RescaleTransferFunction(-0.13434259593486786, 0.08531588315963745)

# Rescale transfer function
pPWF.RescaleTransferFunction(-0.13434259593486786, 0.08531588315963745)

# create a new 'Pass Arrays'
passArrays1 = PassArrays(registrationName="PassArrays1", Input=plotOverLine1)

# save data
SaveData(
    "$ddir/Case_$ii/p2_$jj.csv",
    proxy=passArrays1,
    PointDataArrays=[
        "U",
        "arc_length",
        "div(phi)",
        "magR",
        "momentError",
        "nuTilda",
        "nut",
        "p",
        "turbulenceProperties:I",
        "turbulenceProperties:L",
        "turbulenceProperties:R",
        "turbulenceProperties:devReff",
        "turbulenceProperties:epsilon",
        "turbulenceProperties:k",
        "turbulenceProperties:nuEff",
        "turbulenceProperties:nut",
        "vtkValidPointMask",
    ],
)

# ================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
# ================================================================

# --------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(628, 823)

# -----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [0.0, 0.0, 0.9146790856026675]
renderView1.CameraFocalPoint = [0.0, 0.0, 0.15000000596046448]
renderView1.CameraParallelScale = 0.20062595770137284


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://kitware.github.io/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
