/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_smalest.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 18:40:29 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 09:57:04 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static int	*process_smalest_in_a(t_global_data *data)
{
	int	*arr;
	int	*ptr_ref;

	arr = data->a;
	ptr_ref = data->a;
	while (arr <= data->end)
	{
		if (*arr < *ptr_ref)
			ptr_ref = arr;
		arr++;
	}
	return (ptr_ref);
}

static int	*process_smalest_in_b(t_global_data *data)
{
	int	*arr;
	int	*ptr_ref;
	int	i;

	i = *(data->b);
	arr = data->b;
	ptr_ref = &i;
	while (arr >= data->start)
	{
		if (*arr < *ptr_ref)
			ptr_ref = arr;
		arr--;
	}
	return (ptr_ref);
}

int	*smalest_value(t_global_data *data, int stack)
{
	int	*ptr_ref;

	ptr_ref = NULL;
	if (stack == STACK_A && data->a)
		ptr_ref = process_smalest_in_a(data);
	else if (stack == STACK_B && data->b)
		ptr_ref = process_smalest_in_b(data);
	return (ptr_ref);
}
//int	i;
//i = *(data->a);