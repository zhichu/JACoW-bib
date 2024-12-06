#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb6af5ffe

# Compiled with Coconut version 3.1.2

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
import os as _coconut_os
_coconut_header_info = ('3.1.2', '', False)
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:  # type: ignore
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):  # type: ignore
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")  # type: ignore
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():  # type: ignore
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):  # type: ignore
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)  # type: ignore
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):  # type: ignore
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_tail_call, _coconut_tco, _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_complex_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_arr_concat_op, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in, _coconut_attritemgetter, _coconut_if_op, _coconut_CoconutWarning
if _coconut_pop_path:
    _coconut_sys.path.pop(0)
try:
    __file__ = _coconut_os.path.abspath(__file__) if __file__ else __file__
except NameError:
    pass
else:
    if __file__ and str('__coconut_cache__') in __file__:
        _coconut_file_comps = []
        while __file__:
            __file__, _coconut_file_comp = _coconut_os.path.split(__file__)
            if not _coconut_file_comp:
                _coconut_file_comps.append(__file__)
                break
            if _coconut_file_comp != str('__coconut_cache__'):
                _coconut_file_comps.append(_coconut_file_comp)
        __file__ = _coconut_os.path.join(*reversed(_coconut_file_comps))

# Compiled Coconut: -----------------------------------------------------------

from re import compile as regex  #1 (line in Coconut source)
from glob import glob  #2 (line in Coconut source)
from __constants__ import *  #3 (line in Coconut source)
from os.path import isfile  #4 (line in Coconut source)
from os.path import getmtime  #4 (line in Coconut source)

get_event = ((regex)(r'.*/([^/:.]*):event:\.tsv$')).match  #6 (line in Coconut source)
get_ev_list_from_csv_dir = _coconut_forward_compose((_coconut_complex_partial(_coconut.operator.add, {1: '/*:event:.tsv'}, 2, ())), glob, sorted, _coconut_partial(fmap, _coconut_forward_compose(get_event, _coconut.operator.itemgetter((1)))), list)  #7 (line in Coconut source)
def str_to_file(f, s):  #8 (line in Coconut source)
    (f.write)(s + '\n')  #9 (line in Coconut source)
    (print)('{_coconut_format_0: <16}'.format(_coconut_format_0=(s)), end='')  #10 (line in Coconut source)

ev_bib_file = (lambda _=None: '{_coconut_format_0}/{_coconut_format_1}.bib'.format(_coconut_format_0=(bib_dir), _coconut_format_1=(_)))  #11 (line in Coconut source)
ev_csv_file = (lambda _=None: '{_coconut_format_0}/{_coconut_format_1}:event:.tsv'.format(_coconut_format_0=(csv_dir), _coconut_format_1=(_)))  #12 (line in Coconut source)
file_to_mtime = (lambda _=None: (((getmtime)(_)) if ((isfile)(_)) else inf_past))  #13 (line in Coconut source)
to_updatable = (lambda _=None: (_[0] if _[1] < _[2] else None))  #14 (line in Coconut source)

def update_event_list():  #16 (line in Coconut source)
    with open(ev_list_file, 'w') as evlist_file:  #17 (line in Coconut source)
        (fmap)(_coconut_partial(ident, side_effect=_coconut_call_or_coefficient(_coconut_partial(_coconut_partial, str_to_file), evlist_file)), (get_ev_list_from_csv_dir)(csv_dir))  #18 (line in Coconut source)


def get_event_list():  #20 (line in Coconut source)
    with open(ev_list_file, 'r') as f:  #21 (line in Coconut source)
        lines = f.read().splitlines()  #22 (line in Coconut source)
    return lines  #23 (line in Coconut source)


ev_bib_is_recent = _coconut_forward_compose(_coconut_partial(lift, _coconut_comma_op)(ident, _coconut_forward_compose(ev_bib_file, file_to_mtime), _coconut_forward_compose(ev_csv_file, file_to_mtime)), to_updatable)  #25 (line in Coconut source)
@_coconut_tco  #26 (line in Coconut source)
def get_update_list():  #26 (line in Coconut source)
    return _coconut_tail_call((list), (filter)(lambda x: x is not None, (_coconut_call_or_coefficient(_coconut_partial(_coconut_partial, fmap), ev_bib_is_recent))(get_event_list())))  #27 (line in Coconut source)
