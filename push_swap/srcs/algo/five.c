/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   five.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mabrugge <mabrugge@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/26 16:32:49 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 12:05:52 by mabrugge         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	five_values(t_global_data *data, int stack)
{
	if (!data || stack != STACK_A)
		return (ERR);
	if (stack == STACK_A)
	{
		if (smalest_value(data, STACK_A))
			at_beginning(data, stack, smalest_value(data, STACK_A));
		else
			return (ERR);
		push(data, stack, STACK_B, DISPLAY);
		if (smalest_value(data, STACK_A))
			at_beginning(data, stack, smalest_value(data, STACK_A));
		else
			return (ERR);
		push(data, stack, STACK_B, DISPLAY);
		three_values(data, stack);
		push(data, STACK_B, stack, DISPLAY);
		push(data, STACK_B, stack, DISPLAY);
	}
	return (OK);
}
