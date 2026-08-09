/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   binary_tree.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/07/29 09:12:03 by cebouhad          #+#    #+#             */
/*   Updated: 2026/08/05 03:18:44 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/codexion.h"

/* get_tree_size - 1  is the size of the binary tree */
int	count_tree_node(t_request *root, int size)
{
	if (!root)
		return (1);
	return (count_tree_node(root->left, size + 1)
		+ count_tree_node(root->right, size + 1));
}

int	tree_height(t_request *root)
{
	int	left_h;
	int	right_h;

	if (!root)
		return (0);
	left_h = tree_height(root->left);
	right_h = tree_height(root->right);
	return (max(left_h, right_h) + 1);
}
