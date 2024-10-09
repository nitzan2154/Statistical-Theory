import numpy as np
import pandas as pd
import scipy.stats as stats

def multi_index_df(df, indices_list):
  return df.set_index(indices_list).sort_index()

def reject_H0(p_value, alpha=0.05, n_hypotheses=1):
    # Using Bonferroni correction
    if p_value < alpha/n_hypotheses:
        return "Yes"
    else:
        return "No"

# Normality test

def normality_test(data,
                   selected_index_value,
                   selected_column, selected_column_value,
                   selected_feature_to_test="Life expectancy",
                   threshold=30):
    """
    selected_index_value: categorical feature value by which we want to test.
    selected_column: usually Year.
    """
    data_to_test = (data[data[selected_column]==selected_column_value]
                    .loc[selected_index_value, selected_feature_to_test])
    n = len(data_to_test)

    if n <= threshold:
        test_name = "Shapiro-Wilk"
        statistic, p_value = stats.shapiro(data_to_test)
    else:
        test_name = "Kolmogorov-Smirnov"
        statistic, p_value = stats.kstest(data_to_test, 'norm',
                                          args=(np.mean(data_to_test),
                                                np.std(data_to_test)))

    return round(statistic, 3), round(p_value, 3)

def create_normality_test_df(data,
                             indices_list, selected_index_value,
                             selected_column, selected_column_values_list,
                             selected_feature_to_test="Life_expectancy",
                             threshold=30):
    """
    indices_list: will be of the form: [feature, "Country"].
    selected_index_value: categorical feature value by which we want to test.
    selected_column: usually Year.
    selected_column_values_list: list of years.
    """

    current_multi_index_df = multi_index_df(df=data, indices_list=indices_list)

    results = [normality_test(current_multi_index_df, 
                               selected_index_value, 
                               selected_column, 
                               selected_column_value, 
                               selected_feature_to_test) for selected_column_value in selected_column_values_list]

    D_values = [result[0] for result in results]
    p_values = [result[1] for result in results]
    
    reject_H0_values = [reject_H0(p_value, n_hypotheses=len(selected_column_values_list)) for p_value in p_values]

    return pd.DataFrame({
        selected_column: selected_column_values_list,
        "D value": D_values,
        "p value": p_values,
        "Reject $H_0$": reject_H0_values
    })

# Variance homogeniety

def create_variance_homogeneity_test_df(data,
                              indices_list,
                              selected_index_values,
                              selected_column, selected_column_values,
                              selected_feature_to_test="Life_expectancy"):
    """
    indices_list: will be of the form: [feature, "Country"].
    selected_index_values: list of feature values by which we want to test.
    selected_column: usually Year.
    selected_column_values: list of years.
    """

    current_multi_index_df = multi_index_df(df=data, indices_list=indices_list)
    W_values = []
    p_values = []
    for selected_column_value in selected_column_values:
        samples = [(current_multi_index_df[current_multi_index_df[selected_column]==selected_column_value]
                    .loc[selected_index_value, selected_feature_to_test]) for selected_index_value in selected_index_values]
        W_value, p_value = stats.levene(*samples)
        W_values.append(round(W_value, 3))
        p_values.append(round(p_value, 3))

    reject_H0_values = [reject_H0(p_value, n_hypotheses=len(selected_column_values)) for p_value in p_values]
        
    return pd.DataFrame({
        selected_column: selected_column_values,
        "W value": W_values,
        "p value": p_values,
        "Reject $H_0$": reject_H0_values
    })

# T-test

def independent_2_sample_t_test(data,
                                selected_index_value1, selected_index_value2,
                                selected_column, selected_column_value,
                                selected_feature_to_test = "Life_expectancy"):
    """
    selected_index_value1: first feature value by which we want to test.
    selected_index_value2: second feature value by which we want to test.    
    selected_column: usually Year.
    selected_column_value: year we want to test.    
    """
    data_to_test1 = (data[data[selected_column]==selected_column_value]
                     .loc[selected_index_value1, selected_feature_to_test])
    data_to_test2 = (data[data[selected_column]==selected_column_value]
                     .loc[selected_index_value2, selected_feature_to_test])
    
    t_value, p_value = stats.ttest_ind(data_to_test1, data_to_test2, alternative="greater")
    return round(t_value, 3), round(p_value, 3)

