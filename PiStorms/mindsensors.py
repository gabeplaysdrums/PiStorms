#!/usr/bin/env python
#
# Copyright (c) 2015 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
# 10/14/15  Michael     Initial Authoring

from mindsensors_i2c import mindsensors_i2c

## @package mindsensors
#  This module contains classes and functions necessary for use of mindsensors.com I2C devices with Raspberry Pi

## ABSIMU: this class provides functions for models of the ABSIMU from mindsensors.com
#  for read and write operations.
class ABSIMU(mindsensors_i2c):  

    ## Default ABSIMU I2C Address 
    ABSIMU_ADDRESS = (0x22)
    ## Command Register 
    COMMAND = 0x41
    ## X-Axis Tilt Register. Will return a signed integer reading
    TILT_X = 0x42
    ## Y-Axis Tilt Register. Will return a signed integer reading
    TILT_Y = 0x43
    ## Z-Axis Tilt Register. Will return a signed integer reading
    TILT_Z = 0x44
    ## X-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050) 
    ACCEL_X = 0x45
    ## Y-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050)
    ACCEL_Y = 0x47
    ## Z-Axis Accelerometer Register. Will return a signed integer reading (-1050 - 1050)
    ACCEL_Z = 0x49
    ## Compass Heading Register. Will return an unsigned integer reading (0 - 360)
    CMPS = 0x4B
    ## X-Axis Magnetometer Register. Will return a signed integer reading 
    MAG_X = 0x4D
    ## Y-Axis Magnetometer Register. Will return a signed integer reading 
    MAG_Y = 0x4F
    ## Z-Axis Magnetometer Register. Will return a signed integer reading 
    MAG_Z = 0x51
    ## X-Axis Gyroscope Register. Will return a signed integer reading 
    GYRO_X = 0x53
    ## Y-Axis Gyroscope Register. Will return a signed integer reading 
    GYRO_Y = 0x55
    ## Z-Axis Gyroscope Register. Will return a signed integer reading 
    GYRO_Z = 0x57
    
    ## Initialize the class with the i2c address of your AbsoluteIMU
    #  @param self The object pointer.
    #  @param i2c_address Address of your AbsoluteIMU.
    #  @remark
    def __init__(self, absimu_address = ABSIMU_ADDRESS):
        mindsensors_i2c.__init__(self, absimu_address >> 1)        
        
    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, command):
        self.writeByte(COMMAND, int(cmd)) 
    
    ## Reads the tilt value along the x-axis
    #  @param self The object pointer.
    def get_tiltx(self):
        try:
            return self.readByteSigned(self.TILT_X)
        except:
            print "Error: Could not read tilt along x-axis"
            return ""
      
    ## Reads the tilt value along the y-axis
    #  @param self The object pointer.
    def get_tilty(self):
        try:
            return self.readByteSigned(self.TILT_Y)
        except:
            print "Error: Could not read tilt along y-axis"
            return ""
            
    ## Reads the tilt value along the z-axis
    #  @param self The object pointer.
    def get_tiltz(self):
        try:
            return self.readByteSigned(self.TILT_Z)
        except:
            print "Error: Could not read tilt along z-axis"
            return ""
            
    ## Reads the tilt values 
    #  @param self The object pointer.
    def get_tiltall(self):
        try:
            res = [(self.get_tiltx(),
                    self.get_tilty(),
                    self.get_tiltz())]
            return res
        except:
            print "Error: Could not read tilt values"
            return ""
            
    ## Reads acceleromter value along the x-axis
    #  @param self The object pointer.
    def get_accelx(self):
        try:
            return self.readIntegerSigned(self.ACCEL_X)
        except:
            print "Error: Could not read accelerometer value along x-axis"
            return ""
            
    ## Reads acceleromter value along the y-axis
    #  @param self The object pointer.
    def get_accely(self):
        try:
            return self.readIntegerSigned(self.ACCEL_Y)
        except:
            print "Error: Could not read accelerometer value along y-axis"
            return ""
            
    ## Reads acceleromter value along the z-axis
    #  @param self The object pointer.
    def get_accelz(self):
        try:
            return self.readIntegerSigned(self.ACCEL_Z)
        except:
            print "Error: Could not read accelerometer value along z-axis"
            return ""
            
    ## Reads the accelerometer values 
    #  @param self The object pointer.
    def get_accelall(self):
        try:
            res = [(self.get_accelx(),
                    self.get_accely(),
                    self.get_accelz())]
            return res
        except:
            print "Error: Could not read accelerometer values"
            return ""
            
    ## Reads compass heading
    #  @param self The object pointer.
    def get_heading(self):
        try:
            return self.readInteger(self.CMPS)
        except:
            print "Error: Could not read compass heading"
            return ""
    
    ## Reads magnetometer value along the x-axis
    #  @param self The object pointer.
    def get_magx(self):
        try:
            return self.readIntegerSigned(self.MAG_X)
        except:
            print "Error: Could not read magnetometer value along x-axis"
            return ""
            
    ## Reads magnetometer value along the y-axis
    #  @param self The object pointer.
    def get_magy(self):
        try:
            return self.readIntegerSigned(self.MAG_Y)
        except:
            print "Error: Could not read magnetometer value along y-axis"
            return ""
            
    ## Reads magnetometer value along the z-axis
    #  @param self The object pointer.
    def get_magz(self):
        try:
            return self.readIntegerSigned(self.MAG_Z)
        except:
            print "Error: Could not read magnetometer value along z-axis"
            return ""
            
    ## Reads the magnetometer values 
    #  @param self The object pointer.
    def get_magall(self):
        try:
            res = [(self.get_magx(),
                    self.get_magy(),
                    self.get_magz())]
            return res
        except:
            print "Error: Could not read magnetometer values"
            return ""
            
    ## Reads gyroscope value along the x-axis
    #  @param self The object pointer.
    def get_gyrox(self):
        try:
            return self.readIntegerSigned(self.GYRO_X)
        except:
            print "Error: Could not read gyroscope value along x-axis"
            return ""
            
    ## Reads gyroscope value along the y-axis
    #  @param self The object pointer.
    def get_gyroy(self):
        try:
            return self.readIntegerSigned(self.GYRO_Y)
        except:
            print "Error: Could not read gyroscope value along y-axis"
            return ""
            
    ## Reads gyroscope value along the z-axis
    #  @param self The object pointer.
    def get_gyroz(self):
        try:
            return self.readIntegerSigned(self.GYRO_Z)
        except:
            print "Error: Could not read gyroscope value along z-axis"
            return ""
            
    ## Reads the tilt values 
    #  @param self The object pointer.
    def get_gyroall(self):
        try:
            res = [(self.get_gyrox(),
                    self.get_gyroy(),
                    self.get_gyroz())]
            return res
        except:
            print "Error: Could not read gyroscope values"
            return ""
            
    ## Starts the compass calibration process
    #  @param self The object pointer.
    def start_cmpscal(self):
        try:
            self.command(67)
        except:
            print "Error: Could not start compass calibration process"
            return ""    

    ## Stops the compass calibration process
    #  @param self The object pointer.
    def stop_cmpscal(self):
        try:
            self.command(99)
        except:
            print "Error: Could not stop compass calibration process"
            return ""   
    
    ## Sets accelerometer sensitivity to 2G
    #  @param self The object pointer.
    def accel_2G(self):
        try:
            self.command(49)
        except:
            print "Error: Could not change accelerometer sensitivity"
            return ""   

    ## Sets accelerometer sensitivity to 4G
    #  @param self The object pointer.
    def accel_4G(self):
        try:
            self.command(50)
        except:
            print "Error: Could not change accelerometer sensitivity"
            return ""   

    ## Sets accelerometer sensitivity to 8G
    #  @param self The object pointer.
    def accel_8G(self):
        try:
            self.command(51)
        except:
            print "Error: Could not change accelerometer sensitivity"
            return "" 

    ## Sets accelerometer sensitivity to 16G
    #  @param self The object pointer.
    def accel_16G(self):
        try:
            self.command(52)
        except:
            print "Error: Could not change accelerometer sensitivity"
            return ""  

