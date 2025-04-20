import unittest
import PaymentProcessorFactory   # from payment_processor_factory
import CreditCardProcessor       # from credit_card_processor 
import PayPalProcessor           # from paypal_processor 

class TestPaymentProcessorFactory(unittest.TestCase):
    def test_get_creditcard_processor(self):
        processor = PaymentProcessorFactory.get_payment_processor("creditcard")
        self.assertIsInstance(processor, CreditCardProcessor)

    def test_get_paypal_processor(self):
        processor = PaymentProcessorFactory.get_payment_processor("paypal")
        self.assertIsInstance(processor, PayPalProcessor)

    def test_invalid_payment_method(self):
        with self.assertRaises(ValueError):
            PaymentProcessorFactory.get_payment_processor("bitcoin")
