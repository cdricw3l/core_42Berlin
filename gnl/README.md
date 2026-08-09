*This project has been created as part of the 42 curriculum by cebouhad*

# 🔎 Description

The ft_printf project consists of creating a static library that reproduces the behavior of the printf function.
The conversion specifiers to handle are: cspdiuxX%.

In this project, we do not have to implement buffer management like in the original function.

The function is a variadic function, which means it accepts a variable number of arguments and returns an integer corresponding to the number of printed characters.

# 📋 Instructions

The library is created using the ar program and automated with a Makefile.

To create the library without flag management (mandatory part):

```
make
```

To create the library with flag management (bonus part):

```
make bonus
```

To remove object files:

```
make clean
```

To remove the static library and object files:

```
make fclean
```

To remove the static library and object files and rebuild the library (mandatory part only):

```
make re
```

## 📖 Resources:

* man ar
* man printf
* man stdarg
* 42born2code.slack.com
* https://en.wikipedia.org/wiki/Uncontrolled_format_string
* https://en.wikipedia.org/wiki/Printf
* https://learn.microsoft.com/fr-fr/cpp/c-runtime-library/format-specification-syntax-printf-and-wprintf-functions?view=msvc-170
* https://learn.microsoft.com/fr-fr/cpp/c-runtime-library/reference/va-arg-va-copy-va-end-va-start?view=msvc-170
* https://abdelhalimelbouaami.medium.com/unlocking-the-mystery-of-va-list-understanding-variable-arguments-in-c-a7b2323cf6d3
* https://www.geeksforgeeks.org/c/difference-d-format-specifier-c-language/
* gpt for README help translation


# 🛠️ Detailed Description

## Mandatory Part

Each character of the string passed as an argument is read.
When the % character is detected, the pointer to the character is incremented by 1, and the string is sent to a dispatching function responsible for analyzing the conversion specifier.

A va_list variable is initialized through the va_start macro (which initializes the list so that it points on the stack to the first variable argument of the function).

Each call to the va_arg() macro retrieves the next argument from the list while incrementing the internal pointer of the va_list.

va_arg() takes the list and the type of the argument to retrieve as parameters.

Finally, after the list has been used, the va_end macro is called to reset the va_list pointer to NULL.

Dispatch Specifiers:
```c
c --> ft_putchar_pf(STDOUT_FILENO, va_arg(*ap, int), &r);
```
```c
s --> ft_putstr_pf(STDOUT_FILENO, va_arg(*ap, char *), &r);
```
```c
d --> ft_putnbr_pf(va_arg(*ap, int), &r, DBASE, ft_strlen(DBASE));
```
```c
i --> ft_putnbr_pf(va_arg(*ap, int), &r, DBASE, ft_strlen(DBASE));
```
```c
p --> ft_putptr_pf(ptr, r, base, ft_strlen(H_LOW_BASE));
```
```c
u --> ft_putnbr_pf(va_arg(*ap, unsigned int), &r, base, ft_strlen(base));
```
```c
X --> ft_putnbr_pf(va_arg(*ap, unsigned int), &r, base, ft_strlen(base));
```
```c
x --> ft_putnbr_pf(va_arg(*ap, unsigned int), &r, base, ft_strlen(base));
```
```c
% --> ft_putchar_pf(STDOUT_FILENO, PERCENT, &r);
```

Here, r is a pointer to an integer used to increment the counter of printed characters.

## Bonus Part

The concept of the bonus part is the same as the mandatory part, except that flag characters (+ #) are also handled.

The subject states:

“You don’t have to do all the bonuses.”

Therefore, I focused only on implementing the + , space and # flags.

These are the functions responsible for flag management:

```c
int     get_flag(const char *str);
void    manage_flag(int flag, int arg, char c, int *r);
```

Finally, in the prototype declaration of ft_printf inside the header file, the following attribute is defined:

```c
__attribute__ ((format (__printf__, 1, 2)))
```

The format attribute specifies that a function takes printf style arguments that should be type-checked against a format string.

Reference: https://gcc.gnu.org/onlinedocs/gcc/Common-Attributes.html, 