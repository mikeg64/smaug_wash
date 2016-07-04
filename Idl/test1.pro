;test
 cgDisplay, WID=1
 data = cgScaleVector(cgDemoData(2), 0.1, 4534.5)
 cgLoadCT, 33, NColors=10, Bottom=1
 levels = cgConLevels(data, Factor=100, MINVALUE=0)
 cgContour, data, Levels=levels, /Fill, /Outline, $
       Position=[0.1, 0.1, 0.9, 0.75], C_Colors=Indgen(10)+1
 cgColorbar, NColors=9, Bottom=1, /Discrete, /Fit, $
       Range=[Min(levels), Max(levels)], OOB_High=10, OOB_Low='white'

end