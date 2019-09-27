#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "pattersonday w/guidance from astephens91"

import cProfile
import pstats
import functools
import timeit
import collections


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    functools.wraps(func)

    def decorator(*args, **kwargs):
        profile_func = cProfile.Profile()
        profile_func.enable()
        result = func(*args, **kwargs)
        profile_func.disable()
        pstats_obj = pstats.Stats(profile_func)
        pstats_obj.print_stats().sort_stats('time')
        return result
    return decorator


def read_movies(src):
    """Returns a list of movie titles"""
    with open(src, 'r') as f:
        return f.read().splitlines()


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = [movie for movie, count in collections
                  .Counter(movies).items() if count > 1]

    return duplicates


def timeit_helper(num_repeat, runs_per_repeat):
    """Part A:  Obtain some profiling measurements using timeit"""
    the_time = timeit.Timer(stmt="find_duplicate_movies('movies.txt')",
                            setup="from __main__ import find_duplicate_movies")
    result = the_time.repeat(repeat=num_repeat, number=runs_per_repeat)
    print('code executed {} and then repeated {} times'
          .format(runs_per_repeat, num_repeat))
    print('cumulative time cost = {:.4} secs'.format(result))
    per_call = min(result) / float(runs_per_repeat)
    print('per call time cost = {:.4} secs'.format(per_call))


def main():

    timeit_helper(4, 3)


if __name__ == '__main__':
    main()
