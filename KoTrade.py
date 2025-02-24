import sys
from PyQt5.QtWidgets import *
from PyQt5.QAxContainer import * #QAxWidget 사용하려고
from PyQt5.QtCore import *


class kotrade:
    def __init__(self): #모든 객체는 생성자가 있음
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1") #만들고 싶은 ocx 객체 이름 KHOPENAPI.KHOpenAPICtrl.1 입력
        self.ocx.OnEventConnect.connect(self._handler_login)
    
    
    # Login
    def CommConnect(self):
        self.ocx.dynamicCall("CommConnect()")
        self.login_loop = QEventLoop() #OnEventConnect 가 올때까지 프로그램이 종료되지 않고 계속 대기 해야한다.
        self.login_loop.exec() #QEventLoop만들고 exec() 만들면 while 처럼 루프 생성 *QtCore 안에 QEventLoop있음
    
    
    # Login Information
    def GetLoginInfo(self, tag):   #BSTR GetLoginInfo(BSTR sTag)
        data = self.ocx.dynamicCall("GetLoginInfo(QString)",tag)
        return data

    # Code List
    def GetCodeListByMarket(self, market):
        data = self.ocx.dynamicCall("GetCodeListByMarket(QString)", market)
        codes = data.split(';')
        return codes[:-1]# 마지막에 세미콜론 기준으로 짜르면 공백이 발생하니까, 그것은 제외 마지막은.

    # Code Name
    def GetMasterCodeName(self, code):
        data = self.ocx.dynamicCall("GetMasterCodeName(QString)", code)
        return data
    
    # Number of listed stock
    def GetMasterListedStockCnt(self,code):
        data = self.ocx.dynamicCall("GetMasterListedStockCnt(QString)",code)
        return data

    # Stock Listed Date
    def GetMasterListedStockDate(self, code):
        data = self.ocx.dynamicCall("GetMasterListedStockDate(QString)", code)
        return data

    # Stock Last Price
    def GetMasterLastPrice(self, code):
        data = self.ocx.dynamicCall("GetMasterLastPrice(QString)", code)
        return int(data) # 0056900  string --> int
    
    # Audit Classification
    def GetMasterConstruction(self, code):
        data = self.ocx.dynamicCall("GetMasterConstruction(QString)", code)
        return data
    
    # Stock Status ; Audit/margin/ credit availability etc
    def GetMasterStockState(self, code):
        data = self.ocx.dynamicCall("GetMasterStockState(QString)", code)
        return data
    
    #Login Event Loop
    def _handler_login(self, err):
        self.login_loop.exit() #루프 탈출


    # Now Important part!!!! Sector!
    #반환값의 코드와 코드명 구분은 ‘|’ 코드의 구분은 ‘;’ Ex) 100|태양광_폴리실리콘;152|합성섬유 
    def GetThemeGroupList(self, type):
        data = self.ocx.dynamicCall("GetThemeGroupList(int)", type)
        tokens = data.split(';')
        data_dic = {}
        for theme in tokens:
            code, name = theme.split('|') #unpacking
            if type == 0: # 0:코드순 1: 테마순 ex code: 001, name = AI
                data_dic[code] = name #ex) "001"을 키로 하고 "AI"를 값으로 저장 → { "001": "AI" }
            else:
                data_dic[name] = code #"AI"를 키로 하고 "001"을 값으로 저장 → { "AI": "001" }
        return data_dic
    
    # Stocks that are in the sector
    def GetThemeGroupCode(self, theme_code): #반환값의 종목코드간 구분은 ‘;’ Ex) A000660;A005930 
        data = self.ocx.dynamicCall("GetThemeGroupCode(QString)", theme_code)
        tokens = data.split(';')
        
        result = [] 
        for code in tokens:
            result.append(code[1:])
        return result
        # return tokens


app = QApplication(sys.argv) # 모든 pyqt객체 생성을 위해서는 이것을 무조건 써줘야함
                            #sys.argv : 현재 실행 파일 객체
