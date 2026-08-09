/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_immediat_sup.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 18:41:49 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/01 19:36:11 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static int	*process_immediat_sup_in_a(t_global_data *data, int *value)
{
	int	*arr;
	int	*ptr_ref;
	int	i;

	i = INT_MAX;
	arr = data->a;
	ptr_ref = &i;
	while (arr <= data->end)
	{
		if (*arr < *ptr_ref && *arr > *value)
			ptr_ref = arr;
		arr++;
	}
	return (ptr_ref);
}

static int	*process_immediat_sup_in_b(t_global_data *data, int *value)
{
	int	*arr;
	int	*ptr_ref;
	int	i;

	i = INT_MAX;
	arr = data->a;
	ptr_ref = &i;
	while (arr <= data->end)
	{
		if (*arr < *ptr_ref && *arr > *value)
			ptr_ref = arr;
		arr++;
	}
	return (ptr_ref);
}

int	*immediat_superior(t_global_data *data, int stack, int *value)
{
	int	*ptr_ref;

	ptr_ref = NULL;
	if (bigest_value(data, stack) == value)
		return (value);
	if (stack == STACK_A && data->a)
		ptr_ref = process_immediat_sup_in_a(data, value);
	else if (stack == STACK_B)
		ptr_ref = process_immediat_sup_in_b(data, value);
	return (ptr_ref);
}
