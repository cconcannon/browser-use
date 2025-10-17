"""Action models and parameter definitions for browser automation tools."""

from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field


# Action Input Models
class SearchAction(BaseModel):
	"""Search action to query a search engine."""

	query: str
	engine: str = Field(
		default='duckduckgo', description='duckduckgo, google, bing (use duckduckgo by default because less captchas)'
	)


# Backward compatibility alias
SearchAction = SearchAction


class NavigateAction(BaseModel):
	"""Navigate to a URL."""

	url: str
	new_tab: bool = Field(default=False)


# Backward compatibility alias
GoToUrlAction = NavigateAction


class ClickElementAction(BaseModel):
	"""Click an element on the page."""

	index: int = Field(ge=1, description='from browser_state')
	# expect_download: bool = Field(default=False, description='set True if expecting a download, False otherwise')  # moved to downloads_watchdog.py
	# click_count: int = 1  # TODO


class InputTextAction(BaseModel):
	"""Input text into a form element."""

	index: int = Field(ge=0, description='from browser_state')
	text: str
	clear: bool = Field(default=True, description='1=clear, 0=append')


class DoneAction(BaseModel):
	"""Mark the task as complete."""

	text: str = Field(description='summary for user')
	success: bool = Field(description='True if user_request completed successfully')
	files_to_display: list[str] | None = Field(default=[])


T = TypeVar('T', bound=BaseModel)


class StructuredOutputAction(BaseModel, Generic[T]):
	"""Return structured output."""

	success: bool = Field(default=True, description='1=done')
	data: T


class SwitchTabAction(BaseModel):
	"""Switch to a different browser tab."""

	tab_id: str = Field(min_length=4, max_length=4, description='4-char id')


class CloseTabAction(BaseModel):
	"""Close a browser tab."""

	tab_id: str = Field(min_length=4, max_length=4, description='4-char id')


class ScrollAction(BaseModel):
	"""Scroll the page or a specific element."""

	down: bool = Field(description='down=True=scroll down, down=False scroll up')
	pages: float = Field(default=1.0, description='0.5=half page, 1=full page, 10=to bottom/top')
	index: int | None = Field(default=None, description='Optional element index to scroll within specific container')


class SendKeysAction(BaseModel):
	"""Send keyboard keys to the browser."""

	keys: str = Field(description='keys (Escape, Enter, PageDown) or shortcuts (Control+o)')


class UploadFileAction(BaseModel):
	"""Upload a file to a file input element."""

	index: int
	path: str


class ExtractPageContentAction(BaseModel):
	"""Action model for extracting page content."""

	value: str


class NoParamsAction(BaseModel):
	"""Action model with no parameters."""

	model_config = ConfigDict(extra='ignore')


class GetDropdownOptionsAction(BaseModel):
	"""Action model for getting dropdown options."""

	index: int


class SelectDropdownOptionAction(BaseModel):
	"""Action model for selecting a dropdown option."""

	index: int
	text: str = Field(description='exact text/value')
