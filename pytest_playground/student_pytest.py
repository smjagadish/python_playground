import pytest

from class_playground.student import student
from class_playground.user_class import user
def test_fname():
    s1 = student('john','wark',300)
    assert s1.getfullName() == 'john wark'

def test_hike():
    s1 = student('mark','walters',200)
    assert s1.gethike() == 300

#@pytest.mark.skip
def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
      divide(19,0)

def test_lname():
    s1 = student('thomas','frank',300)
    assert s1.lname == 'frenk'

def divide(a,b):
    return a//b

# below is an example of parametrization where the same code to test is called multiple times with diff arg values
# inputs specified using the first placeholder - input1,input2 with result in result
# the list of tuples are the values for input1, input2 and result
# pay attention to how the input1, input2 and result are passed
@pytest.mark.parametrize('input1,input2,result',
                         [('john','wark','john wark'),('mark','walters','mark walters')
                          ,('tim','duncan','tim duncan')])
def test_fullname_multi(input1,input2,result):
    s1 = student(input1,input2,300)
    assert  s1.getfullName() == result


# using fixtures to slice out repeatable ops for each TC
# the fixture must return the content corresponding to a repeatable data
@pytest.fixture
def test_object():
    s1 = student('johann','warkes',300)
    return s1

def test_fixture_fname(test_object):
    assert test_object.getfullName() == 'johann warkes'

# this test combines fixture with parametrization
# if i include a second tuple in the fixture params , then another test instance would run
# the fixture is a tc level. each tc that references this fixture will have the fixture code run
# if we need fixture to be run once per module , i.e. for all tc's , then leverage the scope parameter as shown un next below.
@pytest.fixture(params=[('johannes','weeked',300,'johannes weeked'),
                        ('mark','walter',200,'mark walter')])
def fix_param(request):
    param = request.param
    print(f'{len(param)}')
    fname , lname , hike , expected = request.param
    s1 = student(fname,lname,hike)
    return s1 , expected

def test_obj_fixture_with_params(fix_param):
    obj , result = fix_param
    assert obj.getfullName() == result

# module level fixture
# object created only once and used by test_obj_fix_param1 and test_pbj_fix_param2
# 2 objects created since fixture params has 2 tuples
@pytest.fixture(scope='module',params=[('tom','smith',200,'tom smith'),
                                       ('tim','david',100,'tim david')])
def fix_param_mod(request):
    fname,lname,hike,exp_res = request.param
    obj = student(fname,lname,hike)
    return obj,exp_res  # also use yield instead of return . makes sense if we want to do cleanup ops

def test_obj_fix_param1(fix_param_mod):
    obj , exp_res = fix_param_mod
    assert obj.getfullName() == exp_res

def test_obj_fix_param2(fix_param_mod):
    obj ,exp_res = fix_param_mod
    assert obj.fname != 'xxx'

# example of fixture defined in conftest.py
def test_obj_conftest(fix_param_conf):
    obj, exp_res = fix_param_conf
    assert obj.getfullName() == 'lisa ray'
    #assert isinstance(obj,user)