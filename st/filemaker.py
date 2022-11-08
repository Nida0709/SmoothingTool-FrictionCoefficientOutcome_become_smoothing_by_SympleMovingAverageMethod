def spritData(DB):
  SlidingTime = []
  FrictionForce = []
  FrictionCoefficient = []
  Temperature = []
  OtherData = []
  for i in range(len(DB)-20):     #Split data
    SlidingTime.append(float(DB[i+20][0]))
    FrictionForce.append(float(DB[i+20][1]))
    FrictionCoefficient.append(float(DB[i+20][2]))
    Temperature.append(float(DB[i+20][3]))
  for i in range(20):
    if len(DB[i]) == 4:
      OtherData.append([DB[i][0], DB[i][1], DB[i][2], DB[i][3]])
    elif len(DB[i]) == 2:
      OtherData.append([DB[i][0], DB[i][1], "", ""])
    elif len(DB[i]) == 1:
      OtherData.append([DB[i][0], "", "", ""])
    elif len(DB[i]) == 0:
      OtherData.append(["", "", "", ""])
  for i in range(3, 7):
    OtherData[i][1] = float(OtherData[i][1])
  for i in range(9, 12):
    OtherData[i][1] = float(OtherData[i][1])
  OtherData[14][1] = float(OtherData[14][1])
  return SlidingTime, FrictionForce, FrictionCoefficient, Temperature, OtherData

def make_fileName(OtherData, data_Path, method_name, save_Path):
    import os
    fileName = os.path.basename(data_Path)
    if "cnf-fr9" in fileName:   #Datamine Material
      Material = "cnf-fr9"
    elif "cnf-fr10" in fileName:
      Material = "cnf-fr10"
    elif "cnf-fr11" in fileName:
      Material = "cnf-fr11"
    elif "cnf-fr12" in fileName:
      Material = "cnf-fr12"
    elif "cnf-fr15" in fileName:
      Material = "cnf-fr15"
    elif "Al+Si (鋳造)" in fileName:
      Material = "Al+Si (鋳造法)"
    elif "Al+Si" in fileName:
      Material = "Al+Si (粉末固化押出)"
    elif "Pure Al (鋳造)" in fileName:
      Material = "Pure Al (鋳造法)"
    elif "Pure Al" in fileName:
      Material = "Pure Al (粉末固化押出)"
    elif "CuO" in fileName:
      Material = "AZ31-CuO"
    elif "Mg-Zn-Si-CuO" in fileName:
      Material = 'Mg-Zn-Si-CuO'
    elif "ImgFric" in fileName:
      Material = "ImgFric"
    else:
      Material = "NotIndexInMaterialList"
    #試験荷重の決定
    if Material == 'ImgFric':
      weight = 'a=' + str(OtherData[9][1])
    else:
      weight = str(OtherData[9][1]) + "g"
    #試験線速度の決定
    if OtherData[11][1] == 9.5:
      Speed = "3mms"
    elif OtherData[11][1] == 63.7 and OtherData[10][1] == 0:
      Speed = "0mms"
    elif OtherData[11][1] == 63.7 and OtherData[10][1] == 3:
      Speed = "20mms"
    elif OtherData[11][1] == 95.5 and OtherData[10][1] == 1:
      Speed = "10mms"
    elif OtherData[11][1] == 191 and OtherData[10][1] == 3:
      Speed = "60mms"  
    #elif OtherData[11][1] == 31.8:
      #Speed = "10mms"
    #elif OtherData[11][1] == 318:
      #Speed = "100mms"
    elif OtherData[11][1] == 955 and OtherData[10][1] == 1:
      Speed = "100mms"
    elif Material == 'ImgFric':
      Speed = 'b=' + str(OtherData[10][1])
    else:
      Speed = "NotIndexInSpeedList"
    #末尾nの決定
    if method_name == '無変換(CSV)':
      for n in range(1, 20000):
        #ファイルがあるか確認
        if not os.path.isfile(save_Path + os.sep +  method_name + os.sep + method_name + "_" + Material + "_" \
                    + weight + "_" + Speed + "_" + str(n) + ".csv"):
          new_fileName = method_name + "_" + Material + "_" + weight + "_" + Speed + "_" + str(n) + ".csv"
          break
    else:
      for n in range(1, 20000):
        #ファイルがあるか確認
        if not os.path.isfile(save_Path + os.sep +  method_name + os.sep + method_name + "_" + Material + "_" \
                    + weight + "_" + Speed + "_" + str(n) + ".xlsx"):
          new_fileName = method_name + "_" + Material + "_" + weight + "_" + Speed + "_" + str(n) + ".xlsx"
          break
    return new_fileName