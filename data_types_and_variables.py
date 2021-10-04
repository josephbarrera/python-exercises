{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1fee32e0",
   "metadata": {},
   "source": [
    "Data_Types"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "89d4ccc5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "27"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# capture number as variables\n",
    "\n",
    "little_mermaid_rental_days = 3\n",
    "brother_bear_rental_days = 5\n",
    "hercules_rental_days = 1\n",
    "\n",
    "movie_cost_per_day = 3\n",
    "\n",
    "# make calculations using variables\n",
    "total_rental_days = little_mermaid_rental_days + brother_bear_rental_days + hercules_rental_days\n",
    "\n",
    "total_spent = total_rental_days * movie_cost_per_day\n",
    "\n",
    "total_spent"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae818f89",
   "metadata": {},
   "source": [
    "Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook, they pay you a different rate per hour. Google pays 400 dollars per hour, Amazon 380, and Facebook 350. How much will you receive in payment for this week? You worked 10 hours for Facebook, 6 hours for Google and 4 hours for Amazon."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "eb3164b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "7420"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#capture numbers as variables\n",
    "hourly_rate_google = 400\n",
    "hourly_rate_amazon = 380\n",
    "hourly_rate_facebook = 350\n",
    "\n",
    "hours_worked_google = 6\n",
    "hours_worked_amazon = 4\n",
    "hours_worked_facebook = 10\n",
    "\n",
    "total_pay_google = hourly_rate_google * hours_worked_google\n",
    "total_pay_amazon = hourly_rate_amazon * hours_worked_amazon\n",
    "total_pay_facebook = hourly_rate_facebook * hours_worked_facebook\n",
    "\n",
    "total_pay = total_pay_google + total_pay_amazon + total_pay_facebook\n",
    "\n",
    "total_pay"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd51722e",
   "metadata": {},
   "source": [
    "A student can be enrolled to a class only if the class is not full and the class schedule does not conflict with her current schedule."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9c614c09",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# capture booleans as variables\n",
    "class_is_full = False\n",
    "schedule_conflict = False\n",
    "\n",
    "# make calculations using variables\n",
    "student_can_enroll = (not class_is_full) and (not schedule_conflict)\n",
    "\n",
    "student_can_enroll"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "247e3dc7",
   "metadata": {},
   "source": [
    "A product offer can be applied only if people buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "91fedc23",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-9-547aaa7a83e8>, line 10)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-9-547aaa7a83e8>\"\u001b[0;36m, line \u001b[0;32m10\u001b[0m\n\u001b[0;31m    offer_can_be_applied\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "# capture booleans and numbers as variables\n",
    "offer_has_expired = False\n",
    "premium_member =False\n",
    "number_of_items_bought = 3\n",
    "items_needed_for_offer = 2\n",
    "\n",
    "# make calculations using variables\n",
    "offer_can_be_applied = (not offer_has_expired) and (premium_member or (number_of_items > items_needed_for_offer or number_of_items_bought > 2)\n",
    "\n",
    "offer_can_be_applied\n",
    "                                                    \n",
    "                                            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "93fc7a89",
   "metadata": {},
   "outputs": [],
   "source": [
    "username = 'codeup'\n",
    "password = 'notastrongpassword'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b42a1e47",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "five_or_more_char = len(password) >= 5\n",
    "five_or_more_char"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c74d8a83",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "twenty_or_less_char = len(password) <= 20\n",
    "twenty_or_less_char"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6c07cde1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "not_the_same = password != username\n",
    "not_the_same"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "24275378",
   "metadata": {},
   "outputs": [],
   "source": [
    "#check for leading and trailing white space in each word\n",
    "leading_white_space_password = password[0] in ' '\n",
    "trailing_white_space_password = password[-1] in ' '\n",
    "\n",
    "leading_white_space_username = username[0] in ' '\n",
    "trailing_white_space_username = username[-1] in ' '\n",
    "\n",
    "#combines checks for each word\n",
    "leading_white_space_password = \n",
    "trailing_white_space_username = \n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
