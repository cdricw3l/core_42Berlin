/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 15:21:52 by cebouhad          #+#    #+#             */
/*   Updated: 2026/05/18 19:53:14 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "include/ft_printf.h"

static int	is_valide_type(int flag, char c)
{
	if (flag == DASH && (c == 'x' || c == 'X'))
		return (1);
	if (flag == SPACE && (c == 'd' || c == 'i' || c == 's'))
		return (1);
	if (flag == PLUS && (c == 'd' || c == 'i'))
		return (1);
	return (0);
}

static int	get_flag(const char *str)
{
	int	f;

	f = 0;
	if (*str == DASH)
		f = DASH;
	else if (*str == SPACE)
		f = SPACE;
	else if (*str == PLUS)
		f = PLUS;
	else
		return (NOFLAGS);
	while (*str && *str == f)
		str++;
	if (*str && is_valide_type(f, *str))
		return (f);
	return (0);
}

void	manage_flag(int flag, int arg, char c, int *r)
{
	if (flag == SPACE && arg >= 0)
		*r += write(STDOUT_FILENO, " ", 1);
	else if (flag == PLUS && arg >= 0)
		*r += write(STDOUT_FILENO, "+", 1);
	else if (flag == DASH && c == 'x' && arg != 0)
		*r += write(STDOUT_FILENO, "0x", 2);
	else if (flag == DASH && c == 'X' && arg != 0)
		*r += write(STDOUT_FILENO, "0X", 2);
}

static int	dispatch_printf(va_list *ap, const char **format)
{
	int	r;
	int	flag;

	flag = get_flag(*format);
	if (flag)
		while (*(*format) == flag)
			(*format)++;
	r = 0;
	if (*(*format) == 'c')
		ft_putchar_pf(STDOUT_FILENO, va_arg(*ap, int), &r);
	else if (*(*format) == 's')
		ft_putstr_pf(STDOUT_FILENO, va_arg(*ap, char *), &r);
	else if (*(*format) == 'd' || *(*format) == 'i')
		print_d_and_i(ap, *(*format), flag, &r);
	else if (*(*format) == 'x' || *(*format) == 'X')
		print_x(ap, *(*format), flag, &r);
	else if (*(*format) == 'p')
		print_p(ap, &r, H_LOW_BASE);
	else if (*(*format) == 'u')
		ft_putnbr_pf(va_arg(*ap, unsigned int), &r, DBASE, ft_strlen(DBASE));
	else if (*(*format) == '%')
		ft_putchar_pf(STDOUT_FILENO, PERCENT, &r);
	return (r);
}

int	ft_printf(const char *format, ...)
{
	va_list	ap;
	int		i;

	i = 0;
	va_start(ap, format);
	while (*format)
	{
		if (*format == PERCENT)
		{
			format++;
			i += dispatch_printf(&ap, &format);
		}
		else
			i += write(STDOUT_FILENO, &(*format), 1);
		format++;
	}
	va_end(ap);
	return (i);
}
