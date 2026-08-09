/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 00:34:00 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 01:16:07 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../checker.h"

int	check_push_input(t_global_data *data, int src, int dst)
{
	if (!data)
		return (ERR);
	else if ((src != STACK_A && src != STACK_B)
		|| (dst != STACK_A && dst != STACK_B))
		return (ERR);
	else if ((src == STACK_A && data->size_a <= 0)
		|| (src == STACK_B && data->size_b <= 0))
		return (ERR);
	return (OK);
}
