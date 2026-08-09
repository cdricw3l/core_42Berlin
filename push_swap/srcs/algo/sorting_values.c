/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sorting_values.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mabrugge <mabrugge@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/27 09:44:49 by mabrugge          #+#    #+#             */
/*   Updated: 2026/06/02 12:12:54 by mabrugge         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	selection_sort(t_global_data *data)
{
	while (data->size_a > 3)
	{
		if (smalest_value(data, STACK_A))
			at_beginning(data, STACK_A, smalest_value(data, STACK_A));
		push(data, STACK_A, STACK_B, DISPLAY);
	}
	three_values(data, STACK_A);
	while (data->b)
		push(data, STACK_B, STACK_A, DISPLAY);
	return (OK);
}
