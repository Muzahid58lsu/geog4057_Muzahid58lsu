# -*- coding: utf-8 -*-

import arcpy
import ComplexNumber


class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "ComplexNumber"
        self.alias = "ComplexNumber"

        # List of tool classes associated with this toolbox
        self.tools = [Tool]


class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "ComplexNumber"
        self.description = "ComplexNumber"

    def getParameterInfo(self):
        """Define the tool parameters."""
        param1 = arcpy.Parameter(
            displayName="Real",
            name="real",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input",
        )
        param2 = arcpy.Parameter(
            displayName="Imaginary",
            name="imag",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input",
        )
        param3 = arcpy.Parameter(
            displayName="Real",
            name="imag",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input",
        )
        param4 = arcpy.Parameter(
            displayName="Imaginary",
            name="imag",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input",
        )
        params = [param1, param2, param3, param4]
        
        return params

    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
