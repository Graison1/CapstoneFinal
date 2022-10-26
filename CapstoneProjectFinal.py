from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import random
while True:
  choice_1 = st.text_input("Would you like to guess a number generated by the computer?: Yes to guess against the computer or No to make the computer guess your number: ")
  if choice_1 == 'No':
    smaller = int(st.number_input("Enter the smaller number and then press 's': ", key = 's'))
    larger = int(st.number_input("Enter the larger number and then press 'l': ", key = 'l'))
    count = 0
    st.write()
    while True:
      count += 1
      myNumber = (smaller + larger) // 2
      st.write('%d %d' % (smaller, larger))
      st.write('Your number is %d' % myNumber)
      choice_2 = st.writeinput('Enter =, <, or >: ')
      if choice_2 == '=':
        st.write("Hooray, I've got it in %d tries" % count)
        break
      elif choice_2 == '<':
        larger = myNumber - 1
      elif choice_2 == '>':
        smaller = myNumber + 1
      if smaller > larger:
        st.write("I'm out of guesses, and you cheated")
        break
  elif choice_1 == 'Yes':
    smaller = int(st.number_input("Enter the smaller number: "))
    larger = int(st.number_input("Enter the larger number: "))
    myNumber = random.randint(smaller, larger)
    count = 0
    while True:
      count += 1
      userNumber = int(st.number_input("Enter your guess: "))
      if userNumber < myNumber:
        st.write("Too small")
      elif userNumber > myNumber:
        st.write("Too large")
      else:
        st.write("You've got it in", count, "tries!")
        break
  else:
    st.write("Please choose Yes or No")
    continue
  choice_3 = st.text_input("Would you like to play again? Yes or No: ", key = 'r')
  if choice_3 == 'Yes':  #go back to the top
    continue
  elif choice_3 == 'No':
    st.write("Thank you for playing!")
    break
  else:
    st.write("Please choose Yes or No")
  choice_3 = st.text_input("Would you like to play again? Yes or No: ", key = 'e')
  if choice_3 == 'Yes':  #go back to the top
    continue
  elif choice_3 == 'No':
    st.write("Thank you for playing!")
  else:
    st.write("Please choose Yes or No")
  continue
  break
