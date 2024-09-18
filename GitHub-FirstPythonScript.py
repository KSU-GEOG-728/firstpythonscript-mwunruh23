#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: GitHub-FirstPythonScript.py
    Author: Miller Unruh
    Description:  This takes an EcoRegion that the user selects and adds a 10km buffer around the ecoregion. The buffer area then clilps the rivers in the ecoregion and adds up all their lengths to get one total for water length. 
    Date created: 09/11/2024
    Python Version: 3.9.16
"""

# Import arcpy module and allow overwrites
import arcpy
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = C:/Users/mwunruh/Documents/GitHub/firstpythonscript-mwunruh23/GISProject/ExerciseData.gdb

#perform geoprocessing
arcpy.management.SelectLayerByAttribute('ks_ecoregions', 'NEW_SELECTION', "US_L3NAME = 'Flint Hills'")

arcpy.analysis.Buffer('ks_ecoregions', "flintHillsBuffer", "10 Kilometers")

arcpy.analysis.Clip('flintHillsBuffer', 'flintHillsBuffer', "RiverClipWithBuffer")

arcpy.management.CalculateField('RiverClipWithBuffer', 'Length_Mi', "!Shape_Length! * 0.000621371")
arcpy.analysis.Statistics('RiverClipWithBuffer', 'outStat', [['Length_Mi', 'SUM']])