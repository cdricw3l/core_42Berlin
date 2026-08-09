/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/09 21:02:58 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 01:17:09 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line.h"

static int	init_gnl(t_gnl *gnl, int fd)
{
	if (fd < 0 || fd > MAX_FD)
		return (ERR);
	gnl->b_read = -2;
	gnl->buffer = malloc(BUFFER_SIZE);
	if (!gnl->buffer)
		return (ERR);
	gnl->line = NULL;
	gnl->fd = fd;
	gnl->idx[0] = 0;
	gnl->idx[1] = 0;
	return (OK);
}

static int	clean_data(char **stash, t_gnl *gnl, int level, int code_return)
{
	if (level == STASH || level == BUFFER_STASH || level == ALL)
	{
		free(*stash);
		*stash = NULL;
	}
	if (level == LINE || level == BUFFER_LINE || level == ALL)
	{
		free(gnl->line);
		gnl->line = NULL;
	}
	if (level == BUFFER || level == BUFFER_LINE
		|| level == BUFFER_STASH || level == ALL)
	{
		free(gnl->buffer);
		gnl->buffer = NULL;
	}
	return (code_return);
}

static int	process_stash(char *stash[MAX_FD], t_gnl *gnl, int idx_nl)
{
	char	*new_stsh;

	if (idx_nl == -1)
	{
		gnl->line = strdup_gnl(stash[gnl->fd], ft_strlen_gnl(stash[gnl->fd]));
		if (!(gnl->line))
			return (clean_data(&stash[gnl->fd], gnl, BUFFER_STASH, ERR));
		else
			return (clean_data(&stash[gnl->fd], gnl, STASH, READ));
	}
	gnl->line = substr_gnl(stash[gnl->fd], 0, idx_nl + 1);
	if (!(gnl->line))
		return (clean_data(&stash[gnl->fd], gnl, BUFFER_STASH, ERR));
	if (!(stash[gnl->fd])[idx_nl + 1])
		return (clean_data(&stash[gnl->fd], gnl, BUFFER_STASH, NOREAD));
	new_stsh = substr_gnl(stash[gnl->fd], idx_nl + 1,
			ft_strlen_gnl(&(stash[gnl->fd])[idx_nl + 1]));
	if (!new_stsh)
		return (clean_data(&stash[gnl->fd], gnl, ALL, ERR));
	free(stash[gnl->fd]);
	stash[gnl->fd] = new_stsh;
	return (clean_data(&stash[gnl->fd], gnl, BUFFER, NOREAD));
}

static int	process_buffer(char **stash, t_gnl *gnl)
{
	int		nl_idx;
	int		r;
	char	*new_stash;

	if (gnl->b_read == 0)
		return (clean_data(stash, gnl, BUFFER, NOREAD));
	nl_idx = idxof(gnl->buffer, NL, gnl->b_read);
	if (nl_idx < 0)
	{
		r = ft_strjoin_gnl(gnl, gnl->buffer, gnl->b_read);
		if (r != OK)
			return (clean_data(stash, gnl, BUFFER_LINE, ERR));
		return (READ);
	}
	r = ft_strjoin_gnl(gnl, gnl->buffer, nl_idx + 1);
	if (r != OK)
		return (clean_data(stash, gnl, ALL, ERR));
	if (nl_idx + 1 == gnl->b_read)
		return (clean_data(stash, gnl, BUFFER_STASH, NOREAD));
	new_stash = substr_gnl(gnl->buffer, nl_idx + 1, gnl->b_read - (nl_idx + 1));
	if (!new_stash)
		return (clean_data(stash, gnl, ALL, ERR));
	free(*stash);
	*stash = new_stash;
	return (clean_data(stash, gnl, BUFFER, NOREAD));
}

char	*get_next_line(int fd, int mode)
{
	t_gnl		gnl;
	static char	*stash[MAX_FD];

	if (mode == CLEAN_MODE)
	{
		free(stash[fd]);
		return (NULL);
	}
	if (init_gnl(&gnl, fd) == ERR)
		return (NULL);
	if (stash[gnl.fd] && process_stash(stash, &gnl,
			idxof(stash[gnl.fd], NL, ft_strlen_gnl(stash[gnl.fd]))) != READ)
		return (gnl.line);
	while (gnl.b_read != 0)
	{
		gnl.b_read = read(gnl.fd, gnl.buffer, BUFFER_SIZE);
		if (gnl.b_read < 0)
		{
			clean_data(&stash[gnl.fd], &gnl, ALL, ERR);
			return (NULL);
		}
		if (process_buffer(&(stash[gnl.fd]), &gnl) != READ)
			return (gnl.line);
	}
	return (NULL);
}
