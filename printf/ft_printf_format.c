/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_format.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/15 16:15:01 by cebouhad          #+#    #+#             */
/*   Updated: 2026/05/18 19:52:21 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "include/ft_printf.h"

size_t	ft_strlen(const char *s)
{
	size_t	i;

	i = 0;
	while (s[i])
		i++;
	return (i);
}

static char	*get_base(char c)
{
	if (c == 'x')
		return (H_LOW_BASE);
	else if (c == 'X')
		return (H_UP_BASE);
	else
		return (DBASE);
	return (0);
}

void	print_d_and_i(va_list *ap, char format, int flag, int *r)
{
	int	v;

	v = va_arg(*ap, int);
	manage_flag(flag, v, format, r);
	ft_putnbr_pf(v, r, DBASE, ft_strlen(DBASE));
}

void	print_x(va_list *ap, char format, int flag, int *r)
{
	char			*base;
	unsigned int	v;

	base = get_base(format);
	v = va_arg(*ap, unsigned int);
	manage_flag(flag, v, format, r);
	ft_putnbr_pf(v, r, base, ft_strlen(base));
}

void	print_p(va_list *ap, int *r, char *base)
{
	long	ptr;

	ptr = va_arg(*ap, long);
	if (ptr)
	{
		*r += write(STDOUT_FILENO, "0x", 2);
		ft_putptr_pf(ptr, r, base, ft_strlen(H_LOW_BASE));
	}
	else
		*r += write(STDOUT_FILENO, "(nil)", 5);
}