## Angle: this class provides functions for GlideWheel-AngleSensor from mindsensors.com
#  for read and write operations.
class ANGLE(mindsensors_i2c):  
    #"""Class for the GlideWheel Angle Sensor"""

    ANGLE_ADDRESS = (0x30)
    COMMAND = 0x41
    ANGLE = 0x42
    RAW = 0x46
    RPM = 0x4A
    
    ## Initialize the class with the i2c address of your AngleSensor
    #  @param self The object pointer.
    #  @param i2c_address Address of your AngleSensor.
    def __init__(self, angle_address = ANGLE_ADDRESS):
        #the ANGLE address
        mindsensors_i2c.__init__(self, angle_address >> 1)        
        
    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, command):
        self.writeByte(self.COMMAND, int(cmd)) 
    
    ## Reads the angle in degrees
    #  @param self The object pointer.
    def get_angle(self):
        try:
            return self.readLongSigned(self.ANGLE)
        except:
            print "Error: Could not read angle"
            return ""
            
    ## Reads the raw angle value, raw = angle x 2
    #  @param self The object pointer.
    def get_raw(self):
        try:
            return self.readLongSigned(self.RAW)
        except:
            print "Error: Could not read raw angle"
            return ""
    
    ## Reads the rotations per minute
    #  @param self The object pointer.
    def get_rpm(self):
        try:
            return self.readIntegerSigned(self.RPM)
        except:
            print "Error: Could not read rpm"
            return "" 
            
## CURRENT: this class provides functions for NXTCurrentMeter from mindsensors.com
#  for read and write operations.
class CURRENT(mindsensors_i2c):  
    #"""Class for the NXTCurrentMeter Sensor"""

    CURRENT_ADDRESS = (0x28)
    COMMAND = 0x41
    CAL = 0x43
    REL = 0x45
    REF = 0x47
   
    ## Initialize the class with the i2c address of your NXTCurrentMeter
    #  @param self The object pointer.
    #  @param i2c_address Address of your NXTCurrentMeter.
    def __init__(self, current_address = CURRENT_ADDRESS):
        #the DIST address
        mindsensors_i2c.__init__(self, current_address >> 1)
                
    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, cmd):
        self.writeByte(self.COMMAND, int(cmd)) 
    
    ## Reads the absolute current value in milliAmps
    #  @param self The object pointer.
    def get_calibrated(self):
        try:
            return self.readIntegerSigned(self.CAL)
        except:
            print "Error: Could not read calibrated current"
            return ""
        
    ## Reads the relative current value in milliAmps
    #  @param self The object pointer.
    def get_relative(self):
        try:
            return self.readIntegerSigned(self.REL)
        except:
            print "Error: Could not read relative current"
            return ""
        
    ## Reads the reference current value in milliAmps
    #  @param self The object pointer.
    def get_reference(self):
        try:
            return self.readIntegerSigned(self.REF)
        except:
            print "Error: Could not read reference current"
            return ""
            
    ## Sets the reference current equal to the absolute current value
    #  @param self The object pointer.
    def set_reference(self):
        try:
            self.command(68)
        except:
            print "Error: Could not set reference current"
            return ""
            
## DIST: this class provides functions for DISTNx from mindsensors.com
#  for read and write operations.
class DIST(mindsensors_i2c):  
    #"""Class for the Distance Infrared Sensor"""

    DIST_ADDRESS = (0x02)
    COMMAND = 0x41
    DISTANCE = 0x42
    VOLTAGE = 0x44
#    TYPE = 0x44
   
    ## Initialize the class with the i2c address of your Dist-Nx
    #  @param self The object pointer.
    #  @param i2c_address Address of your Dist-Nx.
    def __init__(self, dist_address = DIST_ADDRESS):
        #the DIST address
        mindsensors_i2c.__init__(self, dist_address >> 1)
                
    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, command):
        self.writeByte(self.COMMAND, int(cmd)) 
    
    ## Reads the distance in millimeters
    #  @param self The object pointer.
    def get_distance(self):
        try:
            return self.readInteger(self.DISTANCE)
        except:
            print "Error: Could not read distance"
            return ""
        
    ## Reads the distance in inches
    #  @param self The object pointer.
    def get_distance_inches(self):
        try:
            d = self.get_distance()
            return d/25
        except:
            print "Error: Could not read distance"
            return ""
        
    ## Reads the voltage of the Dist-Nx
    #  @param self The object pointer.
    def get_voltage(self):
        try:
            return self.readInteger(self.VOLTAGE)
        except:
            print "Error: Could not read voltage"
            return ""  

