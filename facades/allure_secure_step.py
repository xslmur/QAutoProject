# implements allure_secure_step to hide step parameters in the report
# see: allure_commons/_allure.py

from functools import wraps
from typing import Any, Callable, TypeVar

from allure_commons._core import plugin_manager
from allure_commons.types import LabelType, LinkType, ParameterMode
from allure_commons.utils import uuid4
from allure_commons.utils import func_parameters, represent

_TFunc = TypeVar("_TFunc", bound=Callable[..., Any])


def allure_secure_step(title):
    if callable(title):
        return SecureStepContext(title.__name__, {})(title)
    else:
        return SecureStepContext(title, {})


class SecureStepContext:

    def __init__(self, title, params):
        self.title = title
        self.uuid = uuid4()
        self.params = dict()
        for k in params:
            self.params[k] = '[hidden]'

    def __enter__(self):
        plugin_manager.hook.start_step(uuid=self.uuid, title=self.title, params=self.params)

    def __exit__(self, exc_type, exc_val, exc_tb):
        plugin_manager.hook.stop_step(uuid=self.uuid, title=self.title, exc_type=exc_type, exc_val=exc_val,
                                      exc_tb=exc_tb)

    def __call__(self, func: _TFunc) -> _TFunc:
        @wraps(func)
        def impl(*a, **kw):
            __tracebackhide__ = True
            params = func_parameters(func, *a, **kw)
            args = list(map(lambda x: represent(x), a))
            with SecureStepContext(self.title.format(*args, **params), params):
                return func(*a, **kw)

        return impl