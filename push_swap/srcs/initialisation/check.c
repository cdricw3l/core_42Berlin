/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/19 14:34:24 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 00:19:14 by cdric.b          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static int	init_stack(t_global_data *data)
{
	data->a = data->stack;
	data->start = data->stack;
	data->end = &data->stack[data->size_a - 1];
	data->b = NULL;
	return (OK);
}
/* idx[0]= couter_input idx[1] = idx i idx[2] = idx j*/

int	check_args(char **argv, t_global_data *data)
{
	size_t	idx[3];
	char	**split;

	ft_bzero(&idx, sizeof(size_t) * 3);
	while (argv[idx[1]])
	{
		split = ft_split(argv[idx[1]], SPACE);
		if (!split)
			return (ERR);
		idx[2] = 0;
		flags_check_managment(data, idx, split[0], ARG_CHECK);
		while (split[idx[2]])
		{
			if (check_arg(split[idx[2]++]) == ERR)
				return (ft_split_clean(&split, ERR));
			idx[0]++;
		}
		ft_split_clean(&split, OK);
		idx[1]++;
	}
	return (idx[0]);
}

int	create_stack(char **argv, t_global_data *data)
{
	size_t	i;
	size_t	j;
	size_t	k;
	char	**split;

	k = 0;
	j = 0;
	while (argv[k])
	{
		split = ft_split(argv[k], SPACE);
		if (!split)
			return (ERR);
		i = 0;
		if ((k == 0) && data->bench_mode == BENCH)
			i++;
		if (((k == 0 && data->bench_mode != BENCH)
				|| (k == 1 && data->bench_mode == BENCH))
			&& data->strategy != NONE)
			i++;
		while (split[i])
			data->stack[j++] = ft_atoi_long(split[i++]);
		ft_split_clean(&split, OK);
		k++;
	}
	return (init_stack(data));
}

int	check_duplicate(t_global_data *data)
{
	int	i;
	int	j;

	i = 0;
	while (i < data->size_a)
	{
		j = i + 1;
		while (j < data->size_a)
		{
			if (data->stack[i] == data->stack[j])
				return (ERR);
			j++;
		}
		i++;
	}
	return (OK);
}
