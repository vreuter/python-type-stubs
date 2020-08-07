from collections import OrderedDict
from pandas.errors import UnsupportedFunctionCall as UnsupportedFunctionCall
from pandas.util._validators import validate_args as validate_args, validate_args_and_kwargs as validate_args_and_kwargs, validate_kwargs as validate_kwargs
from typing import Dict, Optional, Union

class CompatValidator:
    fname = ...
    method = ...
    defaults = ...
    max_fname_arg_count = ...
    def __init__(self, defaults, fname: Optional = ..., method: Optional = ..., max_fname_arg_count: Optional = ...) -> None: ...
    def __call__(self, args, kwargs, fname: Optional = ..., max_fname_arg_count: Optional = ..., method: Optional = ...) -> None: ...

ARGMINMAX_DEFAULTS = ...
validate_argmin = ...
validate_argmax = ...

def process_skipna(skipna, args): ...
def validate_argmin_with_skipna(skipna, args, kwargs): ...
def validate_argmax_with_skipna(skipna, args, kwargs): ...

ARGSORT_DEFAULTS: OrderedDict[str, Optional[Union[int, str]]] = ...
validate_argsort = ...
ARGSORT_DEFAULTS_KIND: OrderedDict[str, Optional[int]] = ...
validate_argsort_kind = ...

def validate_argsort_with_ascending(ascending, args, kwargs): ...

CLIP_DEFAULTS = ...
validate_clip = ...

def validate_clip_with_axis(axis, args, kwargs): ...

CUM_FUNC_DEFAULTS: OrderedDict = ...
validate_cum_func = ...
validate_cumsum = ...

def validate_cum_func_with_skipna(skipna, args, kwargs, name): ...

ALLANY_DEFAULTS: OrderedDict[str, Optional[bool]] = ...
validate_all = ...
validate_any = ...
LOGICAL_FUNC_DEFAULTS = ...
validate_logical_func = ...
MINMAX_DEFAULTS = ...
validate_min = ...
validate_max = ...
RESHAPE_DEFAULTS: Dict[str, str] = ...
validate_reshape = ...
REPEAT_DEFAULTS: Dict[str,] = ...
validate_repeat = ...
ROUND_DEFAULTS: Dict[str,]
validate_round = ...
SORT_DEFAULTS: OrderedDict[str, Optional[Union[int, str]]] = ...
validate_sort = ...
STAT_FUNC_DEFAULTS: OrderedDict[str, Optional] = ...
PROD_DEFAULTS = ...
SUM_DEFAULTS = ...
MEDIAN_DEFAULTS = ...
validate_stat_func = ...
validate_sum = ...
validate_prod = ...
validate_mean = ...
validate_median = ...
STAT_DDOF_FUNC_DEFAULTS: OrderedDict[str, Optional[bool]]
validate_stat_ddof_func = ...
TAKE_DEFAULTS: OrderedDict[str, Optional[str]]
validate_take = ...

def validate_take_with_convert(convert, args, kwargs): ...

TRANSPOSE_DEFAULTS = ...
validate_transpose = ...

def validate_window_func(name, args, kwargs) -> None: ...
def validate_rolling_func(name, args, kwargs) -> None: ...
def validate_expanding_func(name, args, kwargs) -> None: ...
def validate_groupby_func(name, args, kwargs, allowed: Optional = ...) -> None: ...

RESAMPLER_NUMPY_OPS = ...

def validate_resampler_func(method, args, kwargs) -> None: ...
def validate_minmax_axis(axis) -> None: ...