def create_independent_2_sample_t_test_df(data,
                                          indices_list,
                                          selected_index_values_pairs_list,
                                          selected_column, selected_column_value,
                                          selected_feature_to_test = "Life_expectancy"):
    """
    indices_list: will be of the form: [feature, "Country"].
    selected_index_values_pairs_list: pairs of feature values.
    selected_column: usually Year.
    selected_column_value: year we want to test.
    """
    current_multi_index_df = multi_index_df(df=data, indices_list=indices_list)

    H0_list = [f"$\mu_{{{selected_index_value1}}} \leq \mu_{{{selected_index_value2}}}$"
               for selected_index_value1, selected_index_value2 in selected_index_values_pairs_list]

    results = [independent_2_sample_t_test(current_multi_index_df, 
                               selected_index_value1, 
                               selected_index_value2,
                               selected_column, 
                               selected_column_value, 
                               selected_feature_to_test) 
               for selected_index_value1, selected_index_value2 in selected_index_values_pairs_list]
    
    T_values = [result[0] for result in results]
    p_values = [result[1] for result in results]
    
    reject_H0_values = [reject_H0(p_value, n_hypotheses=len(H0_list)) for p_value in p_values]

    return pd.DataFrame({
        "$H_0$": H0_list,
        "T value": T_values,
        "p value (one-sided)": p_values,
        "Reject $H_0$": reject_H0_values
    })

# Mann-Whitney

def independent_Mann_Whitney_U_rank_test(data,
                                selected_index_value1, selected_index_value2,
                                selected_column, selected_column_value,
                                selected_feature_to_test = "Life_expectancy"):
    """
    selected_index_value1: first feature value by which we want to test.
    selected_index_value2: second feature value by which we want to test.    
    selected_column: usually Year.
    selected_column_value: year we want to test.    
    """
    data_to_test1 = (data[data[selected_column]==selected_column_value]
                     .loc[selected_index_value1, selected_feature_to_test])
    data_to_test2 = (data[data[selected_column]==selected_column_value]
                     .loc[selected_index_value2, selected_feature_to_test])
    
    U_value, p_value = stats.mannwhitneyu(data_to_test1, data_to_test2, alternative="greater")
    return round(U_value, 3), round(p_value, 3)

def create_independent_Mann_Whitney_U_rank_test_df(data,
                                          indices_list,
                                          selected_index_values_pairs_list,
                                          selected_column, selected_column_value,
                                          selected_feature_to_test = "Life_expectancy"):
    """
    indices_list: will be of the form: [feature, "Country"].
    selected_index_values_pairs_list: pairs of feature values.
    selected_column: usually Year.
    selected_column_value: year we want to test.
    """
    current_multi_index_df = multi_index_df(df=data, indices_list=indices_list)

    H0_list = [f"$\text{{med}}_{{{selected_index_value1}}} \leq \text{{med}}_{{{selected_index_value2}}}$"
               for selected_index_value1, selected_index_value2 in selected_index_values_pairs_list]

    results = [independent_Mann_Whitney_U_rank_test(current_multi_index_df, 
                               selected_index_value1, 
                               selected_index_value2,
                               selected_column, 
                               selected_column_value, 
                               selected_feature_to_test) 
               for selected_index_value1, selected_index_value2 in selected_index_values_pairs_list]
    
    U_values = [result[0] for result in results]
    p_values = [result[1] for result in results]
    
    reject_H0_values = [reject_H0(p_value, n_hypotheses=len(H0_list)) for p_value in p_values]

    return pd.DataFrame({
        "$H_0$": H0_list,
        "U value": U_values,
        "p value (one-sided)": p_values,
        "Reject $H_0$": reject_H0_values
    })

