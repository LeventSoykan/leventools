
import pandas
from leventools.data_science.eda import identify_outliers, remove_outliers

df = pandas.DataFrame({
    'age':[3, 21, 22, 25, 23, 24, 27, 21, 75],
    'weight':[15, 69, 61, 77, 75, 82, 73, 70, 62]
})


def test_identify_outliers():
    assert 3 in identify_outliers(df, 'age')[0]
    assert 75 in identify_outliers(df, 'age')[0]
    assert 15 in identify_outliers(df, 'weight')[0]


def test_remove_outliers():
    assert remove_outliers(df, 'age').shape[0] == 7
    assert remove_outliers(df, 'weight').shape[0] == 8
