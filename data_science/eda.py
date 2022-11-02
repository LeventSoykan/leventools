import pandas
import numpy


def identify_outliers(dataframe: pandas.DataFrame, column: str):
    # calculate inter quartile range
    q25, q75 = numpy.percentile(dataframe[column], 25), numpy.percentile(dataframe[column], 75)
    iqr = q75 - q25
    print(f'COLUMN: {column}\nPercentiles: 25th={q25:.2f}, 75th={q75:.2f}, IQR={iqr:.2f}')
    # calculate the outlier cutoff
    cut_off = iqr * 1.5
    lower, upper = q25 - cut_off, q75 + cut_off
    # identify outliers
    outliers = [x for x in dataframe[column] if x < lower or x > upper]
    print(f'Identified outliers: {len(outliers)} of {len(dataframe[column])} values')
    # return outliers and boundaries
    return outliers, lower, upper


def remove_outliers(dataframe: pandas.DataFrame, column: str):
    _, lower, upper = identify_outliers(dataframe, column)
    return dataframe[(dataframe[column] >= lower) & (dataframe[column] <= upper)]
