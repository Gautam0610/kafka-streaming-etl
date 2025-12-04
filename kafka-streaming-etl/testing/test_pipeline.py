import unittest
import json
from main import SampleTransformer, SampleValidator  # Import pipeline components

class TestPipeline(unittest.TestCase):

    def test_sample_transformer(self):
        transformer = SampleTransformer({})
        data = {'key1': 123, 'key2': 'abc'}
        transformed_data = transformer.transform(data)
        self.assertEqual(transformed_data, {'key1': '123', 'key2': 'ABC'})

    def test_sample_validator(self):
        validator = SampleValidator({})
        valid_data = {'id': 1, 'name': 'test'}
        invalid_data = {'id': -1, 'name': 'test'}
        self.assertTrue(validator.validate(valid_data))
        self.assertFalse(validator.validate(invalid_data))

if __name__ == '__main__':
    unittest.main()