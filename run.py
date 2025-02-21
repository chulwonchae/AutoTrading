from KoTrade import *
import pandas as pd


kotrade = kotrade() #키움클래스에 객체를 생성하면
kotrade.CommConnect() # 호출을 할수 있다. 
print("로그인 완료")

# # 계좌 개수수
# account_cnt = kotrade.GetLoginInfo("ACCOUNT_CNT")
# print(account_cnt)

# # 계좌번호
# user_account = kotrade.GetLoginInfo("ACCNO")
# print(user_account)

# # 아이디
# user_id = kotrade.GetLoginInfo("USER_ID")
# print(user_id)

# # 사용자 이름름
# user_name = kotrade.GetLoginInfo("USER_NAME")
# print(user_name)

# # 종목 ticker #  0:Kospi,   8:ETF,  10:코스닥
# stock_tickers = kotrade.GetCodeListByMarket('0')
# print(stock_tickers)

# # ticker로  종목명 가져오기
# stock_name = kotrade.GetMasterCodeName('005930')
# print(stock_name)

# # kospi, kosdaq list of code and name
# kospi = kotrade.GetCodeListByMarket('0')
# kosdaq = kotrade.GetCodeListByMarket('10')
# codes = kospi + kosdaq
# data = []
# for code in codes:
#     name = kotrade.GetMasterCodeName(code)
#     data.append((code,name))
# df = pd.DataFrame(data=data, columns=['code','종목명']) 
# df = df.set_index('code')
# df.to_csv("code.csv")

# # 상장주식수 
# stock_cnt = kotrade.GetMasterListedStockCnt('005930')
# print(stock_cnt, type(stock_cnt))

# # 주식 상장일
# list_date = kotrade.GetMasterListedStockDate('005930')
# print(list_date, type(list_date))

# # 최근 주식 종가
# last_price = kotrade.GetMasterLastPrice('005930')
# print(last_price, type(last_price))

# # 감리구분
# audit_condition = kotrade.GetMasterConstruction('005930')
# print(audit_condition)

# # 종목 상태
# stock_status = kotrade.GetMasterStockState('005930')
# print(stock_status.split("|"))

# 2025 년 이후 상장 기업 리스트트
# codes = kotrade.GetCodeListByMarket('0') + kotrade.GetCodeListByMarket('10')

# for code in codes:
#     date = kotrade.GetMasterListedStockDate(code)
#     name = kotrade.GetMasterCodeName(code)
#     if date.startswith('2025'):
#         print(date, code, name)


# # GetMasterStockState 사용해서 거래정지, 관리종목, 감리종목, 투자유의종목 출력
# codes = kotrade.GetCodeListByMarket('0') + kotrade.GetCodeListByMarket('10')

# for code in codes:
#     state = kotrade.GetMasterStockState(code)
#     name = kotrade.GetMasterCodeName(code)
#     tokens = state.split("|")

#     target = False
#     if '거래정지' in tokens:
#         target = True #원래 false인데 해당 조건에 만족하면 True로 바꿔 주겠다.
#     elif '관리종목' in tokens:
#         target = True
#     elif '감리종목' in tokens: 
#         target = True
#     elif '투자유의종목' in tokens:
#         target = True

#     if target is True: #만약 타겟이 트루면
#         print(code, name, state)