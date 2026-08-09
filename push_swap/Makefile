NAME=push_swap
NAME_BONUS=checker_bonus/checker
CC=cc 
CFLAGS= -Wall -Wextra -Werror
SRCS= 	srcs/main.c \
		srcs/initialisation/init.c \
		srcs/initialisation/check.c \
		srcs/move/movement.c \
		srcs/move/at_beginning.c \
		srcs/move/get_bigest.c \
		srcs/move/get_immediat_sup.c  \
		srcs/move/get_smalest.c  \
		srcs/utils/utils_1.c \
		srcs/utils/utils_2.c \
		srcs/utils/utils_3.c \
		srcs/utils/display.c \
		srcs/utils/bench.c \
		srcs/algo/two.c \
		srcs/algo/three.c \
		srcs/algo/five.c \
		srcs/algo/sorting_values.c \
		srcs/algo/medium.c \
		srcs/algo/turkish.c \
		srcs/algo/turkish_utils.c

SRCS_BONUS= checker_bonus/checker_bonus.c \
			checker_bonus/move_bonus/movement_bonus.c \
			checker_bonus/move_bonus/utils_bonus.c \
			checker_bonus/initialisation_bonus/init_bonus.c \
			checker_bonus/initialisation_bonus/check_bonus.c \
			checker_bonus/gnl/get_next_line.c \
			checker_bonus/gnl/get_next_line_utils.c

SRCS_OBJS=$(SRCS:.c=.o)
BONUS_OBJS=$(SRCS_BONUS:.c=.o)

all: $(NAME)

$(NAME): $(SRCS_OBJS)
	$(CC) $(CFLAGS) $(SRCS_OBJS) -Llib -lft -o $(NAME)

$(NAME_BONUS): $(BONUS_OBJS)
	$(CC) $(CFLAGS) $(BONUS_OBJS) -Llib -lft -o $(NAME_BONUS)

bonus: $(NAME_BONUS)

clean:
	rm -rf $(SRCS_OBJS) $(BONUS_OBJS)

fclean: clean
	rm -rf $(NAME) $(NAME_BONUS)

re: fclean $(NAME)

.PHONY: all clean fclean re bonus