from sagemaker_inference import content_types, decoder
from sagemaker_inference.default_handler_service import DefaultHandlerService
from sagemaker_inference.transformer import Transformer
from sagemaker_pytorch_serving_container.default_inference_handler import (
    DefaultPytorchInferenceHandler,
)
from sagemaker_inference import encoder


class HandlerService(DefaultHandlerService):
    """Handler service that is executed by the model server.
    Determines specific default inference handlers to use based on model being used.
    This class extends ``DefaultHandlerService``, which define the following:
        - The ``handle`` method is invoked for all incoming inference requests to the model server.
        - The ``initialize`` method is invoked at model server start up.
    Based on: https://github.com/awslabs/mxnet-model-server/blob/master/docs/custom_service.md
    """

    def __init__(self):
        transformer = Transformer(
            default_inference_handler=DefaultPytorchInferenceHandler()
        )
        super(HandlerService, self).__init__(transformer=transformer)

    def input_fn(self, input_data, content_type):
        """A default input_fn that can handle JSON, CSV and NPZ formats.
            
            Args:
                input_data: the request payload serialized in the content_type format
                content_type: the request content_type

            Returns: input_data deserialized into torch.FloatTensor or torch.cuda.FloatTensor depending if cuda is available.
            """
        return decoder.decode(input_data, content_type)

    def predict_fn(self, data, model):
        """A default predict_fn for PyTorch. Calls a model on data deserialized in input_fn.
        Runs prediction on GPU if cuda is available.

        Args:
            data: input data (torch.Tensor) for prediction deserialized by input_fn
            model: PyTorch model loaded in memory by model_fn

        Returns: a prediction
        """
        return model(data)

    def output_fn(self, prediction, accept):
        """A default output_fn for PyTorch. Serializes predictions from predict_fn to JSON, CSV or NPY format.

        Args:
            prediction: a prediction result from predict_fn
            accept: type which the output data needs to be serialized

        Returns: output data serialized
        """
        return encoder.encode(prediction, accept)
