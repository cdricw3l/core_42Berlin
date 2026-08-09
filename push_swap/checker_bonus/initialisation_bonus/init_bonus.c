/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   init_bonus.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/31 20:06:23 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 00:49:03 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../checker.h"

int	init_global_data(char **argv, t_global_data *data)
{
	if (!argv || !*argv)
		return (ERR);
	ft_bzero(data, sizeof(t_global_data));
	data->size_a = check_args(argv);
	if (data->size_a == ERR)
		return (ERR);
	if (create_stack(argv, data) == ERR)
		return (ERR);
	if (check_duplicate(data) == ERR)
		return (ERR);
	return (OK);
}
