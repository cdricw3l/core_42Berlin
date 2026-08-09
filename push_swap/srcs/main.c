/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/19 19:08:25 by cdric.b           #+#    #+#             */
/*   Updated: 2026/06/03 11:38:31 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../include/push_swap.h"

static int	processing_message(int code)
{
	if (code == ERR)
	{
		write(STDOUT_FILENO, "processing error\n",
			ft_strlen("processing error\n"));
		return (1);
	}
	return (0);
}

int	adaptative_stategie(t_global_data *data)
{
	if (data->disorder < 0 || data->disorder > 1)
		return (ERR);
	else if (data->disorder < 0.2)
		return (selection_sort(data));
	else if (data->disorder >= 0.2 && data->disorder < 0.5)
		return (medium_rank(data));
	else if (data->disorder >= 0.5)
		return (turkish(data));
	return (OK);
}

int	processing(t_global_data *data)
{
	int	status;

	status = OK;
	if (data->strategy == SIMPLE)
		status = selection_sort(data);
	else if (data->strategy == MEDIUM)
		status = medium_rank(data);
	else if (data->strategy == COMPLEX)
		status = turkish(data);
	else if (data->strategy == ADAPTATIVE || data->strategy == NONE)
		status = adaptative_stategie(data);
	return (processing_message(status));
}

int	main(int argc, char **argv)
{
	t_global_data	data;
	int				status;

	(void)argc;
	if (argc == 1)
		return (1);
	if (init_global_data(&argv[1], &data) == ERR)
	{
		ft_putstr_fd("Error\n", STDERR_FILENO);
		return (1);
	}
	if (ft_is_sort(&data, STACK_A) && data.bench_mode == BENCH)
		return (benchmark(&data));
	else if (ft_is_sort(&data, STACK_A) && data.bench_mode != BENCH)
		return (0);
	status = processing(&data);
	if (data.bench_mode == BENCH)
		benchmark(&data);
	return (status);
}
