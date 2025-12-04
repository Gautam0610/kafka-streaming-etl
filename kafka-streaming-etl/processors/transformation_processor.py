from processors.base_processor import BaseProcessor
from transformers.base_transformer import BaseTransformer  # Assuming a base transformer

class TransformationProcessor(BaseProcessor):
    def __init__(self, config, transformer):
        super().__init__(config)
        self.transformer = transformer

    def process(self, data):
        """
        Transforms the data using the provided transformer.
        """
        try:
            return self.transformer.transform(data)
        except Exception as e:
            print(f"Error transforming data: {e}")
            return None