import time

from states import States

bloodConductivity = 0
bloodSensor = 0
insulinCount = 0
insulinReservoirConnected = True
insulinReservoirLevel = 100
bloodSensorFunctional = True
pumpFunctional = True
batteryLevel = 0
needleInsulinContained = 0
needleConnected = True
manualButton = False

pumpSelfTest = False
bloodSensorSelfTest = False
pumpActivate = True

currentState = States.INSULIN_PUMP_STATE
clock = 0
if __name__ == '__main__':
    while clock < 6:
        if pumpActivate & insulinReservoirConnected & bloodSensorFunctional & needleConnected:
            insulinCount+=10
            needleInsulinContained+=10
            bloodSensor += insulinCount
            bloodConductivity = bloodSensor/10
            insulinReservoirLevel-=10
        if clock>2:
            needleConnected = False
        time.sleep(1)
        if not needleConnected:
            print("Needle Disconnected!\n")
            pumpFunctional = False
        print(str(bloodConductivity) + " mmol/L \nInsulin Count:"+str(insulinCount) +"\nPump is Connected:" +str(pumpFunctional) +"\n")


        clock+=1

    # if(currentState == States.INSULIN_PUMP_STATE):
    #     pumpSelfTest = True
    # elif (currentState == States.RUN):
    #
    #
    # elif (currentState == States.MANUAL):
    #
    # elif (currentState == States.SUGAR_LOW):
    #
    # elif (currentState == States.SUGAR_HIGH):
    #
    # elif (currentState == States.STARTUP):
    #
    # elif (currentState == States.RESET):
    #
    # elif (currentState == States.TEST):

