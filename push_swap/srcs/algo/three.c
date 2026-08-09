/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   three.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 16:31:22 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/01 20:25:28 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static int	three_value_data(t_global_data *data, int stack, int idx[3])
{
	if (stack != STACK_A && stack != STACK_B)
		return (ERR);
	if (stack == STACK_A)
	{
		idx[0] = *(data->a);
		idx[1] = *(data->a + 1);
		idx[2] = *(data->a + 2);
	}
	else if (stack == STACK_B)
	{
		idx[0] = *(data->b);
		idx[1] = *(data->b - 1);
		idx[2] = *(data->b - 2);
	}
	return (OK);
}

static int	three_values_stack_a(t_global_data *data, int stack)
{
	int	idx[3];

	if (three_value_data(data, stack, idx) == ERR)
		return (ERR);
	if (idx[0] < idx[1] && idx[0] < idx[2])
	{
		swap(data, stack, DISPLAY);
		rotate(data, stack, DISPLAY);
	}
	else if (idx[0] > idx[1] && idx[1] > idx[2])
	{
		swap(data, stack, DISPLAY);
		rev_rotate(data, stack, DISPLAY);
	}
	else if (idx[0] > idx[1] && idx[0] < idx[2])
		swap(data, stack, DISPLAY);
	else if (idx[0] < idx[1] && idx[1] > idx[2])
		rev_rotate(data, stack, DISPLAY);
	else if (idx[0] > idx[1] && idx[0] > idx[2])
		rotate(data, stack, DISPLAY);
	return (OK);
}

static int	three_values_stack_b(t_global_data *data, int stack)
{
	int	idx[3];

	if (three_value_data(data, stack, idx) == ERR)
		return (ERR);
	if (idx[0] < idx[1] && idx[1] < idx[2])
	{
		swap(data, stack, DISPLAY);
		rev_rotate(data, stack, DISPLAY);
	}
	else if (idx[0] > idx[1] && idx[0] > idx[2])
	{
		swap(data, stack, DISPLAY);
		rotate(data, stack, DISPLAY);
	}
	else if (idx[0] < idx[1] && idx[0] < idx[2])
		rotate(data, stack, DISPLAY);
	else if (idx[0] > idx[1] && idx[1] < idx[2])
		rev_rotate(data, stack, DISPLAY);
	else if (idx[0] < idx[1] && idx[1] > idx[2])
		swap(data, stack, DISPLAY);
	return (OK);
}

int	three_values(t_global_data *data, int stack)
{
	if (ft_is_sort(data, stack))
		return (NO_MOVE);
	if (stack == STACK_A)
		return (three_values_stack_a(data, stack));
	if (stack == STACK_B)
		return (three_values_stack_b(data, stack));
	return (ERR);
}
