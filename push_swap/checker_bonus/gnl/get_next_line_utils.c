/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/09 21:02:58 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 00:58:32 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

char	*strdup_gnl(char *s, int len)
{
	int		i;
	char	*new_str;

	i = 0;
	new_str = malloc(sizeof(char) * (len + 1));
	if (!new_str)
		return (NULL);
	while (i < len)
	{
		new_str[i] = s[i];
		i++;
	}
	new_str[i] = '\0';
	return (new_str);
}

char	*substr_gnl(char const *s, unsigned int start, size_t len)
{
	size_t	bytes_cpy;
	char	*new_str;

	if (!s)
		return (NULL);
	new_str = malloc(sizeof(char) * (len + 1));
	if (!new_str)
		return (NULL);
	bytes_cpy = 0;
	while (bytes_cpy < len)
		new_str[bytes_cpy++] = s[start++];
	new_str[bytes_cpy] = '\0';
	return (new_str);
}

int	idxof(char *str, char c, int size)
{
	int	idx;

	idx = 0;
	while (idx < size)
	{
		if (str[idx] == c)
			return (idx);
		idx++;
	}
	return (-1);
}

size_t	ft_strlen_gnl(char *str)
{
	int	i;

	i = 0;
	if (!str)
		return (0);
	while (str[i])
		i++;
	return (i);
}

int	ft_strjoin_gnl(t_gnl *gnl, char *buffer, int len)
{
	char	*str;

	if (!gnl->line)
	{
		gnl->line = strdup_gnl(buffer, len);
		if (!gnl->line)
			return (ERR);
		return (OK);
	}
	str = malloc(ft_strlen_gnl(gnl->line) + len + 1);
	if (!str)
		return (ERR);
	(gnl->idx)[0] = 0;
	while ((gnl->line)[(gnl->idx)[0]])
	{
		str[(gnl->idx)[0]] = (gnl->line)[(gnl->idx)[0]];
		(gnl->idx)[0]++;
	}
	(gnl->idx)[1] = 0;
	while ((gnl->idx)[1] < len)
		str[(gnl->idx)[0]++] = buffer[(gnl->idx)[1]++];
	str[(gnl->idx)[0]] = '\0';
	free(gnl->line);
	gnl->line = str;
	return (OK);
}
