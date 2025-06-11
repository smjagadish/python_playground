import pytest

from class_playground.student import student

#placeholder file for all fixtures

@pytest.fixture(params=[('lisa','ray',1300,'lisa ray')
                       ])
def fix_param_conf(request):
    param = request.param
    print(f'{len(param)}')
    fname , lname , hike , expected = request.param
    s1 = student(fname,lname,hike)
    return s1 , expected