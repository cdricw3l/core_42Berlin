/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   movement.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/21 09:01:59 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 10:17:01 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	push(t_global_data *data, int src, int dst, int mode)
{
	if (check_push_input(data, src, dst) != OK)
		return (check_push_input(data, src, dst));
	if (src == STACK_A && dst == STACK_B && data->size_a)
	{
		data->move_count[B_PB] += 1;
		data->b = data->a;
		data->size_b++;
		data->a++;
		data->size_a--;
		if (data->size_a == 0)
			data->a = NULL;
	}
	if (src == STACK_B && dst == STACK_A && data->size_b)
	{
		data->move_count[B_PA] += 1;
		data->a = data->b;
		data->size_a++;
		data->b--;
		data->size_b--;
		if (data->size_b == 0)
			data->b = NULL;
	}
	if (mode == DISPLAY)
		print_move(P, dst);
	return (OK);
}

int	swap(t_global_data *data, int stack, int mode)
{
	t_stack_data	stk;

	if (!data || get_stack_data(data, stack, &stk) == ERR)
		return (ERR);
	if (!stk.arr && stk.len < 2)
		return (NO_MOVE);
	if (stack == STACK_A)
	{
		ft_swap(stk.arr, stk.arr + 1);
		data->move_count[B_SA] += 1;
	}
	else if (stack == STACK_B)
	{
		ft_swap(stk.arr, stk.arr - 1);
		data->move_count[B_SB] += 1;
	}
	if (mode == DISPLAY)
		print_move(S, stack);
	return (OK);
}

int	rotate(t_global_data *data, int stack, int mode)
{
	int	tmp;

	if (!data || (stack != STACK_A && stack != STACK_B))
		return (NO_MOVE);
	if (stack == STACK_A && data->a && data->size_a > 0)
	{
		tmp = *(data->a);
		ft_memmove(data->a, data->a + 1, (data->size_a - 1) * sizeof(int));
		*(data->a + (data->size_a - 1)) = tmp;
		data->move_count[B_RA] += 1;
	}
	else if (stack == STACK_B && data->b && data->size_b > 0)
	{
		tmp = *(data->b);
		ft_memmove(data->b - (data->size_b - 2), data->b - (data->size_b - 1),
			(data->size_b - 1) * sizeof(int));
		*(data->b - (data->size_b - 1)) = tmp;
		data->move_count[B_RB] += 1;
	}
	if (mode == DISPLAY)
		print_move(R, stack);
	return (OK);
}

int	rev_rotate(t_global_data *data, int stack, int mode)
{
	int	tmp;

	if (!data || (stack != STACK_A && stack != STACK_B))
		return (NO_MOVE);
	if (stack == STACK_A && data->a && data->size_a > 0)
	{
		tmp = *(data->a + data->size_a - 1);
		ft_memmove(data->a + 1, data->a, (data->size_a - 1) * sizeof(int));
		*(data->a) = tmp;
		data->move_count[B_RRA] += 1;
	}
	else if (stack == STACK_B && data->b && data->size_b > 0)
	{
		tmp = *(data->b - (data->size_b - 1));
		ft_memmove(data->b - (data->size_b - 1), data->b - (data->size_b - 2),
			(data->size_b - 1) * sizeof(int));
		*(data->b) = tmp;
		data->move_count[B_RRB] += 1;
	}
	if (mode == DISPLAY)
		print_move(RV, stack);
	return (OK);
}

int	double_rotation(t_global_data *data, int move, int mode)
{
	if (move != RR && move != RRR)
		return (NO_MOVE);
	if (move == RR)
	{
		rotate(data, STACK_A, NO_DISPLAY);
		rotate(data, STACK_B, NO_DISPLAY);
		if (mode == DISPLAY)
			print_move(RR, A_AND_B);
		data->move_count[B_RR] += 1;
	}
	else if (move == RRR)
	{
		rev_rotate(data, STACK_A, NO_DISPLAY);
		rev_rotate(data, STACK_B, NO_DISPLAY);
		if (mode == DISPLAY)
			print_move(RRR, A_AND_B);
		data->move_count[B_RRR] += 1;
	}
	return (OK);
}
