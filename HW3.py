{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Бинарный поиск"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "sequence's length:  17\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 13, 23, 25, 25, 30, 34, 34, 46, 47, 54, 64, 69, 77, 83, 85, 92]\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Введите искомое число:  13\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "chislo  v spiske\n"
     ]
    }
   ],
   "source": [
    "from random import randint\n",
    "\n",
    "length = int(input(\"sequence's length: \"))\n",
    "seq = sorted([randint(1,100) for i in range(length)])\n",
    "print(seq)\n",
    "value = int(input(\"Введите искомое число: \"))\n",
    "\n",
    "def binary_search(seq, value):\n",
    "    if len(seq) == 0:\n",
    "        return False\n",
    "    else:\n",
    "        if value == seq[len(seq) //2]:\n",
    "            return True\n",
    "        elif value < seq[len(seq) // 2]:\n",
    "            return binary_search(seq[:len(seq) // 2], value)\n",
    "        elif value > seq[len(seq) // 2]:\n",
    "            return binary_search(seq[len(seq) // 2 + 1:], value)\n",
    "    \n",
    "a = binary_search(seq, value)\n",
    "\n",
    "if a == True:\n",
    "    print('chislo {} v spiske'.format(str()))\n",
    "else:\n",
    "    print('chislo {} NE v spiske'.format(str()))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Алиса"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# максимальное число вопросов, которые нужно задать, чтобы найти число, соответствует макс.  глубине рекурсии -- логарифму по основанию двойки от длины списка, в котором мы ищем число, плюс 1. В случае с сотней его длина = 101, так как отсчет начинается с нуля и 100 включено. Всего листьев у дерева столько, сколько элементов в списке (в нашем случае 101). Таким образом, вопросов со сравнением должно быть 7(лог от 101 по основанию 2 + 1), если их будет меньше, они не покроют все элементы списка и искомое число может не попасть. \n",
    "\n",
    "\n",
    "values = [int(i) for i in range(101)]\n",
    "values.append(i)\n",
    "print(values)\n",
    "    \n",
    "def question():\n",
    "    response = input()\n",
    "    \n",
    "    if response == (\"да\" or \"нет\" or \"yes\" or \"no\"):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "    \n",
    "    \n",
    "def binsearch(values):\n",
    "    if len(values) == 1:\n",
    "        return values[0]\n",
    "    \n",
    "    length = len(values)\n",
    "    key = values[length//2] \n",
    "\n",
    "    print(\"Ваше значение больше, чем {}?\".format(key)) \n",
    "    answer = question()\n",
    "\n",
    "    if answer:\n",
    "    \n",
    "        if len(values[length//2+1:])==0:\n",
    "            print(\"Ложный ответ\")\n",
    "            values = values[length//2+1]\n",
    "            \n",
    "    return binsearch(values)\n",
    "    \n",
    "    else:\n",
    "        print(\"Ваше значение меньше, чем {}?\".format(str(key)))\n",
    "        answer = question()\n",
    "    \n",
    "    if answer:\n",
    "        if len(values[:length//2])==0:\n",
    "            print(\"Ложный ответ\")\n",
    "            return key\n",
    "            values = values[:length//2]\n",
    "            return binsearch \n",
    "    else:\n",
    "        return key"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Медиана"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ввдите длину списка: 4\n",
      "Введите элементы списка по одному: 18\n",
      "Введите элементы списка по одному: 28\n",
      "Введите элементы списка по одному: 19\n",
      "Введите элементы списка по одному: 92\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[18.0, 19.0, 28.0, 92.0]\n",
      "23.5\n"
     ]
    }
   ],
   "source": [
    "values = []\n",
    "for i in range(int(input(\"Ввдите длину списка:\"))):\n",
    "    a = float(input(\"Введите элементы списка по одному:\"))\n",
    "    values.append(a)\n",
    "values.sort()\n",
    "print(values)\n",
    "med_idx = (len(values))//2\n",
    "median = 0.0\n",
    "if len(values) % 2 == 1:\n",
    "    median = values[med_idx]\n",
    "else:\n",
    "    median = (values[med_idx] + values[med_idx-1]) / 2\n",
    "print(median)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Ввдите длину списка: 5\n",
      "Введите элементы списка по одному: 1\n",
      "Введите элементы списка по одному: 4\n",
      "Введите элементы списка по одному: 2\n",
      "Введите элементы списка по одному: 5\n",
      "Введите элементы списка по одному: 6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1.0, 2.0, 4.0, 5.0, 6.0]\n",
      "4.0\n"
     ]
    }
   ],
   "source": [
    "# тупое решение, сверху получше\n",
    "spis = []\n",
    "\n",
    "for i in range(int(input(\"Ввдите длину списка:\"))):\n",
    "    a = float(input(\"Введите элементы списка по одному:\"))\n",
    "    spis.append(a)\n",
    "spis.sort()\n",
    "print(spis)\n",
    "\n",
    "if len(spis) % 2 == 1:\n",
    "    med_elem = (len(spis)-1)/2\n",
    "    print(spis[int(med_elem)])\n",
    "    \n",
    "elif len(spis) % 2 == 0:\n",
    "    med_elem1 = len(spis)/2 - 1\n",
    "    med_elem2 = len(spis)/2 \n",
    "    \n",
    "    a = spis[int(med_elem1)] \n",
    "    b = spis[int(med_elem2)]\n",
    "    \n",
    "    med_element = ((a) + (b))/2\n",
    "    print(med_element)\n",
    "    \n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Пузырьковая сортировка"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "oldl = [int(i) for i in input(\"введите список чисел через пробел:\").split()]\n",
    "\n",
    "for j in range(len(oldl)-1):\n",
    "    for i in range(len(oldl)-1):\n",
    "        if oldl[i+1] < oldl[i]:\n",
    "            oldl[i], oldl[i+1] = oldl[i+1], oldl[i]\n",
    "    \n",
    "print(oldl)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Реверс-комплемент"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " ATGC\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "GCAT\n"
     ]
    }
   ],
   "source": [
    "DNA_seq = input()\n",
    "newseq = ''\n",
    "for i in range(len(DNA_seq)):\n",
    "    if DNA_seq[i] == 'A' or DNA_seq[i] == 'a':\n",
    "        newseq += 'T'\n",
    "    if DNA_seq[i] == 'T' or DNA_seq[i] == 't':\n",
    "        newseq += 'A'\n",
    "    if DNA_seq[i] == 'G' or DNA_seq[i] == 'g':\n",
    "        newseq += 'C'\n",
    "    if DNA_seq[i] == 'C'or DNA_seq[i] == 'c':\n",
    "        newseq += 'G'\n",
    "        \n",
    "reverse_complement = newseq[::-1]\n",
    "print(reverse_complement)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
