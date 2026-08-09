/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/19 14:35:55 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/03 11:59:23 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include <unistd.h>
# include "../lib/libft.h"
# include <stdbool.h>

# define LIMIT 1024
# define OK 0
# define ERR -1
# define SPACE 32
# define PLUS 43
# define MINUS 45
# define STACK_A 0
# define STACK_B 1
# define A_AND_B 3
# define NO_MOVE 1
# define DISPLAY 0
# define NO_DISPLAY 1
# define LE 0
# define RI 1
# define RANGE_SIZE 1
# define ARG_CHECK 0
# define ARG_INIT 0

enum			e_algo
{
	NONE,
	SIMPLE,
	MEDIUM,
	COMPLEX,
	ADAPTATIVE,
	BENCH
};

enum			e_move
{
	S,
	P,
	R,
	RV,
	RR,
	RRR
};

enum			e_bench
{
	B_SA,
	B_SB,
	B_PA,
	B_PB,
	B_RA,
	B_RB,
	B_RR,
	B_RRA,
	B_RRB,
	B_RRR
};

typedef struct s_global_data
{
	int		*a;
	int		*b;
	int		*start;
	int		*end;
	int		stack[1024];
	int		strategy;
	int		bench_mode;
	float	disorder;
	int		size_a;
	int		size_b;
	int		move_count[10];
}	t_global_data;

typedef struct s_stack_data
{
	int	*arr;
	int	len;

}	t_stack_data;

typedef struct s_best_move
{
	int	number;
	int	value;
	int	(*move)(t_global_data *, int, int);

}	t_best_move;

typedef struct s_best_cost
{
	int			value;
	int			stack;
	int			number_of_move;
	int			(*move)(t_global_data *, int, int);
	int			target_value;
	int			best_move;
	int			*address_ptr_value;
	int			*address_ptr_target_value;
}				t_best_cost;

typedef struct s_target_result
{
	bool		found;
	int			best_cost;
	int			*ptr_to_value_a;
}				t_target_result;

/* initialisation */
int				check_args(char **argv, t_global_data *data);
int				create_stack(char **argv, t_global_data *data);
int				check_duplicate(t_global_data *data);
int				init_global_data(char **argv, t_global_data *data);

/* movement */

int				push(t_global_data *data, int src, int dst, int mode);
int				swap(t_global_data *data, int stack, int mode);
int				rotate(t_global_data *data, int stack, int mode);
int				rev_rotate(t_global_data *data, int stack, int mode);
int				double_rotation(t_global_data *data, int move, int mode);
int				move(t_global_data *data, int stack,
					int (f)(t_global_data *, int, int), int counter);

/* algo */
int				two_values(t_global_data *data, int stack);
int				three_values(t_global_data *data, int stack);
int				five_values(t_global_data *data, int stack);
int				selection_sort(t_global_data *data);
int				medium_rank(t_global_data *data);
int				turkish(t_global_data *data);

/* utils */
int				check_digit(char *str);
int				check_arg(char *arg);
void			flags_check_managment(t_global_data *data, size_t idx[3],
					char *value, int mode);
void			print_move(int move, int stack);
float			compute_disorder(t_global_data *data);
void			put_float(float nb, int fd);
int				get_complexity(char *arg);
int				ft_is_sort(t_global_data *data, int stack);
int				*smalest_value(t_global_data *data, int stack);
int				*bigest_value(t_global_data *data, int stack);
int				get_stack_data(t_global_data *data, int stack,
					t_stack_data *stk);
int				at_beginning(t_global_data *data, int stack, int *value);
int				*immediat_superior(t_global_data *data, int stack, int *value);
int				get_range_size(int size_list);
int				generate_range(int ranges[LIMIT][2],
					int total_size, int nb_range);
int				check_push_input(t_global_data *data, int src, int dst);
int				get_born(long born[2], t_global_data *data,
					int stack, int *value);
t_best_move		*best_move(t_global_data *data, int range[2]);
t_best_move		*build_best_move(
					int value, int counter, int (f)(t_global_data *, int, int)
					);
void			set_move(t_best_cost *best, long born[2]);
void			init_best_cost(t_best_cost *best, t_global_data *data,
					int stack, int *ptr);
int				get_target_number(t_global_data *data, int stack, t_list **lst);
int				free_list(t_list **list);
int				get_total_cost(t_best_cost *target, t_list *list);

/* bench */
int				benchmark(t_global_data *data);
#endif
