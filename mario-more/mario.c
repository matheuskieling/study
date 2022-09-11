//So... this was probably overengineered as f. I apologize for it, couldn't think a better solution by now.
//I'm sure there is a very simple way to solve this, but atm I put I all got in this project.
//Hope it is not THAT bad!
//Hugs from Brazil!


#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
    printf("\n\n");


    //get input from user and store it in an int variable

    h = get_int("Height: ");
    }


    //reject anything that isn't an int between 1 and 8

    while (h < 1 || h > 8);
    printf("\n");
    //formula for difining first number of spaces and blocks
    int line_num_spaces = (h-1);
    int line_num_blocks = (h-(h-1));


    //for each bigger loop, start a variable named i with the value of 0, then compare it to height(h)
    //at the end of each bigger cycle, increment i by 1

    for (int i = 0; i < h; i++)
    {


        //tiny loop to print the spaces
        //just like in bigger loops, but smaller

        for (int space = 0 ; space < line_num_spaces; space++)
        {
            printf(" ");
        }


        //same for blocks

        for (int block = 0; block < line_num_blocks; block++)
        {
            printf("#");
        }


        //print two empty spaces irrespective of the value of h

        printf("  ");


        //blocks again

        for (int block =0; block < line_num_blocks; block++)
        {
            printf("#");
        }

        //break line

        printf("\n");


        //reduce number of dots in the role by 1 and increment number of bocks by 1

        line_num_spaces--;
        line_num_blocks++;

        //aaaand return to line 35


    }

}