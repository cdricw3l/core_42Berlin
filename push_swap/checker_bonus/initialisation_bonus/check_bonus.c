/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   check_bonus.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cdric.b <cdric.b@student.42.fr>            +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/19 14:34:24 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 00:22:17 by cdric.b          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../checker.h"

static int	check_digit(char *str)
{
	char	*ptr;

	ptr = str;
	if (!ptr || !*ptr)
		return (ERR);
	if (*ptr == MINUS || *ptr == PLUS)
		ptr++;
	while (*ptr)
	{
		if (!ft_isdigit(*ptr))
			return (ERR);
		ptr++;
	}
	return (OK);
}

static int	check_arg(char *arg)
{
	if (!arg)
		return (ERR);
	if (check_digit(arg) == ERR || ft_atoi_long(arg) > INT_MAX
		|| ft_atoi_long(arg) < INT_MIN)
		return (ERR);
	return (OK);
}
/* idx[0]= couter_input idx[1] = idx i idx[2] = idx j*/

int	check_args(char **argv)
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
		if (k == 0 && data->algo != NONE)
			i++;
		while (split[i])
			data->stack[j++] = ft_atoi_long(split[i++]);
		ft_split_clean(&split, OK);
		k++;
	}
	data->a = data->stack;
	data->start = data->stack;
	data->end = &data->stack[data->size_a - 1];
	data->b = NULL;
	return (OK);
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
