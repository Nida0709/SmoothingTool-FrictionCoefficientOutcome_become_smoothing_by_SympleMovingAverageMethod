import sys
import os
import pandas as pd
import tkinter.filedialog
from tkinter import messagebox
import csv
import pandas
import glob

from requests import head
from . import filemaker as fm

def AsItIs(SlidingTime, FrictionForce, FrictionCoefficient, Temperature):
  #DB as it is
  AfterSlidingTime = []
  AfterFrictionForce = []
  AfterFrictionCoefficient = []
  AfterTemperature = []
  for i in range(len(SlidingTime)):
    AfterSlidingTime.append(SlidingTime[i])
    AfterFrictionForce.append(FrictionForce[i])
    AfterFrictionCoefficient.append(FrictionCoefficient[i])
    AfterTemperature.append(Temperature[i])
  return AfterSlidingTime, AfterFrictionForce, AfterFrictionCoefficient, AfterTemperature

def SimpleMovingAverage(SlidingTime, FrictionForce, FrictionCoefficient, Temperature, delta):
  from .calcbox import SimpleMovingAverage as SMA
  #DB → 移動平均
  temp_AfterFrictionForce = SMA.SMAcalc(SlidingTime, FrictionForce, delta)
  temp_AfterFrictionCoefficient = SMA.SMAcalc(SlidingTime, FrictionCoefficient, delta)
  #DB(Column) → Output_DB
  AfterSlidingTime = []
  AfterFrictionForce = []
  AfterFrictionCoefficient = []
  AfterTemperature = []
  for i in range(len(SlidingTime)):
    AfterSlidingTime.append(SlidingTime[i])
    AfterFrictionForce.append(temp_AfterFrictionForce[i])
    AfterFrictionCoefficient.append(temp_AfterFrictionCoefficient[i])
    AfterTemperature.append(Temperature[i])
  return AfterSlidingTime, AfterFrictionForce, AfterFrictionCoefficient, AfterTemperature

def SavitzkyGolay(SlidingTime, FrictionForce, FrictionCoefficient, Temperature, delta, degree):
  from scipy import signal
  #DB → Savitzky-Golay Method
  temp_AfterFrictionForce = signal.savgol_filter(FrictionForce, delta, int(degree))
  temp_AfterFrictionCoefficient = signal.savgol_filter(FrictionCoefficient, delta, int(degree))
  #DB(Column) → Output_DB
  AfterSlidingTime = []
  AfterFrictionForce = []
  AfterFrictionCoefficient = []
  AfterTemperature = []
  for i in range(len(SlidingTime)):
    AfterSlidingTime.append(SlidingTime[i])
    AfterFrictionForce.append(temp_AfterFrictionForce[i])
    AfterFrictionCoefficient.append(temp_AfterFrictionCoefficient[i])
    AfterTemperature.append(Temperature[i])
  return AfterSlidingTime, AfterFrictionForce, AfterFrictionCoefficient, AfterTemperature


def main_logic(targetPath=None, savePath=None, frag_method=None, method_name=None, delta=None, degree=None):
  fileList = glob.glob(targetPath + os.sep + '*.csv')      #Get reference data path → input "fileList" variable
  if len(fileList) == 0:
    messagebox.showerror('error', 'Caution! The Browse have no data.\nClose system.')
    sys.exit()
  if not os.path.exists(savePath + os.sep + method_name):
    os.makedirs(savePath + os.sep + method_name)    #Make fold
  for count_fL in range(len(fileList)):     #count_fL = count_fileList
    DB_Outcome = []
    data_Path = fileList[count_fL]
    with open(data_Path, encoding='shift-jis') as f:
      csvreader = csv.reader(f)
      DB = [row for row in csvreader]
    SlidingTime, FrictionForce, FrictionCoefficient, Temperature, OtherData = fm.spritData(DB)        #Split data

    if frag_method == 0:        #As it is
      AfterSlidingTime, AfterFrictionForce, AfterFrictionCoefficient, AfterTemperature =\
        AsItIs(SlidingTime, FrictionForce, FrictionCoefficient, Temperature)
    elif frag_method == 1:        #As it is
      AfterSlidingTime, AfterFrictionForce, AfterFrictionCoefficient, AfterTemperature =\
        AsItIs(SlidingTime, FrictionForce, FrictionCoefficient, Temperature)
    elif frag_method == 2:        #Simple Moving Average(delta X point)
      AfterSlidingTime, AfterFrictionForce, AfterFrictionCoefficient, AfterTemperature =\
        SimpleMovingAverage(SlidingTime, FrictionForce, FrictionCoefficient, Temperature, delta)
    elif frag_method == 3:        #Savitzky-Golay(X degree, delta Y point)
      AfterSlidingTime, AfterFrictionForce, AfterFrictionCoefficient, AfterTemperature =\
        SavitzkyGolay(SlidingTime, FrictionForce, FrictionCoefficient, Temperature, delta, degree)
    else:
      messagebox.showerror('error', 'Caution! There is no data in Method index.\nClose system.')
      sys.exit()

    for i in range(len(OtherData)):   #Make DB for output
      DB_Outcome.append([OtherData[i][0], OtherData[i][1], OtherData[i][2], OtherData[i][3]])
    for i in range(len(AfterSlidingTime)):
      DB_Outcome.append([AfterSlidingTime[i], AfterFrictionForce[i], AfterFrictionCoefficient[i], AfterTemperature[i]])
    if method_name == 0:
      pass
    fileName = fm.make_fileName(OtherData, data_Path, method_name, savePath)    #DB→make File Name
    new_fileName = method_name + os.sep + fileName

    def export_DB(dataPath, DB, savePath):
      df = pandas.DataFrame(DB)
      df.to_excel(savePath + os.sep + dataPath, index=False, header=False)

    def export_DB_CSV(dataPath, DB, savePath):
      dataPath = dataPath.replace('xlsx', 'csv')
      df = pd.DataFrame(DB)
      df.to_csv(savePath + os.sep + dataPath, encoding='shift-jis', index=False, header=False)

    
    if frag_method == 0:
      export_DB_CSV(new_fileName, DB_Outcome, savePath)
      export_DB_CSV(fileName, DB_Outcome, savePath)
    else:
      export_DB(new_fileName, DB_Outcome, savePath)
      export_DB(fileName, DB_Outcome, savePath)
    print(str(count_fL+1) + ' of ' + str(len(fileList)) + ' :seved [' + fileName + ']')
  messagebox.showinfo('complete', 'All process is done\nstop Running')



if __name__ == '__main__':
  targetPath = '              '       #Must fill in
  savePath = '              '        #Must fill in
  main_logic(targetPath=targetPath, savePath=savePath)





#UPDATE LOG

#1.0.0 基本的な設計
#1.1.0 関数の数を減らすことでupdateしやすく整理
#1.1.1 数値計算エラー修正,自作モジュールに一部移動