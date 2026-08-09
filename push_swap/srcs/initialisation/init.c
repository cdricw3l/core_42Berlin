/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/31 20:06:23 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 08:59:03 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	init_global_data(char **argv, t_global_data *data)
{
	if (!argv || !*argv)
		return (ERR);
	ft_bzero(data, sizeof(t_global_data));
	data->size_a = check_args(argv, data);
	if (data->size_a == ERR || data->size_a > LIMIT)
		return (ERR);
	if (create_stack(argv, data) == ERR)
		return (ERR);
	if (check_duplicate(data) == ERR)
		return (ERR);
	data->disorder = compute_disorder(data);
	return (OK);
}
