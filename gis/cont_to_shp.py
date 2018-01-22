__author__ = 'are'

from ipywidgets import FloatProgress
from IPython.display import display

import shapefile

def cont_to_shp(contour_set, levels, filename):

    # create shape instance and field
    w = shapefile.Writer()
    w.field("Head", "N", decimal=2)

    # create shapes and records
    wdgt = FloatProgress(min=0, max=len(levels), description="collecting shapes ... ")
    display(wdgt)
        
    for collection, h in zip(contour_set.collections, levels):
        #sys.stdout.write(" {:.1f}".format(h))
        wdgt.value += 1
        for path in collection.get_paths():
            for polygon in path.to_polygons():
                #sys.stdout.write("|")
                w.line(parts=[[list(p) for p in polygon ][:-1]])
                w.record(h)
                
    # save file
    print("\nsaving " + filename)
    w.save(filename)
