"""Custom exceptions for browser-use library."""


class LLMException(Exception):
	"""Exception raised when LLM API calls fail."""

	def __init__(self, status_code, message):
		"""Initialize the LLM exception.

		Args:
		        status_code: HTTP status code from the API.
		        message: Error message describing the failure.
		"""
		self.status_code = status_code
		self.message = message
		super().__init__(f'Error {status_code}: {message}')
