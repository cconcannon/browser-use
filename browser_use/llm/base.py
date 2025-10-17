"""
We have switched all of our code from langchain to openai.types.chat.chat_completion_message_param.

For easier transition we have
"""

from typing import Any, Protocol, TypeVar, overload, runtime_checkable

from pydantic import BaseModel

from browser_use.llm.messages import BaseMessage
from browser_use.llm.views import ChatInvokeCompletion

T = TypeVar('T', bound=BaseModel)


@runtime_checkable
class BaseChatModel(Protocol):
	"""Base protocol for chat models."""

	_verified_api_keys: bool = False

	model: str

	@property
	def provider(self) -> str:
		"""Return the provider name."""
		...

	@property
	def name(self) -> str:
		"""Return the model name."""
		...

	@property
	def model_name(self) -> str:
		"""Return model name for legacy support."""
		# for legacy support
		return self.model

	@overload
	async def ainvoke(self, messages: list[BaseMessage], output_format: None = None) -> ChatInvokeCompletion[str]:
		"""Invoke LLM with messages and return unstructured text completion."""
		...

	@overload
	async def ainvoke(self, messages: list[BaseMessage], output_format: type[T]) -> ChatInvokeCompletion[T]:
		"""Invoke LLM with messages and return structured output of type T."""
		...

	async def ainvoke(
		self, messages: list[BaseMessage], output_format: type[T] | None = None
	) -> ChatInvokeCompletion[T] | ChatInvokeCompletion[str]:
		"""Invoke LLM with messages, optionally returning structured output."""
		...

	@classmethod
	def __get_pydantic_core_schema__(
		cls,
		source_type: type,
		handler: Any,
	) -> Any:
		"""
		Allow this Protocol to be used in Pydantic models -> very useful to typesafe the agent settings for example.
		Returns a schema that allows any object (since this is a Protocol).
		"""
		from pydantic_core import core_schema

		# Return a schema that accepts any object for Protocol types
		return core_schema.any_schema()
