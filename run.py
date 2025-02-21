from kiwoom import *
import pandas as pd


kiwoom = Kiwoom() #키움클래스에 객체를 생성하면
kiwoom.CommConnect() # 호출을 할수 있다. 
print("로그인 완료")

# # 계좌 개수수
# cnt = kiwoom.GetLoginInfo("ACCOUNT_CNT")
# print(cnt)

# # 계좌번호
# account = kiwoom.GetLoginInfo("ACCNO")
# print(account)

# # 아이디
# user = kiwoom.GetLoginInfo("USER_ID")
# print(user)

# # 사용자 이름름
# name = kiwoom.GetLoginInfo("USER_NAME")
# print(name)

# # 종목 ticker #  0:Kospi,   8:ETF,  10:코스닥
# codes = kiwoom.GetCodeListByMarket('0')
# print(codes)

# # ticker로  종목명 가져오기
# name = kiwoom.GetMasterCodeName('005930')
# print(name)

# # kospi, kosdaq list of code and name
# kospi = kiwoom.GetCodeListByMarket('0')
# kosdaq = kiwoom.GetCodeListByMarket('10')
# codes = kospi + kosdaq
# data = []
# for code in codes:
#     name = kiwoom.GetMasterCodeName(code)
#     data.append((code,name))
# df = pd.DataFrame(data=data, columns=['code','종목명']) 
# df = df.set_index('code')
# df.to_csv("code.csv")

# # 상장주식수 
# cnt = kiwoom.GetMasterListedStockCnt('005930')
# print(cnt, type(cnt))