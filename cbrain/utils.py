"""
Helper functions that are used throughout cbrain

Created on 2019-01-28-10-33
Author: Stephan Rasp, raspstephan@gmail.com
"""
from .imports import *


def return_var_idxs(ds, var_list):
    """
    To be used on stacked variable dimension. Returns bool array.

    Parameters
    ----------
    ds: xarray dataset
    var_list: list of variables

    Returns
    -------
    var_idxs: bool array. True where any of var_list is True.

    """
    var_idxs = ds.var_names == var_list[0]
    for v in var_list[1:]:
        var_idxs = np.bitwise_or(var_idxs, ds.var_names == v)
    return var_idxs