## LSA: this class provides functions for LightSensorArray from mindsensors.com
#  for read and write operations.
class LSA(mindsensors_i2c):  
    #"""Class for the LineSensorArray"""

    LSA_ADDRESS = 0x14
    LSA_COMMAND = 0x41
    LSA_CALIBRATED = 0x42
    LSA_UNCALIBRATED = 0x6A
    
    ## Initialize the class with the i2c address of your LightSensorArray
    #  @param self The object pointer.
    #  @param i2c_address Address of your LightSensorArray.
    def __init__(self, lsa_address = LSA_ADDRESS):
        #the LSA address
        mindsensors_i2c.__init__(self, lsa_address >> 1)        
        
    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, cmd):
        self.writeByte(self.LSA_COMMAND, int(cmd)) 

    ## Calibrates the white value for the LightSensorArray
    #  @param self The object pointer.
    def LSA_White_Cal(self):
        self.command(87)
        
    ## Calibrates the black value for the LightSensorArray
    #  @param self The object pointer.
    def LSA_Black_Cal(self):
        self.command(66)
        
    ## Wakes up or turns on the LEDs of the LightSensorArray
    #  @param self The object pointer.
    def LSA_Wakeup(self):
        self.command(80)
        
    ## Puts to sleep, or turns off the LEDs of the LightSensorArray
    #  @param self The object pointer.
    def LSA_Sleep(self):
        self.command(68)
    
    ## Reads the eight(8) calibrated light sensor values of the LightSensorArray
    #  @param self The object pointer.
    def LSA_ReadRaw_Calibrated(self):
        try:
            return self.readArray(self.LSA_CALIBRATED, 8)
        except:
            print "Error: Could not read LSArray"
            return ""
    
    ## Reads the eight(8) uncalibrated light sensor values of the LightSensorArray
    #  @param self The object pointer.    
    def LSA_ReadRaw_Uncalibrated(self):
        try:
            s1 = self.readInteger(self.LSA_UNCALIBRATED)
            s2 = self.readInteger(self.LSA_UNCALIBRATED + 2)
            s3 = self.readInteger(self.LSA_UNCALIBRATED + 4)
            s4 = self.readInteger(self.LSA_UNCALIBRATED + 6)
            s5 = self.readInteger(self.LSA_UNCALIBRATED + 8)
            s6 = self.readInteger(self.LSA_UNCALIBRATED + 10)
            s7 = self.readInteger(self.LSA_UNCALIBRATED + 12)
            s8 = self.readInteger(self.LSA_UNCALIBRATED + 14)
            array = [s1, s2, s3, s4, s5, s6, s7, s8]
            return array
        except:
            print "Error: Could not read LSArray"
            return "" 

## BLOB: this class is a subclass of NXTCAM. There is no need to call this class directly.
class BLOB():

    def __init__(self, color, left, top, right, bottom):
        self.color = color
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom        

## NXTCAM: this class provides functions for models of the NXTCAM and PixyAdapter from mindsensors.com
#  for read and write operations.
class NXTCAM(mindsensors_i2c):  

    ## Default NXTCAM I2C Address 
    NXTCAM_ADDRESS = (0x02)
    ## Command Register 
    COMMAND = 0x41
    ## Number of Tracked Ojects Register. Will return a byte (0-8)
    NumberObjects = 0x42
    ## First Register Containing Tracked Object Data. This is to be read in an array
    Color = 0x43
    X_Top = 0x44
    Y_Top = 0x45
    X_Bottom = 0x46
    Y_Bottom = 0x47
    
    ## Initialize the class with the i2c address of your NXTCAM
    #  @param self The object pointer.
    #  @param i2c_address Address of your AngleSensor.
    #  @remark
    def __init__(self, nxtcam_address = NXTCAM_ADDRESS):
        mindsensors_i2c.__init__(self, nxtcam_address >> 1)        
        
    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, command):
        self.writeByte(COMMAND, int(cmd)) 
    
    ## Sort the detected objects by size
    #  @param self The object pointer.
    def sortSize(self):
        try:
            self.command(65)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Track detected colors as objects
    #  @param self The object pointer.
    def trackObject(self):
        try:
            self.command(66)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Write to image sensor registers
    #  @param self The object pointer.
    def writeImageRegisters(self):
        try:
            self.command(67)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Disable tracking
    #  @param self The object pointer.
    def stopTracking(self):
        try:
            self.command(68)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Enable tracking
    #  @param self The object pointer.
    def startTracking(self):
        try:
            self.command(69)
        except:
            print "Error: Could write command to Cam."
            return ""
       
    ## Get the color map from NXTCAM
    #  @param self The object pointer.
    def getColorMap(self):
        try:
            self.command(71)
        except:
            print "Error: Could write command to Cam."
            return ""
            
##    ## Turn on illumination
    #  @param self The object pointer.
    def illuminationOn(self):
        try:
            self.command(73)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Read to image sensor registers
    #  @param self The object pointer.
    def readImageRegisters(self):
        try:
            self.command(72)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Track detected colors as lines
    #  @param self The object pointer.
    def trackLine(self):
        try:
            self.command(76)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Ping the NXTCAM
    #  @param self The object pointer.
    def ping(self):
        try:
            self.command(80)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Reset the NXTCAM
    #  @param self The object pointer.
    def reset(self):
        try:
            self.command(82)
        except:
            print "Error: Could write command to Cam."
            return ""
      
    ## Send ColorMap to NXTCAM
    #  @param self The object pointer.
    def sendColorMap(self):
        try:
            self.command(83)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Turn off illumination
    #  @param self The object pointer.
    def illuminationOff(self):
        try:
            self.command(84)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Sort tracked objects by color
    #  @param self The object pointer.
    def sortColor(self):
        try:
            self.command(85)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Get the firmware version of the NXTCAM
    #  @param self The object pointer.
    def firmware(self):
        try:
            self.command(86)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Do not sort tracked objects
    #  @param self The object pointer.
    def sortNone(self):
        try:
            self.command(88)
        except:
            print "Error: Could write command to Cam."
            return ""
            
    ## Read the number of objects detected (0-8)
    #  @param self The object pointer.
    def getNumberObjects(self):
        try:
            return self.readByte(self.NumberObjects)
        except:
            print "Error: Could not read from Cam."
            return ""
    
    ## Reads data of the tracked object(s)
    #  @param self The object pointer.
    #  @param blobNum The number of the tracked object.
    #  @remark
    #  To use this function in your program:
    #  @code
    #  from mindsensors  import NXTCAM 
    #  ...
    #  cam = NXTCAM()
    #  cam.startTracking()
    #  cam.trackObject() 
    #  b = cam.getBlobs(1) 
    #  print "Color: " + str(b.color)
    #  print "Left: " + str(b.left)
    #  print "Top: " + str(b.top)
    #  print "Right: " + str(b.right)
    #  print "Bottom: " + str(b.bottom)    
    #  @endcode   
    def getBlobs(self, blobNum = 1):
        try:
            
            data= [0,0,0,0,0]
            blobs = self.getNumberObjects()            
            i = blobNum - 1
            if (blobNum > blobs):
                print "blobNum is greater than amount of blobs tracked."
                return 0
            else:            
                #while(i < blobs):              
                data[0] = color = self.readByte(self.Color + (i*5))  
                data[1] = left = self.readByte(self.X_Top + (i*5))
                data[2] = top = self.readByte(self.Y_Top + (i*5))
                data[3] = right = self.readByte(self.X_Bottom + (i*5))
                data[4] = bottom = self.readByte(self.Y_Bottom + (i*5))       
                return BLOB(color,left,top,right,bottom)
        except:
            print "Error: Could not read from Cam."
            return ""
            
            ## MMX: this class provides motor control functions
