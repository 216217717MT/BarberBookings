import PaymentProcessor    # from src.payment_processor 
import CreditCardProcessor #from src.credit_card_processor
import PayPalProcessor     # from src.paypal_processor 

class PaymentProcessorFactory:
    @staticmethod
    def get_payment_processor(payment_method: str) -> PaymentProcessor:
        if payment_method.lower() == "creditcard":
            return CreditCardProcessor()
        elif payment_method.lower() == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError(f"Unknown payment method: {payment_method}")
