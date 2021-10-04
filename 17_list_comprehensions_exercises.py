{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "976ce17d",
   "metadata": {},
   "source": [
    "# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f25e8402",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']\n",
    "\n",
    "numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9ae50e28",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'fruit' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-b23ac29f9c3d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0muppercased_\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mfruit\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mupper\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m: name 'fruit' is not defined"
     ]
    }
   ],
   "source": [
    "uppercased_ = [fruit.upper]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "75b285af",
   "metadata": {},
   "source": [
    "# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bf24d702",
   "metadata": {},
   "outputs": [],
   "source": [
    "capitalized_fruits = [fruits]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "767c08ab",
   "metadata": {},
   "source": [
    "# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3b92ea97",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "object of type 'generator' has no len()",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-8-11c1d1a2e3d3>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mfruits_with_more_than_two_vowels\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mfruit\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mfruit\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfruits\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mletter\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mletter\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfruit\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mletter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m'aeiou'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mfruits_with_more_than_two_vowels\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m<ipython-input-8-11c1d1a2e3d3>\u001b[0m in \u001b[0;36m<listcomp>\u001b[0;34m(.0)\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mfruits_with_more_than_two_vowels\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mfruit\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mfruit\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfruits\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mletter\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0mletter\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mfruit\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0mletter\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32min\u001b[0m \u001b[0;34m'aeiou'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0mfruits_with_more_than_two_vowels\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTypeError\u001b[0m: object of type 'generator' has no len()"
     ]
    }
   ],
   "source": [
    "fruits_with_more_than_two_vowels = [fruit for fruit in fruits if len(letter for letter in fruit if letter.lower() in 'aeiou')]\n",
    "\n",
    "fruits_with_more_than_two_vowels\n",
    "                            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b9829507",
   "metadata": {},
   "outputs": [],
   "source": [
    "def has_two_vowels(fruit):\n",
    "    ' ' ' "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2d7eb7de",
   "metadata": {},
   "source": [
    "# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30e1f5d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits_with_only_two_vowels =\n",
    "fruits_with_only_two_vowels"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25f858c0",
   "metadata": {},
   "source": [
    "# Exercise 5 - make a list that contains each fruit with more than 5 characters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "cca91873",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['strawberry', 'pineapple', 'mandarin orange']"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[fruit for fruit in fruits if len(fruit) > 5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e960b42c",
   "metadata": {},
   "source": [
    "# Exercise 6 - make a list that contains each fruit with exactly 5 characters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "16545bee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['mango', 'guava']"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[fruit for fruit in fruits if len(fruit) == 5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "784bac1e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "71df9b22",
   "metadata": {},
   "outputs": [],
   "source": [
    "[fruit for fruit in fruits if len(fruit) > 5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1bdc1980",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "4a29e2f5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[5, 4, 10, 5, 9, 15]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[len(fruit) for fruit in fruits]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "17490001",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c263bfa3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def contains_a(fruit):\n",
    "    ' ' ' Returns true or False if the input fruit string contains an a character\n",
    "    \n",
    "    return len([letter for letter in fruit if letter == 'a']) > 0\n",
    "\n",
    "fruits_with_letter_a = [fruit for fuit in fruits if contains_a ? ]\n",
    "fruits_with_letter_a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "893bfdae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4700d8a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "even_numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a958dbc4",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e9ddf43",
   "metadata": {},
   "outputs": [],
   "source": [
    "odd_numbers = [number for number in numbers if number % 2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3b8a6aa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0400ddf3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, 5]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "positive_numbers = [number for number in numbers if number > 0]\n",
    "positive_numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0a40204",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b890922b",
   "metadata": {},
   "outputs": [],
   "source": [
    "negative_number = "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bb6a751",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "95ffd0e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[10, 11, 13, 17, 19, 23, 256]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[number for number in numbers if len(str(abs(number))) >= 2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85d78570",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "91ff3f3f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[4,\n",
       " 9,\n",
       " 16,\n",
       " 25,\n",
       " 36,\n",
       " 49,\n",
       " 64,\n",
       " 81,\n",
       " 100,\n",
       " 121,\n",
       " 169,\n",
       " 289,\n",
       " 361,\n",
       " 529,\n",
       " 65536,\n",
       " 64,\n",
       " 16,\n",
       " 4,\n",
       " 25,\n",
       " 81]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "numbers_squared = [number**2 for number in numbers]\n",
    "numbers_squared"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "57d70d61",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "c187d594",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[-9]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "odd_negative_numbers = [number for number in numbers if (number % 2 != 0) and (number < 0)\n",
    "                    ]\n",
    "odd_negative_numbers"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f0cebd5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "dee902cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "numbers_plus_5 = numbers\n",
    "numbers_plus_5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6bcf5e7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9404b6e5",
   "metadata": {},
   "outputs": [],
   "source": [
    "def is_prime(number):\n",
    "    \n",
    "    #if number is not postive return False else check for primeness\n",
    "    if number <= 0:\n",
    "        return False\n",
    "    else:\n",
    "        #get numbers in range 2 through the input number-1\n",
    "        dividers = [r for r in range(2, number)]\n",
    "        \n",
    "        #get a list of all numbers in divders that divide th einput number evenly, return if list length is great\n",
    "        return len([divider for divider in dividers if number % divider == 0]) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25c4244c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70fe91cd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6475a64b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ff30ac8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "02891f99",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9fe51386",
   "metadata": {},
   "outputs": [],
   "source": []
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
