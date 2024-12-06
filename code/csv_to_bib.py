#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x24d8a231

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

from pandas import read_table  #1 (line in Coconut source)
from re import compile as regex  #2 (line in Coconut source)
from __constants__ import *  #3 (line in Coconut source)
from os.path import isfile  #4 (line in Coconut source)
from event_list import get_update_list  #5 (line in Coconut source)

data_only = _coconut.dict((('key', 'options'), ('value', 'dataonly')))  #7 (line in Coconut source)

csv_to_dicts = _coconut_forward_compose(_coconut_partial(read_table, dtype=str), _coconut.operator.methodcaller("apply", lambda _=None: _.dropna().to_dict(), axis=1), _coconut.operator.methodcaller("tolist"))  #9 (line in Coconut source)
find_dates = ((regex)(r'<([\d-]*)>')).findall  #10 (line in Coconut source)
to_iso8061 = (lambda _=None: ((lambda x: '{_coconut_format_0}/{_coconut_format_1}'.format(_coconut_format_0=(x[0]), _coconut_format_1=(x[-1]))))((find_dates)(_)))  #11 (line in Coconut source)
is_date = ((regex)(r'^.*date$')).search  #12 (line in Coconut source)
get_special = (regex)(r'([%&])')  #13 (line in Coconut source)
to_TeX = _coconut_partial(get_special.sub, r'\\\1')  #14 (line in Coconut source)
def key_value_short_to_strs(k, v, s):  #15 (line in Coconut source)
    return (['{_coconut_format_0} = {{{_coconut_format_1}}}'.format(_coconut_format_0=(k), _coconut_format_1=((to_iso8061)(v))),] if (is_date)(k) else ['{_coconut_format_0} = {{{_coconut_format_1}}}'.format(_coconut_format_0=(k), _coconut_format_1=((to_TeX)(v))),]) + (['{_coconut_format_0}+an:short = {{="{_coconut_format_1}"}}'.format(_coconut_format_0=(k), _coconut_format_1=((to_TeX)(s))),] if s else [])  #16 (line in Coconut source)

indent = (_coconut_partial(_coconut.operator.add, '  '))  #17 (line in Coconut source)
dont_show = (_coconut_complex_partial(_coconut.operator.add, {1: [data_only,]}, 2, ()))  #18 (line in Coconut source)
proc_ref = (lambda _=None: 'JACoW:{_coconut_format_0}:'.format(_coconut_format_0=(_)))  #19 (line in Coconut source)
def add_label_to_list(x, y):  #20 (line in Coconut source)
    return [x,] + y  #20 (line in Coconut source)

format_fld = (_coconut_complex_partial(_coconut.operator.add, {1: ',\n'}, 2, ()))  #21 (line in Coconut source)
str_to_proc = (lambda _=None: '@proceedings{{{_coconut_format_0}}}\n\n'.format(_coconut_format_0=(_)))  #22 (line in Coconut source)
@_coconut_tco  #23 (line in Coconut source)
def exclude_keys(ks, d):  #23 (line in Coconut source)
    return _coconut_tail_call(_coconut.dict, (((k), (d[k])) for k in d.keys() - ks))  #23 (line in Coconut source)

simple_key_val = (lambda _=None: '{_coconut_format_0} = {{{_coconut_format_1}}}'.format(_coconut_format_0=(_[0]), _coconut_format_1=((to_TeX)(_[1]))))  #24 (line in Coconut source)
paper_dict_to_label = _coconut_forward_compose(_coconut_partial(lift, _coconut_comma_op)(_coconut.operator.methodcaller("get", 'crossref'), _coconut.operator.methodcaller("get", 'eid')), _coconut_partial(reduce, _coconut.operator.add), to_TeX)  #25 (line in Coconut source)
str_to_inproc = (lambda _=None: '@inproceedings{{{_coconut_format_0}}}\n\n'.format(_coconut_format_0=(_)))  #26 (line in Coconut source)
crossref = (lambda _=None: _coconut.dict((('crossref', ((proc_ref)(_))),)))  #27 (line in Coconut source)
str_to_unpub = (lambda _=None: '@unpublished{{{_coconut_format_0}}}\n\n'.format(_coconut_format_0=(_)))  #28 (line in Coconut source)
def write_str_to_bib(bib_str, ev):  #29 (line in Coconut source)
    with open('{_coconut_format_0}/{_coconut_format_1}.bib'.format(_coconut_format_0=(bib_dir), _coconut_format_1=(ev)), 'w') as f:  #30 (line in Coconut source)
        (f.write)(bib_str)  #31 (line in Coconut source)
    (print)('{_coconut_format_0}.bib generated'.format(_coconut_format_0=(ev)))  #32 (line in Coconut source)


