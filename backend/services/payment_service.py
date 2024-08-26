from ..hotmart_integration import HotmartIntegration
from ..models import User
from ..database import db
from datetime import datetime, timedelta

class PaymentService:
    @staticmethod
    def process_payment(transaction_code):
        purchase_data = HotmartIntegration.verify_purchase(transaction_code)
        if purchase_data and purchase_data['status'] == 'APPROVED':
            user = User.query.filter_by(email=purchase_data['buyer']['email']).first()
            if user:
                user.subscription_end = datetime.utcnow() + timedelta(days=30)  # Assume 30-day subscription
                db.session.commit()
                return True
        return False