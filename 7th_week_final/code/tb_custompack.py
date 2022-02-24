import numpy as module_np

def function_tsig(
    list_indicator
):

    '''
    This function accepts a list of
    indicator values and converts it
    to a trade signal series as a list.
    '''

    # Transform the entries of the
    # indicator series to create the
    # trade signal series 'list_sign'
    list_sign = [

        # Pass through 'sign' function
        module_np.sign(

            # Pass through 'maximum' function
            module_np.maximum(
                float_value,
                0
            )
        )

        # Iterate for all values in 'list_indicator'
        for float_value
        in list_indicator

    ]

    # Output 'list_sign'
    return list_sign

def function_action(
    list_sign
):

    '''
    This function accepts a list
    representing a trade signal series
    and transforms it to an action
    series.
    '''

    # Shift 'list_sign' by one step
    # and fill the first value with zero
    list_shift = [0] + list_sign[:-1]

    # Subtract entries 'list_shift' 
    # from 'list_sign' element-wise
    list_output = [

        list_sign[int_i] -
        list_shift[int_i]

        for int_i
        in range(
            0,
            len(list_sign)
        )
    ]

    # Return final action series
    # as a list
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

    # Derive the trade signal series
    # from the indicator series in the form
    # of 'list_inidcator'
    list_tsig = function_tsig(
        list_indicator = list_indicator
    )

    # Derive the action series from
    # the previously derived trade
    # signal series
    list_action = function_action(
        list_sign = list_tsig
    )

    # Create a list for storing the
    # alpha series of the trading
    # strategy
    list_alpha = []

    # Set the length of the list of
    # prices
    int_length = len(list_prices)

    # Carry out the algorithm to 
    # generate the alpha series
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

    # Return the final alpha series
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