/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   movement.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 09:01:59 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 13:32:46 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../checker.h"

int	push(t_global_data *data, int src, int dst)
{
	if (check_push_input(data, src, dst) != OK)
		return (check_push_input(data, src, dst));
	if (src == STACK_A && dst == STACK_B && data->size_a)
	{
		data->b = data->a;
		data->size_b++;
		data->a++;
		data->size_a--;
		if (data->size_a == 0)
			data->a = NULL;
	}
	if (src == STACK_B && dst == STACK_A && data->size_b)
	{
		data->a = data->b;
		data->size_a++;
		data->b--;
		data->size_b--;
		if (data->size_b == 0)
			data->b = NULL;
	}
	return (OK);
}

int	swap(t_global_data *data, int stack)
{
	if (!data || (stack != STACK_A && stack != STACK_B))
		return (ERR);
	if (stack == STACK_A && data->size_a > 1)
		ft_swap(data->a, data->a + 1);
	else if (stack == STACK_B)
		ft_swap(data->b, data->b - 1);
	return (OK);
}

int	rotate(t_global_data *data, int stack)
{
	int	tmp;

	if (!data || (stack != STACK_A && stack != STACK_B))
		return (ERR);
	if (stack == STACK_A && data->a && data->size_a > 0)
	{
		tmp = *(data->a);
		ft_memmove(data->a, data->a + 1, (data->size_a - 1) * sizeof(int));
		*(data->a + (data->size_a - 1)) = tmp;
	}
	else if (stack == STACK_B && data->b && data->size_b > 0)
	{
		tmp = *(data->b);
		ft_memmove(data->b - (data->size_b - 2), data->b - (data->size_b - 1),
			(data->size_b - 1) * sizeof(int));
		*(data->b - (data->size_b - 1)) = tmp;
	}
	return (OK);
}

int	rev_rotate(t_global_data *data, int stack)
{
	int	tmp;

	if (!data || (stack != STACK_A && stack != STACK_B))
		return (ERR);
	if (stack == STACK_A && data->a && data->size_a > 0)
	{
		tmp = *(data->a + data->size_a - 1);
		ft_memmove(data->a + 1, data->a, (data->size_a - 1) * sizeof(int));
		*(data->a) = tmp;
	}
	else if (stack == STACK_B && data->b && data->size_b > 0)
	{
		tmp = *(data->b - (data->size_b - 1));
		ft_memmove(data->b - (data->size_b - 1), data->b - (data->size_b - 2),
			(data->size_b - 1) * sizeof(int));
		*(data->b) = tmp;
	}
	return (OK);
}

int	double_rotation(t_global_data *data, int move)
{
	if (move != RR && move != RRR)
		return (ERR);
	if (move == RR)
	{
		rotate(data, STACK_A);
		rotate(data, STACK_B);
	}
	else if (move == RRR)
	{
		rev_rotate(data, STACK_A);
		rev_rotate(data, STACK_B);
	}
	return (OK);
}
