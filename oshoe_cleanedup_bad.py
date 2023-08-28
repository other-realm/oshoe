#%%
from IPython.display import Image
from IPython.display import display
from IPython.core.interactiveshell import InteractiveShell
from nbconvert.preprocessors import ExecutePreprocessor
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import scipy.linalg as li
import sympy as sy
from re import T
import cadquery as cq
import cq_warehouse as cqw
import cq_warehouse.extensions
# from cadquery import *
from cadquery import exporters
import matplotlib
from IPython.display import Image
from IPython.display import display
from IPython.core.interactiveshell import InteractiveShell
from nbconvert.preprocessors import ExecutePreprocessor
from IPython.core.display import HTML
from typing import Union
from build123d import *
from ocp_vscode import show, show_object, reset_show, set_port, set_defaults, get_defaults
set_port(3939)
plt.rcParams['figure.figsize'] = [9, 9]
InteractiveShell.ast_node_interactivity = "all"
np.random.default_rng()
np.set_printoptions(suppress=True)
#%%
soleInnerDim=np.array([(0, 285, 0),
                 (-40, 270, 0),
                 (-46,239,1),
                 (-47,221.5,1),
                 (-47,202.5,1),
                 (-47,195,1),
                 (-45,174,1),
                 (-40, 167, 4),
                 (-38, 136, 8),
                 (-39.5,117.5,16),
                 (-40,97.5,10),
                 (-38,72,5),
                 (-35,48,3),
                 (-30,35,0),
                 (-26,24,0),
                 (0,0,0),
                 (16,9,20),
                 (22,20,30),
                 (27,33,30),
                 (35,57,30),
                 (42,82.5,30),
                 (46,96.5,30),
                 (57,121,33),
                 (58,153.5,33),
                 (63,174,30),
                 (60,192.5,30),
                 (57,202.5,30),
                 (54,221.5,30),
                 (45,242,20),
                 (39,270,7),
                 (20,280,0)
                 ])
#%%
soleOuterBtmDim=[]
soleInnerBtmDim=soleInnerDim.copy()
soleInnerBtmDim[:,2]=[0]
for p in soleInnerBtmDim:
    longLeng=(((soleInnerBtmDim[:,1])-100))
    if(p[0]>=0 ):
        soleOuterBtmDim.append((p[0]*1.3,p[1],(.0008*((p[1]/102)**10))))
    elif(p[0]<0):
        soleOuterBtmDim.append((p[0],p[1],(.0008*((p[1]/102)**10))))
    else:
        soleOuterBtmDim.append((p[0],p[1],0))
soleInnerBtmLn=Edge.make_spline(soleInnerBtmDim.tolist(),periodic=True)
soleInnerTopLn=Edge.make_spline(soleInnerDim.tolist(),periodic=True)
soleFcLw=Face.make_surface([soleInnerBtmLn])
soleFcUp=Face.make_surface([soleInnerTopLn])
soleFcUp=soleFcUp.transformed((0,0,0),(0,0,0))
soleFcLw=soleFcLw.transformed((0,0,0,),(0,0,-30))
soleFc=soleFcUp+soleFcLw
sliceBelow=Box(length=200,width=350,height=200).transformed((0,0,0),(-20,150,-99))
insole=loft([soleFc],ruled=True)
insole=insole-sliceBelow
insole
show(insole)
#%%


#%%
insole.export_stl('insoleRight2023-08-28-1348.stl')
#%%
