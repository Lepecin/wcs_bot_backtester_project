import yfinance as module_yf
import pandas as module_pd
import numpy as module_np
import collections as module_cl



def function_tsig(
    list_indicator
):

    vector_indicator = module_np.array(
        object = list_indicator
    )

    vector_non_neg = module_np.maximum(
        vector_indicator,
        0
    )

    vector_sign = module_np.sign(
        vector_non_neg
    )

    list_sign = list(
        vector_sign
    )

    return list_sign


def function_list_shift(
    list_input,
    float_fill
):

    deque_input = module_cl.deque(
        iterable = list_input
    )

    deque_input.pop()

    deque_input.appendleft(
        float_fill
    )

    return list(
        deque_input
    )

def function_action(
    list_sign
):

    list_shift = function_list_shift(
        list_input = list_sign,
        float_fill = 0
    )

    list_output = list(
        module_np.array(
            list_sign
        ) - 
        module_np.array(
            list_shift
        )
    )

    return list_output


def function_backtester(
    list_prices,
    list_indicator,
    float_ratio
):

    '''
    Backtester for either a long or short position.

    Long positions are tested with positive 'float_ratio'.

    Short positions are tested with negative 'float_ratio'.
    '''

    list_tsig = function_tsig(
        list_indicator = list_indicator
    )

    list_action = function_action(
        list_sign = list_tsig
    )

    list_alpha = []

    int_length = len(list_prices)

    for int_i in range(0, int_length):

        if list_action[int_i] == 1:

            list_alpha.append(1)
            float_inprice = list_prices[int_i]

        if list_action[int_i] == 0:

            if list_tsig[int_i] == 1:

                list_alpha.append(
                    (float_inprice + (list_prices[int_i] - float_inprice) * float_ratio) / 
                    (float_inprice + (list_prices[int_i - 1] - float_inprice) * float_ratio)
                )

            if list_tsig[int_i] == 0:

                list_alpha.append(1)

        if list_action[int_i] == -1:

            list_alpha.append(
                (float_inprice + (list_prices[int_i] - float_inprice) * float_ratio) / 
                (float_inprice + (list_prices[int_i - 1] - float_inprice) * float_ratio)
            )

    return list_alpha
    



def function_heikin_ashi_gen(
    list_values,
    float_initial,
    float_strength
):

    list_output = [
        float_initial
    ]

    int_length = len(
        list_values
    )

    for int_i in range(0, int_length - 1):

        float_new_ha = list_output[int_i] * float_strength + list_values[int_i + 1] - list_values[int_i]

        list_output.append(
            float_new_ha
        )

    return list_output