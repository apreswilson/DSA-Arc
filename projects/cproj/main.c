#include <stdio.h>
#include "globals.h"

int main()
{
   printf("Hello, what's your name? \n");
   char nameOfPerson[100] = "";
   scanf("%s", nameOfPerson);
   printf("Welcome %s to your CLI todo list.\n", nameOfPerson);

   char addTask = 'y';
   char *array[] = {"This is your first task"};
   while (addTask != 'n')
   {
      printf("Do you want to add a task (y / n)?\n");
      scanf(" %c", &addTask);
      if (addTask == 'y')
      {
         char newTask[100];
         printf("What is the name of the task you want to add?\n");
         scanf("%s", newTask);
         myFunction(newTask);
      }
   }
   return 0;
}