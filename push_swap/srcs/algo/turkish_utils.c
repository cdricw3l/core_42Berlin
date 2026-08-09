/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   turkish_utils.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mabrugge <mabrugge@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 12:21:03 by mabrugge          #+#    #+#             */
/*   Updated: 2026/06/02 18:14:59 by mabrugge         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	get_total_cost(t_best_cost *target, t_list *list)
{
	t_list		*current;
	t_best_cost	*cur;

	current = list;
	while (current)
	{
		cur = (t_best_cost *)(current->content);
		if (cur && cur->value == target->target_value)
			return (cur->number_of_move + target->number_of_move);
		current = current->next;
	}
	return (0);
}
