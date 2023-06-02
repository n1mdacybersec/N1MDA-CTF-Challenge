#include <stdio.h>
#include <windows.h>

void obfuscateFlag(char *flag)
{
  for (int i = 0; flag[i] != '\0'; i++)
  {
    flag[i] ^= 0x20;
  }
}

BOOL antiDebuggingCheck()
{
  return IsDebuggerPresent();
}

int main()
{
  int x = 5;
  int y = 10;
  int result = x + y;
  char flag[] = {'n' ^ 0x20, '1' ^ 0x20, 'm' ^ 0x20, 'd' ^ 0x20, 'a' ^ 0x20, 'C' ^ 0x20, 'T' ^ 0x20, 'F' ^ 0x20, '{' ^ 0x20, '0' ^ 0x20, 'b' ^ 0x20, 'f' ^ 0x20, 'u' ^ 0x20, '5' ^ 0x20, 'c' ^ 0x20, '4' ^ 0x20, '7' ^ 0x20, '1' ^ 0x20, '0' ^ 0x20, 'n' ^ 0x20, '_' ^ 0x20, 'i' ^ 0x20, 'S' ^ 0x20, '_' ^ 0x20, 'm' ^ 0x20, 'y' ^ 0x20, '_' ^ 0x20, 'F' ^ 0x20, '4' ^ 0x20, 'v' ^ 0x20, '0' ^ 0x20, 'u' ^ 0x20, '1' ^ 0x20, '2' ^ 0x20, '!' ^ 0x20, 't' ^ 0x20, '3' ^ 0x20, '}' ^ 0x20, '\0'};

  if (antiDebuggingCheck())
  {
    printf("Debugger detected! Exiting...\n");
    return -1;
  }

  obfuscateFlag(flag);

  printf("The result is: %d\n", result);
  printf("Flag: %s\n", flag);
  return 0;
}