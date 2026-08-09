/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   checker.h                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/06/01 22:35:38 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 11:59:16 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef CHECKER_H
# define CHECKER_H

# include <limits.h>
# include <unistd.h>
# include "../lib/libft.h"
# include "gnl/get_next_line.h"

# define OK 0
# define ERR -1
# define PLUS 43
# define MINUS 45
# define SPACE 32
# define STACK_A 0
# define STACK_B 1
# define DISPLAY 0
# define NO_DISPLAY 1
# define NO_MOVE 1

typedef struct s_stack_data
{
	int	*arr;
	int	len;

}	t_stack_data;

enum e_move
{
	RR,
	RRR
};

enum e_algo
{
	NONE,
	SIMPLE,
	MEDIUM,
	COMPLEX,
	ADAPTATIVE
};

typedef struct s_global_data
{
	int		*a;
	int		*b;
	int		*start;
	int		*end;
	int		stack[1024];
	int		algo;
	int		size_a;
	int		size_b;

}	t_global_data;

/* initialisation */
int			check_args(char **argv);
int			create_stack(char **argv, t_global_data *data);
int			check_duplicate(t_global_data *data);
int			init_global_data(char **argv, t_global_data *data);

/* movement */
int			push(t_global_data *data, int src, int dst);
int			swap(t_global_data *data, int stack);
int			rotate(t_global_data *data, int stack);
int			rev_rotate(t_global_data *data, int stack);
int			double_rotation(t_global_data *data, int move);
int			check_push_input(t_global_data *data, int src, int dst);

#endif