#  Raspberry Pi i2c baud rate must be 35000 or less to ensure proper functionality of nxtmmx.
class MMX(mindsensors_i2c):
    
    MMX_ADDRESS = (0x06)
    MMX_VOLTAGE_MULTIPLIER = 37
    
    #  Motor selection related constants
    MMX_Motor_1        =        0x01
    MMX_Motor_2        =        0x02
    MMX_Motor_Both     =        0x03

    # Motor action constants
    # stop and let the motor coast.
    MMX_Next_Action_Float   =   0x00
    # apply brakes, and resist change to tachometer
    MMX_Next_Action_Brake   =   0x01
    # apply brakes, and restore externally forced change to tachometer
    MMX_Next_Action_BrakeHold = 0x02
    
    #Direction related constants
    MMX_Direction_Forward   =   0x01
    MMX_Direction_Reverse   =   0x00

    # Tachometer related constants
    MMX_Move_Relative = 0x01
    MMX_Move_Absolute = 0x00

    # Next action (upon completion of current action)
    MMX_Completion_Wait_For   =  0x01
    MMX_Completion_Dont_Wait  = 0x00

    # Commonly used speed constants, these are just convenience constants,
    # You can use any value between 0 and 100.
    MMX_Speed_Full = 90
    MMX_Speed_Medium = 60
    MMX_Speed_Slow  = 25

    MMX_CONTROL_SPEED  =    0x01
    MMX_CONTROL_RAMP   =    0x02
    MMX_CONTROL_RELATIVE =  0x04
    MMX_CONTROL_TACHO  =    0x08
    MMX_CONTROL_BRK    =    0x10
    MMX_CONTROL_ON     =    0x20
    MMX_CONTROL_TIME  =     0x40
    MMX_CONTROL_GO   =      0x80
    
    MMX_COMMAND = 0x41
    MMX_SETPT_M1  =   0x42
    MMX_SPEED_M1  =   0x46
    MMX_TIME_M1  =    0x47
    MMX_CMD_B_M1  =   0x48
    MMX_CMD_A_M1  =   0x49

    MMX_SETPT_M2  =   0x4A
    MMX_SPEED_M2  =   0x4E
    MMX_TIME_M2   =   0x4F
    MMX_CMD_B_M2  =   0x50
    MMX_CMD_A_M2  =   0x51

    #Read registers.
    MMX_POSITION_M1 = 0x62
    MMX_POSITION_M2 = 0x66
    MMX_STATUS_M1   = 0x72
    MMX_STATUS_M2   = 0x73
    MMX_TASKS_M1    = 0x76
    MMX_TASKS_M2   =  0x77
    
    #PID control registers
    MMX_P_Kp  =  0x7A            
    MMX_P_Ki  =  0x7C            
    MMX_P_Kd  =  0x7E           
    MMX_S_Kp  =  0x80           
    MMX_S_Ki  =  0x82            
    MMX_S_Kd  =  0x84            
    MMX_PASSCOUNT  =  0x86
    MMX_PASSTOLERANCE  =  0x87
    
    ## Initialize the class with the i2c address of your NXTMMX
    #  @param self The object pointer.
    #  @param PiDrive_address Address of your NXTMMX.
    def __init__(self, mmx_address = MMX_ADDRESS):
        #the NXTMMX address
        mindsensors_i2c.__init__(self, mmx_address >> 1)       
    
    ## Writes a specified command on the command register of the NXTMMX
    #  @param self The object pointer.
    #  @param cmd The command you wish the NXTMMX to execute.    
    def command(self, cmd):
       self.writeByte(self.MMX_COMMAND, int(cmd))       
    
    ## Reads the battery voltage
    #  @param self The object pointer.
    def battVoltage(self):
        try:
            return self.readByte(self.MMX_COMMAND) * self.MMX_VOLTAGE_MULTIPLIER #37
        except:
            print "Error: Could not read voltage"
            return ""
        
    ## Reads the encoder position of the specified motor
    #  @param self The object pointer.
    #  @param motor_number Number of the motor you wish to read.
    def pos(self, motor_number):
        try:
            if motor_number == 1 :
                return self.readLongSigned(self.MMX_POSITION_M1) 
            if motor_number == 2 :
                return self.readLongSigned(self.MMX_POSITION_M2) 
        except:
            print "Error: Could not read encoder position"
            return ""
            
    ## Run the motor(s) at a set speed for an unlimited duration
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) you wish to turn.
    #  @param speed The speed at which you wish to turn the motor(s).
    def setSpeed( self, motor_number, speed ):

        ctrl = 0
        ctrl |= self.MMX_CONTROL_SPEED
        ctrl |= self.MMX_CONTROL_BRK
        
        if ( motor_number != self.MMX_Motor_Both ):
            ctrl |= self.MMX_CONTROL_GO
        if ( (motor_number & 0x01) != 0 ): 
            array = [speed, 0, 0, ctrl]
            self.writeArray( self.MMX_SPEED_M1, array)
        if ( (motor_number & 0x02) != 0 ):
            array = [speed, 0, 0, ctrl]
            self.writeArray( self.MMX_SPEED_M2, array); 
        if ( motor_number == self.MMX_Motor_Both ) :
            self.writeByte(self.MMX_COMMAND, 83)  
    
    ### @cond
    ## Stops the specified motor(s)
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) you wish to turn.
    #  @param next_action How you wish to stop the motor(s).        
    def MMX_Stop( self, motor_number, next_action ):
        
        if ( next_action == self.MMX_Next_Action_Brake or next_action == self.MMX_Next_Action_BrakeHold ):
            if (motor_number == self.MMX_Motor_1):
                self.writeByte(self.MMX_COMMAND, 65)
            if (motor_number == self.MMX_Motor_2):
                self.writeByte(self.MMX_COMMAND, 66)
            if (motor_number == self.MMX_Motor_Both):
                self.writeByte(self.MMX_COMMAND, 67)
        else:
            if (motor_number == self.MMX_Motor_1):
                self.writeByte(self.MMX_COMMAND, 97)
            if (motor_number == self.MMX_Motor_2):
                self.writeByte(self.MMX_COMMAND, 98)
            if (motor_number == self.MMX_Motor_Both):
                self.writeByte(self.MMX_COMMAND, 99)
                
    def status(self, motor_number):
        if (motor_number == 1):
            return self.readByte(self.MMX_STATUS_M1)
        if (motor_number == 2):
            return self.readByte(self.MMX_STATUS_M2)
    
    def statusBit(self, motor_number, bitno = 0):
        return (self.status(motor_number) >> bitno) & 1
    ### @endcond
                
    ## Stop the motor with abruptly with brake
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) you wish to turn.
    def brake(self, motor_number):
        self.MMX_Stop(motor_number, self.MMX_Next_Action_Brake)
            
    ## Stop the motor smoothly with float
    #  @param self The object pointer. 
    #  @param motor_number Number of the motor(s) you wish to turn.
    def float(self, motor_number):
        self.MMX_Stop(motor_number, self.MMX_Next_Action_Float)
        
    ## Stop the motor abruptly and hold the current position
    #  @param self The object pointer. 
    #  @param motor_number Number of the motor(s) you wish to turn.
    def hold(self, motor_number):
        self.MMX_Stop(motor_number, self.MMX_Next_Action_BrakeHold)
        
    ## Check if the motor is running
    #  @param self The object pointer.
    def isBusy(self, motor_number):
        return self.statusBit(motor_number, 0) == 1 or self.statusBit(motor_number, 1) == 1 or self.statusBit(motor_number, 3) == 1 or self.statusBit(motor_number, 6) == 1
    
    ## Wait until the motor is no longer running
    #  @param self The object pointer.
    #  @param timeout The timeout value as a factor of 10ms.
    def waitUntilNotBusy(self, motor_number, timeout=-1):
        while(self.isBusy(motor_number)):
            time.sleep(.01)
            timeout -= 1
            if(timeout == 0):
                return 1
            if(timeout <-5):
                timeout = -1
            pass
        return 0
    
    ## Check if the motor is stalled
    #  @param self The object pointer.
    def isStalled(self, motor_number):
        return self.statusBit(motor_number, 7) == 1
    
    ## Check if the motor is overloaded
    #  @param self The object pointer.  
    def isOverloaded(self):
        return self.statusBit(motor_number, 5) == 1
    
    ## Run the motor for a specific time in seconds
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) you wish to turn.
    #  @param secs The number of seconds to run the motor.
    #  @param speed The speed at which to turn the motor.
    #  @param brakeOnCompletion Choose to brake or float the motor upon completion with True (brake) or False (float). 
    #  @param waitForCompletion Wait until the motor is finished running before continuing the program.    
    def runSecs( self, motor_number, secs, speed, brakeOnCompletion = False, waitForCompletion = False ):        
        ctrl = 0
        ctrl |= self.MMX_CONTROL_SPEED
        ctrl |= self.MMX_CONTROL_TIME

        if ( brakeOnCompletion == True ):
            ctrl |= self.MMX_CONTROL_BRK
        if ( motor_number != self.MMX_Motor_Both ):
            ctrl |= self.MMX_CONTROL_GO
        if ( (motor_number & 0x01) != 0 ):
            array = [speed, secs, 0, ctrl]
            self.writeArray( self.MMX_SPEED_M1, array) 
        if ( (motor_number & 0x02) != 0 ) :
            array = [speed, secs, 0, ctrl]
            self.writeArray( self.MMX_SPEED_M2, array)
        if ( motor_number == self.MMX_Motor_Both ) :
            self.writeByte(self.MMX_COMMAND, 83)        
        if ( waitForCompletion == True ):
            time.sleep(0.050);  # this delay is required for the status byte to be available for reading.
            self.MMX_WaitUntilTimeDone(motor_number)
    
    ### @cond
    ## Waits until the specified time for the motor(s) to run is completed
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) to wait for.
    def MMX_WaitUntilTimeDone(self,motor_number):
        while self.MMX_IsTimeDone(motor_number) != True:
            time.sleep(0.050)        
        
    ## Checks to ensure the specified time for the motor(s) to run is completed.
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) to check.
    def  MMX_IsTimeDone(self, motor_number):
        if ( motor_number == self.MMX_Motor_1 ):
            result = self.readByte(self.MMX_STATUS_M1)
            # look for the time bit to be zero.
            if (( result & 0x40 ) == 0 ):
                return True         
        elif ( motor_number == self.MMX_Motor_2 ) :
            result = self.readByte(self.MMX_STATUS_M2)
            # look for the time bit to be zero.
            if (( result & 0x40 ) == 0 ):
                return True
        elif ( motor_number == self.MMX_Motor_Both ):
            result = self.readByte(self.MMX_STATUS_M1)
            result2 = self.readByte(self.MMX_STATUS_M2)
            # look for both time bits to be zero
            if (((result & 0x40) == 0) &((result2 & 0x40) == 0) ):
                return True
        else :
            return False
    ### @endcond
            
    ## Run the motor for a specific amount of degrees
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) you wish to turn.
    #  @param degs The number of degrees to run the motor(s).
    #  @param speed The speed at which to turn the motor(s).
    #  @param brakeOnCompletion Choose to brake or float the motor upon completion with True (brake) or False (float).
    #  @param holdOnCompletion Choose to hold the motor position upon completion with True (hold) or False (release).
    #  @param waitForCompletion Tells the program when to handle the next line of code.
    def runDegs(self, motor_number, degs, speed, brakeOnCompletion = False, holdOnCompletion = False, waitForCompletion = False):
        ctrl = 0
        ctrl |= self.MMX_CONTROL_SPEED
        ctrl |= self.MMX_CONTROL_TACHO
        ctrl |= self.MMX_CONTROL_RELATIVE
        
        d = degs
        t4 = (d/0x1000000)
        t3 = ((d%0x1000000)/0x10000)
        t2 = (((d%0x1000000)%0x10000)/0x100)
        t1 = (((d%0x1000000)%0x10000)%0x100)
        
        if ( brakeOnCompletion == True ):
            ctrl |= self.MMX_CONTROL_BRK
        if ( holdOnCompletion == True ):
            ctrl |= self.MMX_CONTROL_BRK
            ctrl |= self.MMX_CONTROL_ON
        if ( motor_number != self.MMX_Motor_Both ):
            ctrl |= self.MMX_CONTROL_GO        
        if ( (motor_number & 0x01) != 0 ):
            array = [t1, t2, t3, t4, speed, 0, 0, ctrl]
            self.writeArray(self.MMX_SETPT_M1, array) 
        if ( (motor_number & 0x02) != 0 ) :
            array = [t1, t2, t3, t4, speed, 0, 0, ctrl]
            self.writeArray(self.MMX_SETPT_M2, array) 
        if ( motor_number == self.MMX_Motor_Both ) :
            self.writeByte(self.MMX_COMMAND, 83)         
        if ( waitForCompletion == True ):
            time.sleep(0.050);  # this delay is required for the status byte to be available for reading.
            self.MMX_WaitUntilTachoDone(motor_number)
            
    ## Run the motor for a specific amount of rotations
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) you wish to turn.
    #  @param rotations The number of rotations to run the motor(s).
    #  @param speed The speed at which to turn the motor(s).
    #  @param brakeOnCompletion Choose to brake or float the motor upon completion with True (brake) or False (float).
    #  @param holdOnCompletion Choose to hold the motor position upon completion with True (hold) or False (release).
    #  @param waitForCompletion Tells the program when to handle the next line of code.
    def runRotations(self, motor_number, rotations, speed, brakeOnCompletion = False, holdOnCompletion = False, waitForCompletion = False):
        ctrl = 0
        ctrl |= self.MMX_CONTROL_SPEED
        ctrl |= self.MMX_CONTROL_TACHO
        ctrl |= self.MMX_CONTROL_RELATIVE
        
        d = rotations * 360
        
        t4 = (d/0x1000000)
        t3 = ((d%0x1000000)/0x10000)
        t2 = (((d%0x1000000)%0x10000)/0x100)
        t1 = (((d%0x1000000)%0x10000)%0x100)
        
        if ( brakeOnCompletion == True ):
            ctrl |= self.MMX_CONTROL_BRK
        if ( holdOnCompletion == True ):
            ctrl |= self.MMX_CONTROL_BRK
            ctrl |= self.MMX_CONTROL_ON
        if ( motor_number != self.MMX_Motor_Both ):
            ctrl |= self.MMX_CONTROL_GO
        if ( (motor_number & 0x01) != 0 ):
            array = [t1, t2, t3, t4, speed, 0, 0, ctrl]
            self.writeArray(self.MMX_SETPT_M1, array) 
        if ( (motor_number & 0x02) != 0 ) :
            array = [t1, t2, t3, t4, speed, 0, 0, ctrl]
            self.writeArray(self.MMX_SETPT_M2, array) 
        if ( motor_number == self.MMX_Motor_Both ) :
            self.writeByte(self.MMX_COMMAND, 83)        
        if ( waitForCompletion == True ):
            time.sleep(0.050);  # this delay is required for the status byte to be available for reading.
            self.MMX_WaitUntilTachoDone(motor_number)

    ## Run the motor for a specific amount of rotations
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) you wish to turn.
    #  @param pos The encoder value to which to run the motor(s).
    #  @param speed The speed at which to turn the motor(s).
    #  @param brakeOnCompletion Choose to brake or float the motor upon completion with True (brake) or False (float).
    #  @param holdOnCompletion Choose to hold the motor position upon completion with True (hold) or False (release).
    #  @param waitForCompletion Tells the program when to handle the next line of code.
    def runEncoderPos(self, motor_number, pos, speed, brakeOnCompletion = False, holdOnCompletion = False, waitForCompletion = False):
        ctrl = 0
        ctrl |= self.MMX_CONTROL_SPEED
        ctrl |= self.MMX_CONTROL_TACHO
        d = pos
        
        t4 = (d/0x1000000)
        t3 = ((d%0x1000000)/0x10000)
        t2 = (((d%0x1000000)%0x10000)/0x100)
        t1 = (((d%0x1000000)%0x10000)%0x100)
        
        if ( brakeOnCompletion == True ):
            ctrl |= self.MMX_CONTROL_BRK
        if ( holdOnCompletion == True ):
            ctrl |= self.MMX_CONTROL_BRK
            ctrl |= self.MMX_CONTROL_ON
        if ( motor_number != self.MMX_Motor_Both ):
            ctrl |= self.MMX_CONTROL_GO
        if ( (motor_number & 0x01) != 0 ):
            array = [t1, t2, t3, t4, speed, 0, 0, ctrl]
            self.writeArray(self.MMX_SETPT_M1, array) 
        if ( (motor_number & 0x02) != 0 ):
            array = [t1, t2, t3, t4, speed, 0, 0, ctrl]
            self.writeArray(self.MMX_SETPT_M2, array) 
        if ( motor_number == self.MMX_Motor_Both ) :
            self.writeByte(self.MMX_COMMAND, 83)         
        if ( waitForCompletion == True ):
            time.sleep(0.050);  # this delay is required for the status byte to be available for reading.
            self.MMX_WaitUntilTachoDone(motor_number) 
    
    ### @cond
    ## Waits until the specified tacheomter count for the motor(s) to run is reached.
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) to wait for.
    def MMX_WaitUntilTachoDone(self,motor_number):
        while self.MMX_IsTachoDone(motor_number) != True:
            time.sleep(0.050)        
        
    ## Checks to ensure the specified tacheomter count for the motor(s) to run is reached.
    #  @param self The object pointer.
    #  @param motor_number Number of the motor(s) to check. 
    def  MMX_IsTachoDone(self, motor_number):
        if ( motor_number == self.MMX_Motor_1 ):
            result = self.readByte(self.MMX_STATUS_M1)
            # look for the time bit to be zero.
            if (( result & 0x08 ) == 0 ):
                return True         
        elif ( motor_number == self.MMX_Motor_2 ) :
            result = self.readByte(self.MMX_STATUS_M2)
            # look for the time bit to be zero.
            if (( result & 0x08 ) == 0 ):
                return True
        elif ( motor_number == self.MMX_Motor_Both ):
            result = self.readByte(self.MMX_STATUS_M1)
            result2 = self.readByte(self.MMX_STATUS_M2)
            # look for both time bits to be zero
            if (((result & 0x08) == 0) & ((result2 & 0x08) == 0) ):
                return True
        else :
            return False
    ### @endcond
            
    ## Writes user specified values to the PID control registers
    #  @param self The object pointer.
    #  @param Kp_tacho Proportional-gain of the encoder position of the motor.
    #  @param Ki_tacho Integral-gain of the encoder position of the motor.
    #  @param Kd_tacho Derivative-gain of the encoder position of the motor.
    #  @param Kp_speed Proportional-gain of the speed of the motor.
    #  @param Ki_speed Integral-gain of the speed of the motor.
    #  @param Kd_speed Derivative-gain of the speed of the motor.
    #  @param passcount The number of times the encoder reading should be within tolerance.
    #  @param tolerance The tolerance (in ticks) for encoder positioning .
    def SetPerformanceParameters(self, Kp_tacho, Ki_tacho, Kd_tacho, Kp_speed, Ki_speed, Kd_speed, passcount, tolerance):        
        Kp_t1 = Kp_tacho%0x100
        Kp_t2 = Kp_tacho/0x100      
        Ki_t1 = Ki_tacho%0x100
        Ki_t2 = Ki_tacho/0x100
        Kd_t1 = Kd_tacho%0x100
        Kd_t2 = Kd_tacho/0x100
        Kp_s1 = Kp_speed%0x100        
        Kp_s2 = Kp_speed/0x100
        Ki_s1 = Ki_speed%0x100 
        Ki_s2 = Ki_speed/0x100
        Kd_s1 = Kd_speed%0x100
        Kd_s2 = Kd_speed/0x100
        print "Kp_t1: " + str(Kp_t1)
        print "Kp_t2: " + str(Kp_t2)
        print "Ki_t1: " + str(Ki_t1)
        print "Ki_t2: " + str(Ki_t2)
        print "Kd_t1: " + str(Kd_t1)
        print "Kd_t2: " + str(Kd_t2)
        print "Kp_s1: " + str(Kp_s1)
        print "Kp_s2: " + str(Kp_s2)
        print "Ki_s1: " + str(Ki_s1)
        print "Ki_s2: " + str(Ki_s2)
        print "Kd_s1: " + str(Kd_s1)
        print "Kd_s2: " + str(Kd_s2)
        passcount = passcount
        tolerance = tolerance
        array = [Kp_t1 , Kp_t2 , Ki_t1, Ki_t2, Kd_t1, Kd_t2, Kp_s1, Kp_s2, Ki_s1, Ki_s2, Kd_s1, Kd_s2, passcount, tolerance]
        self.writeArray(self.MMX_P_Kp, array)
        
    ## Reads the values of the PID control registers
    #  @param self The object pointer.
    def ReadPerformanceParameters(self):    
        try:
            print "Pkp: " + str(self.readInteger(self.MMX_P_Kp))
            print "Pki: " + str(self.readInteger(self.MMX_P_Ki))
            print "Pkd: " + str(self.readInteger(self.MMX_P_Kd))
            print "Skp: " + str(self.readInteger(self.MMX_S_Kp))
            print "Ski: " + str(self.readInteger(self.MMX_S_Ki))
            print "Skd: " + str(self.readInteger(self.MMX_S_Kd))
            print "Passcount: " + str(self.MMX_PASSCOUNT)
            print "Tolerance: " + str(self.MMX_PASSTOLERANCE)
        except:
            print "Error: Could not read PID values"
            return ""            

