/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_1.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 10:11:29 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 11:35:53 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	get_complexity(char *arg)
{
	if (ft_strncmp(arg, "--simple", ft_strlen_longest("--simple", arg)) == OK)
		return (SIMPLE);
	else if (ft_strncmp(arg, "--medium", ft_strlen_longest("--medium",
				arg)) == OK)
		return (MEDIUM);
	else if (ft_strncmp(arg, "--complex", ft_strlen_longest("--complex",
				arg)) == OK)
		return (COMPLEX);
	else if (ft_strncmp(arg, "--adaptive", ft_strlen_longest("--adaptive",
				arg)) == OK)
		return (ADAPTATIVE);
	else if (ft_strncmp(arg, "--bench", ft_strlen_longest("--bench",
				arg)) == OK)
		return (BENCH);
	return (NONE);
}

int	check_arg(char *arg)
{
	if (!arg)
		return (ERR);
	if (check_digit(arg) == ERR || ft_atoi_long(arg) > INT_MAX
		|| ft_atoi_long(arg) < INT_MIN)
		return (ERR);
	return (OK);
}

float	compute_disorder(t_global_data *data)
{
	int		i;
	int		j;
	float	mistakes;
	float	total_pairs;

	i = 0;
	mistakes = 0;
	total_pairs = 0;
	while (i < data->size_a)
	{
		j = i + 1;
		while (j < data->size_a)
		{
			total_pairs++;
			if (data->stack[i] > data->stack[j])
				mistakes++;
			j++;
		}
		i++;
	}
	return (mistakes / total_pairs);
}

int	ft_is_sort(t_global_data *data, int stack)
{
	int				i;
	t_stack_data	stk;

	if (get_stack_data(data, stack, &stk) == ERR)
		return (-1);
	i = 0;
	while (i < stk.len - 1)
	{
		if (stack == STACK_A)
		{
			if (*(stk.arr) > *(stk.arr + 1))
				return (0);
			stk.arr++;
		}
		else if (stack == STACK_B)
		{
			if (*(stk.arr) < *(stk.arr - 1))
				return (0);
			stk.arr--;
		}
		i++;
	}
	return (1);
}

int	check_digit(char *str)
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
