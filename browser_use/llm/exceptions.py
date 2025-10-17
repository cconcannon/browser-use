"""Model error exceptions."""


class ModelError(Exception):
	"""Base exception for model errors."""

	pass


class ModelProviderError(ModelError):
	"""Exception raised when a model provider returns an error."""

	def __init__(
		self,
		message: str,
		status_code: int = 502,
		model: str | None = None,
	):
		"""Initialize ModelProviderError with message, status code, and model."""
		super().__init__(message)
		self.message = message
		self.status_code = status_code
		self.model = model


class ModelRateLimitError(ModelProviderError):
	"""Exception raised when a model provider returns a rate limit error."""

	def __init__(
		self,
		message: str,
		status_code: int = 429,
		model: str | None = None,
	):
		"""Initialize ModelRateLimitError with message, status code, and model."""
		super().__init__(message, status_code, model)
