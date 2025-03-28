# -*- coding: utf-8 -*-

import arcpy
import ComplexNumber
import HelloWorld


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
            displayName="Real1",
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
            displayName="Real1",
            name="imag",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input",
        )
        param4 = arcpy.Parameter(
            displayName="Imaginary",
            name="imag1",
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
        img1 = parameters[1].value
        real1 = parameters[0].value
        img2 = parameters[3].value
        real2 = parameters[2].value
        c1 = HelloWorld.ComplexNumber (real1, img1)
        c2 = HelloWorld.ComplexNumber (real2, img2)
        c3 = c1.add(c2)
        messages.addMessages(
            "The sum of the two complex number is: "
            +str(c3.real)+ " + " + str(c3.imag) + "i")
        
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
