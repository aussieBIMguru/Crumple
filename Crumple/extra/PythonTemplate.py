# Made by Gavin Crump
# Free for use
# BIM Guru, www.bimguru.com.au

# Boilerplate text
import clr

import sys
sys.path.append('C:\Program Files (x86)\IronPython 2.7\Lib')

import System
from System import Array
from System.Collections.Generic import *

clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)
clr.ImportExtensions(Revit.GeometryConversion)

clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager 
from RevitServices.Transactions import TransactionManager 

clr.AddReference("RevitAPI")
clr.AddReference("RevitAPIUI")

import Autodesk 
from Autodesk.Revit.DB import *
from Autodesk.Revit.UI import *

# Current doc/app/ui
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication 
app = uiapp.Application 
uidoc = uiapp.ActiveUIDocument

# Define list/unwrap list functions
def tolist(input):
    result = input if isinstance(input, list) else [input]
    return result

def uwlist(input):
    result = input if isinstance(input, list) else [input]
    return UnwrapElement(result)

def objOrList(input):
    if isinstance(input, list) and len(input) == 1:
        return input[0]
    else:
        return input

# Preparing input from dynamo to revit
element    = IN[0]
elements = tolist(IN[0])
uw_list  = uwlist(IN[0])

# Do some action in a Transaction
TransactionManager.Instance.EnsureInTransaction(doc)
# your actions
TransactionManager.Instance.TransactionTaskDone()

# Output and Changing element to Dynamo for export
# <element>.ToDSType(True), #Not created in script, mark as Revit-owned
# <element>.ToDSType(False) #Created in script, mark as non-Revit-owned

# Preparing output to Dynamo
OUT = element