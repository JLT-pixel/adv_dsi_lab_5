{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_class_perf(y_preds, y_actuals, set_name=None, average='binary'):\n",
    "    \"\"\"Print the Accuracy and F1 score for the provided data\n",
    "\n",
    "    Parameters\n",
    "    ----------\n",
    "    y_preds : Numpy Array\n",
    "        Predicted target\n",
    "    y_actuals : Numpy Array\n",
    "        Actual target\n",
    "    set_name : str\n",
    "        Name of the set to be printed\n",
    "    average : str\n",
    "        Parameter  for F1-score averaging\n",
    "    Returns\n",
    "    -------\n",
    "    \"\"\"\n",
    "    from sklearn.metrics import accuracy_score\n",
    "    from sklearn.metrics import f1_score\n",
    "\n",
    "    print(f\"Accuracy {set_name}: {accuracy_score(y_actuals, y_preds)}\")\n",
    "    print(f\"F1 {set_name}: {f1_score(y_actuals, y_preds, average=average)}\")"
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
