/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   two.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 16:32:49 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/01 20:31:23 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	two_values(t_global_data *data, int stack)
{
	if (!data || (stack != STACK_A && stack != STACK_B))
		return (ERR);
	if (ft_is_sort(data, stack))
		return (OK);
	if (stack == STACK_A && data->a && *data->a > *(data->a + 1))
		swap(data, STACK_A, DISPLAY);
	if (stack == STACK_B && data->b && *data->b < *(data->b - 1))
		swap(data, STACK_B, DISPLAY);
	return (OK);
}
