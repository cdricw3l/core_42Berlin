/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_utils.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/14 10:39:45 by cebouhad          #+#    #+#             */
/*   Updated: 2026/05/18 19:58:08 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "include/ft_printf.h"

int	ft_strncmp(const char *p1, const char *p2, size_t n)
{
	size_t			i;
	unsigned char	*s1;
	unsigned char	*s2;

	s1 = (unsigned char *)p1;
	s2 = (unsigned char *)p2;
	i = 0;
	if (n == 0)
		return (0);
	while ((s1[i] || s2[i]) && i < n)
	{
		if (s1[i] < s2[i])
			return (-1);
		if (s1[i] > s2[i])
			return (1);
		i++;
	}
	return (0);
}

void	ft_putchar_pf(int fd, char c, int *r)
{
	*r += write(fd, &c, 1);
}

void	ft_putstr_pf(int fd, char *str, int *r)
{
	char	*ptr;

	ptr = str;
	if (!ptr)
	{
		*r += write(STDOUT_FILENO, "(null)", 6);
		return ;
	}
	while (ptr && *ptr)
	{
		ft_putchar_pf(fd, *ptr, r);
		ptr++;
	}
}

void	ft_putnbr_pf(long n, int *r, char *base, size_t base_len)
{
	char			c;
	long			nb;

	nb = n;
	if (nb < 0 && !ft_strncmp(base, DBASE, base_len))
	{
		write(STDOUT_FILENO, "-", 1);
		nb = nb * -1;
		(*r)++;
	}
	if (nb >= (long)base_len)
		ft_putnbr_pf(nb / base_len, r, base, base_len);
	c = base[(nb % base_len)];
	ft_putchar_pf(STDOUT_FILENO, c, r);
}

void	ft_putptr_pf(unsigned long n, int *r, char *base, size_t base_len)
{
	char			c;
	unsigned long	nb;

	nb = n;
	if (nb >= (unsigned long)base_len)
		ft_putptr_pf(nb / base_len, r, base, base_len);
	c = base[(nb % base_len)];
	ft_putchar_pf(STDOUT_FILENO, c, r);
}