## NXTSERVO: this class provides servo motor control functions
class NXTSERVO(mindsensors_i2c):
    
    # Default PFMate i2c address
    NXTSERVO_ADDRESS = (0xB0)
    
    # Voltage multiplier
    NXTSERVO_VBATT_SCALER = 41
    
    # Register addresses
    NXTSERVO_COMMAND = 0x41    
    NXTSERVO_VBATT = 0x62
    
    ## Initialize the class with the i2c address of your NXTServo
    #  @param self The object pointer.
    #  @param PiDrive_address Address of your NXTServo.
    def __init__(self, nxtservo_address = NXTSERVO_ADDRESS):
        mindsensors_i2c.__init__(self, nxtservo_address >> 1)       
    
    ## Writes a specified command on the command register of the NXTServo
    #  @param self The object pointer.
    #  @param cmd The command you wish the NXTServo to execute.    
    def command(self, cmd):
       self.writeByte(self.NXTSERVO_COMMAND, int(cmd))       

    ## Reads NXTServo battery voltage in millivolts
    #  @param self The object pointer.  
    def battVoltage(self):
        try:
            return self.readByte(self.NXTSERVO_VBATT) * self.NXTSERVO_VBATT_SCALER
        except:
            print "Error: Could not read battery voltage"
            return ""
            
    ## Sets the position of a user defined servo
    #  @param self The object pointer
    #  @param servoNumber The number of the servo you wish to move.
    #  @param position The position to set the servo.
    def setPosition(self, servoNumber, position):
        reg = 64 + (servoNumber*2) 
        p1 = position%256
        p2 = position/256
        array = [p1, p2]
        self.writeArray(reg, array)

    ## Sets the default neutral position of a user defined servo
    #  @param self The object pointer
    #  @param servoNumber The number of the servo you wish to set to the default position.
    def setNeutral(self, servoNumber):
        self.command(73)
        time.sleep(.1)
        servo = servoNumber + 48
        self.command(servo) 

