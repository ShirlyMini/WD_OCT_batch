
import pytest

class Test_001_comparator:#
    @pytest.mark.skip(reason="skipped test case")
    @pytest.mark.regression
    def test_equal(self, start3, start1, start4):
        assert 5==5

    @pytest.mark.skipif(3>2, reason="condition became true")
    @pytest.mark.functionality
    def test_greater(self, start3, start1, start4):
        assert 5>2

    @pytest.mark.functionality
    def test_lesser(self, start3, start1, start4):
        assert 6<17

    @pytest.mark.parametrize('name',['name1', "name2", 'name3'])
    @pytest.mark.regression
    def test_name(self, name):
        print(name)

    @pytest.mark.xfail
    @pytest.mark.parametrize('a,b,c', [(1,2,4),(5,6,7),(7,6,10)])
    @pytest.mark.functionality
    def test_greater_than(self, a,b,c):
        print(a,b,c)
        assert c>=b

# Step1. Install-->
# 	Selenium
# 	Pytest
# 	Pytest-html
# 	Pytest-xdist(running tcs parallely)
# Openpyxl
# dashboard, chart

