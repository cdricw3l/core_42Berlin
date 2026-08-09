/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   display.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/23 13:39:03 by cebouhad          #+#    #+#             */
/*   Updated: 2026/06/02 18:59:45 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "../../include/push_swap.h"

static int	float_precision_ajustement(int n)
{
	if (n % 10 > 5)
		while (n % 10 != 0)
			n++;
	return (n);
}

void	put_float(float nb, int fd)
{
	int		ipart;
	int		f_adjusted;
	float	fpart;

	ipart = (int)nb * 100;
	if (ipart == 100)
	{
		ft_putnbr_fd(ipart, fd);
		return ;
	}
	fpart = (nb - (float)ipart) * 10;
	if (ipart == 0 && fpart == 0)
	{
		ft_putnbr_fd(0, fd);
		return ;
	}
	f_adjusted = float_precision_ajustement((int)(fpart * 10000)) / 10;
	ft_putnbr_fd((f_adjusted / 1000) % 10, fd);
	ft_putnbr_fd((f_adjusted / 100) % 10, fd);
	write(fd, ".", 1);
	ft_putnbr_fd((f_adjusted / 10) % 10, fd);
	ft_putnbr_fd((f_adjusted) % 10, fd);
}

/* display the move in STDOUT */
void	print_move(int move, int stack)
{
	if (move == S && stack == STACK_A)
		write(STDOUT_FILENO, "sa\n", 3);
	if (move == S && stack == STACK_B)
		write(STDOUT_FILENO, "sb\n", 3);
	if (move == P && stack == STACK_A)
		write(STDOUT_FILENO, "pa\n", 3);
	if (move == P && stack == STACK_B)
		write(STDOUT_FILENO, "pb\n", 3);
	if (move == R && stack == STACK_A)
		write(STDOUT_FILENO, "ra\n", 3);
	if (move == R && stack == STACK_B)
		write(STDOUT_FILENO, "rb\n", 3);
	if (move == RV && stack == STACK_A)
		write(STDOUT_FILENO, "rra\n", 4);
	if (move == RV && stack == STACK_B)
		write(STDOUT_FILENO, "rrb\n", 4);
	if (move == RR && stack == A_AND_B)
		write(STDOUT_FILENO, "rr\n", 3);
	if (move == RRR && stack == A_AND_B)
		write(STDOUT_FILENO, "rrr\n", 4);
}
/*
	putfloat:

	get int value part */
	//ipart = (int)nb;
	/* get float part */
	//fpart = nb - (float)ipart;
	/* check if third number is greater than 5. Exemple: 0.586 -> 0.59 */
	//f_adjusted = float_precision_ajustement((int)(fpart * 1000)) / 10;
	/* write integer part */
	//ft_putnbr_fd(ipart, STDOUT_FILENO);
	/* write '.' */
	//write(STDOUT_FILENO, ".", 1);
	/* write float part */
	/*ft_putnbr_fd(f_adjusted, STDOUT_FILENO);

*/