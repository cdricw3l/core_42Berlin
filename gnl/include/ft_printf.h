/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: cebouhad <cebouhad@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/05/13 15:22:08 by cebouhad          #+#    #+#             */
/*   Updated: 2026/05/18 19:52:44 by cebouhad         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdarg.h>

# define SPACE   32
# define PLUS    43
# define DASH    35
# define PERCENT 37
# define NOFLAGS  0
# define DBASE "0123456789"
# define H_UP_BASE "0123456789ABCDEF"
# define H_LOW_BASE "0123456789abcdef"

int		ft_printf(const char *format, ...)
		__attribute__ ((format (__printf__, 1, 2)));
void	ft_putchar_pf(int fd, char c, int *r);
void	ft_putstr_pf(int fd, char *str, int *r);
void	ft_putnbr_pf(long n, int *r, char *base, size_t base_len);
void	ft_putptr_pf(unsigned long n, int *r, char *base, size_t base_len);
void	print_d_and_i(va_list *ap, char format, int flag, int *r);
void	print_x(va_list *ap, char format, int flag, int *r);
void	print_p(va_list *ap, int *r, char *base);
void	manage_flag(int flag, int arg, char c, int *r);
size_t	ft_strlen(const char *s);
int		ft_strncmp(const char *p1, const char *p2, size_t n);

#endif