## PFMATE: this class provides motor control functions
class PFMATE(mindsensors_i2c):
    
    # Default PFMate i2c address
    PFMATE_ADDRESS = (0x48)
    
    # Operation constants
    PFMATE_FLOAT = 0
    PFMATE_FORWARD = 1
    PFMATE_REVERSE = 2
    PFMATE_BRAKE = 3
    
    # Channel constants
    PFMATE_CHANNEL1 = 1
    PFMATE_CHANNEL2 = 2
    PFMATE_CHANNEL3 = 3
    PFMATE_CHANNEL4 = 4
    
    # Register addresses
    PFMATE_COMMAND  = 0x41
    PFMATE_CHANNEL  =   0x42    # 1 2 3 4 
    PFMATE_MOTORS    =   0x43   # both or A or B (0/1/2)
    PFMATE_OPER_A =    0x44     # float/forward/reverse/brake (0/1/2/3)
    PFMATE_SPEED_A   =   0x45   # 0-7
    PFMATE_OPER_B =    0x46     # float/forward/reverse/brake (0/1/2/3)
    PFMATE_SPEED_B   =   0x47   # 0-7
    
    ## Initialize the class with the i2c address of your PFMate
    #  @param self The object pointer.
    #  @param PiDrive_address Address of your PFMate.
    def __init__(self, pfmate_address = PFMATE_ADDRESS):
        #the NXTMMX address
        mindsensors_i2c.__init__(self, pfmate_address >> 1)       
    
    ## Writes a specified command on the command register of the PFMate
    #  @param self The object pointer.
    #  @param cmd The command you wish the PFMate to execute.    
    def command(self, cmd):
       self.writeByte(self.PFMATE_COMMAND, int(cmd))       

    ## Controls both motors
    #  @param self The object pointer.
    #  @param channel Communication channel to transmit to LEGO PF IR receiver.
    #  @param operationA Operation command for motor A.     
    #  @param speedA Speed of motor A.    
    #  @param operationB Operation command for motor B.     
    #  @param speedB Speed of motor B.    
    def controlBothMotors(self, channel, operationA, speedA, operationB, speedB):
        array = [channel, 0x00, operationA, speedA, operationB, speedB]
        self.writeArray(self.PFMATE_CHANNEL, array)
        time.sleep(.1)
        self.command(71)
        time.sleep(.1)
        
    ## Controls motor A
    #  @param self The object pointer.
    #  @param channel Communication channel to transmit to LEGO PF IR receiver.
    #  @param operationA Operation command for motor A.     
    #  @param speedA Speed of motor A.    
    def controlMotorA(self, channel, operationA, speedA):
        array = [channel, 0x01, operationA, speedA]
        self.writeArray(self.PFMATE_CHANNEL, array)
        time.sleep(.1)
        self.command(71)
        time.sleep(.1)
        
    ## Controls motor B
    #  @param self The object pointer.
    #  @param channel Communication channel to transmit to LEGO PF IR receiver.
    #  @param operationB Operation command for motor B.     
    #  @param speedB Speed of motor B.    
    def controlMotorB(self, channel, operationB, speedB):
        array = [channel, 0x02]
        array2 = [operationB, speedB]
        self.writeArray(self.PFMATE_CHANNEL, array)
        self.writeArray(self.PFMATE_OPER_B, array2)
        time.sleep(.1)
        self.command(71)
        time.sleep(.1)        

