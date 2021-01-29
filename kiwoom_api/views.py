from django.shortcuts import render
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QAxContainer import *


def login(request):
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    app.exec_()
    return render(request, 'kiwoom_api/login.html')


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Python 로그인")
        self.ocx = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.ocx.OnEventConnect.connect(self._handler_login)

        # login
        self.ocx.dynamicCall("CommConnect()")
        self.login_loop = QEventLoop()
        self.login_loop.exec()

        self.ocx.dynamicCall(
            "KOA_Functions(QString, QString)", "ShowAccountWindow", "")

        self.user_id = self.ocx.GetLoginInfo("USER_ID")                # 사용자 ID
        self.user_name = self.ocx.GetLoginInfo("USER_NAME")            # 사용자명
        self.accounts = self.ocx.GetLoginInfo("ACCNO")
        self.stock_account = self.accounts[:len(self.accounts)-1]
        print("유저 ID:", self. user_id)
        print("유저 이름:", self.user_name)
        print("계좌번호:", self.stock_account)

        # 삼성전자, 10주, 시장가주문 매수
        self.ocx.SendOrder("시장가매수", "0101", self.stock_account,
                           1, "005930", 10, 0, "03", "")
        print("삼성전자 10주 매수완료")

        self.ocx.SendOrder("시장가매도", "0101", self.stock_account,
                           2, "005930", 10, 0, "03", "")
        print("삼성전자 10주 매도완료")

    def _handler_login(self):
        try:
            self.login_loop.exit()
        except:
            pass
