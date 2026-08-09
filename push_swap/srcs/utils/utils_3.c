/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils_3.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: mabrugge <mabrugge@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/02 12:18:19 by mabrugge          #+#    #+#             */
/*   Updated: 2026/06/02 20:05:50 by mabrugge         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

int	check_push_input(t_global_data *data, int src, int dst)
{
	if (!data)
		return (ERR);
	else if ((src != STACK_A && src != STACK_B) || (dst != STACK_A
			&& dst != STACK_B))
		return (ERR);
	else if ((src == STACK_A && data->size_a <= 0) || (src == STACK_B
			&& data->size_b <= 0))
		return (NO_MOVE);
	return (OK);
}

int	get_target_number(t_global_data *data, int stack, t_list **lst)
{
	t_stack_data	stk;
	t_list			*new_node;
	t_best_cost		*best;
	int				i;

	i = 0;
	get_stack_data(data, stack, &stk);
	while (i < stk.len)
	{
		best = malloc(sizeof(t_best_cost));
		if (!best)
			return (free_list(lst));
		*best = (t_best_cost){0};
		if (stack == STACK_A)
			init_best_cost(best, data, stack, stk.arr + i);
		else
			init_best_cost(best, data, stack, stk.arr - i);
		new_node = ft_lstnew(best);
		if (!new_node)
			return (free(best), free_list(lst), ERR);
		ft_lstadd_back(lst, new_node);
		i++;
	}
	return (OK);
}

void	set_move(t_best_cost *best, long born[2])
{
	if (born[LE] <= born[RI])
	{
		best->move = rev_rotate;
		best->number_of_move = born[LE];
	}
	else
	{
		best->move = rotate;
		best->number_of_move = born[RI];
	}
}

void	init_best_cost(t_best_cost *best, t_global_data *data, int stack,
		int *ptr)
{
	long	born[2];

	born[0] = 0;
	born[1] = 0;
	get_born(born, data, stack, ptr);
	best->number_of_move = 0;
	best->value = *ptr;
	if (ptr)
		best->address_ptr_value = ptr;
	best->stack = stack;
	best->target_value = 0;
	set_move(best, born);
}

int	free_list(t_list **list)
{
	t_list		*tmp;
	t_best_cost	*content;

	while (*list)
	{
		tmp = (*list)->next;
		content = (*list)->content;
		free(content);
		free(*list);
		*list = tmp;
	}
	*list = NULL;
	return (ERR);
}
