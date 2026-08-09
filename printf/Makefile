NAME=libftprintf.a
CC=cc
AR=ar -rcs
CFLAGS= -Wall -Werror -Wextra

SRCS= ft_printf.c ft_printf_format.c ft_printf_utils.c

OBJS= $(SRCS:.c=.o)


all: $(NAME)

$(NAME):$(OBJS)
	$(AR) $(NAME) $(OBJS)

bonus: $(NAME)

clean:
	rm -f $(OBJS) $(OBJS_B)

fclean: clean
	rm -f $(NAME) $(NAME_BONUS)

re: fclean all

.PHONY: bonus clean fclean re
