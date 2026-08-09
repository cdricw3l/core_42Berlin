/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   at_beginning.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mabrugge <mabrugge@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 15:27:23 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 12:08:33 by mabrugge         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

/**
 * @brief return the absolute value for long type
 * @param value value to convert
 * @return return the absolut value
 */
static long	ft_abs(long value)
{
	if (value < 0)
		return (value * -1);
	return (value);
}

/**
 * @brief return the cost of a 
 * rotation and a rev_rotation for a value in the stack
 * @param born Le premier entier.
 * @param data structure with stack data.
 * @param stack stack of calculation (STACK_A or STACK_B)
 * @param value pointer to the value to analyse
 * @return OK, NO_MOVE or ERR.
 */
int	get_born(long born[2], t_global_data *data, int stack, int *value)
{
	if (!value || (stack != STACK_A && stack != STACK_B))
		return (ERR);
	if (stack == STACK_A)
	{
		if (data->size_a == 0
			|| value > data->a + (data->size_a - 1) || value < data->a)
			return (NO_MOVE);
		born[LE] = (((long)value - (long)data->a) / 4);
		born[RI] = ft_abs((long)value - ((long)(data->a + (data->size_a - 1))))
			/ sizeof(int) + 1;
		if (value == data->a)
			return (NO_MOVE);
	}
	else if (stack == STACK_B)
	{
		if (data->size_b == 0
			|| value < data->b - (data->size_b - 1) || value > data->b)
			return (NO_MOVE);
		born[LE] = ft_abs(((long)value - (long) data->b) / 4);
		born[RI] = (((long)value - ((long)(data->b - (data->size_b - 1))))
				/ sizeof(int)) + 1;
		if (value == data->b)
			return (NO_MOVE);
	}
	return (OK);
}
/**
 * @brief take the integer pointer gived as argument and do an otimised rotation
 * @param born Le premier entier.
 * @param data structure with stack data.
 * @param stack stack where de rotation is made (STACK_A or STACK_B)
 * @param value pointer to the value to analyse
 * @return OK, NO_MOVE or ERR.
 */

int	at_beginning(t_global_data *data, int stack, int *value)
{
	long	born[2];
	int		status;

	status = get_born(born, data, stack, value);
	if (status == ERR)
		return (ERR);
	else if (status == NO_MOVE)
		return (NO_MOVE);
	if (born[LE] > born[RI] || born[LE] == born[RI])
		move(data, stack, rev_rotate, born[RI]);
	else if (born[RI] > born[LE])
		move(data, stack, rotate, born[LE]);
	return (OK);
}
/**
 * @brief apply the fonction movement given as argument (rotate or rev_rotate)
 * @param data structure with stack data.
 * @param stack stack where de rotation is made (STACK_A or STACK_B)
 * @param f the fonction to apply to the stack
 * @param counter number of application
 * @return OK, NO_MOVE or ERR.
 */

int	move(t_global_data *data, int stack,
	int (f)(t_global_data *, int, int), int counter
)
{
	int	i;

	i = 0;
	if ((stack != STACK_A && stack != STACK_B) || !data || !f)
		return (ERR);
	while (i < counter)
	{
		f(data, stack, DISPLAY);
		i++;
	}
	return (OK);
}
