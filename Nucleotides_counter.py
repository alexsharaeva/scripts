{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "e50f71cd",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('/home/gunter/Introduction_to_Genomics/Files/human.fasta') as f:\n",
    "    first_line = f.readline()\n",
    "    lines = f.read().split('\\n')\n",
    "lines = ''.join(lines)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "573648eb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "G = 48111528, C = 48055043, A = 67070557, T = 67244164\n"
     ]
    }
   ],
   "source": [
    "instring = lines\n",
    "g = instring.upper().count('G')\n",
    "c = instring.upper().count('C')\n",
    "a = instring.upper().count('A')\n",
    "t = instring.upper().count('T')\n",
    "print(f'G = {g}, C = {c}, A = {a}, T = {t}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3d9dffe3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55179b0d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
