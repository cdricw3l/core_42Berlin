/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/11 11:38:03 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 01:18:09 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 1
# endif

# include <stdlib.h>
# include <fcntl.h>
# include <unistd.h>

# define MAX_FD 		1024
# define NL				10
# define STANDARD_MODE	0
# define CLEAN_MODE 		1

typedef struct s_gnl
{
	int		fd;
	int		idx[2];
	char	*line;
	char	*buffer;
	int		b_read;
}	t_gnl;

enum e_clean_level
{
	STASH,
	LINE,
	BUFFER,
	LINE_STASH,
	BUFFER_LINE,
	BUFFER_STASH,
	ALL
};

enum e_status
{
	ERR,
	OK,
	READ,
	NOREAD
};

char	*get_next_line(int fd, int mode);
size_t	ft_strlen_gnl(char *str);
int		idxof(char *str, char c, int size);
int		ft_strjoin_gnl(t_gnl *gnl, char *buffer, int len);
char	*strdup_gnl(char *s, int len);
char	*substr_gnl(char const *s, unsigned int start, size_t len);

#endif