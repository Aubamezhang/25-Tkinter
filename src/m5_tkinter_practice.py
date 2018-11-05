"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Jake Zhang.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # DONE: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    window = tkinter.Tk()

    # ------------------------------------------------------------------
    # DONE: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1 = ttk.Frame(window, padding=10)
    frame1.grid()

    # ------------------------------------------------------------------
    # DONE: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------
    go_forward_button = ttk.Button(frame1, text='Forward')

    # ------------------------------------------------------------------
    # DONE: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    go_forward_button['command'] = (lambda:
                                    Hello())
    go_forward_button.grid()

    # ------------------------------------------------------------------
    # DONE: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    my_entry_box = ttk.Entry(frame1)
    my_entry_box.grid()

    go_forward_button['command'] = (lambda:
                                    entry_box(my_entry_box))

    other_button = ttk.Button(frame1, text='Hello/Goodbye Button')
    other_button.grid()

    other_button['command'] = (lambda:
                               check_entry_box(my_entry_box))

    # ------------------------------------------------------------------
    # DONE: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    button3 = ttk.Button(frame1, text='Repeater')
    button3.grid()

    my_entry_box2 = ttk.Entry(frame1)
    my_entry_box2.grid()

    button3['command'] = (lambda:
                          loop_entry_box(my_entry_box2, my_entry_box))
    # ------------------------------------------------------------------
    # DONE: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------
    window.mainloop()

def Hello():
    print('Hello!')

def Good_bye():
    print('Good Bye!')

def entry_box(entry_box):
    contents_of_entry_box = entry_box.get()
    print(contents_of_entry_box)

def check_entry_box(entry_box):
    contents_of_entry_box = entry_box.get()
    if contents_of_entry_box == 'ok':
        Hello()
    else:
        Good_bye()

def loop_entry_box(n, entry_box):
    contents_of_n = n.get()
    contents_of_entry_box = entry_box.get()
    n = int(contents_of_n)
    for k in range(n):
        print(contents_of_entry_box)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