## PPS58: this class provides functions for PPS58 from mindsensors.com
#  for read and write operations.
class PPS58(mindsensors_i2c):  
    #"""Class for the PPS58 pressure Sensor"""

    PPS58_ADDRESS = (0x18)
    COMMAND = 0x41
    UNIT = 0x42
    ABS = 0x43
    GAUGE = 0x45
    REF = 0x47
    RAW = 0x53
   
    ## Initialize the class with the i2c address of your PPS58
    #  @param self The object pointer.
    #  @param i2c_address Address of your PPS58.
    def __init__(self, pps58_address = PPS58_ADDRESS):
        #the DIST address
        mindsensors_i2c.__init__(self, pps58_address >> 1)
                
    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, cmd):
        self.writeByte(self.COMMAND, int(cmd)) 
    
    ## Reads a value assigned to the unit of pressure cureently in use on the PPS58
    #  @param self The object pointer.
    def get_unit(self):
        try:
            return self.readByte(self.UNIT)
        except:
            print "Error: Could not read unit value"
            return ""
    
    ## Reads the absolute pressure of the PPS58
    #  @param self The object pointer.
    def get_absolute(self):
        try:
            return self.readIntegerSigned(self.ABS)
        except:
            print "Error: Could not read absolute pressure"
            return ""
        
    ## Reads the gauge, or relative, pressure of the PPS58
    #  @param self The object pointer.
    def get_gauge(self):
        try:
            return self.readIntegerSigned(self.GAUGE)
        except:
            print "Error: Could not read gauge pressure"
            return ""
        
    ## Reads the reference pressure of the PPS58
    #  @param self The object pointer.
    def get_reference(self):
        try:
            return self.readIntegerSigned(self.REF)
        except:
            print "Error: Could not read reference pressure"
            return ""
            
    ## Reads the raw pressure value of the PPS58
    #  @param self The object pointer.
    def get_raw(self):
        try:
            return self.readLongSigned(self.RAW)
        except:
            print "Error: Could not read raw pressure"
            return ""
            
    ## Sets the reference pressure to the current absolute pressure value
    #  @param self The object pointer.
    def set_reference(self):
        try:
            self.command(68)
        except:
            print "Error: Could not set reference pressure"
            return ""
            
    ## Sets the unit of measure to pounds per square inch
    #  @param self The object pointer.
    def set_unit_PSI(self):
        try:
            self.command(80)
        except:
            print "Error: Could not set PSI as unit"
            return ""
            
    ## Sets the unit of measure to millibar
    #  @param self The object pointer.
    def set_unit_mbar(self):
        try:
            self.command(98)
        except:
            print "Error: Could not set millibar as unit"
            return ""
            
    ## Sets the unit of measure to kilopascal
    #  @param self The object pointer.
    def set_unit_kpascal(self):
        try:
            self.command(107)
        except:
            print "Error: Could not set kilopascal as unit"
            return ""  

