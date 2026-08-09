/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   bench.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 14:29:56 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 10:09:15 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

void	write_strategy(t_global_data *data)
{
	ft_putstr_fd("strategy: ", STDERR_FILENO);
	if (data->strategy == SIMPLE)
		ft_putstr_fd("Simple / O(n2)\n", STDERR_FILENO);
	if (data->strategy == MEDIUM)
		ft_putstr_fd("Medium / O(n√n)\n", STDERR_FILENO);
	if (data->strategy == COMPLEX)
		ft_putstr_fd("Complex / O(n log n)\n", STDERR_FILENO);
	if (data->strategy == ADAPTATIVE)
	{
		ft_putstr_fd("Adaptive / ", STDERR_FILENO);
		if (data->disorder < 0.2)
			ft_putstr_fd("O(n2)\n", STDERR_FILENO);
		else if (data->disorder >= 0.2 && data->disorder < 0.5)
			ft_putstr_fd("O(n√n)\n", STDERR_FILENO);
		else if (data->disorder > 0.5)
			ft_putstr_fd("O(n log n)\n", STDERR_FILENO);
	}
}

void	write_disorder(t_global_data *data)
{
	ft_putstr_fd("disorder: ", STDERR_FILENO);
	put_float(data->disorder, STDERR_FILENO);
	ft_putchar_fd('%', STDERR_FILENO);
	ft_putendl_fd("", STDERR_FILENO);
}

void	write_total_ops(t_global_data *data)
{
	int	i;
	int	total_ops;

	i = 0;
	total_ops = 0;
	while (i < 10)
		total_ops += data->move_count[i++];
	ft_putstr_fd("total_ops: ", STDERR_FILENO);
	ft_putnbr_fd(total_ops, STDERR_FILENO);
	ft_putendl_fd("", STDERR_FILENO);
}

void	write_move_ops(t_global_data *data)
{
	ft_putstr_fd("sa: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_SA], STDERR_FILENO);
	ft_putstr_fd(" sb: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_SB], STDERR_FILENO);
	ft_putstr_fd(" pa: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_PA], STDERR_FILENO);
	ft_putstr_fd(" pb: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_PB], STDERR_FILENO);
	ft_putendl_fd("", STDERR_FILENO);
	ft_putstr_fd("[bench] ", STDERR_FILENO);
	ft_putstr_fd("ra: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_RA], STDERR_FILENO);
	ft_putstr_fd(" rb: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_RB], STDERR_FILENO);
	ft_putstr_fd(" rr: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_RR], STDERR_FILENO);
	ft_putstr_fd(" rra: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_RRA], STDERR_FILENO);
	ft_putstr_fd(" rrb: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_RRB], STDERR_FILENO);
	ft_putstr_fd(" rrr: ", STDERR_FILENO);
	ft_putnbr_fd(data->move_count[B_RRR], STDERR_FILENO);
	ft_putendl_fd("", STDERR_FILENO);
}

int	benchmark(t_global_data *data)
{
	if (!data)
		return (ERR);
	ft_putstr_fd("[bench] ", STDERR_FILENO);
	write_disorder(data);
	ft_putstr_fd("[bench] ", STDERR_FILENO);
	write_strategy(data);
	ft_putstr_fd("[bench] ", STDERR_FILENO);
	write_total_ops(data);
	ft_putstr_fd("[bench] ", STDERR_FILENO);
	write_move_ops(data);
	return (OK);
}
