from processors.base_processor import BaseProcessor
from validators.base_validator import BaseValidator # Assuming a base validator

class ValidationProcessor(BaseProcessor):
    def __init__(self, config, validator):
        super().__init__(config)
        self.validator = validator

    def process(self, data):
        """
        Validates the data using the provided validator.
        """
        try:
            if self.validator.validate(data):
                return data
            else:
                print(f"Data validation failed: {data}")
                return None
        except Exception as e:
            print(f"Error validating data: {e}")
            return None