## Volt: this class provides functions for NXTVoltMeter from mindsensors.com
#  for read and write operations.
class VOLT(mindsensors_i2c):  
    #"""Class for the NXTVoltMeter Sensor"""

    VOLT_ADDRESS = (0x26)
    COMMAND = 0x41
    CAL = 0x43
    REL = 0x45
    REF = 0x47
   
    ## Initialize the class with the i2c address of your NXTVoltMeter
    #  @param self The object pointer.
    #  @param i2c_address Address of your NXTVoltMeter.
    def __init__(self, volt_address = VOLT_ADDRESS):
        #the DIST address
        mindsensors_i2c.__init__(self, volt_address >> 1)
                
    ## Writes a value to the command register
    #  @param self The object pointer.
    #  @param commands Value to write to the command register.
    def command(self, cmd):
        self.writeByte(self.COMMAND, int(cmd)) 
    
    ## Reads the absolute voltage of the NXTVoltMeter
    #  @param self The object pointer.
    def get_calibrated(self):
        try:
            return self.readIntegerSigned(self.CAL)
        except:
            print "Error: Could not read calibrated voltage"
            return ""
        
    ## Reads the relative voltage of the NXTVoltMeter
    #  @param self The object pointer.
    def get_relative(self):
        try:
            return self.readIntegerSigned(self.REL)
        except:
            print "Error: Could not read relative voltage"
            return ""
        
    ## Reads the reference voltage of the NXTVoltMeter
    #  @param self The object pointer.
    def get_reference(self):
        try:
            return self.readIntegerSigned(self.REF)
        except:
            print "Error: Could not read reference voltage"
            return ""
            
    ## Sets the reference voltage to the current absolute voltage value
    #  @param self The object pointer.
    def set_reference(self):
        try:
            self.command(68)
        except:
            print "Error: Could not set reference voltage"
            return ""