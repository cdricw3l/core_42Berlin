/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   medium.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 17:17:06 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 09:18:00 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static int	place_int_stack(t_global_data *data, int value)
{
	int	count;
	int	*p_start;

	p_start = data->start;
	count = 1;
	while (p_start <= data->end)
	{
		if (*p_start < value)
			count++;
		p_start++;
	}
	return (count);
}

static void	get_fist_ptr_in_range(t_global_data *data, int range[2],
	int **p_start, int **p_end
)
{
	int			place;

	while (*p_start < *p_end)
	{
		place = place_int_stack(data, *(*p_start));
		if (place >= range[0] && place <= range[1])
			break ;
		(*p_start)++;
	}
	while (*p_end >= data->a)
	{
		place = place_int_stack(data, *(*p_end));
		if (place >= range[0] && place <= range[1])
			break ;
		(*p_end)--;
	}
}

t_best_move	*best_move(t_global_data *data, int range[2])
{
	int			*p_start;
	int			*p_end;
	t_best_move	*best;

	p_start = data->a;
	p_end = data->a + (data->size_a - 1);
	if (!data->a)
		return (NULL);
	get_fist_ptr_in_range(data, range, &p_start, &p_end);
	if (p_start > p_end)
		return (NULL);
	if (p_start - data->a < (data->a + (data->size_a - 1) - p_end) + 1
		|| p_end == p_start)
		best = build_best_move(*p_start, p_start - data->a, rotate);
	else
		best = build_best_move(*p_end, ((data->a + (data->size_a - 1)) - p_end)
				+ 1, rev_rotate);
	return (best);
}

static int	process_best_move(t_global_data *data)
{
	int			i;
	int			nb_range;
	int			ranges[LIMIT][2];
	t_best_move	*best;

	nb_range = generate_range(ranges, data->size_a,
			get_range_size(data->size_a));
	if (nb_range == ERR)
		return (ERR);
	i = 0;
	while (i < nb_range)
	{
		best = best_move(data, ranges[i]);
		while (best != NULL)
		{
			move(data, STACK_A, best->move, best->number);
			free(best);
			push(data, STACK_A, STACK_B, DISPLAY);
			best = best_move(data, ranges[i]);
		}
		i++;
	}
	return (OK);
}

int	medium_rank(t_global_data *data)
{
	if (data->size_a == 2)
		return (two_values(data, STACK_A));
	if (data->size_a == 3)
		return (three_values(data, STACK_A));
	if (process_best_move(data) == ERR)
		return (ERR);
	while (data->size_a < 3)
	{
		if (bigest_value(data, STACK_B))
			at_beginning(data, STACK_B, bigest_value(data, STACK_B));
		push(data, STACK_B, STACK_A, DISPLAY);
	}
	three_values(data, STACK_A);
	while (data->b)
	{
		if (immediat_superior(data, STACK_A, data->b))
			at_beginning(data, STACK_A,
				immediat_superior(data, STACK_A, data->b));
		push(data, STACK_B, STACK_A, DISPLAY);
	}
	if (smalest_value(data, STACK_A))
		at_beginning(data, STACK_A, smalest_value(data, STACK_A));
	return (OK);
}
