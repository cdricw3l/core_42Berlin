/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_2.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/28 09:51:58 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 09:14:01 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	flags_check_managment(t_global_data *data, size_t idx[3],
	char *value, int mode)
{
	if (mode == ARG_CHECK && idx[1] == 0 && get_complexity(value) == BENCH)
	{
		data->bench_mode = get_complexity(value);
		idx[2]++;
	}
	if (mode == ARG_CHECK && ((idx[1] == 0 && data->bench_mode != BENCH)
			|| idx[1] == 1) && get_complexity(value) != NONE)
	{
		data->strategy = get_complexity(value);
		idx[2]++;
	}
}

t_best_move	*build_best_move(int value, int counter,
	int (f)(t_global_data *, int, int)
)
{
	t_best_move	*best_move;

	best_move = malloc(sizeof(t_best_move));
	if (!best_move)
		return (NULL);
	best_move->value = value;
	best_move->number = counter;
	best_move->move = f;
	return (best_move);
}

int	get_range_size(int size_list)
{
	if (size_list >= 1 && size_list <= 10)
		return (size_list);
	else if (size_list > 10)
		return (10);
	return (0);
}

int	generate_range(int ranges[LIMIT][2], int total_size, int range_size)
{
	int	base;
	int	range_start;
	int	range_end;
	int	i;

	if (total_size > LIMIT || total_size < 1)
		return (ERR);
	range_start = 1;
	range_end = total_size / range_size;
	base = total_size / (total_size / range_size);
	i = 0;
	if (total_size % range_size)
		base += 1;
	while (i < base)
	{
		ranges[i][0] = range_start;
		ranges[i][1] = range_end;
		range_start += (total_size / range_size);
		range_end += (total_size / range_size);
		if (i == base - 1 && total_size % range_size > 0)
			ranges[i][1] = ranges[i][0] + (total_size % range_size) - 1;
		i += 1;
	}
	return (i);
}

int	get_stack_data(t_global_data *data, int stack, t_stack_data *stk)
{
	if (!data || (stack != STACK_A && stack != STACK_B))
		return (ERR);
	if (stack == STACK_A)
	{
		stk->arr = data->a;
		stk->len = data->size_a;
	}
	else if (stack == STACK_B)
	{
		stk->arr = data->b;
		stk->len = data->size_b;
	}
	return (OK);
}
