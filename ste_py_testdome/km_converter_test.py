"""
Created on 24.11.2020

@author: sbiker99-prog
"""
import unittest as ut
from .km_converter import MilesToKmConverter, NauticalMilesToKmConverter
from .km_converter import NauticalMilesToKmConverter


class Test(ut.TestCase):

    def test_MilesToKmConverter_get_miles_to_km_factor(self):
        mkm = MilesToKmConverter()
        print(f'MilesToKmConverter::get_miles_to_km_factor {mkm.get_miles_to_km_factor()}')

    def test_MilesToKmConverter_miles_to_km(self):
        mkm = MilesToKmConverter()
        print(f'Convert 2 miles to km using MilesToKmConverter::miles_to_km {mkm.miles_to_km(2)}')

    def test_NauticalMilesToKmConverter_get_miles_to_km_factor(self):
        nmkm = NauticalMilesToKmConverter()
        print(f'NauticalMilesToKmConverter::get_miles_to_km_factor {nmkm.get_miles_to_km_factor()}')

    def test_NauticalMilesToKmConverter_miles_to_km(self):
        nmkm = NauticalMilesToKmConverter()
        print(f'Convert 2 miles to km using NauticalMilesToKmConverter::miles_to_km {nmkm.miles_to_km(2)}')

    def test_NauticalMilesToKmConverter_self(self):
        nmkm: NauticalMilesToKmConverter = NauticalMilesToKmConverter()
        print('printFactors_self: ')
        nmkm.printFactors_self()

    def test_NauticalMilesToKmConverter_super(self):
        nmkm = NauticalMilesToKmConverter()
        print('printFactors_super: ')
        nmkm.printFactors_super()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    ut.main()
