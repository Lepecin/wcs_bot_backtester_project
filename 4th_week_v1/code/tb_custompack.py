import yfinance as module_yf
import pandas as module_pd
import numpy as module_np




def function_iind(
    series_indicator
):

    series_non_neg = module_np.maximum(
        series_indicator,
        0
    )

    series_sign = module_np.sign(
        series_non_neg
    )

    return series_sign




def function_sind(
    series_iindicator
):

    series_shift = series_iindicator.shift(
        fill_value = 0
    )

    series_diff = series_iindicator - series_shift

    return series_diff




def function_backtester(
    series_prices,
    series_indicator,
    float_ratio
):

    '''
    Backtester for either a long or short position.

    Long positions are tested with positive 'float_ratio'.

    Short positions are tested with negative 'float_ratio'.
    '''

    series_prices = series_prices.reset_index(
        drop = True
    )
    series_indicator = series_indicator.reset_index(
        drop = True
    )

    series_iind = function_iind(
        series_indicator = series_indicator
    )
    series_sind = function_sind(
        series_iindicator = series_iind
    )

    list_alpha_plus = list()
    int_length = len(series_prices)

    for int_i in range(0, int_length):

        if series_sind[int_i] == 1:

            list_alpha_plus.append(1)
            float_invest_price = series_prices[int_i]

        if series_sind[int_i] == 0:

            if series_iind[int_i] == 1:

                list_alpha_plus.append(
                    (float_invest_price + (series_prices[int_i] - float_invest_price) * float_ratio) / 
                    (float_invest_price + (series_prices[int_i - 1] - float_invest_price) * float_ratio)
                )

            if series_iind[int_i] == 0:

                list_alpha_plus.append(1)

        if series_sind[int_i] == -1:

            list_alpha_plus.append(
                (float_invest_price + (series_prices[int_i] - float_invest_price) * float_ratio) / 
                (float_invest_price + (series_prices[int_i - 1] - float_invest_price) * float_ratio)
            )
    
    series_alpha_plus = module_pd.Series(
        data = list_alpha_plus
    )

    return series_alpha_plus
    
