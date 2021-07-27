from __future__ import unicode_literals
from typing import List, Optional


class CustomException(Exception):
    """
    custom Exception class.
    """

    def __init__(
        self,
        title: str,
        detail: Optional[str] = "",
        invalid_params: Optional[List] = None,
    ):
        if invalid_params is None:
            invalid_params = []
        self._title = title
        self._detail = detail
        self._invalid_params = invalid_params
        super(CustomException, self).__init__(title)

    @property
    def title(self):
        """title: exception message"""
        return self._title

    @property
    def detail(self):
        """detail: exception detail message"""
        return self._detail

    @property
    def invalid_params(self):
        """exception params that cause the exception"""
        return self._invalid_params

    def as_dict(self):
        """return dict object of the exception"""
        return {
            "title": self._title,
            "detail": self._detail,
            "invalid_params": self._invalid_params,
        }