ev_dict_to_strs = (lambda _=None: (_coconut_call_or_coefficient(_coconut_partial(_coconut_partial, fmap), indent))((key_value_short_to_strs)(*(_coconut_partial(lift, _coconut_comma_op)(_coconut.operator.methodcaller("get", 'key'), _coconut.operator.methodcaller("get", 'value'), _coconut.operator.methodcaller("get", 'short')))(_))))  #34 (line in Coconut source)
ev_to_fields = (lambda _=None: (reduce)(_coconut.operator.add, (_coconut_call_or_coefficient(_coconut_partial(_coconut_partial, fmap), ev_dict_to_strs))((dont_show)((csv_to_dicts)('{_coconut_format_0}/{_coconut_format_1}:event:.tsv'.format(_coconut_format_0=(csv_dir), _coconut_format_1=(_)))))))  #35 (line in Coconut source)
ev_to_labeled_fields = (lambda _=None: (add_label_to_list)(*(lift(_coconut_comma_op)(proc_ref, ev_to_fields))(_)))  #36 (line in Coconut source)
labeled_fields_to_str = _coconut_forward_compose(_coconut_call_or_coefficient(_coconut_partial(_coconut_partial, fmap), format_fld), ''.join)  #37 (line in Coconut source)
ev_to_proc = _coconut_forward_compose(ev_to_labeled_fields, labeled_fields_to_str, str_to_proc)  #38 (line in Coconut source)

paper_dict_to_fields = (lambda _=None: (fmap)(_coconut_forward_compose(simple_key_val, indent), (list)(((exclude_keys)(_coconut.set(('firstpage', 'lastpage')), _)).items())))  #40 (line in Coconut source)
paper_dict_to_labeled_fields = (lambda _=None: (add_label_to_list)(*(lift(_coconut_comma_op)(paper_dict_to_label, paper_dict_to_fields))(_)))  #41 (line in Coconut source)
paper_dict_to_inproc = _coconut_forward_compose(paper_dict_to_labeled_fields, labeled_fields_to_str, str_to_inproc)  #42 (line in Coconut source)
ev_to_inproc_lists = (lambda _=None: (fmap)(_coconut_forward_compose((_coconut_complex_partial(_coconut.operator.or_, {1: ((crossref)(_))}, 2, ())), paper_dict_to_inproc), (csv_to_dicts)('{_coconut_format_0}/{_coconut_format_1}:inproceedings:.tsv'.format(_coconut_format_0=(csv_dir), _coconut_format_1=(_)))))  #43 (line in Coconut source)
ev_to_inprocs = _coconut_forward_compose(ev_to_inproc_lists, ''.join)  #44 (line in Coconut source)

paper_dict_to_unpub = _coconut_forward_compose(paper_dict_to_labeled_fields, labeled_fields_to_str, str_to_unpub)  #46 (line in Coconut source)
maybe_file_to_unpub_lists = (lambda _=None: (((fmap)(_coconut_forward_compose((_coconut_complex_partial(_coconut.operator.or_, {1: ((crossref)(_))}, 2, ())), paper_dict_to_unpub), (csv_to_dicts)(_[1]))) if _[0] else []))  #47 (line in Coconut source)
ev_to_unpub_lists = (lambda _=None: (maybe_file_to_unpub_lists)((_coconut_partial(lift, _coconut_comma_op)(isfile, ident))('{_coconut_format_0}/{_coconut_format_1} :unpublished:.tsv'.format(_coconut_format_0=(csv_dir), _coconut_format_1=(_)))))  #48 (line in Coconut source)
ev_to_unpubs = _coconut_forward_compose(ev_to_unpub_lists, ''.join)  #49 (line in Coconut source)

ev_to_bib = (lambda _=None: (reduce)(_coconut.operator.add, (_coconut_partial(lift, _coconut_comma_op)(ev_to_proc, ev_to_inprocs, ev_to_unpubs))(_)))  #51 (line in Coconut source)
ev_to_bib_file = (lambda _=None: (write_str_to_bib)(*(_coconut_partial(lift, _coconut_comma_op)(ev_to_bib, ident))(_)))  #52 (line in Coconut source)
def generate_bib():  #53 (line in Coconut source)
    (fmap)(_coconut_partial(ident, side_effect=ev_to_bib_file), get_update_list())  #54 (line in Coconut source)
