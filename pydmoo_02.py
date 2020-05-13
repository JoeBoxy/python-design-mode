# Simple Factory Model

from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def __init__(self, use_huabei=True):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print(f"Huabei pay {money} RMB.")
        print(f"Ali pay {money} RMB.")

class WechatPay(Payment):
    def pay(self, money):
        print("Wechat pay {money} RMB.")

class PaymentFactory:
    def create_payment(self, method):
        if method == 'alipay':
            return Alipay()
        elif method == 'wechat':
            return WechatPay()
        elif method == 'huabei':
            return Alipay(use_huabei=True)
        else:
            raise TypeError(f"No such payment named {method}")


pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)
